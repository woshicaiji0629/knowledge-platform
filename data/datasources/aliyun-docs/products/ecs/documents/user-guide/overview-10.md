# 云助手的功能特性、应用场景及常用操作-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/overview-10

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

# 云助手概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云助手是专为云服务器ECS打造的原生自动化运维工具，免密码、免登录、无需使用跳板机，即可批量执行命令（Shell、PowerShell、Bat等），实现自动化运维脚本、轮询进程、安装卸载软件、启动或停止服务、安装补丁或安全更新等任务。

## 功能特性

- 

批量运维

同一脚本命令可在多台安装了云助手Agent的实例上执行，实例间互不影响。

- 

上传文件

可以将本地的文件（例如配置文件、脚本等），通过云助手上传到ECS实例。

- 

公共命令

公共命令包含一些比较复杂的服务器配置、健康或安全检测、应用安装、文件处理、系统补丁安装、更改系统配置、服务或应用管理的脚本，以及云助手插件（包含脚本或可执行程序）。使用公共命令，可以快速地完成某些复杂配置，极大地提升您的操作和运维效率。

- 

简单易用

您可以使用自定义参数/内置参数实现命令的简单灵活配置，使一份云助手命令在多种场景中使用。

- 

安全可控

云助手不会主动发起任何操作，所有操作都在您的可控范围内。

## 应用场景

云助手可帮您完成部署与运维任务，包括但不限于：

- 

上传并运行自动化运维脚本

- 

运行实例上已有的脚本

- 

管理软件生命周期

- 

部署代码或者应用

- 

轮询进程

- 

安装补丁或安装安全更新

- 

从对象存储OSS或者YUM源获取更新

- 

修改主机名或用户登录密码

## 使用限制

- 

实例处于运行中（Running）状态，并安装了云助手Agent。

- 

创建的Bat、PowerShell或者Shell脚本和自定义参数在Base64编码后，使用场景与文件大小说明如下：

- 

创建命令：综合大小不能超过18 KB。

- 

立即执行并保存命令：综合大小不能超过18 KB。

- 

立即执行但不保存命令：综合大小不能超过24 KB。

- 

上传文件：文件大小不能超过32 KB。

- 

一条命令中，自定义参数的个数不能超过20个。

- 

您只能在以下操作系统中运行云助手命令：

- 

Alibaba Cloud Linux

- 

CentOS 6/7/8及更高版本

- 

CoreOS

- 

Debian 8/9/10及更高版本

- 

OpenSUSE

- 

RedHat 5/6/7及更高版本

说明

RedHat中需要您自行下载rpm包安装云助手Agent，具体操作，请参见[安装云助手](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)[Agent](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)。

- 

SUSE Linux Enterprise Server 11/12/15及更高版本

- 

Ubuntu 12/14/16/18及更高版本

- 

FreeBSD 11/12/13/14及更高版本

- 

Window Server 2012/2016/2019及更高版本

说明

- 

使用ECS公共镜像创建的实例会默认安装云助手Agent。

- 

使用自定义镜像或者云市场镜像创建的实例需要您首先确认操作系统是否支持云助手，再自行安装云助手Agent。具体步骤请参见[安装云助手](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)[Agent](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)。

## 支持功能及版本

云助手所支持的功能及其对应的最低版本号如下表所示：

| 云助手支持的功能 | 云助手最低版本号（Linux 实例） | 云助手最低版本号（Windows 实例） |
| --- | --- | --- |
| 支持上报云助手心跳 | 1.0.2.458 | 1.0.0.149 |
| 发送文件 | 1.0.2.569 | 1.0.0.149 |
| 执行命令支持指定用户名称 | 2.2.0.106 | 2.1.0.50 |
| 支持设置实例下次启动时执行命令 | 2.2.0.46 | 2.1.0.50 |
| 支持设置实例每次启动时执行命令 |  |  |
| 支持会话管理（Session Manager） | 2.2.3.196 | 2.1.3.196 |
| 定时任务的执行规则支持 Rate 表达式、At 表达式 | 2.2.3.282 | 2.1.3.282 |
| 定时任务的执行规则中，Cron 表达式支持指定年份或时区 | 2.2.3.282 | 2.1.3.282 |
| 支持内置环境参数 | 2.2.3.309 | 2.1.3.309 |
| 支持将实例名称作为内置环境参数 | 2.2.3.344 | 2.1.3.344 |
| 支持通过指定特殊退出码停止或重启实例 | 2.2.3.317 | 2.1.3.317 |
| 支持通过指定容器名称，在容器内执行命令 | 2.2.3.344 | 2.1.3.344 |
| 支持通过指定容器 ID，在容器内执行命令 | 2.2.3.344 | 2.1.3.344 |


