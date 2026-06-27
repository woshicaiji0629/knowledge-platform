# 机器组与采集配置关联指南-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/machine-group-and-collection-configuration-association-guide

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 机器组与采集配置关联指南

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在服务器上成功安装日志服务采集器后，还需要设置机器组将服务器关联到日志服务指定资源中，并通过采集配置定义数据的采集规则。随后手动绑定采集配置到机器组中，将采集规则应用到服务器上。

## 什么是机器组

机器组是包含多台服务器的虚拟分组，属于日志服务Project中的资源，日志服务通过机器组管理服务器，服务器通过心跳与机器组关联。Project支持将一个采集配置应用到多个机器组，或将一个机器组绑定到多个采集配置。

日志服务提供以下两种机器组类型：

### IP地址机器组

使用IP地址机器组时，需要在机器组中添加IP地址信息来与服务器关联。

- 

该种方式创建与配置更简单。

- 

当IP地址发生冲突或IP改变会导致心跳失败，影响数据采集。

### 用户自定义标识机器组(推荐使用)

通过在机器组中配置一个用户自定义的字符串作为识别标识，并在服务器上的标识文件中添加该字符串来进行关联。一台服务器的标识文件中可配置多个用户自定义标识，标识之间以换行符分隔。

- 

配置流程相比IP地址机器组更复杂。但在VPC等自定义网络环境，IP地址冲突会导致采集失败。而用户自定义标识可避免此类情况发生。

- 

可实现机器组的自动弹性伸缩。为新增的服务器配置相同的用户自定义标识，日志服务可自动识别并添加至机器组中。若不再需要采集服务器日志，直接删除服务器上配置的标识文件，机器组自动将该服务器移除。

- 

通常业务系统由多个模块组成，各模块均可进行独立的水平扩展，即支持添加多台服务器。为实现高效的日志数据收集和分类，建议为各模块创建单独的机器组。如常见网站分为HTTP请求模块、逻辑模块和存储模块，其自定义标识可分别定义为http_module、logic_module和store_module。

### 如何创建机器组

机器组与服务器之间建立心跳关联的前提是在服务器上成功安装采集器。建议您在安装采集器时一并创建机器组，详情可参考[安装采集器](products/sls/documents/loongcollector-installation-linux.md)或[安装配置](products/sls/documents/loongcollector-installation-kubernetes-1.md)。

步骤一：配置用户标识（可选）

说明

存在如下任一情况时，需要在服务器上配置用户标识，若ECS与日志服务同账号可跳过该步骤。用户标识的作用在于标识这台服务器有权限被该账号访问，并授权日志服务Project通过Logtail采集该服务器日志。

- 

服务器类型不是ECS。

- 

服务器类型是ECS，但是与日志服务不属于同一个账号。

- 

