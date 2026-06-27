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
#cloud-config packages: - nginx runcmd: - systemctl start nginx.servic