## 云助手安装目录文件说明

## Linux 实例

在 Linux 操作系统的实例中，云助手的主要文件和目录位于 /usr/local/share/aliyun-assist/。

- 

/usr/local/share/aliyun-assist/

- 

2.x.x.xxx/ (例如: 2.2.4.965) -云助手具体版本安装目录

- 

acs-plugin-manager: 云助手插件管理器程序。

- 

aliyun_assist_update: 云助手升级程序。

- 

aliyun_installer: 早期的组件安装器（已废弃，功能由 acs-plugin-manager 替代）。

- 

aliyun-service: 云助手 Agent 的主程序。

- 

assist_daemon: 云助手守护进程，确保主程序 aliyun-service 的稳定运行。

- 

config/: 配置文件目录。

- 

GlobalSignRootCA.crt: 用于与云助手服务端进行 HTTPS 安全通信的根证书文件。

- 

hash_file: 程序文件的哈希记录，用于文件一致性校验，确保核心文件未被篡改。

- 

init/: 安装及卸载脚本目录。

- 

clean: 清理脚本，用于移除云助手相关配置和文件。

- 

install: 安装脚本。

- 

uninstall: 卸载脚本。

- 

version: 记录当前云助手客户端版本信息的文件。

- 

log/: 日志文件目录。

- 

aliyun_assist_main.log: 记录云助手当天的运行日志。

- 

aliyun_assist_main.log.YYYYMMDD: 历史日志文件，按日期归档。

- 

plugin/: 预装插件目录。

- 

ACS-ECS-SysInfoGatherer: 云助手数据采集插件。

- 

cache/: 缓存文件目录。

- 

state_configs.json: 云助手Agent 本地缓存的运维与配置OOS Inventory 采集配置文件。

- 

config/: 全局配置文件目录。

- 

task_sign_certs/: 云助手Agent 本地缓存的、用于校验任务签名的公钥。

- 

hybrid/: 托管实例注册信息目录。

- 

hardwareHash: 当实例注册为托管实例时，由云助手 Agent 生成的用于标识机器的硬件信息记录文件。

- 

plugin/: 云助手插件目录。

- 

installed_plugins.db: 记录插件的数据信息。

- 

work/: 执行文件存放目录。

- 

script/: 云助手执行文件存放目录。

- 

注意：从 2.x.3.704 版本开始，为增强安全性，云助手默认不再将执行脚本自动落盘。您需要手动开启相关配置，才能在此目录下看到执行的脚本文件。

- 

region-id: 记录当前实例所处地域（Region）信息的文件。

## Windows 实例

在 Windows 操作系统的实例中，云助手的主要文件和目录位于 C:\ProgramData\aliyun\assist\。

- 

C:\ProgramData\aliyun\assist\

- 

2.x.x.xxx/ (例如: 2.1.4.965) -云助手具体版本安装目录

- 

acs-plugin-manager.exe: 云助手插件管理器程序。

- 

aliyun_assist_update.exe: 云助手升级程序。

- 

aliyun_installer.exe: 云助手安装程序。

- 

aliyun_assist_service.exe: 云助手服务的主程序。

- 

install.bat: 云助手安装脚本。

- 

install.exe: 云助手安装程序。

- 

PatchGo.dll: 针对 Windows Server 2008 环境的补丁，用于避免 Go 语言运行时导致的时钟跳变问题。

