# 自定义数据格式运行频率与用法-云服务器ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/user-guide/customize-the-initialization-configuration-for-an-instance

# 使用自定义数据进行实例初始化
如您希望在创建ECS实例时完成系统配置或运行特定业务脚本，例如预装Nginx、Docker等软件或修改主机名等，可以通过设置自定义数据参数来实现。
## 自定义数据介绍
实例自定义数据是指用户上传给实例的脚本、指令或配置文件等数据，可用来完成实例初始化或其他配置，例如，在实例首次启动时，自动运行服务启动脚本、安装软件、打印日志等。自定义数据支持在实例首次启动时自动运行，部分自定义数据格式还支持在Linux实例每次启动时都运行。详细说明，请参见[自定义数据格式及运行频率](customize-the-initialization-configuration-for-an-instance.md)。
## 使用限制
实例的网络类型必须为专有网络VPC。
实例必须使用公共镜像或基于公共镜像创建的自定义镜像，且操作系统需为以下类型之一：
Alibaba Cloud Linux、CentOS、CentOS Stream、Ubuntu、SUSE Linux Enterprise Server、Red Hat Enterprise Linux、OpenSUSE、Debian、AlmaLinux、Rocky Linux、Fedora
Windows Server 2008 R2及更高版本
已停售的实例规格中，仅I/O优化实例支持实例自定义数据功能，非I/O优化实例不支持该功能。更多信息，请参见[已停售的实例规格](retired-instance-types.md)。
## 创建实例时使用自定义数据
### 1. 准备自定义数据
初始化工具在实例初始化过程中，通过读取用户提供的自定义数据以完成自定义配置。Linux实例和Windows实例使用不同的初始化工具。此外，同一初始化工具支持多种自定义数据格式。有关数据格式及其运行频率的详细说明，请参见以下内容。
自定义数据格式及运行频率
## Linux实例
Linux实例使用cloud-init组件实现实例初始化动作。根据实例是否首次启动，执行不同的配置内容（一些使用较早版本镜像的实例也采用Upstart Job进行初始化工作）。
cloud-init工具支持的自定义数据类型包括可直接配置实例的User-Data和Cloud Config格式，同时还支持其他用户数据格式，最常见的为include文件和Gzip压缩内容。除cloud-init初始化工具外，一些使用较早版本镜像的实例也采用Upstart Job进行初始化工作。
说明
自定义数据格式的详细说明，可参见cloud-init文档[User-Data Formats](https://cloudinit.readthedocs.io/en/latest/topics/format.html)。
如果您的User-Data脚本、Cloud Config数据或Include文件内容的大小超过32 KB，数据类型建议选择Gzip压缩内容。
如果任务需要在实例每次启动时都执行，数据类型建议选择Cloud Config数据或Upstart Job。
## User-Data脚本
简介
User-Data脚本传入Linux实例后直接作为Shell脚本执行，且仅在实例首次启动时运行一次。
运行频率
启动实例：仅在实例首次启动时运行一次，重启实例不会再自动运行。
更换操作系统：自动运行。
重新初始化系统盘：自动运行。
重要
以下情况不会自动运行脚本：
如果更换操作系统使用的是自定义镜像且来源于原实例，更换操作系统时会判断实例不是初次启动，因此不会自动运行脚本。
如果创建使用的是自定义镜像，则创建实例时系统盘就有数据，初始化系统盘时会判断实例不是首次启动，因此不会自动运行脚本。
格式
首行均以#!开头。
User-Data脚本示例
运行自定义脚本
#!/bin/sh echo "Hello World. The time is now $(date -R)!" | tee /root/userdata_test.txt
示例User-Data脚本的效果是在实例首次启动时，向userdata_test.txt文件写入系统时间。
自定义实例软件源、DNS解析配置及时间同步服务
在创建实例时，您可以通过User-Data脚本自定义实例的软件源、DNS解析配置及时间同步服务。以下示例以CentOS Stream 9为例，实际使用中请根据您的操作系统进行相应配置替换。
重要
系统会在实例启动时自动配置默认的yum源、NTP服务和DNS服务，您可以使用实例自定义数据更改默认的yum源、NTP服务和DNS服务，但请注意：
如果您自定义了yum源，阿里云官方不再提供yum源相关支持。
如果您自定义了NTP服务，阿里云官方不再提供相关时间同步服务。
#!/bin/sh # Modify DNS echo "nameserver 114.114.114.114" | tee /etc/resolv.conf # Modify yum repo and update cp /etc/yum.repos.d/centos.repo /etc/yum.repos.d/centos.repo.bak cp /etc/yum.repos.d/centos-addons.repo /etc/yum.repos.d/centos-addons.repo.bak sed -i "s@http://mirrors.cloud.aliyuncs.com/centos-stream/@https://mirror.stream.centos.org/@g" /etc/yum.repos.d/centos.repo sed -i "s@http://mirrors.cloud.aliyuncs.com/centos-stream/@https://mirror.stream.centos.org/@g" /etc/yum.repos.d/centos-addons.repo yum update -y # Modify NTP Server echo "server ntp1.aliyun.com" | tee /etc/ntp.conf systemctl restart ntpd.service
说明
其中114.114.114.114为DNS服务器地址、https://mirror.stream.centos.org为CentOS Stream的yum仓库地址、server ntp1.aliyun.com为阿里云的NTP服务器地址，请您根据实际环境替换。
您也可以使用Cloud Config数据更改yum源，但是不够灵活，不能适配阿里云已对部分yum源进行预配置的情况，建议使用User-Data脚本。
自定义管理员账号
Linux实例默认使用root用户作为管理员，您可以使用实例自定义数据使用其他用户作为管理员。
#!/bin/sh useradd test-user echo "test-user ALL=(ALL) NOPASSWD:ALL" | tee -a /etc/sudoers mkdir /home/test-user/.ssh touch /home/test-user/.ssh/authorized_keys echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCRnnUveAis****" | tee -a /home/test-user/.ssh/authorized_keys
说明
请使用您的公钥替换示例中的公钥ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCRnnUveAis****。
说明
当User-Data执行遇到问题时，可以通过云助手公共命令ACS-ECS-UserData-Check-for-linux.sh来获取失败相关的错误日志。如果返回有错误信息表示脚本执行有问题，如果没有返回错误信息表示执行没有报错，需要排查其他方面。关于云助手公共命令的更多信息，请参见[查看和执行公共命令](view-and-run-common-cloud-assistant-commands.md)。
## Cloud Config数据
简介
在Cloud-init中，定义了一系列的功能模块，来完成部分需要执行的任务和配置，例如安装软件包、设置网络等。执行哪些模块及具体的执行逻辑，由Cloud Config数据决定，可从vendordata、自定义数据、内核参数中获取。在创建ECS实例时，用户可自定义Cloud Config数据，指定需要执行的模块和任务，并作为自定义数据提供给实例。实例启动时，cloud-init会读取并解析Cloud Config数据，并按照配置文件中的指示运行对应模块并执行配置任务，自动配置和部署ECS实例。
运行频率
启动实例：Cloud Config数据中的任务是否会被执行，取决于这些任务对应模块的频率设置。各模块的说明，请参见[Modules](https://cloudinit.readthedocs.io/en/latest/topics/modules.html)。
频率为once-per-instance：仅在实例首次启动时运行。例如配置的是Apt、Set Passwords等模块，运行频率为once-per-instance，重启实例时不会运行。
频率为always：实例每次启动都运行。例如配置的是Bootcmd、Update Etc Hosts等模块，运行频率为always，实例每次启动都运行。
更换操作系统：自动运行。
重新初始化系统盘：自动运行。
重要
以下情况不会自动运行脚本：
如果更换操作系统使用的是自定义镜像且来源于原实例，更换操作系统时会判断实例不是初次启动，因此不会自动运行脚本。
如果创建使用的是自定义镜像，则创建实例时系统盘就有数据，初始化系统盘时会判断实例不是首次启动，因此不会自动运行脚本。
格式
首行为#cloud-config，且起始位置不能有空格。
必须遵循YAML语法编写内容。
Cloud Config数据示例
自定义实例软件源
在自定义数据区域输入以下内容，以配置自定义实例软件源。示例中使用Ubuntu镜像创建实例，如果您使用其他镜像，请替换为对应模块的配置内容。
#cloud-config apt: preserve_sources_list: false disable_suites: - $RELEASE-updates - backports - $RELEASE - mysuite primary: - arches: - amd64 - i386 - default uri: http://us.archive.ubuntu.com/ubuntu
配置自动安装nginx服务
在自定义数据区域输入如下内容，以配置实例自动安装nginx服务。
#cloud-config packages: - nginx runcmd: - systemctl start nginx.service
配置自定义主机名
在自定义数据区域输入如下内容，以自定义设置主机名。
#cloud-config hostname: my-instance fqdn: my-instance.localdomain
配置自动运行自定义脚本
在自定义数据区域输入如下内容，以配置实例每次启动时自动运行Shell脚本。
#cloud-config bootcmd: - echo "Hello World. The time is now $(date -R)!" | tee /root/userdata_test.txt
## Include文件
简介
通过Include文件指向一个或多个User-Data脚本或Cloud Config数据的链接，多个链接按行分隔。实例启动时，cloud-init会逐个解析并读取链接里的内容。如果在读取某一个链接的内容时出错，则停止读取剩余的链接。
说明
您可以通过阿里云对象存储OSS，上传User-Data脚本或Cloud Config数据、获取链接、设置链接有效期等。具体操作，请参见[OSS](../../../oss/documents/user-guide/console-quick-start.md)[控制台快速入门](../../../oss/documents/user-guide/console-quick-start.md)。
运行频率
启动实例：执行频率由链接里的内容决定。例如，链接的内容为User-Data脚本，则仅在实例首次启动时运行一次；脚本类型链接的内容为Cloud Config数据，则遵循Cloud Config数据的运行频率。
更换操作系统：自动运行。
重新初始化系统盘：自动运行。
重要
以下情况不会自动运行脚本：
如果更换操作系统使用的是自定义镜像且来源于原实例，更换操作系统时会判断实例不是初次启动，因此不会自动运行脚本。
如果创建使用的是自定义镜像，则创建实例时系统盘就有数据，初始化系统盘时会判断实例不是首次启动，因此不会自动运行脚本。
格式
首行为#include，且起始位置不能有空格。
Include文件示例
#include https://ecs-image-test.oss-cn-hangzhou.aliyuncs.com/userdata/myscript.sh
示例Include文件包含一个脚本链接，该脚本为User-Data脚本，则仅在实例首次启动时运行一次。
说明
如果您采用Include文件或Gzip压缩内容的方式，需要使用存储服务上传脚本、获取脚本链接、设置链接有效期等操作，推荐您使用阿里云对象存储OSS。具体操作，请参见[OSS](../../../oss/documents/user-guide/console-quick-start.md)[控制台快速入门](../../../oss/documents/user-guide/console-quick-start.md)。
## Gzip压缩内容
简介
如果您的User-Data脚本、Cloud Config数据或Include文件内容的大小超过32 KB，可以采用Gzip压缩内容（.gz格式）并做成链接，然后以Include文件的形式输入。cloud-init会自动解压Gzip压缩内容，运行解压后内容的效果和直接传入后运行没有区别。
说明
您可以通过阿里云对象存储OSS，上传User-Data脚本或Cloud Config数据、获取链接、设置链接有效期等。具体操作，请参见[OSS](../../../oss/documents/user-guide/console-quick-start.md)[控制台快速入门](../../../oss/documents/user-guide/console-quick-start.md)。
运行频率
启动实例：由脚本类型和模块类型决定。例如，Gzip压缩内容链接的脚本类型为User-Data脚本，则仅在实例首次启动时运行一次。
更换操作系统：自动运行。
重新初始化系统盘：自动运行。
重要
以下情况不会自动运行脚本：
如果更换操作系统使用的是自定义镜像且来源于原实例，更换操作系统时会判断实例不是初次启动，因此不会自动运行脚本。
如果创建使用的是自定义镜像，则创建实例时系统盘就有数据，初始化系统盘时会判断实例不是首次启动，因此不会自动运行脚本。
格式
首行为#include，且起始位置不能有空格。
Gzip压缩内容示例
#include https://ecs-image-test.oss-cn-hangzhou.aliyuncs.com/userdata/myscript.gz
示例Gzip压缩内容表示Include文件包含一个Gzip压缩内容链接，cloud-init读取该Gzip压缩内容后会自动解压并运行，该Gzip压缩内容由User-Data脚本压缩得到，所以仅在实例首次启动时运行一次。
## Upstart Job
说明
如需使用Upstart Job，您需要为实例安装upstart服务，支持采用upstart服务管理启动行为的操作系统有CentOS 6、Ubuntu 10/12/14以及Debian 6/7。
简介
Upstart是一个事件驱动型的初始化系统，Upstart Job是一个配置文件，定义了一个服务或任务何时启动、停止和如何运行。它通常放置在/etc/init/目录下，文件扩展名为.conf。
运行频率
启动实例：实例每次启动都会自动运行。
更换操作系统：自动运行。
重新初始化系统盘：自动运行。
重要
以下情况不会自动运行脚本：
如果更换操作系统使用的是自定义镜像且来源于原实例，更换操作系统时会判断实例不是初次启动，因此不会自动运行脚本。
如果创建使用的是自定义镜像，则创建实例时系统盘就有数据，初始化系统盘时会判断实例不是首次启动，因此不会自动运行脚本。
格式
首行为#upstart-job，且起始位置不能有空格。
Upstart Job内容示例
#upstart-job description "upstart test" start on runlevel [2345] #在运行级别2、3、4、5执行 stop on runlevel [!2345] #在运行级别2、3、4、5以外不执行 exec echo "Hello World. The time is now $(date -R)!" | tee /root/output.txt
示例Upstart Job表示在系统进入指定的运行级别时输出一条包含时间戳的消息，并将该消息记录到/root/output.txt文件中。当系统离开这些运行级别时，作业会停止执行。
## MIME multi-part文件
简介
MIME multi-part文件可以传输多类型指令。例如，您可以使用MIME multi-part文件将text/cloud-config（用于Cloud-Init配置）和text/x-shellscript（Shell脚本） 同时包含在用户数据中。Cloud-Init会分别解析并执行这些不同类型的指令。
运行频率
启动实例：由MIME消息中各个部分的类型和cloud-init的配置。例如，MIME消息中内容类型为User-Data脚本，则仅在实例首次启动时运行一次；MIME消息中内容类型为Cloud Config数据，则遵循Cloud Config数据的运行频率。
更换操作系统：自动运行。
重新初始化系统盘：自动运行。
重要
以下情况不会自动运行脚本：
如果更换操作系统使用的是自定义镜像且来源于原实例，更换操作系统时会判断实例不是初次启动，因此不会自动运行脚本。
如果创建使用的是自定义镜像，则创建实例时系统盘就有数据，初始化系统盘时会判断实例不是首次启动，因此不会自动运行脚本。
格式
首行为Content-Type：multipart/mixed：boundary="****"，boundary可自定义，且起始位置不能有空格。
第二行指定版本MIME-Version：1.0，该字段通常在每个MIME消息中是必需的。
MIME multi-part文件示例
Content-Type: multipart/mixed; boundary="//" MIME-Version: 1.0 --// Content-Type: text/cloud-config; charset="us-ascii" MIME-Version: 1.0 Content-Transfer-Encoding: 7bit Content-Disposition: attachment; filename="cloud-config.txt" #cloud-config runcmd: - [ mkdir, /test-cloudinit ] write_files: - path: /test-cloudinit/cloud-init.txt content: | Created by cloud-init append: true --// Content-Type: text/x-shellscript; charset="us-ascii" MIME-Version: 1.0 Content-Transfer-Encoding: 7bit Content-Disposition: attachment; filename="userdata.txt" #!/bin/bash mkdir test-userscript touch /test-userscript/userscript.txt echo "Created by bash shell script" >> /test-userscript/userscript.txt --//--
示例MIME multi-part文件包含cloud-init指令和一个Bash Shell脚本：
cloud-init指令创建一个文件 (/test-cloudinit/cloud-init.txt)，并写入Created by cloud-init。
Bash Shell脚本创建一个文件 (/test-userscript/userscript.txt)，并写入Created by bash shell script。
## Windows实例
Windows实例是通过Vminit工具的Plugin_Main_CloudinitUserData插件来运行自定义数据脚本，该插件仅支持在实例首次启动时运行，该插件支持Bat和PowerShell两种脚本。
## bat脚本
运行频率
启动实例：实例首次启动时运行一次，重启实例不会自动运行。
更换操作系统：自动运行。
重新初始化系统盘：自动运行。
重要
以下情况不会自动运行脚本：
如果更换操作系统使用的是自定义镜像且来源于原实例，更换操作系统时会判断实例不是初次启动，因此不会自动运行脚本。
如果创建使用的是自定义镜像，则创建实例时系统盘就有数据，初始化系统盘时会判断实例不是首次启动，因此不会自动运行脚本。
格式
首行为[bat]，且起始位置不能有空格。
只能输入半角字符，不能有多余字符。
写入数据的路径不能为C:\Users目录，否则自定义数据会执行失败。
说明
在Windows系统中，C:\Users及其子目录是用户配置文件和数据的默认存储位置，需要登录系统后才可以访问，而在系统初始化执行userdata阶段实际还未登录系统，所以写入数据到C:\Users目录会失败。
Bat脚本示例
运行自定义脚本
[bat] echo "bat test" > C:\userdata_test.txt
示例Bat脚本的效果是在实例首次启动时向userdata_test.txt文件写入内容"bat test"。
## PowerShell脚本
运行频率
启动实例：实例首次启动时运行一次，重启实例不会自动运行。
更换操作系统：自动运行。
重新初始化系统盘：自动运行。
重要
以下情况不会自动运行脚本：
如果更换操作系统使用的是自定义镜像且来源于原实例，更换操作系统时会判断实例不是初次启动，因此不会自动运行脚本。
如果创建使用的是自定义镜像，则创建实例时系统盘就有数据，初始化系统盘时会判断实例不是首次启动，因此不会自动运行脚本。
格式
首行为[powershell]，且起始位置不能有空格。
只能输入半角字符，不能有多余字符。
写入数据的路径不能为C:\Users目录，否则自定义数据会执行失败。
说明
在Windows系统中，C:\Users及其子目录是用户配置文件和数据的默认存储位置，需要登录系统后才可以访问，而在系统初始化执行userdata阶段实际还未登录系统，所以写入数据到C:\Users目录会失败。
PowerShell脚本示例
运行自定义脚本
[powershell] write-output "powershell test" | Out-File C:\userdata_test.txt
示例PowerShell脚本的效果是在实例首次启动时向userdata_test.txt文件写入内容powershell test。
### 2. 创建实例时使用自定义数据
通过控制台创建实例
在[实例购买页](https://ecs-buy.aliyun.com/wizard/#/)展开高级选项区域，在自定义数据区域输入实例自定义数据。
重要
如果实例自定义数据已进行Base64编码，请勾选输入已采用Base64编码，且在进行Base64编码前自定义数据内容的大小不能超过32 KB。否则，无需勾选，系统会自动对内容进行Base64编码。
通过API创建实例
如果您通过API方式创建实例，请在[RunInstances - 批量创建实例](../developer-reference/api-ecs-2014-05-26-runinstances.md)或[CreateInstance - 创建实例](../developer-reference/api-ecs-2014-05-26-createinstance.md)接口指定UserData字段。
### 3. 验证自定义数据运行效果
您需要结合自定义脚本的实际内容进行运行效果的验证，以下以在Linux实例中传入如下User-Data脚本为例，为您演示如何进行脚本运行效果验证。
#!/bin/sh echo "Hello World. The time is now $(date -R)!" | tee /root/userdata_test.txt
该示例中，User-Data脚本的效果是在实例首次启动时，向userdata_test.txt文件写入系统时间。为验证该脚本的执行效果，您可以运行cat userdata_test.txt命令来查看效果，系统已经向userdata_test.txt文件写入系统时间。
说明
当User-Data执行遇到问题时，可以通过云助手公共命令ACS-ECS-UserData-Check-for-linux.sh来获取失败相关的错误日志。如果返回有错误信息表示脚本执行有问题，如果没有返回错误信息表示执行没有报错，需要排查其他方面。关于云助手公共命令的更多信息，请参见[查看和执行公共命令](view-and-run-common-cloud-assistant-commands.md)。
## 其他操作
### 查看已有实例自定义数据
自定义数据传入实例后，您可以通过元数据服务或控制台查看实例的自定义数据信息。
## 通过元数据服务获取（加固模式）
Linux实例
TOKEN=`curl -X PUT "http://100.100.100.200/latest/api/token" -H "X-aliyun-ecs-metadata-token-ttl-seconds:180"` curl -H "X-aliyun-ecs-metadata-token: $TOKEN" http://100.100.100.200/latest/user-data
Windows实例
$token = Invoke-RestMethod -Headers @{"X-aliyun-ecs-metadata-token-ttl-seconds" = "180"} -Method PUT -Uri http://100.100.100.200/latest/api/token Invoke-RestMethod -Headers @{"X-aliyun-ecs-metadata-token" = $token} -Method GET -Uri http://100.100.100.200/latest/user-data
说明
在上述示例中，设置的token有效期为180秒，实际应用时可根据具体使用场景进行调整。
本示例使用元数据服务的加固模式来获取元数据，关于元数据服务获取信息的更多内容，请参见[实例元数据](view-instance-metadata.md)。
关于元数据的更多说明，请参见[实例元数据](view-instance-metadata.md)。
## 通过控制台获取
确保实例处于已停止状态。
重要
如果实例的计费方式为按量付费、网络类型为专有网络，停止实例时，停止模式建议选择普通停机模式，选择节省停机模式会因计算资源（vCPU和内存）被回收，再次启动实例时可能因为库存不足导致启动失败。更多信息，请参见[节省停机模式](economical-mode.md)。
单击目标实例ID进入实例详情页，单击全部操作展开所有操作面板，搜索并单击设置用户数据，然后在用户数据区域查看已设置的自定义数据。
## 通过调用API获取
您可以通过调用DescribeUserData接口查询一台ECS实例的自定义数据。更多信息，请参见[DescribeUserData](../developer-reference/api-ecs-2014-05-26-describeuserdata.md)。
### 修改已有实例自定义数据
如需修改已有实例的自定义数据，您可以通过控制台进行操作。
确保实例处于已停止状态。
重要
如果实例的计费方式为按量付费、网络类型为专有网络，停止实例时，停止模式建议选择普通停机模式，选择节省停机模式会因计算资源（vCPU和内存）被回收，再次启动实例时可能因为库存不足导致启动失败。更多信息，请参见[节省停机模式](economical-mode.md)。
单击目标实例ID进入实例详情页，单击全部操作展开所有操作面板，搜索并单击设置用户数据，然后在用户数据区域输入自定义数据。
重要
修改已有实例的自定义数据之后，在启动实例后自定义数据脚本是否被执行，取决于自定义数据的格式及运行频率，请您在修改自定义数据之前明确您的需求，更多信息，请参见[自定义数据格式及运行频率](customize-the-initialization-configuration-for-an-instance.md)。
## 相关文档
您也可以通过弹性伸缩的自定义数据功能，让多台ECS实例在启动时自动执行配置的脚本或命令，确保ECS实例配置的一致性，简化了运维工作。更多信息，请参见[使用实例自定义数据自动配置](https://help.aliyun.com/zh/auto-scaling/use-cases/enable-the-instance-user-data-feature-to-automatically-configure-ecs-instances)[ECS](https://help.aliyun.com/zh/auto-scaling/use-cases/enable-the-instance-user-data-feature-to-automatically-configure-ecs-instances)[实例](https://help.aliyun.com/zh/auto-scaling/use-cases/enable-the-instance-user-data-feature-to-automatically-configure-ecs-instances)。
如果希望服务或脚本因程序异常、服务器重启、掉电等被中断时，及时恢复运行，云助手插件ecs-tool-servicekeepalive实现。具体操作，请参见[使用云助手插件进行服务保活](use-the-cloud-assistant-plugin-for-service-keepalive.md)。
如果您希望了解更多关于管理实例初始化的相关信息，请参见[初始化工具介绍](manage-the-instance-initialization-configuration.md)。
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
