## Windows
解压程序包，例如解压后的目录为D:\tool\terraform。
在桌面右键单击此电脑，选择属性>高级系统设置>环境变量>系统变量/用户变量。
在系统变量/用户变量中单击Path，选择编辑 > 新建，输入Terraform的解压目录（如D:\tool\terraform），单击确定完成配置。
运行terraform验证路径配置。
terraform
命令运行后将显示可用的Terraform选项的列表，如下所示，表示安装完成。
➜ ~ terraform Usage: terraform [global options] <subcommand> [args] The available commands for execution are listed below. The primary workflow commands are given first, followed by less common or more advanced commands. Main commands: init Prepare your working directory for other commands validate Check whether the configuration is valid plan Show changes required by the current configuration apply Create or update infrastructure destroy Destroy previously-created infrastructure All other commands: console Try Terraform expressions at an interactive command prompt fmt Reformat your configuration in the standard style force-unlock Release a stuck lock on the current workspace get Install or upgrade remote Terraform modules graph Generate a Graphviz graph of the steps in an operation import Associate existing infrastructure with a Terraform resource login Obtain and save credentials for a remote host logout Remove locally-stored credentials for a remote host m