- 

version.ini: 记录云助手版本信息。

- 

config/: 配置文件目录。

- 

GlobalSignRootCA.crt: 云助手服务端通信所需的证书文件。

- 

hash_file: 程序文件的哈希记录，用于文件一致性验证。

- 

log/: 日志文件目录。

- 

aliyun_assist_main.log: 当天的运行日志。

- 

aliyun_assist_main.log.YYYYMMDD: 历史日志文件，按日期归档。

- 

plugin/: 预装及已安装插件目录。

- 

ACS-ECS-SysInfoGatherer: 数据采集插件。

- 

SessionManager: 实现免密登录功能的插件。

- 

installed_plugins.db: 云助手插件的信息。

- 

cache/: 缓存文件目录。

- 

state_configs.json: 云助手Agent 本地缓存的 OOS Inventory 采集配置文件。

- 

config/: 配置文件目录。

- 

task_sign_certs/: 云助手Agent 本地缓存的任务签名校验公钥。

- 

hybrid/: 托管实例信息目录。

- 

plugin/: 插件数据目录。

- 

installed_plugins.db: 插件的数据信息。

- 

work/: 执行文件存放目录。

- 

script/: 云助手执行的脚本文件存放目录。

- 

注意：从 2.x.3.704 版本开始，默认不自动保存脚本文件到此目录，需手动开启。

- 

config.ini: 记录云助手版本等配置信息的文件。

- 

region-id: 记录实例所处地域信息的文件。

- 

version: 记录当前云助手版本信息的文件。

## 计费说明

云助手服务本身不收费。

但是使用云助手在部署与运维云资源过程中可能会产生费用。ECS资源计费详情，请参见[计费概述](products/ecs/documents/billing-overview.md)。

## 资源占用

云助手Agent所在主机的各项资源占用情况如下：

| 主机资源 | Linux 操作系统 | Windows 操作系统 |
| --- | --- | --- |
| CPU | 平均 CPU 使用率不到 1% |  |
| 物理内存 | 约 20 MB | 约 30 MB |
| 磁盘 I/O | 平稳运行时几乎没有 I/O，仅在下载升级安装包和保存命令脚本等场景下产生磁盘 I/O |  |
| 网络 I/O | 平稳运行时仅有心跳上报等数据产生的少量 I/O |  |


## 名词解释

云助手的常用名词及其具体描述如下表所示。

- 

- 

- 

- 

- 

- 

| 常见名词 | 说明 |
| --- | --- |
| 云助手 | 云助手官方名称，可以帮您在 ECS 实例以及弹性裸金属服务器实例上自动以及批量执行日常维护任务。所有阿里云地域均支持云助手服务。 |
| 云助手 Agent | 安装在 ECS 实例中的轻量级插件，所有在实例中完成的命令都会通过云助手 Agent 执行。 Windows 操作系统中任务进程名称为 aliyun_assist_service。 Linux 操作系统中任务进程名称为 aliyun-service。 |
| 云助手守护进程 | 用于监控 云助手 Agent 的资源消耗情况，上报 云助手 Agent 的运行状态，以及当 云助手 Agent 崩溃时重启 云助手 Agent 。 服务名称： AssistDaemon 路径： /usr/local/share/assist-daemon/assist_daemon 说明 目前云助手守护进程仅支持 Linux 操作系统。 |
| 任务执行路径 | 云助手会将用户的命令内容以文件形式先保存到实例上，然后再执行文件，具体保存路径如下： Linux： /tmp Windows： 云助手安装路径/work/script |
| 命令 | 需要在实例中执行的具体命令操作，如一份 Shell 脚本或者 PowerShell 脚本。 |
| 自定义参数 | 您在命令中设置的变量值，以 {{key}} 的形式表示，可以在执行命令时以 {{"key":"value"}} 的形式设置自定义参数的值。由于您在一个地域下能保有的云助手命令有配额限制，建议您通过设置自定义参数提高命令的灵活性以及多场景适用性。您也可以指定内置环境参数作为自定义参数，执行命令时无需手动对参数赋值，云助手将为您自动替换为环境中对应的值。 |
| 单次执行 | 在一台或者多台实例中执行某个命令，即为一次执行（ Invocation ）。 |
| 定时执行 | 在一台或者多台实例中执行某个命令时，您可以指定执行时序或周期，定时执行命令进程。 |


