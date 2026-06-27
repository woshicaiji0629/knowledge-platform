的权限。本文提供的示例代码需要创建实例、VPC、交换机等资源，建议授予以下权限：

| 云产品 | 授予权限 |
| --- | --- |
| 专有网络 VPC | 本示例选择系统策略：AliyunVPCFullAccess |
| 云服务器 ECS | 本示例选择系统策略：AliyunECSFullAccess |

安装和配置CLI。调试使用阿里云CLI前，您需要先安装阿里云CLI。阿里云CLI提供了Windows、Linux和macOS三种操作系统下的安装服务，请根据您使用设备的操作系统选择：
安装CLI。
[安装](https://help.aliyun.com/zh/cli/install-cli-on-windows#task-525890)[CLI（Windows）](https://help.aliyun.com/zh/cli/install-cli-on-windows#task-525890)
[安装/更新 CLI](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli#task-592837)
[安装](https://help.aliyun.com/zh/cli/install-cli-on-macos#task-592875)[CLI（macOS）](https://help.aliyun.com/zh/cli/install-cli-on-macos#task-592875)
配置CLI。
配置调用阿里云资源所需的身份凭证信息、服务请求地域等。具体配置，请参见[配置身份凭证](https://help.aliyun.com/zh/cli/configure-credentials/#41e7063556zzq)。
如果您只是用于临时调试，不需要安装阿里云CLI，您可使用阿里云提供的云命令行[Cloud Shell](https://shell.aliyun.com/)。更多信息，请参见[什么是云命令行？](https://help.aliyun.com/zh/cloud-shell/what-is-the-cloud-command-line)。登录阿里云控制台，单击顶部导航栏中工单右侧的 Cloud Shell 图标（终端样式图标）即可启动 Cloud Shell。
