## 使用限制
实例处于运行中（Running）状态，并安装了云助手Agent。
创建的Bat、PowerShell或者Shell脚本和自定义参数在Base64编码后，使用场景与文件大小说明如下：
创建命令：综合大小不能超过18 KB。
立即执行并保存命令：综合大小不能超过18 KB。
立即执行但不保存命令：综合大小不能超过24 KB。
上传文件：文件大小不能超过32 KB。
一条命令中，自定义参数的个数不能超过20个。
您只能在以下操作系统中运行云助手命令：
Alibaba Cloud Linux
CentOS 6/7/8及更高版本
CoreOS
Debian 8/9/10及更高版本
OpenSUSE
RedHat 5/6/7及更高版本
说明
RedHat中需要您自行下载rpm包安装云助手Agent，具体操作，请参见[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
SUSE Linux Enterprise Server 11/12/15及更高版本
Ubuntu 12/14/16/18及更高版本
FreeBSD 11/12/13/14及更高版本
Window Server 2012/2016/2019及更高版本
说明
使用ECS公共镜像创建的实例会默认安装云助手Agent。
使用自定义镜像或者云市场镜像创建的实例需要您首先确认操作系统是否支持云助手，再自行安装云助手Agent。具体步骤请参见[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