## 命令执行状态

### 单条命令执行状态

在一台实例上运行一条命令时，实例级别的状态如下表所示，对应[DescribeInvocations](products/ecs/documents/api-describeinvocations.md)中InvokeInstance下的InvocationStatus字段，或[DescribeInvocationResults](products/ecs/documents/api-describeinvocationresults.md)中的InvocationStatus字段。

- 

- 

- 

- 

| API 状态 | 状态显示 | 描述 |
| --- | --- | --- |
| Pending | 下发中 | 系统正在校验或发送命令。 |
| Invalid | 校验不通过 | 指定命令类型或参数有误。 |
| Aborted | 下发失败 | 向实例发送命令失败。实例必须在运行中，且命令可以 1 分钟内发送完成。 |
| Running | 执行中 | 命令正在被执行。 |
| Success | 执行成功 | 单次执行的命令：命令执行完成，且退出码为 0。 定时执行的命令：上一次运行成功且退出码为 0，且指定的时间已结束。 |
| Failed | 执行完成，退出码非 0 | 单次执行的命令：命令执行完成，且退出码非 0。 定时执行的命令：上一次运行成功且退出码非 0，且指定的时间将中止。 |
| Error | 执行异常 | 命令执行时发生异常无法继续。 |
| Timeout | 执行超时 | 命令执行超时。 |
| Cancelled | 执行取消 | 命令的执行动作已经取消，命令未曾启动。 |
| Stopping | 停止执行中 | 命令正在被停止执行。 |
| Stopped | 已停止执行 | 命令已经被停止。 |
| Terminated | 执行已终止 | 命令运行时被终止。 |
| Scheduled | 命令等待运行 | 定时执行的命令等待运行。 |


### 批量命令执行状态

为便于管理批量执行或者定时执行，您可以从总执行状态、实例级别执行状态以及执行记录级别的状态概念出发管理命令运行的生命周期，对应[DescribeInvocations](products/ecs/documents/api-describeinvocations.md)中Invocation下的InvocationStatus字段。状态各级别之间的包含关系如下图所示。

在多台实例上运行一条命令，总执行状态说明如下表所示。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| API 状态 | 状态显示 | 描述 |
| --- | --- | --- |
| Pending | 系统正在校验或发送命令 | 存在至少一台实例的命令执行状态为 Pending ，则总执行状态为 Pending 。 |
| Scheduled | 定时执行的命令已发送，等待运行 | 存在至少一台实例的命令执行状态为 Scheduled ，则总执行状态为 Scheduled 。 |
| Running | 命令正在实例上运行 | 存在至少一台实例的命令执行状态为 Running ，则总执行状态为 Running 。 |
| Success | 命令执行成功 | 各个实例上的命令执行状态均为 Stopped 或 Success ，且至少一个实例的命令执行状态是 Success ，则总执行状态为 Success 。 立即运行的任务：命令执行完成，且退出码为 0。 定时运行的任务：最近一次执行成功且退出码为 0，且指定的时间已全部完成。 |
| Failed | 命令执行失败 | 各个实例上的命令执行状态均为 Stopped 或 Failed ，则总执行状态为 Failed 。实例上的命令执行状态一项或多项为以下状态时，返回值均为 Failed 状态： 命令校验失败（ Invalid ）。 命令发送失败（ Aborted ）。 命令执行完成但退出码非 0（ Failed ）。 命令执行超时（ Timeout ）。 命令执行异常（ Error ）。 |
| Stopping | 正在停止任务 | 存在至少一台实例的命令执行状态为 Stopping ，则总执行状态为 Stopping 。 |
| Stopped | 任务已停止 | 所有实例的命令执行状态是 Stopped ，则总执行状态为 Stopped 。实例上的命令执行状态为以下状态时，返回值均为 Stopped 状态： 任务已取消（ Cancelled ）。 任务已终止（ Terminated ）。 |
| PartialFailed | 部分实例执行成功且部分实例执行失败 | 各个实例的命令执行状态均为 Success 、 Failed 或 Stopped ，则总执行状态为 PartialFailed 。 |