使用阿里云账号（主账号）登录[日志服务控制台](https://sls.console.aliyun.com)。鼠标悬浮在右上角用户头像，然后在弹出的标签页中查看并复制账号ID。如果您使用RAM用户登录，请复制主账号ID。

- 

登录需要采集数据的服务器，通过以下方式配置用户标识，即配置阿里云账号ID文件。

### Linux系统

- 

在/etc/ilogtail/users目录下，创建日志服务所属的阿里云账号ID文件。

touch /etc/ilogtail/users/{阿里云账号ID}

重要

- 

如果/etc/ilogtail/users目录不存在，请手动创建目录。

- 

新增、删除用户标识后，1分钟之内即可生效。

- 

当您使用多个阿里云账号下的日志服务Project对同一台服务器进行日志采集时，您可以在同一台服务器上创建多个阿里云账号ID文件。例如：

touch /etc/ilogtail/users/{阿里云账号ID 1} touch /etc/ilogtail/users/{阿里云账号ID 2}

### Windows系统

- 

在C:\LogtailData\users目录下，创建日志服务所属的阿里云账号ID文件。

- 

使用Windows PowerShell。

ni C:\LogtailData\users\{阿里云账号ID}

- 

使用命令提示符（cmd）。

type nul > C:\LogtailData\users\{阿里云账号ID}

- 

当您使用多个阿里云账号下的日志服务Project对同一台服务器进行日志采集时，您可以在同一台服务器上创建多个阿里云账号ID文件。

### 容器环境

如果Logtail部署在阿里云Kubernetes集群中，且为Logtail-ds 1.7.3及以上版本，则您可以通过[容器服务管理控制台](https://cs.console.aliyun.com)设置用户自定义标识，即在组件管理页面，修改logtail-ds组件中的LogtailDSExternalUserDefinelDs参数。具体操作，请参见[管理组件](products/ack/documents/manage-system-components.md)。

说明

- 

用户标识配置只需配置文件名，无需配置文件后缀。

- 

一台服务器上可配置多个用户标识，Logtail容器中仅支持配置一个用户标识。

- 

若您不再使用某个用户标识，直接删除服务器上阿里云账号ID文件即可。

步骤二：创建机器组

说明

日志服务Project支持使用IP地址或用户自定义标识创建机器组。使用IP地址创建相对更简单，但使用用户自定义标识具有以下优势，推荐使用。

- 

在VPC等自定义网络环境中，可能出现服务器IP地址冲突问题，导致Logtail采集失败。使用用户自定义标识可避免此类情况发生。

- 

使用用户自定义标识可实现机器组的弹性伸缩。为新增的服务器配置相同的用户自定义标识，日志服务可自动识别，并将其添加至机器组中。如果不再需要采集服务器日志，直接删除在服务器上配置的用户自定义标识文件，日志服务可自动将该服务器从机器组中移除。

创建用户自定义标识机器组

通常情况下，业务系统由多个模块组成，每个模块都可以进行独立的水平扩展，即支持添加多台服务器。为了实现高效的日志数据收集和分类，建议为每个模块创建单独的机器组。用户需要在各个模块的服务器上配置自定义标识，以确保每个服务器能归属于正确的机器组。

例如常见网站分为前端HTTP请求处理模块、缓存模块、逻辑处理模块和存储模块，其自定义标识可以分别定义为http_module、cache_module、logic_module和store_module。

重要

- 

同一机器组中不允许同时存在Linux和Windows服务器，请勿在Linux和Windows服务器上配置相同的用户自定义标识。

- 

一个服务器可配置多个用户自定义标识，标识之间以换行符分割。

- 

配置用户自定义标识。

Linux环境

- 

登录已安装Logtail的Linux服务器，使用以下命令配置用户自定义标识。

说明

如果目录/etc/ilogtail/不存在，请先手动创建该目录。

echo "user-defined-1" > /etc/ilogtail/user_defined_id

- 

（可选）使用以下命令检查用户自定义标识是否写入成功。如果返回user-defined-1，则表示写入成功。

cat /etc/ilogtail/user_defined_id

- 

新增、删除、修改user_defined_id文件后，默认情况下，1分钟内生效。如果需要立即生效，请执行以下命令重启Logtail。

/etc/init.d/ilogtaild stop /etc/init.d/ilogtaild start

Windows环境

- 

登录已安装Logtail的Windows服务器，在C:\LogtailData目录下新建user_defined_id文件并写入user-defined-1，完成后保存。

说明

如果目录C:\LogtailData不存在，请先手动创建该目录。

- 

新增、删除、修改user_defined_id文件后，默认情况下，1分钟内生效。如需立即生效，请根据以下步骤重启Logtail。

- 

选择开始>控制面板>管理工具>服务。

- 

在服务对话框中，选择对应的服务。

- 

如果是0.x.x.x版本，选择LogtailWorker服务。

- 

如果是1.0.0.0及以上版本，选择LogtailDaemon服务。

- 

右键单击重新启动使配置生效。

容器环境

用户自定义标识配置在Logtail容器的环境变量ALIYUN_LOGTAIL_USER_DEFINED_ID中，可通过docker inspect ${logtail_container_name} | grep ALIYUN_LOGTAIL_USER_DEFINED_ID命令查看。

- 

登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表，单击打开目标Project。在左侧导航栏中，选择资源>机器组。在打开的机器组页面中，选择机器组右侧的>创建机器组。

- 

在弹出的创建机器组页面，填写以下信息，并单击确定。

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 名称 | 机器组 名称，命名规则如下所示： 只能包括小写字母、数字、短划线（-）和下划线（_）。 必须以小写字母或者数字开头和结尾。 长度必须在 2~128 字符之间。 重要 创建后，不支持修改机器组名称，请谨慎填写。 |
| 机器组标识 | 选择 用户自定义标识 。 |
| 机器组 Topic | （可选） 机器组 Topic 用于区分不同服务器产生的日志数据。 |
| 用户自定义标识 | 填入已配置的 用户自定义标识 ，例如 user-defined-1 。 |


创建IP地址机器组

- 

登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表，单击打开目标Project。

- 

左侧导航栏中，选择资源>机器组。在打开的机器组页面中，选择机器组右侧的>创建机器组。登录日志服务控制台，在机器组页面单击创建机器组。

- 

在弹出的创建机器组页面，填写以下信息，并单击确定。

- 

- 

- 

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 名称 | 机器组 名称，命名规则如下所示： 只能包括小写字母、数字、短划线（-）和下划线（_）。 必须以小写字母或者数字开头和结尾。 长度必须在 2~128 字符之间。 重要 创建后，不支持修改机器组名称，请谨慎填写。 |
| 机器组标识 | 选择 IP 地址 。 |
| 机器组 Topic | （可选） 机器组 Topic 用于区分不同服务器产生的日志数据。 |
| IP 地址 | 填入 Logtail 自动获取的服务器 IP： 在已安装 Logtail 的服务器，打开 app_info.json 文件，并查看 ip 字段的值。 app_info.json 文件路径说明 Logtail 自动获取的服务器 IP 地址记录在 app_info.json 文件的 ip 字段中。 [root@iZ2zexxx ]# cat /usr/local/ilogtail/app_info.json { "UUID" : "Cxxx", "compiler" : "GCC 9.3.1", "hostname" : "iZ2zeixxx", "instance_id" : "xxx_l_172.26.128.15_1730267282", "ip" : "172.26.128.15", "logtail_version" : "1.8.7", "os" : "Linux; 5.10.134-17.2.al8.x86_64; #1 SMP Fri Aug 9 15:49:42 CST 2024; x86_64", "update_time" : "2024-10-30 13:48:02" } 重要 存在多台服务器时，请手动输入对应的 IP 地址，IP 地址之间需使用换行符分隔。 同一机器组中不允许同时存在 Linux 和 Windows 服务器。请勿将 Windows 和 Linux 服务器 IP 添加到同一 机器组 中。 |


## 什么是采集配置

采集配置是定义如何采集、处理数据的核心规则。其目的是通过灵活配置，实现数据的高效采集、结构化解析、过滤加工等效果。采集配置通过绑定到机器组中来实现下发采集规则到服务器上，并在数据采集时使用服务器上资源进行处理。采集配置项主要包含三部分内容：

- 

全局配置：包含采集配置的名称，日志主题（Topic）与Tag 等，利用Topic与Tag可对采集到的日志进行标记与分类。

全局配置参数介绍

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 配置项 | 说明 |
| --- | --- |
| 配置名称 | Logtail 配置名称，在其所属 Project 内必须唯一。创建 Logtail 配置成功后，无法修改其名称。 |
| 日志主题类型 | 选择日志主题（Topic）的生成方式。 机器组 Topic ：日志服务支持将一个 Logtail 配置 应用到多个 机器组 。使用 机器组 Topic 可用于区分来自不同机器组的日志。Logtail 上报数据时，会将服务器所在机器组的 机器组 Topic 作为日志主题上传至 Project。用户在查询日志时需要指定日志主题作为查询条件。 文件路径提取 ：若不同的用户或应用将日志保存在不同的顶级目录中，但下级目录和日志文件名相同，日志服务在采集日志时无法明确区分日志是由哪个用户或应用产生的。此时 文件路径提取 方式可用于区分不同用户或应用产生的日志数据。通过正则表达式来完整匹配文件路径，并将表达式匹配的结果（用户名或应用名）作为日志主题（Topic）上传至日志服务。 文件路径提取场景示例 说明 文件路径的正则表达式中，需要对正斜线（/）进行转义。 场景 1 ：不同用户将日志记录在不同目录下，但是日志文件名称相同，目录路径如下所示。 /data/logs ├── userA │ └── serviceA │ └── service.log ├── userB │ └── serviceA │ └── service.log └── userC └── serviceA └── service.log 如果在 Logtail 配置 中仅配置文件路径为 /data/logs 且文件名称为 service.log ，Logtail 会将三个 service.log 文件中的内容采集至同一个 LogStore 中，因此无法区分日志具体由哪个用户产生。您可以使用正则表达式提取文件路径中的值，生成不同的日志主题。 正则表达式 \/data\/logs\/(.*)\/serviceA\/.* 提取结果 __topic__: userA __topic__: userB __topic__: userC 场景 2 ：如果单个日志主题不足以区分日志的来源，您可以在日志文件路径中配置多个正则捕获组来提取关键信息。其中捕获组包括命名捕获组（?P<name>）与非命名捕获组两类。如果使用命名捕获组，则生成的 tag 字段为 __tag__:{name} ；如果使用非命名捕获组，则生成的 tag 字段为 __tag__:__topic_{i}__ ，其中 {i} 为捕获组的序号。 说明 当正则表达式中存在多个捕获组时，不会生成 __topic__ 字段。 例如，文件路径为 /data/logs/userA/serviceA/service.log ，您可以通过以下方式提取文件路径中的多个值。 示例 1：使用非命名捕获组进行正则提取。 正则表达式 \/data\/logs\/(.*?)\/(.*?)\/service.log 提取结果 __tag__:__topic_1__: userA __tag__:__topic_2__: serviceA 示例 2：使用命名捕获组进行正则提取。 正则表达式 \/data\/logs\/(?P<user>.*?)\/(?P<service>.*?)\/service.log 提取结果 __tag__:user: userA __tag__:service: serviceA 验证 ：配置完成后，根据日志主题查询日志：在日志查询分析页面，输入对应生成的日志主题，例如 __topic__: userA 、 __tag__:__topic_1__: userA 查询相应主题的日志。更多信息，请参见 [查询语法与功能](products/sls/documents/query-syntax.md) 。 在日志服务控制台的查询分析页面，输入查询语句 __topic__: userA ，单击 查询/分析 ，查询结果显示日志条数为 14 条，验证 Topic 提取配置已生效。日志详情中可见路径为 /var/log/a.log ，用户字段为 userA 。 自定义： 输入 customized:// + 自定义主题名 ，使用自定义的静态日志主题。 |
| 高级参数 | 其它可选的与配置全局相关的高级功能参数，请参见 [创建](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [Logtail](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [流水线配置](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) 。 |


- 

输入配置：定义了待采集数据的类型（如文件输入，集群标准输出，SQL查询结果，HTTP输入等），以及不同类型数据的采集路径、来源等信息。

输入配置参数介绍

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

### 

- 

- 

### 

### 

- 

- 

- 

| 配置项 | 说明 |
| --- | --- |
| 文件路径 | 根据日志在主机（例如 ECS）上的位置，设置日志目录和文件名称。 如果目标主机是 Linux 系统，则日志路径必须以正斜线（/）开头，例如 /apsara/nuwa/**/app.Log 。 如果目标主机是 Windows 系统，则日志路径必须以盘符开头，例如 C:\Program Files\Intel\**\*.Log 。 目录名和文件名均支持完整模式和通配符模式，文件名规则请参见 [Wildcard matching](https://man7.org/linux/man-pages/man7/glob.7.html) 。其中，日志路径通配符只支持星号（*）和半角问号（?）。 日志文件查找模式为多层目录匹配，即符合条件的指定目录（包含所有层级的目录）下所有符合条件的文件都会被查找到。例如： /apsara/nuwa/**/*.log 表示 /apsara/nuwa 目录（包含该目录的递归子目录）中后缀名为.log 的文件。 /var/logs/app_*/**/*.log 表示 /var/logs 目录下所有符合 app_* 格式的目录（包含该目录的递归子目录）中后缀名为 .log 的文件。 /var/log/nginx/**/access* 表示 /var/log/nginx 目录（包含该目录的递归子目录）中以 access 开头的文件。 |
| 最大目录监控深度 | 设置日志目录被监控的最大深度，即 文件路径 中通配符 ** 匹配的最大目录深度。0 代表只监控本层目录。 |
| 文件编码 | 选择日志文件的编码格式。 |
| 首次采集大小 | 配置首次生效时，匹配文件的起始采集位置距离文件结尾的大小。首次采集大小设定值为 1024 KB。 首次采集时，如果文件小于 1024 KB，则从文件内容起始位置开始采集。 首次采集时，如果文件大于 1024 KB，则从距离文件末尾 1024 KB 的位置开始采集。 您可以通过此处修改 首次采集大小 ，取值范围为 0~10485760，单位为 KB。 |
| 采集黑名单 | 打开 采集黑名单 开关后，可进行黑名单配置，即可在采集时忽略指定的目录或文件。支持完整匹配和通配符匹配目录和文件名。其中，通配符只支持星号（*）和半角问号（?）。 重要 如果您在配置 文件路径 时使用了通配符，但又需要过滤掉其中部分路径，则需在 采集黑名单 中填写对应的完整路径来保证黑名单配置生效。 例如您配置 文件路径 为 /home/admin/app*/log/*.log ，但要过滤 /home/admin/app1* 目录下的所有子目录，则需选择 目录黑名单 ，配置目录为 /home/admin/app1*/** 。如果配置为 /home/admin/app1* ，黑名单不会生效。 匹配黑名单过程存在计算开销，建议黑名单条目数控制在 10 条内。 目录路径不能以正斜线（/）结尾，例如将设置路径为 /home/admin/dir1/ ，目录黑名单不会生效。 支持按照文件路径黑名单、文件黑名单、目录黑名单设置，详细说明如下： 文件路径黑名单 选择 文件路径黑名单 ，配置路径为 /home/admin/private*.log ，则表示在采集时忽略 /home/admin/ 目录下所有以 private 开头，以.log 结尾的文件。 选择 文件路径黑名单 ，配置路径为 /home/admin/private*/*_inner.log ，则表示在采集时忽略 /home/admin/ 目录下以 private 开头的目录内，以_inner.log 结尾的文件。例如 /home/admin/private/app_inner.log 文件被忽略， /home/admin/private/app.log 文件被采集。 文件黑名单 选择 文件黑名单 ，配置文件名为 app_inner.log ，则表示采集时忽略所有名为 app_inner.log 的文件。 目录黑名单 选择 目录黑名单 ，配置目录为 /home/admin/dir1 ，则表示在采集时忽略 /home/admin/dir1 目录下的所有文件。 选择 目录黑名单 ，配置目录为 /home/admin/dir* ，则表示在采集时忽略 /home/admin/ 目录下所有以 dir 开头的子目录下的文件。 选择 目录黑名单 ，配置目录为 /home/admin/*/dir ，则表示在采集时忽略 /home/admin/ 目录下二级目录名为 dir 的子目录下的所有文件。例如 /home/admin/a/dir 目录下的文件被忽略， /home/admin/a/b/dir 目录下的文件被采集。 |
| 允许文件多次采集 | 默认情况下，一个日志文件只能匹配一个 Logtail 配置。如果文件中的日志需要被采集多份，需要打开 允许文件多次采集 开关。 |
| 高级参数 | 其它可选的与文件输入插件相关的高级功能参数，请参见 [创建](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [Logtail](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [流水线配置](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) 。 |


- 

处理配置：通过[处理插件](products/sls/documents/logtail-plug-in-list.md)的组合，来定义解析数据的规则，将待采集数据按需格式化（如过滤，脱敏，正则匹配，JSON解析等）。

处理配置参数介绍

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 配置项 | 说明 |
| --- | --- |
| 日志样例 | 待采集日志的样例，请务必使用实际场景的日志。日志样例可协助您配置日志处理相关参数，降低配置难度。支持添加多条样例，总长度不超过 1500 个字符。 [2023-10-01T10:30:01,000] [INFO] java.lang.Exception: exception happened at TestPrintStackTrace.f(TestPrintStackTrace.java:3) at TestPrintStackTrace.g(TestPrintStackTrace.java:7) at TestPrintStackTrace.main(TestPrintStackTrace.java:16) |
| 多行模式 | 多行日志的类型：多行日志是指每条日志分布在连续的多行中，需要从日志内容中区分出每一条日志。 自定义 ：通过 行首正则表达式 区分每一条日志。 多行 JSON ：每个 JSON 对象被展开为多行，例如： { "name": "John Doe", "age": 30, "address": { "city": "New York", "country": "USA" } } 切分失败处理方式： Exception in thread "main" java.lang.NullPointerException at com.example.MyClass.methodA(MyClass.java:12) at com.example.MyClass.methodB(MyClass.java:34) at com.example.MyClass.main(MyClass.java:10) 对于以上日志内容，如果日志服务切分失败： 丢弃 ：直接丢弃这段日志。 保留单行 ：将每行日志文本单独保留为一条日志，保留为一共四条日志。 |
| 处理模式 | 处理插件组合 ，包括 原生插件 和 拓展插件 。有关处理插件的更多信息，请参见 [处理插件概述](products/sls/documents/overview-22.md) 。 重要 处理插件的使用限制，请以控制台页面的提示为准。 2.0 版本的 Logtail： 原生处理插件可任意组合。 原生处理插件和扩展处理插件可同时使用，但扩展处理插件只能出现在所有的原生处理插件之后。 低于 2.0 版本的 Logtail： 不支持同时添加原生插件和扩展插件。 原生插件仅可用于采集文本日志。使用原生插件时，须符合如下要求： 第一个处理插件必须为正则解析插件、分隔符模式解析插件、JSON 解析插件、Nginx 模式解析插件、Apache 模式解析插件或 IIS 模式解析插件。 从第二个处理插件到最后一个处理插件，最多包括 1 个时间解析处理插件，1 个过滤处理插件和多个脱敏处理插件。 对于 解析失败时保留原始字段 和 解析成功时保留原始字段 参数，只有以下组合有效，其余组合无效。 只上传解析成功的日志： 解析成功时上传解析后的日志，解析失败时上传原始日志： 解析成功时不仅上传解析后的日志，并且追加原始日志字段，解析失败时上传原始日志。 例如，原始日志 "content": "{"request_method":"GET", "request_time":"200"}" 解析成功，追加原始字段是在解析后日志的基础上再增加一个字段，字段名为 重命名的原始字段 （如果不填则默认为原始字段名），字段值为原始日志 {"request_method":"GET", "request_time":"200"} 。 |


### 如何创建采集配置

采集配置需要绑定到生效的机器组中才能下发到服务器上，因此建议您根据不同数据源类型，参考完整采集流程进行配置，详情可参考[日志数据采集（Log）](products/sls/documents/sls-log-collection.md)。

### 如何修改采集配置

为确保日志采集配置稳定可靠，修改操作必须在采集配置的原始创建位置进行。若跨途径修改（如配置由环境变量创建却在控制台调整），采集配置可能在Pod重建、组件更新等运维操作中被原始来源覆盖，引发日志格式异常、采集中断等风险。

以下是各创建方式对应的规范修改方法及关键注意事项：

- 

SLS控制台/CLI/SDK创建：在SLS控制台/CLI/SDK直接修改采集配置。

- 

容器服务控制台/业务容器环境变量创建：调整容器环境变量（如 aliyun_logs_*），参数详见[采集](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)[集群容器日志](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)。不支持在SLS控制台修改。

- 

环境变量创建采集配置是一种快速接入方式，仅支持基础采集路径配置，无法设置高级参数或处理插件，如需使用高级功能，建议：删除当前容器环境变量与已创建的采集配置 → 改用SLS控制台、SDK、CLI或CRD方式重新创建。

- 

若采集配置通过环境变量方式创建，并曾经在SLS控制台补充过处理插件或高级参数，这些修改可能在Pod重建或组件更新等情况下被原始采集配置覆盖丢失，请尽快迁移。

- 

CRD方式创建：直接编辑对应的CR资源（如 AliyunPipelineConfig），参数详见[AliyunPipelineConfig](products/sls/documents/kubernetes-cr-parameter-description.md)[参数说明](products/sls/documents/kubernetes-cr-parameter-description.md)。不支持在SLS控制台修改。

- 

若采集配置通过CRD - AliyunPipelineConfig方式创建，并曾经在SLS控制台修改，所有改动均会在修改后30分钟内被还原，请检查当前采集配置是否符合预期。

- 

若采集配置通过CRD - AliyunLogConfig方式创建，并曾经在SLS控制台修改，这些修改可能在Pod重建或组件更新等情况下被原始采集配置覆盖丢失，请尽快检查当前采集配置是否符合预期并更新CR，建议升级至AliyunPipelineConfig。

### 机器组与采集配置的关系

日志服务支持将一个LoongCollector采集配置应用到多个机器组，一个机器组也支持应用多个LoongCollector采集配置，采集配置仅与机器组绑定，机器组中服务器增减将自动应用或取消相应采集配置，从而实现了服务器与采集配置的解耦。不同系统类型的服务器不支持添加到同一个机器组中。

## 机器组与采集配置关联场景

### 采集怎么匹配多个目录

需求：例如需要同时采集/var/log/messages和/opt/app/logs/*.log到同一LogStore中。

解决方案：

- 

在目标LogStore中创建两个采集配置，路径分别为/var/log/messages与/opt/app/logs/*.log。

- 

将这两个采集配置应用到同一个机器组中。

- 

日志服务会将该机器组中所有服务器上路径为/var/log/messages与/opt/app/logs/*.log的数据采集到目标LogStore中。

### 同服务器日志上传至多LogStore

需求：例如单台服务器上存在多目录下多类型日志，需要保存到不同LogStore中。

解决方案：

- 

在不同LogStore中分别创建不同的采集配置。

需要注意：若多个配置采集同一个文件，需要在输入配置中，打开允许文件多次采集开关。详情参考[日志多次采集](products/sls/documents/what-do-i-do-if-i-want-to-use-multiple-logtail-configurations-to-collect-logs-from-a-log-file.md)。

- 

将这些采集配置应用到同一个机器组中。

- 

日志服务会根据不同的采集配置将该机器组中不同日志上传到不同LogStore中。

### 不同服务器上日志如何集中汇总

需求：例如多台服务器分散在不同机器组中，但存在某类日志需要汇总到同一LogStore保存。

解决方案：

- 

在目标LogStore中创建一个采集配置。

- 

将这个采集配置应用到多台服务器所在的多个机器组中。

- 

日志服务会将多个机器组中服务器上的日志采集到目标LogStore中。

### 变更服务器上的采集规则

需求1：机器组绑定的采集配置所定义的规则不符合预期，需要修改为其他采集配置。

解决方案：

- 

登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表，单击打开目标Project。在左侧导航栏中，选择资源>>>机器组。在打开的机器组页面中，选择需要修改的机器组后，在机器组配置页面单击修改。

- 

在管理配置中查看左侧采集配置列表，勾选需要的采集配置后添加到右侧应用列表中。

需求2：新增服务器时需要应用已有的采集配置，或已有服务器不再需要继续采集。

解决方案：

- 

登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表，单击打开目标Project。在左侧导航栏中，选择资源>>>机器组。在打开的机器组页面中，选择需要修改的机器组后，在机器组配置页面单击修改。

- 

修改机器组覆盖的服务器数量，来应用或取消采集配置：

- 

若是IP地址型机器组，在IP地址栏中增加或删除IP地址信息，多台服务器IP地址之间需使用换行符分隔。

IP值必须与服务器的/usr/local/ilogtail/app_info.json文件中ip字段相同。

- 

若是用户自定义标识型机器组，在新增的服务器上配置相同的用户自定义标识，日志服务可自动识别并添加至机器组中。若不再需要采集服务器日志，直接删除服务器上配置的标识文件，机器组自动将该服务器移除，实现自动弹性伸缩。

说明

将服务器添加到机器组并不会自动安装LoongCollector，您需要先在新增服务器上安装LoongCollector。

## 相关参考

### 采集性能如何优化

- 

调整启动参数：[通过修改配置解决常见采集问题](products/sls/documents/resolve-common-collection-issues-through-configuration-changes.md)。

- 

调整处理插件：通过写入处理器或数据加工进行数据处理，具体可参考[处理插件、写入处理器、数据加工、消费处理器的对比](products/sls/documents/comparison-of-processing-plug-ins-write-processors-data-processing-and-consumer-processors.md)。

### 采集异常如何处理

[LoongCollector](products/sls/documents/loongcollector-collection-exception-troubleshooting.md)[采集异常问题汇总排查](products/sls/documents/loongcollector-collection-exception-troubleshooting.md)

[上一篇：VPC网络下启用internal域名](products/sls/documents/internal-domain-name.md)[下一篇：运行情况诊断与监控](products/sls/documents/automatic-diagnosis-and-monitoring-of-loongcollector-operation.md)

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
