# 日志服务安装、运行、升级、卸载Logtail-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/install-run-upgrade-and-uninstall-logtail

# 安装、运行、升级、卸载Logtail
如果您要使用日志服务Project采集服务器日志，首先需要在目标服务器上安装Logtail客户端。本文介绍如何在目标服务器中安装、运行，升级和卸载Logtail。
## 概述
日志服务Logtail的使用场景根据目标服务器类型可分为以下两类：
[主机场景](install-run-upgrade-and-uninstall-logtail.md)：适用于物理服务器、云服务器（ECS）等传统计算环境。
[容器场景](install-run-upgrade-and-uninstall-logtail.md)：基于Kubernetes容器化平台部署的业务场景。
请根据您的服务器运行环境选择对应的方案，不同场景的使用流程及配置要求存在差异。若混合环境部署，需分别完成对应环境的安装配置。
## 主机场景
### 安装Logtail
安装Logtail有一键安装与手动安装两种方式，当且仅当您使用的是ECS机器，且ECS与Project属于同账号同地域时，日志服务才支持一键安装Logtail。否则请使用手动方式安装Logtail。
## 一键安装Logtail
日志服务可一键在ECS中安装Logtail，借助OOS编排能力，无需登录ECS手动执行安装步骤。如果您使用阿里云主账号登录，默认拥有所有操作权限，可直接进行相关操作。
若您使用RAM用户登录，请联系主账号授予操作OOS资源的权限，主账号可以通过系统权限或自定义权限为您[创建](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md)[RAM](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md)[用户及授权](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md)：
系统权限：
AliyunOOSFullAccess：用于管理系统运维管理（OOS）的所有权限。
AliyunECSFullAccess：管理ECS的权限。
自定义权限：若对数据安全要求高，可以[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)实现精细化授权。如下为操作OOS资源的权限策略：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ecs:DescribeTagKeys", "ecs:DescribeTags", "ecs:DescribeInstances", "ecs:DescribeInvocationResults", "ecs:RunCommand", "ecs:DescribeInvocations", "ecs:InvokeCommand" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "oos:ListTemplates", "oos:StartExecution", "oos:ListExecutions", "oos:GetExecutionTemplate", "oos:ListExecutionLogs", "oos:ListTaskExecutions" ], "Resource": "*" } ] }
通过以下操作步骤，您可以实现在ECS实例中一键安装Logtail的同时，完成机器组的创建和配置：
登录[日志服务控制台](https://sls.console.aliyun.com/)，单击管理日志资源的Project查看日志库列表，单击存放日志的LogStore名称前的展开，之后单击数据接入后的，在弹框中选择文本日志接入模板，单击立即接入。
日志服务提供了正则、单行、多行等多种文本日志接入模板，各模板之间除了日志解析插件不同外，其余配置完全相同；同时，模板内支持添加、删除日志解析插件。此处您可以根据采集日志的特点选择模板，也可以任意选择文本日志模板后再根据日志特点进行插件配置。
在机器组配置页面，选择主机场景和ECS安装环境后单击创建机器组。
在创建机器组面板中，选择与Project同地域的ECS实例（ECS实例可以选择多台），单击安装并创建为机器组，等待安装完成，配置机器组名称并单击确定。
如果安装失败或一直处于等待中，请检查ECS地域是否与Project相同。
安装后，您可前往资源>>>机器组页面，单击新建的机器组，在机器组配置>>>机器组状态区域，查看心跳状态。如果心跳为OK则表示创建成功。
## 手动安装Logtail
请根据表格选择Logtail下载与安装方式：
说明
示例代码中${region_id}为日志服务Project所在地域，请参见[开服地域](sls-supported-regions1.md)后替换，例如华东 1（杭州）对应的${region_id}为cn-hangzhou。
重要
如果您使用的机器配置较低或者操作系统较为陈旧，安装Logtail2.0可能会出现兼容性问题，导致软件无法正常运行，建议下载版本[1.8.7](https://logtail-release-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/linux64/1.8.7/logtail.sh)，执行命令./logtail.sh install ${region_id} -v 1.8.7安装。
传输加速安装方式不支持金融云和政务云。
| 主机类型 | 架构 | 下载方式 | 安装方式 |
| --- | --- | --- | --- |
| Linux 支持如下版本的 Linux x86-64（64 位）服务器。 Alibaba Cloud Linux 2、3 Anolis OS 7、8 CentOS Linux 6、7、8 Debian GNU/Linux 8、9、10、11、12 RedHat Enterprise 6、7、8、9 OpenSUSE 15.1、15.2、42.3 SUSE Linux Enterprise Server 11、12、15 Ubuntu 14.04、16.04、18.04、20.04、22.04、24.0 其他基于 glibc 2.5 及以上版本的 Linux 操作系统（2.0 以上版本的 Logtail 需要 glibc2.6 及以上版本） CPU 支持 sse4_2 和 avx 指令集（2.0 以上版本的 Logtail） 支持如下版本的 Linux ARM（64 位）服务器。 Alibaba Cloud Linux 3.2 ARM 版 Anolis OS 8.2 ARM 版及以上版本 CentOS 8.4 ARM 版 Debian 11.2、12.2 ARM 版 Ubuntu 20.04、22.04、24.04 ARM 版 CPU 架构要求最低为 ARMv8.2-A（2.0 以上版本的 iLogtail） | ARM | 主机可联网，直接下载： #内网下载方式 wget http://logtail-release-${region_id}.oss-${region_id}-internal.aliyuncs.com/linux64/logtail.sh -O logtail.sh; #公网下载方式 wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh -O logtail.sh; | 根据 [网络情况选择](select-a-network-type.md) 安装命令： #公网方式安装 chmod +x logtail.sh; ./logtail.sh install ${region_id}-internet #服务器分布在海外各地的自建机房或者来自海外云厂商，使用公网传输数据可能会出现网络延迟高、传输不稳定等问题，推荐选择传输加速传输数据。 chmod +x logtail.sh; ./logtail.sh install ${region_id}-acceleration #内网方式安装，适用于自建 IDC 已经打通内网的情况 chmod +x logtail.sh; ./logtail.sh install ${region_id} |
| x86-64 |  |  |  |
| ARM | 主机离线，需先在可以访问公网的服务器上下载安装脚本与安装包： wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh; wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/aarch64/logtail-linux64.tar.gz | 请 将安装脚本和安装包拷贝至需要安装 Logtail 的服务器上后， 根据 [网络情况选择](select-a-network-type.md) 安装命令： #公网方式安装 chmod +x logtail.sh; ./logtail.sh install-local ${region_id}-internet #服务器分布在海外各地的自建机房或者来自海外云厂商，使用公网传输数据可能会出现网络延迟高、传输不稳定等问题，推荐选择传输加速传输数据。 chmod +x logtail.sh; ./logtail.sh install-local ${region_id}-acceleration |  |
| x86-64 | 主机离线，需先在可以访问公网的服务器上下载安装脚本与安装包： wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh; wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail-linux64.tar.gz |  |  |
| Windows 说明 如果是 Microsoft Windows Server 2008 和 Microsoft Windows 7，则支持在其 X86 版本或 X86_64 版本中安装 Logtail。 如果是其他 Windows 操作系统，则只支持在其 X86_64 版本中安装 Logtail。 Microsoft Windows Server 2008、2012、2016、2019、2022、2025 Microsoft Windows 7 Microsoft Windows 10 Microsoft Windows Server Version 1909 Microsoft Windows Server Version 2004 | 32 位 | 中国地域 ： [Logtail](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/win/win32/1.6.1.0/logtail_installer.zip) [安装包 32](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/win/win32/1.6.1.0/logtail_installer.zip) [位](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/win/win32/1.6.1.0/logtail_installer.zip) | 解压安装包，以管理员身份运行 Windows PowerShell，进入 logtail_installer 目录（您的安装包的解压目录）。根据 [网络情况选择](select-a-network-type.md) 安装命令： #公网方式安装 .\logtail_installer.exe install ${region_id}-internet #服务器分布在海外各地的自建机房或者来自海外云厂商，使用公网传输数据可能会出现网络延迟高、传输不稳定等问题，推荐选择传输加速传输数据。 .\logtail_installer.exe install ${region_id}-acceleration |
| 海外地域 ： [Logtail](https://logtail-release-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/win/win32/1.6.1.0/logtail_installer.zip) [安装包 32](https://logtail-release-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/win/win32/1.6.1.0/logtail_installer.zip) [位](https://logtail-release-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/win/win32/1.6.1.0/logtail_installer.zip) |  |  |  |
| 64 位 | 中国地域 ： [Logtail](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/win/win64/1.6.1.0/logtail_installer.zip) [安装包 64](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/win/win64/1.6.1.0/logtail_installer.zip) [位](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/win/win64/1.6.1.0/logtail_installer.zip) |  |  |
| 海外地域 ： [Logtail](https://logtail-release-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/win/win64/1.6.1.0/logtail_installer.zip) [安装包 64](https://logtail-release-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/win/win64/1.6.1.0/logtail_installer.zip) [位](https://logtail-release-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/win/win64/1.6.1.0/logtail_installer.zip) |  |  |  |
## ECS金融云和政务云
### ECS金融云
请根据日志服务Project所在的地域执行对应的安装命令。
| Project 所在的地域 | 安装命令 |
| --- | --- |
| 华东 1 金融云 | wget http://logtail-release-cn-hangzhou-finance-1.oss-cn-hzfinance-internal.aliyuncs.com/linux64/logtail.sh -O logtail.sh; chmod +x logtail.sh; ./logtail.sh install cn-hangzhou-finance |
| 华东 1 金融云（公网） | wget http://logtail-release-cn-hangzhou-finance-1.oss-cn-hzfinance.aliyuncs.com/linux64/logtail.sh -O logtail.sh; chmod +x logtail.sh; ./logtail.sh install cn-hangzhou-finance-internet |
| 华东 2 金融云 | wget http://logtail-release-cn-shanghai-finance-1.oss-cn-shanghai-finance-1-internal.aliyuncs.com/linux64/logtail.sh -O logtail.sh; chmod +x logtail.sh; ./logtail.sh install cn-shanghai-finance-1 |
| 华东 2 金融云（公网） | wget http://logtail-release-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/linux64/logtail.sh -O logtail.sh; wget http://logtail-release-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/linux64/logtail-linux64.tar.gz -O logtail-linux64.tar.gz; chmod +x logtail.sh; ./logtail.sh install-local cn-shanghai-finance-1-internet |
| 华北 2 金融云（邀测） | wget http://logtail-release-cn-beijing-finance-1.oss-cn-beijing-finance-1-internal.aliyuncs.com/linux64/logtail.sh -O logtail.sh; chmod +x logtail.sh; ./logtail.sh install cn-beijing-finance-1 |
| 华北 2 金融云（邀测） （公网） | wget http://logtail-release-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/linux64/logtail.sh -O logtail.sh; wget http://logtail-release-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/linux64/logtail-linux64.tar.gz -O logtail-linux64.tar.gz; chmod +x logtail.sh; ./logtail.sh install-local cn-beijing-finance-1-internet |
| 华南 1 金融云 | wget http://logtail-release-cn-shenzhen-finance-1.oss-cn-szfinance-internal.aliyuncs.com/linux64/logtail.sh -O logtail.sh; chmod +x logtail.sh; ./logtail.sh install cn-shenzhen-finance-1 |
| 华南 1 金融云（公网） | wget http://logtail-release-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/linux64/logtail.sh -O logtail.sh; wget http://logtail-release-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/linux64/logtail-linux64.tar.gz -O logtail-linux64.tar.gz; chmod +x logtail.sh; ./logtail.sh install-local cn-shenzhen-finance-1-internet |
### 政务云
请根据日志服务Project所在的地域执行对应的安装命令。
| Project 所在的地域 | 安装命令 |
| --- | --- |
| 华北 2 阿里政务云 1 | wget http://logtail-release-cn-north-2-gov-1.oss-cn-north-2-gov-1.aliyuncs.com/linux64/logtail.sh -O logtail.sh;chmod +x logtail.sh; ./logtail.sh install cn-north-2-gov-1 |
### 批量安装Logtail
批量安装Logtail有如下两种方式：
OOS编排：适合有权限要求场景，并发度较高，适合大规模批量操作。具体请参考[使用](best-practice-use-oos-to-batch-install-or-upgrade-logtail.md)[OOS](best-practice-use-oos-to-batch-install-or-upgrade-logtail.md)[批量安装或升级](best-practice-use-oos-to-batch-install-or-upgrade-logtail.md)[Logtail](best-practice-use-oos-to-batch-install-or-upgrade-logtail.md)。
ECS云助手功能：简单易用，直接通过命令的方式执行临时任务。具体操作步骤如下：
访问[ECS](https://ecs.console.aliyun.com/cloud-assistant/region)[控制台-云助手](https://ecs.console.aliyun.com/cloud-assistant/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
在ECS 云助手页面右上角，单击创建/执行命令。
在创建执行命令面板中，命令内容输入安装命令（此处以公网安装方式为例，更多安装命令，请参见[安装](install-run-upgrade-and-uninstall-logtail.md)[Logtail](install-run-upgrade-and-uninstall-logtail.md)）。
此处用到的安装命令如下所示：
#!/bin/bash region_id='cn-hangzhou' wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh -O logtail.sh chmod +x logtail.sh ./logtail.sh install ${region_id}-internet
重要
安装Logtail后，如果ECS的网络由经典网络切换至VPC，则需要更新Logtail配置。更多信息，请参见[ECS](update-a-logtail-configuration-after-i-switch-the-network-type-to-vpc.md)[经典网络切换为](update-a-logtail-configuration-after-i-switch-the-network-type-to-vpc.md)[VPC](update-a-logtail-configuration-after-i-switch-the-network-type-to-vpc.md)[后，如何更新机器组配置？](update-a-logtail-configuration-after-i-switch-the-network-type-to-vpc.md)。
在选择实例区域，确认目标实例的Agent状态是正常状态（如果不是正常状态，请参见[安装云助手](../../ecs/documents/user-guide/install-the-cloud-assistant-agent.md)[Agent](../../ecs/documents/user-guide/install-the-cloud-assistant-agent.md)，完成云助手安装。），选择目标实例，单击执行。然后执行状态为成功执行。如果执行失败，请参见[查看执行结果及修复常见问题](../../ecs/documents/user-guide/check-execution-results-and-troubleshoot-common-issues.md)。
### 启动和停止Logtail
## Linux
启动Logtail
sudo /etc/init.d/ilogtaild start
停止Logtail
sudo /etc/init.d/ilogtaild stop
## Windows
登录目标服务器。
选择开始>>>控制面板>>>管理工具>>>服务。
在服务对话框中，选择对应的服务。
如果是0.x.x.x版本，选择LogtailWorker服务。
如果是1.0.0.0及以上版本，选择LogtailDaemon服务。
右键选择对应的操作，包括启动、停止或重新启动。
### 查看Logtail状态及版本
## Linux
### 查看Logtail状态
使用sudo /etc/init.d/ilogtaild status命令查看Logtail状态。若系统返回ilogtail is running，表示已安装Logtail。如果Logtail状态显示未运行，请卸载后重新安装。
### 查看Logtail版本
Logtail会将版本信息存储在/usr/local/ilogtail/app_info.json文件的logtail_version字段中。您可以通过以下命令查看Logtail版本信息。
cat /usr/local/ilogtail/app_info.json
返回结果如下所示：
{ "logtail_version" : "0.16.30", }
## Windows
### 查看Logtail状态
您可以通过查看Logtail状态确定是否已在目标服务器上安装Logtail。
打开运行窗口，输入services.msc，打开服务窗口。
查看LogtailDaemon服务（Logtail 1.0.0.0及以上版本）或LogtailWorker服务（Logtail 0.x.x.x版本）的运行状态。
如果显示正在运行，表示已安装Logtail。
### 查看Logtail版本
您可以通过安装路径下的app_info.json文件中的logtail_version字段查看Logtail版本。
例如，以下内容表示Logtail的版本号为1.0.0.0。
{ "logtail_version" : "1.0.0.0" }
### 升级Logtail
## Linux
重要
升级Logtail时，请使用upgrade命令。若使用install命令，将会执行覆盖安装，丢失原配置。
升级过程中，Logtail会短暂停止运行，升级完成后，Logtail 将自动启动，并注册为开机启动项。升级仅覆盖必要的文件，配置文件和Checkpoint文件将被保留，确保升级期间日志不会丢失。
说明
示例代码中${region_id}为日志服务Project所在地域，请参见[开服地域](sls-supported-regions1.md)后替换，例如华东 1（杭州）对应的${region_id}为cn-hangzhou。
请根据表格选择Logtail升级方式：
| 操作系统 | 下载方式 | 升级方式 |
| --- | --- | --- |
| ARM 与 x86-64 | 主机可联网： wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh -O logtail.sh; | 下载完成后执行升级命令： chmod +x logtail.sh; sudo ./logtail.sh upgrade; |
| ARM | 主机离线，需先在可以访问公网的服务器上下载安装脚本与安装包： wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh; wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/aarch64/logtail-linux64.tar.gz; | 请 将安装脚本和安装包拷贝至需要升级 Logtail 的服务器上后，执行如下升级命令： chmod +x logtail.sh; ./logtail.sh upgrade-local; |
| x86-64 | 主机离线，需先在可以访问公网的服务器上下载安装脚本与安装包： wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh; wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail-linux64.tar.gz; |  |
如果显示以下信息，则表示升级成功。
stop successfully Stop logtail successfully. Upgrading logtail files ... Upgrade logtail files successfully. Starting logtail ... ilogtail is running Upgrade logtail successfully. { "UUID" : "XXXXXXXX-XXXX", "compiler" : "GCC 9.3.1", "hostname" : "xxx", "instance_id" : "XXXXXXXX-XXXX_172.16.0.75_1730950372", "ip" : "172.16.0.75", "logtail_version" : "2.0.8", "os" : "Linux; 5.10.134-13.an8.x86_64; #1 SMP Mon Jan 9 10:39:46 CST 2023; x86_64", "update_time" : "2024-11-07 11:32:52" }
## Windows
升级的操作和安装Logtail的操作相同，您只需要下载并解压最新的安装包，然后按照步骤执行安装。更多信息，请参见[安装](install-run-upgrade-and-uninstall-logtail.md)[Logtail](install-run-upgrade-and-uninstall-logtail.md)。
重要
升级相当于自动卸载并重新安装，会删除您原先安装目录中的内容，请您在执行升级前做好备份工作。
在Windows 64位操作系统中，如果您要将32位Logtail升级到64位，需要先卸载32位的Logtail，再重新安装64位的Logtail。
### 卸载Logtail
## Linux
根据日志服务Project所在地域，获取对应的${region_id}。替换${region_id}后，执行以下命令卸载Logtail。
重要
各地域对应的${region_id}请参见[开服地域](sls-supported-regions1.md)，例如华东 1（杭州）对应的${region_id}为cn-hangzhou。
wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh -O logtail.sh; chmod +x logtail.sh; ./logtail.sh uninstall
## Windows
以管理员身份运行Windows PowerShell或cmd进入logtail_installer目录（安装包的解压目录），执行如下命令。
.\logtail_installer.exe uninstall
卸载成功后，您的Logtail的安装目录会被删除，但仍有部分配置被保留在C:\LogtailData目录中，您可以根据实际情况进行手动删除。遗留信息包括：
checkpoint：存放所有Logtail插件的Checkpoint信息。只有您使用了Logtail插件后，才会出现此文件。
user_config.d：存放本地采集配置的目录。
其中以.json结尾的文件会被视为采集配置，格式类似于/usr/local/ilogtail/user_log_config.json。
logtail_check_point：存放Logtail主体部分的Checkpoint信息。
users：存放您所配置的用户标识文件。
## 容器场景
### 安装Logtail组件
当您使用的是ACK集群且集群与日志服务属于同一个阿里云账号时，参考ACK集群安装方式。若使用自建集群或ACK集群与日志服务属于不同的阿里云账号，请参考自建集群安装方式。
## ACK集群安装方式
重要
此操作仅适用于专有版Kubernetes和托管版Kubernetes。
### 为已有的ACK集群安装Logtail组件
登录[容器服务管理控制台](https://cs.console.aliyun.com)。
在集群列表页面中，单击目标集群最右侧的更多>运维管理>组件管理
在日志与监控页签中，找到logtail-ds，然后单击安装。
安装完成后，日志服务会自动生成名称k8s-log-${your_k8s_cluster_id}的Project。
### 新建ACK集群时安装Logtail组件
登录[容器服务管理控制台](https://cs.console.aliyun.com)。
在左侧导航栏中，单击集群列表。
在集群列表页面中，单击创建集群。
在组件配置配置项页中，选中使用日志服务。
说明
本操作仅介绍开启日志服务的关键步骤。关于创建集群的具体操作，请参见[创建](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。
当选中使用日志服务后，会出现创建项目（Project）的提示。关于日志服务管理日志的组织结构，请参见[项目（Project）](project.md)。有以下两种创建Project方式。
使用已有 Project
您可以选择一个已有的Project来管理采集到的容器日志。
创建新 Project
日志服务自动创建一个Project来管理采集到的容器日志。其中ClusterID为您新建的Kubernetes集群的唯一标识。
在日志服务区域勾选使用日志服务，选择创建新 Project后，系统将自动创建名称为k8s-log-{ClusterID}的 Project。
安装完成后，在选择的Project下自动创建如下日志服务资源。
| 资源类型 | 资源名称 | 作用 | 示例 |
| --- | --- | --- | --- |
| 机器组 | k8s-group-${your_k8s_cluster_id} | logtail-daemonset 的机器组，主要用于日志采集场景。 | k8s-group-my-cluster-123 |
| k8s-group-${your_k8s_cluster_id}-statefulset | logtail-statefulset 的机器组，主要用于指标采集场景。 | k8s-group-my-cluster-123-statefulset |  |
| k8s-group-${your_k8s_cluster_id}-singleton | 单实例机器组，主要用于部分单实例采集配置。 | k8s-group-my-cluster-123-singleton |  |
| LogStore | config-operation-log | 用于存储 Logtail 组件中的 alibaba-log-controller 日志。建议不要在此 LogStore 下创建采集配置。该 LogStore 可以删除，删除后不会再采集 alibaba-log-controller 的运行日志。该 LogStore 的收费标准和普通的 LogStore 收费标准是一致的，具体请参见 [按写入数据量计费模式计费项](billing-items-in-the-pay-per-data-write-mode.md) 。 | config-operation-log |
## 自建集群安装方式
登录[日志服务控制台](https://sls.console.aliyun.com)，创建Project。具体操作，请参见[管理](manage-a-project.md)[Project](manage-a-project.md)。建议创建一个以k8s-log-custom-开头的Project，例如k8s-log-custom-sd89ehdq。
登录您的Kubernetes集群，根据地域选择命令下载Logtail及其他依赖组件。
#中国地域 wget https://logtail-release-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/kubernetes/0.5.5/alibaba-cloud-log-all.tgz; tar xvf alibaba-cloud-log-all.tgz; chmod 744 ./alibaba-cloud-log-all/k8s-custom-install.sh #海外地域 wget https://logtail-release-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/kubernetes/0.5.5/alibaba-cloud-log-all.tgz; tar xvf alibaba-cloud-log-all.tgz; chmod 744 ./alibaba-cloud-log-all/k8s-custom-install.sh
修改配置文件./alibaba-cloud-log-all/values.yaml。
##
| 参数说明 | values.yaml # ===================== 必需要补充的内容 ===================== # 目标 Project 名称。 SlsProjectName: # Project 所属地域。 Region: # Project 所属阿里云账号 ID，需使用双引号（""）包裹。 AliUid: "11099" # 阿里云账号或 RAM 用户的 AccessKey ID 和 AccessKey Secret，需具备 AliyunLogFullAccess 权限。 AccessKeyID: AccessKeySercret: # 自定义集群 ID，命名只支持大小写，数字，短划线(-)。 ClusterID: # ========================================================== # 是否开启指标采集相关组件，可选参数: true、false, 默认 true。 SlsMonitoring: true # 网络类型，可选参数：Internet、Intranet，默认使用 Internet。 Net: Internet # 容器运行时是否为 containerd，可选参数: true, false, 默认 false。 SLS_CONTAINERD_USED: true |
| --- | --- |
| SlsProjectName Project 名称，Logtail 将上传日志到该 Project 中。 |  |
| Region 您的 Project 所在的地域 ID。例如华东 1（杭州）的地域 ID 为 cn-hangzhou 。更多信息，请参见 [开服地域](sls-supported-regions1.md) 。 |  |
| AliUid Project 所属账号的阿里云主账号 ID，需使用双引号包裹（""），例如 AliUid: "11**99" 。如何获取，请参见 [获取日志服务所在的阿里云账号（主账号）ID](configure-a-user-identifier.md) 。 |  |
| AccessKeyID Project 所属账号的阿里云账号的 AccessKey ID。推荐使用 RAM 用户的 AccessKey，并授予 RAM 用户 AliyunLogFullAccess 权限。相关操作，请参见 [创建](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md) [RAM](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md) [用户及授权](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md) 。 |  |
| AccessKeySercret Project 所属账号的阿里云账号的 AccessKey Secret。推荐使用 RAM 用户的 AccessKey 并授予 RAM 用户 AliyunLogFullAccess 权限。相关操作，请参见 [创建](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md) [RAM](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md) [用户及授权](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md) 。 |  |
| ClusterID 自定义集群 ID，命名只支持大小写字母、数字、短划线(-)。该参数对应后面操作中的 ${your_k8s_cluster_id} 。不同的 Kubernetes 集群，请勿配置相同的集群 ID。 |  |
| SlsMonitoring 是否开启集群指标数据采集的开关，可选项： true（默认值）：开启。 false：不开启。 |  |
| Net Logtail 传输数据时的网络类型，若您的集群未打通阿里云内网访问，请使用公网。可选项： Internet（默认值）：公网。 Intranet：内网。 |  |
| SLS_CONTAINERD_USED 设定容器运行时是否为 containerd，可选项： true：是。 false（默认值）：否。 在使用 containerd 作为容器运行时的自建 Kubernetes 集群中，若未开启相关参数，可能导致日志无法被 Logtail 采集。 |  |
安装Logtail及其他依赖组件。
说明
您可以执行echo "$(uname -s | tr '[:upper:]' '[:lower:]')-$(uname -m)"命令查询您主机的操作系统-架构。k8s-custom-install.sh支持的操作系统-架构有：linux-386、linux-amd64、linux-arm、linux-arm64、linux-ppc64le、linux-s390x和darwin-amd64。
bash k8s-custom-install.sh; kubectl apply -R -f result
安装完成后，在该Project下自动创建如下日志服务资源。若创建不成功请仔细核对修改的values.yaml。
| 资源类型 | 资源名称 | 作用 | 示例 |
| --- | --- | --- | --- |
| 机器组 | k8s-group-${your_k8s_cluster_id} | logtail-daemonset 的机器组，主要用于日志采集场景。 | k8s-group-my-cluster-123 |
| k8s-group-${your_k8s_cluster_id}-statefulset | logtail-statefulset 的机器组，主要用于指标采集场景。 | k8s-group-my-cluster-123-statefulset |  |
| k8s-group-${your_k8s_cluster_id}-singleton | 单实例机器组，主要用于部分单实例采集配置。 | k8s-group-my-cluster-123-singleton |  |
| LogStore | config-operation-log | 用于存储 Logtail 组件中的 alibaba-log-controller 日志。建议不要在此 LogStore 下创建采集配置。该 LogStore 可以删除，删除后不会再采集 alibaba-log-controller 的运行日志。该 LogStore 的收费标准和普通的 LogStore 收费标准是一致的，具体请参见 [按写入数据量计费模式计费项](billing-items-in-the-pay-per-data-write-mode.md) 。 | 无 |
### 查看Logtail状态、版本及IP地址
运行如下命令，查看Logtail状态。
kubectl get po -n kube-system | grep logtail
返回结果如下：
NAME READY STATUS RESTARTS AGE logtail-ds-gb92k 1/1 Running 0 2h logtail-ds-wm7lw 1/1 Running 0 4d
运行如下命令，查看Logtail的版本号、IP地址等信息。
kubectl exec logtail-ds-gb92k -n kube-system cat /usr/local/ilogtail/app_info.json
返回结果如下：
{ "hostname" : "logtail-ds-gb92k", "instance_id" : "0EBB2B0E-0A3B-11E8-B0CE-0A58AC140402_172.20.4.2_1517810940", "ip" : "192.0.2.0", "logtail_version" : "0.16.2", "os" : "Linux; 3.10.0-693.2.2.el7.x86_64; #1 SMP Tue Sep 12 22:26:13 UTC 2017; x86_64", "update_time" : "2021-02-05 06:09:01" }
### 升级与回滚Logtail
在升级前，您需要对Logtail组件相关描述文件进行备份。
重要
在升级前如果已存在明显的采集延迟，执行 Logtail 升级操作可能会导致少量日志丢失。
kubectl get ds -n kube-system logtail-ds -o yaml > logtail-ds.yaml kubectl get deployment -n kube-system alibaba-log-controller -o yaml > alibaba-log-controller.yaml kubectl get crd aliyunlogconfigs.log.alibabacloud.com -o yaml > aliyunlogconfigs-crd.yaml kubectl get cm -n kube-system alibaba-log-configuration -o yaml > alibaba-log-configuration.yaml kubectl get aliyunlogconfigs --all-namespaces -o yaml > aliyunlogconfigs-cr.yaml
请根据集群情况选择组件升级方式，当您使用的是ACK集群且集群与日志服务属于同一个阿里云账号时，参考ACK集群升级方式。若使用自建集群或ACK集群与日志服务属于不同的阿里云账号，请参考自建集群升级方式。
## ACK集群升级方式
一般情况下，推荐您使用自动升级方式。如果您在logtail-ds的DaemonSet中或者在alibaba-log-controller的Deployment中修改过参数（例如环境变量），那么为了使您的修改不被重置，请使用手动升级方式。
自动升级
重要
自动升级会重置您在logtail-ds和alibaba-log-controller中手动修改的配置。
登录[容器服务管理控制台](https://cs.console.aliyun.com)。
在集群列表页面中，单击目标集群最右侧的更多>运维管理>组件管理
在日志与监控页签中，找到logtail-ds，然后单击升级。
在升级组件对话框中，单击确定。
重要
如果无法升级到最新版本的Logtail，说明您的Kubernetes集群版本太旧。请先升级Kubernetes集群或者使用手动升级方式。
执行升级操作后，您可以在容器服务管理控制台上查看logtail-ds pod状态。如果logtail-ds pod状态都为Running，表示升级成功。
手动升级
重要
手动升级不会根据最新版本的Logtail组件更新您的配置，部分特性优化可能不可用。
手动升级包括升级logtail-ds和alibaba-log-controller。一般情况下，您只需要升级logtail-ds即可获取新版本Logtail提供的采集能力。当您需要获取新版Logtail CRD方式的采集能力时，需要升级alibaba-log-controller。以下步骤以logtail-ds为例。
登录[容器服务管理控制台](https://cs.console.aliyun.com)。
在集群列表页面中，单击目标集群最右侧的更多>运维管理>组件管理
选择工作负载>守护进程集。
说明
当您要升级alibaba-log-controller时，请选择工作负载>无状态，然后在kube-system命名空间下，找到alibaba-log-controller，完成升级。
选择命名空间为kube-system，然后单击logtail-ds对应的编辑。
检查如下环境变量是否存在。
如果不存在ALIYUN_LOGTAIL_CONFIG、ALIYUN_LOGTAIL_USER_ID、ALIYUN_LOGTAIL_USER_DEFINED_ID这三个环境变量，可能是因为您的Logtail版本太旧，请升级。
单击镜像Tag对应的选择镜像Tag。
在镜像Tag对话框中，单击最新版本，然后单击确定。
在页面右侧，单击更新。
执行升级操作后，您可以在容器服务管理控制台上查看logtail-ds pod状态。如果logtail-ds pod状态都为Running，表示升级成功。
## 自建集群升级方式
说明
建议通过安装最新Logtail组件进行更新，如果只更新部分组件（如logtail-ds、alibaba-log-controller）的镜像版本号可能导致升级失败。
重新安装Logtail组件，即可完成自动升级。具体操作，请参见[安装](install-run-upgrade-and-uninstall-logtail.md)[Logtail](install-run-upgrade-and-uninstall-logtail.md)[组件](install-run-upgrade-and-uninstall-logtail.md)。
如果您要回滚到某个版本，可参考如下步骤。
说明
升级前备份的YAML文件中包含不少冗余信息，需要您手动删除后，才能用于恢复Logtail配置。您可以使用kubectl-neat工具完成此操作。需要删除的字段为metadata.creationTimestamp、metadata.generation、metadata.resourceVersion、metadata.uid和status。
根据业务需求判断升级之后的新Logtail配置是否需要保留。
如果不需要保留，则可以删除升级之后的新Logtail配置。
删除备份文件中的冗余信息。
cat logtail-ds.yaml | kubectl-neat > neat-logtail-ds.yaml cat alibaba-log-controller.yaml | kubectl-neat > neat-alibaba-log-controller.yaml cat aliyunlogconfigs-crd.yaml | kubectl-neat > neat-aliyunlogconfigs-crd.yaml cat alibaba-log-configuration.yaml | kubectl-neat > neat-alibaba-log-configuration.yaml cat aliyunlogconfigs-cr.yaml | kubectl-neat > neat-aliyunlogconfigs-cr.yaml
应用精简后的备份文件，恢复Logtail配置。
kubectl apply -f neat-logtail-ds.yaml kubectl apply -f neat-alibaba-log-controller.yaml kubectl apply -f neat-aliyunlogconfigs-crd.yaml kubectl apply -f neat-alibaba-log-configuration.yaml kubectl apply -f neat-aliyunlogconfigs-cr.yaml
### 卸载Logtail
请根据集群情况选择组件卸载方式，当您使用的是ACK集群且集群与日志服务属于同一个阿里云账号时，参考ACK集群卸载方式。若使用自建集群或ACK集群与日志服务属于不同的阿里云账号，请参考自建集群卸载方式。
## ACK集群卸载方式
登录[容器服务管理控制台](https://cs.console.aliyun.com)。
在集群列表页面中，单击目标集群最右侧的更多>运维管理>组件管理
在日志与监控页签中，找到logtail-ds，然后单击卸载。
根据界面提示单击确定，完成卸载。
## 自建集群卸载方式
### 如何卸载已安装的logtail-ds、alibaba-log-controller等组件？
执行kubectl delete -R -f result卸载已安装的logtail-ds、alibaba-log-controller等组件。
重要
该命令会递归删除result目录中所有资源，若目录下存在其他资源请谨慎使用。
### 集群常见问题
多个Kubernetes集群如何共用一个日志服务Project？
如果您希望将多个集群中的容器日志采集到同一个日志服务Project中，安装其他集群日志服务组件时，将安装参数中的设置与您第一次安装集群日志服务组件时保持一致。
如何查看Logtail日志？
Logtail日志存储在Logtail容器中的/usr/local/ilogtail/目录中，文件名为ilogtail.LOG和logtail_plugin.LOG。
Logtail容器中的标准输出并不具备参考意义，请忽略以下标准输出内容。
start umount useless mount points, /shm$|/merged$|/mqueue$ umount: /logtail_host/var/lib/docker/overlay2/3fd0043af174cb0273c3c7869500fbe2bdb95d13b1e110172ef57fe840c82155/merged: must be superuser to unmount umount: /logtail_host/var/lib/docker/overlay2/d5b10aa19399992755de1f85d25009528daa749c1bf8c16edff44beab6e69718/merged: must be superuser to unmount umount: /logtail_host/var/lib/docker/overlay2/5c3125daddacedec29df72ad0c52fac800cd56c6e880dc4e8a640b1e16c22dbe/merged: must be superuser to unmount ...... xargs: umount: exited with status 255; aborting umount done start logtail ilogtail is running logtail status: ilogtail is running
如何查看Kubernetes集群中日志服务相关组件的状态？
执行如下命令进行查看。
kubectl get deploy alibaba-log-controller -n kube-system kubectl get ds logtail-ds -n kube-system
alibaba-log-controller启动失败，该怎么处理？
请确认您是否按照以下方式进行安装。
在Kubernetes集群的Master节点中执行安装命令。
安装命令参数中输入的是您的集群ID。
如果由于以上问题安装失败，请使用kubectl delete -f deploy命令删除已生成的安装模板并重新执行安装命令。
如何查看Kubernetes集群中Logtail-ds DaemonSet状态？
执行kubectl get ds -n kube-system命令查看Logtail-ds DaemonSet状态。
说明
Logtail容器所在的命名空间，默认为kube-system。
如何查看Logtail的运行日志？
Logtail运行日志保存在/usr/local/ilogtail/目录下，文件名为ilogtail.LOG，轮转文件会压缩存储为ilogtail.LOG.x.gz。例如执行如下命令查看日志。
kubectl exec logtail-ds-gb92k -n kube-system tail /usr/local/ilogtail/ilogtail.LOG
返回结果如下：
[2018-02-05 06:09:02.168693] [INFO] [9] [build/release64/sls/ilogtail/LogtailPlugin.cpp:104] logtail plugin Resume:start [2018-02-05 06:09:02.168807] [INFO] [9] [build/release64/sls/ilogtail/LogtailPlugin.cpp:106] logtail plugin Resume:success [2018-02-05 06:09:02.168822] [INFO] [9] [build/release64/sls/ilogtail/EventDispatcher.cpp:369] start add existed check point events, size:0 [2018-02-05 06:09:02.168827] [INFO] [9] [build/release64/sls/ilogtail/EventDispatcher.cpp:511] add existed check point events, size:0 cache size:0 event size:0 success count:0
如何重启某个Pod中的Logtail？
停止Logtail。
其中logtail-ds-gb92k表示容器名，kube-system表示命名空间，请根据实际情况替换。
kubectl exec logtail-ds-gb92k -n kube-system /etc/init.d/ilogtaild stop
返回如下结果表示停止成功。
kill process Name: ilogtail pid: 7 kill process Name: ilogtail pid: 9 stop success
启动Logtail。
其中logtail-ds-gb92k表示容器名，kube-system表示命名空间，请根据实际情况替换。
kubectl exec logtail-ds-gb92k -n kube-system /etc/init.d/ilogtaild start
返回如下结果表示启动成功。
ilogtail is running
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
