# 实例登录名、密码、密钥对管理-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/instance-logon-credential-management

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 实例登录凭证管理（登录名/密码/密钥对）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

实例无默认密码，如忘记密码可[重置](products/ecs/documents/user-guide/instance-logon-credential-management.md)。创建实例时如未设置登录名，则会使用默认登录名。

| 操作系统 | 默认登录名 | 说明 |
| --- | --- | --- |
| Linux | root | 对应 Linux 系统的超级管理员用户。 |
| Windows | Administrator | 对应 Windows 系统的超级管理员用户。 |


重要

root用户权限较高，直接使用存在安全风险。建议使用ecs-user，通过sudo获取临时root权限执行敏感操作。

## 一、密码管理

### 1.1 重置密码（不知道/忘记原密码）

在线重置密码无需重启，建议优先尝试在线重置密码。

## 在线重置密码（不重启）

说明

在线重置密码依赖实例中安装的云助手Agent。[查看云助手状态](products/ecs/documents/user-guide/check-the-status-of-cloud-assistant-and-handle-exceptions.md)，[安装云助手](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)[Agent](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)。

- 

进入[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，选择地域与资源组，找到待操作实例。

- 

根据以下指引，进入重置实例密码功能对话框。

| 简捷版控制台 | 标准版控制台 |
| --- | --- |
| 单击 重置密码 。 | 单击 操作 列下的 重置实例密码 。 |


- 

在重置实例密码对话框，完成如下配置后单击确认修改等待密码重置完成。其余配置保持默认。

- 

新密码/确认密码：输入实例新密码。请为实例设置强密码（包含大小写字母、数字、特殊字符）。

- 

重置密码的方式：在线重置密码。

重要

如无法选择在线重置实例密码，请使用[离线重置密码（需重启）](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

若提示重置密码[失败](products/ecs/documents/user-guide/instance-logon-credential-management.md)，请使用[离线重置密码（需重启）](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

## 离线重置密码（需重启）

重要

离线重置密码需要重启实例才能生效。重启可能会中断实例中的业务，请合理规划时间。

- 

进入[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，选择地域与资源组，找到待操作实例。

- 

根据以下指引，进入重置实例密码功能对话框。

| 简捷版控制台 | 标准版控制台 |
| --- | --- |
| 单击 重置密码 。 | 单击 操作 列下的 重置实例密码 。 |


- 

在重置实例密码对话框，完成如下配置后单击确认修改等待密码重置完成。

- 

新密码/确认密码：输入新实例密码。请为实例设置强密码（包含大小写字母、数字、特殊字符）。

- 

重置密码的方式：离线重置密码。

- 

[重启实例](products/ecs/documents/user-guide/restart-instances.md)。

重置密码需要重启实例才能生效。可在业务低峰期重启，以免影响业务稳定性。

- 

[通过](products/ecs/documents/user-guide/log-on-to-an-instance-by-using-vnc.md)[VNC](products/ecs/documents/user-guide/log-on-to-an-instance-by-using-vnc.md)[连接并登录实例](products/ecs/documents/user-guide/log-on-to-an-instance-by-using-vnc.md)。

VNC登录成功，代表在操作系统中，密码已经成功重置。

如果VNC登录实例成功，但Workbench等工具登录失败，证明密码已经重置成功，可能是SSH配置存在问题，建议通过[无法连接](products/ecs/documents/troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)[Linux](products/ecs/documents/troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)[实例的排查方法](products/ecs/documents/troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)。

### 1.2 修改密码（知道原密码）

建议优先从控制台在线重置密码。

## 在线重置密码

说明

在线重置密码依赖实例中安装的云助手Agent。[查看云助手状态](products/ecs/documents/user-guide/check-the-status-of-cloud-assistant-and-handle-exceptions.md)，[安装云助手](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)[Agent](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)。

- 

进入[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，选择地域与资源组，找到待操作实例。

- 

根据不同的控制台页面，进入重置实例密码功能对话框。

| 简捷版控制台 | 标准版控制台 |
| --- | --- |
| 单击 重置密码 。 | 单击 操作 列下的 重置实例密码 。 |


- 

在重置实例密码对话框，完成如下配置后单击确认修改等待密码重置完成。其余配置保持默认。

- 

新密码/确认密码：输入新实例密码。请为实例设置强密码（包含大小写字母、数字、特殊字符）。

- 

重置密码的方式：在线重置密码。

重要

如无法选择在线重置实例密码，请[登录实例手动修改密码](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

若提示重置密码[失败](products/ecs/documents/user-guide/instance-logon-credential-management.md)，请[登录实例手动修改密码](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

## 登录实例手动修改密码

## Windows实例

以Windows Server 2019操作系统为例：

- 

[使用](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)[Workbench](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)[登录](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)[Windows](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)。

- 

右键，单击运行(R)，输入compmgmt.msc并按Enter键。

- 

在左侧导航栏，选择计算机管理>本地用户和组>用户。

- 

右键需要修改密码的用户名称（如Administrator），单击设置密码。

- 

在为 Administrator 设置密码对话框中，单击继续，输入新密码并确认密码。

重要

请设置强密码（包含大小写字母、数字、特殊字符）。

- 

单击确定后，系统会显示密码已设置的确认信息，代表密码修改成功。

## Linux实例

以Alibaba Cloud Linux 3操作系统为例：

- 

[使用](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)。

- 

运行以下命令：

请将<username>替换为待修改密码的用户名。sudo passwd <username>

- 

输入新密码后按Enter键，再次输入新密码并按Enter键。

重要

请设置强密码（包含大小写字母、数字、特殊字符）。

- 

修改成功后，系统输出类似以下信息：

passwd: all authentication tokens updated successfully.

## 二、密钥对管理

创建实例时，可直接绑定一个已在阿里云[创建或导入](products/ecs/documents/user-guide/instance-logon-credential-management.md)的密钥对，用于登录。如果创建实例时未绑定密钥对，需[为实例绑定密钥对](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

密钥对是一种更安全的凭证，可以有效抵御暴力破解、字典攻击等。它包含两部分：公钥（存储在实例内）、私钥（由您个人保管）。登录实例时，必须提供私钥以完成身份验证。

密钥对认证原理

简化后的SSH密钥对认证流程如图所示。在客户端发起登录请求后，服务端会通过公钥加密一个随机字符串，客户端通过私钥解密该字符串返回给服务端，通过对比两个字符串是否一致来认证身份。

Windows实例使用密钥对须在实例中开启SSH服务，且不支持控制台管理。

### 2.1 创建/导入

## 控制台

创建密钥对

- 

进入[ECS](https://ecs.console.aliyun.com/keyPair/region)[控制台-密钥对](https://ecs.console.aliyun.com/keyPair/region)，在左上角选择地域与资源组。

ECS实例仅支持绑定与其同地域的密钥对。

- 

单击创建密钥对，创建类型选择自动创建密钥对。

- 

单击确定。

密钥对创建成功后，浏览器自动下载私钥文件（密钥对名称.pem）到本地。

导入密钥对

支持导入的密钥对加密方式

- 

rsa

- 

dsa

- 

ssh-rsa

- 

ssh-dss

- 

ecdsa

- 

根据私钥查看对应公钥

## 本地为Linux/macOS

使用ssh-keygen命令从一个现有的私钥文件中提取并显示其对应的公钥

<path_to_key_pair>为私钥文件的路径，例如/path_to_key_pair/my-key-pair.pem。ssh-keygen -y -f <path_to_key_pair>

返回公钥信息：

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABA****+GF9q7rhc6vYrExwT4WU4fsaRcVXGV2Mg9RHex21hl1au77GkmnIgukBZjywlQOT4GDdsJy2nBOdJPrCEBIPxxxxxxxxxx/fctNuKjcmMMOA8YUT+sJKn3l7rCLkesE+S5880yNdRjBiiUy40kyr7Y+fqGVdSOHGMXZQPpkBtojcxxxxxxxxxxx/htEqGa/Jq4fH7bR6CYQ2XgH/hCap29Mdi/G5Tx1nbUKuIHdMWOPvjxxxxxxxxxx+lHtTGiAIRG1riyNRVC47ZEVCxxxxxx

## 本地为Windows系统

完成以下操作，查看公钥信息：

- 

启动[PuTTYgen](https://www.puttygen.com/)。

- 

单击Load。

- 

选择.ppk或.pem文件。

PuTTYgen会显示公钥信息。

- 导入密钥对（公钥）

- 

进入[ECS](https://ecs.console.aliyun.com/keyPair/region)[控制台-密钥对](https://ecs.console.aliyun.com/keyPair/region)，在左上角选择地域。

ECS实例仅支持绑定与其同地域的密钥对。

- 

单击创建密钥对，创建类型选择导入已有密钥对，并提供公钥内容。

- 

单击确定，完成导入。

## API

- 

创建密钥对：[CreateKeyPair](products/ecs/documents/developer-reference/api-ecs-2014-05-26-createkeypair.md)。

- 

导入密钥对中的公钥：[ImportKeyPair](products/ecs/documents/developer-reference/api-ecs-2014-05-26-importkeypair.md)。

### 2.2 绑定/换绑

## 控制台

说明

仅Linux实例，支持在控制台绑定、解绑、换绑密钥对。

创建实例时绑定密钥对

可在通过[自定义购买](products/ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)创建实例时，设置登录凭证为密钥对，然后选择已创建的密钥对。

绑定/换绑密钥对

重要

- 

在控制台绑定/换绑密钥对需要重启实例才能生效。重启可能会中断实例中的业务，请合理规划时间。

- 

每个实例在控制台最多绑定一个密钥对，如需绑定多个，请[在实例内手动绑定](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

## 控制台绑定/换绑（需重启）

进入[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，在左上角选择地域与资源组，找到对应ECS实例后，根据以下指引操作：

| 简捷版控制台 | 标准版控制台 |
| --- | --- |
| 单击 全部操作 > 绑定密钥对 ，选择已创建的密钥对后，单击 确定 。重启实例后生效。 | 单击 操作 列下的 > 绑定密钥对 ，选择已创建的密钥对后，单击 确定 。重启实例后生效。 |


## 实例内手动绑定（无需重启）

- 生成密钥对

不同的工具生成密钥对的步骤有所差别，本步骤以ssh-keygen工具为例。

输入以下命令生成密钥对。

ssh-keygen -t rsa -b 2048 -f id_rsa

参数说明：

- 

-t rsa：代表密钥类型为rsa密钥对。

- 

-b 2048：代表密钥长度为2048位。

- 

-f id_rsa：代表生成密钥对的文件名以及保存位置。

系统将提示你输入一个口令（passphrase）。这个口令用于保护你的私钥。设置口令是推荐的安全措施。如果不需要口令，直接按回车键继续。

命令执行成功后，当前目录下会生成两个文件：

- 

id_rsa：你的私钥。

- 

id_rsa.pub：你的公钥。

重要

请妥善保存私钥，不要泄漏给他人。

- 为实例绑定公钥

在[使用](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录实例](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)后，按以下步骤操作。

为root用户绑定公钥与为非root用户绑定公钥操作有所差异，根据实际情况选择对应操作。

## 设置root用户的公钥

- 

创建authorized_keys配置文件。

如果/root/.ssh目录或authorized_keys文件不存在，运行以下命令创建。

sudo mkdir /root/.ssh sudo touch /root/.ssh/authorized_keys

- 

添加公钥。

使用文本编辑器（如[Vim](products/ecs/documents/user-guide/use-the-vim-editor.md)）打开authorized_keys文件。

sudo vim /root/.ssh/authorized_keys

将你的公钥内容粘贴到文件中。可配置多个公钥，每个公钥占一行。配置完成后保存并关闭文件。

- 

设置文件权限。

SSH 要求严格的权限设置，错误的权限会导致 SSH 登录失败。

运行以下命令，设置正确的权限。

sudo chmod 700 /root/.ssh sudo chmod 600 /root/.ssh/authorized_keys

## 设置非root用户的公钥

- 

创建authorized_keys配置文件。

如果/root/.ssh目录或authorized_keys文件不存在，运行以下命令创建。

命令中<username>为待绑定公钥用户的用户名。sudo mkdir /home/<username>/.ssh sudo touch /home/<username>/.ssh/authorized_keys

- 

添加公钥。

使用文本编辑器（如[Vim](products/ecs/documents/user-guide/use-the-vim-editor.md)）打开authorized_keys文件。

sudo vim /home/<username>/.ssh/authorized_keys

将你的公钥内容粘贴到文件中。可配置多个公钥，每个公钥占一行。配置完成后保存并关闭文件。

- 

设置文件权限。

SSH 要求严格的权限设置，错误的权限会导致 SSH 登录失败。

运行以下命令，设置正确的权限。

sudo chown -R <username>:<username> /home/<username>/.ssh sudo chmod 700 /home/<username>/.ssh sudo chmod 600 /home/<username>/.ssh/authorized_keys

- 开启SSH服务的公钥认证功能

配置公钥后，必须在服务器上启用 SSH 公钥认证。否则，密钥登录会失败。

- 

备份SSH配置文件/etc/ssh/sshd_config。

sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak

- 

使用文本编辑器（如[Vim](products/ecs/documents/user-guide/use-the-vim-editor.md)）打开/etc/ssh/sshd_config文件，并找到PubkeyAuthentication参数，设置为yes，代表开启公钥认证功能。

sudo vim /etc/ssh/sshd_config

- 

重启SSH服务以应用更改。

以Alibaba Cloud Linux 3为例：

sudo systemctl restart sshd部分操作系统（Ubuntu/Debian）的SSH服务名为ssh而非sshd，请根据实际情况调整。

重要

如果正通过SSH的方式连接到实例，重启服务可能导致连接中断，服务重启完成后，即可重新连接。

## API

说明

仅Linux实例支持通过API绑定、换绑或解绑密钥对。

- 

创建实例时设置密钥对：在调用[RunInstances](products/ecs/documents/developer-reference/api-ecs-2014-05-26-runinstances.md)创建实例时，将KeyPairName设置为对应的密钥对名称。

- 

绑定/换绑密钥对：调用[AttachKeyPair](products/ecs/documents/developer-reference/api-ecs-2014-05-26-attachkeypair.md)，并指定密钥对名称KeyPairName和实例IDInstanceIds。

- 

解绑密钥对：调用[DetachKeyPair](products/ecs/documents/developer-reference/api-ecs-2014-05-26-detachkeypair.md)，并指定密钥对名称KeyPairName和实例IDInstanceIds。

### 2.3 解绑

重要

在控制台解绑密钥对需要重启实例才能生效。重启可能会中断实例中的业务，请合理规划时间。

## 控制台解绑（需重启）

进入[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，在左上角选择地域与资源组，找到对应ECS实例后，根据以下指引操作：

| 简捷版控制台 | 标准版控制台 |
| --- | --- |
| 在 全部操作 ，单击 绑定密钥对 ，单击 解绑 。重启实例后生效。 | 单击 操作 列下的 解绑密钥对 ，单击 解绑 。重启实例后生效。 |


## 实例内手动解绑（无需重启）

可在实例内手动清除authorized_keys中存储的公钥，实现解绑密钥对。针对不同用户，authorized_keys配置文件路径如下：

- 

root用户：/root/.ssh/authorized_keys

- 

非root用户：/home/<username>/.ssh/authorized_keys

其中<username>为待绑定公钥用户的用户名

### 2.4 删除

## 控制台

重要

已绑定实例的密钥对不支持删除。

- 

进入[ECS](https://ecs.console.aliyun.com/keyPair/region)[控制台-密钥对](https://ecs.console.aliyun.com/keyPair/region)，在左上角选择地域与资源组。

- 

找到需要删除的密钥对，单击操作列下的删除。完成密钥对的删除。

## API

调用[DeleteKeyPairs](products/ecs/documents/developer-reference/api-ecs-2014-05-26-deletekeypairs.md)，并指定KeyPairNames为要删除的密钥对名称列表。

## 三、多用户远程登录

在需要设置多个用户使用ECS实例时，请遵循以下步骤，创建普通用户并启用远程访问。

## Linux系统

[使用](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录实例](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)，按以下步骤创建用户：

- 创建用户命令中<username>需替换为要创建用户的用户名。例如创建名为exampleuser的用户时，可执行sudo useradd -m exampleuser。sudo useradd -m <username>

- 设置密码/密钥对

## 绑定密钥对

- 

在本机生成密钥对文件。

重要

安全起见，请不要在实例中通过ssh-keygen创建密钥对，请不要将生成的私钥保存在需要连接的ECS实例中。

不同的工具生成密钥对的步骤有所差别，本步骤以ssh-keygen工具为例。

输入以下命令生成密钥对。

ssh-keygen -t rsa -b 2048 -f id_rsa

参数说明：

- 

-t rsa：代表密钥类型为rsa密钥对。

- 

-b 2048：代表密钥长度为2048位。

- 

-f id_rsa：代表生成密钥对的文件名以及保存位置。

系统将提示你输入一个口令（passphrase）。这个口令用于保护你的私钥。设置口令是推荐的安全措施。如果不需要口令，直接按回车键继续。

命令执行成功后，当前目录下会生成两个文件：

- 

id_rsa：你的私钥。

- 

id_rsa.pub：你的公钥。

重要

请妥善保存私钥，不要泄漏给他人。

- 

为用户绑定公钥。

- 

创建authorized_keys配置文件。

如果/root/.ssh目录或authorized_keys文件不存在，运行以下命令创建。

命令中<username>为待绑定公钥用户的用户名。sudo mkdir /home/<username>/.ssh sudo touch /home/<username>/.ssh/authorized_keys

- 

添加公钥。

使用文本编辑器（如[Vim](products/ecs/documents/user-guide/use-the-vim-editor.md)）打开authorized_keys文件。

sudo vim /home/<username>/.ssh/authorized_keys

将你的公钥内容粘贴到文件中。可配置多个公钥，每个公钥占一行。配置完成后保存并关闭文件。

- 

设置文件权限。

SSH 要求严格的权限设置，错误的权限会导致 SSH 登录失败。

运行以下命令，设置正确的权限。

sudo chown -R <username>:<username> /home/<username>/.ssh sudo chmod 700 /home/<username>/.ssh sudo chmod 600 /home/<username>/.ssh/authorized_keys

- 

开启SSH服务的公钥认证功能。

配置公钥后，必须在服务器上启用 SSH 公钥认证。否则，密钥登录会失败。

- 

备份SSH配置文件/etc/ssh/sshd_config。

sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak

- 

使用文本编辑器（如[Vim](products/ecs/documents/user-guide/use-the-vim-editor.md)）打开/etc/ssh/sshd_config文件，并找到PubkeyAuthentication参数，设置为yes，代表开启公钥认证功能。

sudo vim /etc/ssh/sshd_config

- 

重启SSH服务以应用更改。

以Alibaba Cloud Linux 3为例：

sudo systemctl restart sshd部分操作系统（Ubuntu/Debian）的SSH服务名为ssh而非sshd，请根据实际情况调整。

重要

如果正通过SSH的方式连接到实例，重启服务可能导致连接中断，服务重启完成后，即可重新连接。

## 设置密码

运行以下命令：

请将<username>替换为待修改密码的用户名。sudo passwd <username>

输入新密码后按Enter键，再次输入新密码并按Enter键。

修改成功后，系统输出类似以下信息：

passwd: all authentication tokens updated successfully.

- （验证）使用新创建的用户远程登录到ECS实例。

## Windows系统

重要

默认情况下，Windows系统仅支持两个不同的用户同时通过RDP远程连接实例，如需两个以上用户同时登录Windows实例，需要使用微软的[远程桌面服务（Remote Desktop Services）](https://learn.microsoft.com/zh-cn/windows-server/remote/remote-desktop-services/remote-desktop-services-overview)的能力。

[使用](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)[Workbench](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)[登录实例](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)，按以下步骤操作：

- 创建用户

- 

- 

- 

- 

| 打开控制面板，找到 用户账户 ， 单击下面的 更改账户类型 。 |  |
| --- | --- |
| 在 管理账户 页面，单击 添加用户账户 ，进入 添加用户 页面。 |  |
| 在添加用户页面，根据界面提示，设置新用户的用户名及密码。 本示例以创建 exampleuser 为例，请根据需求设置 用户名 。 单击 下一步 ，然后单击 完成 。完成新用户的创建。 |  |


- 将新用户添加到Remote Desktop Users用户组

只有Remote Desktop Users用户组下的用户，才能以远程登录的方式登录实例。

- 

- 

- 

- 

- 

- 

| 在任务栏的搜索框搜索 计算机管理 ， 单击搜索到的 计算机管理 进入 计算机管理 页面。 |  |
| --- | --- |
| 在 系统工具 > 本地用户和组 > 组 下，找到 Remote Desktop Users 用户组。双击进入 Remote Desktop Users 属性 页面。 |  |
| 操作流程如图所示。 在 Remote Desktop Users 属性 页面，单击 添加 。 输入 步骤 2 中创建用户的用户名，单击 检查名称 ，之后输入框会自动根据输入的用户名补全用户的名称全称。 单击 确定 。在 Remote Desktop Users 属性 页面依次单击 应用 、 确定 。完成将用户添加到用户组的操作。 |  |


- （验证）使用新创建的用户远程登录到ECS实例。

## 四、常见问题

Q1：ECS默认用户名、初始用户名、默认登录名、初始登录名是什么？

- 

Linux系统实例：默认为root，若创建实例时设置了使用ecs-user则为ecs-user。

- 

Windows系统实例：默认为Administrator。

Q2：ECS默认密码、初始密码、默认远程密码、初始登录密码是什么？

没有。

出于安全考虑，阿里云不会为ECS实例设置默认或初始密码。如在创建实例时未设置密码，可使用[重置密码（不知道/忘记原密码）](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

Q3：如何查看实例密码？

阿里云不会保存您设置的实例密码，因此不支持查看。

Q4：凭证找回（忘记登录名、忘记密码）

忘记登录名：可通过控制[重置密码](products/ecs/documents/user-guide/instance-logon-credential-management.md)功能查看。创建实例时设置的登录名会在重置实例密码对话框的最上方显示。

忘记密码：[重置密码（不知道/忘记原密码）](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

Q5：在线重置密码失败的原因？

大多数情况下，是由于实例中的安全软件拦截云助手修改密码指令造成的。建议使用[离线重置密码](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

Q6：「root」和「ecs-user」切换

- 

原来使用root，切换到ecs-user

仅通过[自定义购买](products/ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)创建部分Linux镜像的实例时，支持设置ecs-user。

实例创建后，不支持直接切换到ecs-user，但可通过[添加多用户远程登录](products/ecs/documents/user-guide/instance-logon-credential-management.md)的方式自行创建ecs-user后，并为该用户授予sudo权限，达到切换的效果。

- 

原来使用ecs-user，切换到root

强烈建议继续使用ecs-user并通过sudo执行需要特权的命令，而不是直接使用root用户登录。

如果确实需要在已登录的会话中切换到root用户，可通过ecs-user登录实例后，执行sudo su命令，切换到root用户。

控制台的离线重置密码、绑定密钥对等功能仅对创建实例时设置的登录名生效。

Q7：如何让Linux实例同时支持「SSH 密钥对」和「密码」两种登录方式？

可通过修改 SSH 服务的/etc/ssh/sshd_config配置文件 实现。

- 

开启SSH密钥对认证（推荐、更安全）：由PubkeyAuthentication选项控制，设为yes代表开启密钥对认证。修改配置后需重启实例的SSH服务。

- 

开启SSH密码认证（不推荐、安全系数低）：由PasswordAuthentication选项控制，设为yes代表开启密码认证。修改配置后需重启实例的SSH服务。

Q8：使用Terraform创建实例时，如何设置ECS登录用户名？

ECS 实例的默认用户名通常由镜像决定（Linux默认为root，Windows默认为Administrator）。[使用](products/ecs/documents/developer-reference/create-and-use-an-ecs-instance-by-using-terraform.md)[Terraform](products/ecs/documents/developer-reference/create-and-use-an-ecs-instance-by-using-terraform.md)[创建](products/ecs/documents/developer-reference/create-and-use-an-ecs-instance-by-using-terraform.md)[ECS](products/ecs/documents/developer-reference/create-and-use-an-ecs-instance-by-using-terraform.md)[实例](products/ecs/documents/developer-reference/create-and-use-an-ecs-instance-by-using-terraform.md)时，可通过image_options块中的login_as_non_root参数来配置实例使用非root用户登录。

- 

参数：login_as_non_root（布尔值）。

- 

设置方法：将其设置为true。

- 

结果：实例的登录用户名将变为ecs-user。

[上一篇：选择ECS远程连接方式](products/ecs/documents/user-guide/connect-to-instance.md)[下一篇：通过Workbench连接实例](products/ecs/documents/user-guide/workbench-overview.md)

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