## 授权RAM用户使用云助手

由于阿里云账号（即主账号）具备所有资源的权限，为确保您的阿里云账号及云资源的安全使用，如非必要应避免直接使用阿里云账号进行操作。推荐使用RAM用户代替阿里云账号进行相关操作，在使用云助手时，RAM用户需要获得云助手的相关权限授权。如何为RAM用户授予云助手权限，请参见[授权](products/ecs/documents/user-guide/use-ram-to-implement-permission-control.md)[RAM](products/ecs/documents/user-guide/use-ram-to-implement-permission-control.md)[用户使用云助手](products/ecs/documents/user-guide/use-ram-to-implement-permission-control.md)。

## 使用云助手

您可以通过ECS控制台或者调用API使用云助手。

- 

- 

- 

- 

- 

- 

- 

- 

| 业务场景 | 参考文档 | 相关 API |
| --- | --- | --- |
| 2017 年 12 月 01 日之后使用公共镜像创建的 ECS 实例，默认预装 云助手 Agent ，因此，部分 ECS 实例仍需自行安装。 | [安装云助手](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md) [Agent](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md) | [InstallCloudAssistant](products/ecs/documents/api-installcloudassistant.md) [DescribeCloudAssistantStatus](products/ecs/documents/api-describecloudassistantstatus.md) |
| 通过程序调用 API。 | [通过](products/ecs/documents/user-guide/java-programs-use-cloud-assistant-to-manage-ecs-instances.md) [SDK](products/ecs/documents/user-guide/java-programs-use-cloud-assistant-to-manage-ecs-instances.md) [执行命令](products/ecs/documents/user-guide/java-programs-use-cloud-assistant-to-manage-ecs-instances.md) | 不涉及 |
| 新建一份云助手命令。 | [创建命令](products/ecs/documents/user-guide/create-a-command.md) | [RunCommand](products/ecs/documents/api-runcommand.md) [CreateCommand](products/ecs/documents/api-createcommand.md) |
| 对目标 ECS 实例执行已创建的命令。 | [执行命令](products/ecs/documents/user-guide/run-a-command.md) | [RunCommand](products/ecs/documents/api-runcommand.md) [InvokeCommand](products/ecs/documents/api-invokecommand.md) |
| 查看命令的执行状态，查看命令的执行结果，即在指定 ECS 实例中的实际输出信息。 | [查看执行结果及修复常见问题](products/ecs/documents/user-guide/check-execution-results-and-troubleshoot-common-issues.md) | [DescribeInvocations](products/ecs/documents/api-describeinvocations.md) [DescribeInvocationResults](products/ecs/documents/api-describeinvocationresults.md) |
| 修改已创建的命令，支持修改命令名称和描述。 | [修改命令](products/ecs/documents/user-guide/modify-a-command.md) | 不涉及 |
| 为一份云助手命令新增版本。或者您希望修改命令的名称、描述、类型、内容、执行路径或者超时时间等更多属性。 | [克隆命令](products/ecs/documents/user-guide/clone-a-command.md) | 不涉及 |
| 停止正在进行的命令进程。 | [停止命令](products/ecs/documents/user-guide/stop-a-command.md) | [StopInvocation](products/ecs/documents/api-stopinvocation.md) |
| 删除不再需要的云助手命令，避免命令达到配额上限时影响新建命令。 | [删除命令](products/ecs/documents/user-guide/delete-a-command.md) | [DeleteCommand](products/ecs/documents/api-deletecommand.md) |


[上一篇：云助手](products/ecs/documents/user-guide/cloud-assistant.md)[下一篇：配置云助手Agent](products/ecs/documents/user-guide/configure-the-cloud-assistant-agent.md)

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
