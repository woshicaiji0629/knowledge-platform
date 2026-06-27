# 如何部署Logtail容器采集Docker容器的标准输出-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/collect-docker-container-standard-output

# 采集Docker容器的标准输出（旧版）
在服务器上部署Docker后可以采集日志，Docker的日志分为两种类型：标准输出和文件日志。文件日志是指容器内生成的日志被写入服务器的指定文件目录中，而标准输出则指容器自身的实时输出流。本文介绍使用Logtail采集容器的标准输出到LogStore的操作步骤。
## 概览
在宿主机中安装Docker后，针对您在该环境中部署的业务容器所产生的标准输出（stdout）及标准错误（stderr）日志，您可以使用Logtail进行采集。采集的日志数据将被传输至LogStore中，便于查询和分析。
## 前提条件
已创建Project和LogStore。更多信息，请参见[管理](manage-a-project.md)[Project](manage-a-project.md)和[管理](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
宿主机已[安装并使用](../../ecs/documents/user-guide/install-and-use-docker.md)[Docker](../../ecs/documents/user-guide/install-and-use-docker.md)[和](../../ecs/documents/user-guide/install-and-use-docker.md)[Docker Compose](../../ecs/documents/user-guide/install-and-use-docker.md)且可以持续产生标准输出日志。
说明
Logtail只采集增量日志。如果下发Logtail配置后，日志文件无更新，则Logtail不会采集该文件中的日志。更多信息，请参见[读取日志](log-collection-process-of-logtail.md)。
## 步骤一：安装Logtail容器并创建机器组
拉取Logtail镜像
登录宿主机，根据日志服务Project所在地域，获取对应的${region_id}。替换${region_id}后，使用以下命令拉取Logtail镜像。
重要
各地域对应的${region_id}请参见[开服地域](sls-supported-regions1.md)，例如华东 1（杭州）对应的${region_id}为cn-hangzhou。
#拉取Logtail镜像： docker pull registry.${region_id}.aliyuncs.com/log-service/logtail:v2.1.11.0-aliyun #如果您的服务器处于阿里云VPC网络中，请使用如下命令行拉取Logtail镜像： docker pull registry-vpc.${region_id}.aliyuncs.com/log-service/logtail:v2.1.11.0-aliyun
启动Logtail容器
参数说明
| 参数 | 参数说明 |
| --- | --- |
| ${region_id} | 根据 日志服务 Project 所在地域，获取对应的 ${region_id} ，各地域对应的 ${region_id} 请参见 [开服地域](sls-supported-regions1.md) 。网络类型选择请参见 [Logtail](select-a-network-type.md) [网络类型，启动参数与配置文件](select-a-network-type.md) 。 示例：若 Project 位于华东 1（杭州），则以阿里云内网访问时 ${region_id} 为 cn-hangzhou ，公网访问时使用 cn-hangzhou-internet 。 |
| ${aliyun_account_id} | 日志服务 所在的阿里云账号（主账号）ID。获取方法，请参见 [获取日志服务所在的阿里云账号（主账号）ID](configure-a-user-identifier.md) 。 |
| ${user_defined_id} | 设置机器组的用户自定义标识，例如 user-defined-docker-1 。该标识在 Project 所在地域内必须唯一。 |
根据参数说明，替换命令模板中的3个参数：${region_id}、${aliyun_account_id}和${user_defined_id}，然后执行以下命令启动Logtail容器。
# 启动Logtail容器，替换${region_id}，${aliyun_account_id}，${user_defined_id} docker run -d \ -v /:/logtail_host:ro \ -v /var/run/docker.sock:/var/run/docker.sock \ --env ALIYUN_LOGTAIL_CONFIG=/etc/ilogtail/conf/${region_id}/ilogtail_config.json \ --env ALIYUN_LOGTAIL_USER_ID=${aliyun_account_id} \ --env ALIYUN_LOGTAIL_USER_DEFINED_ID=${user_defined_id} \ registry.${region_id}.aliyuncs.com/log-service/logtail:v2.1.11.0-aliyun
重要
如果您要自定义配置Logtail容器的启动参数，只需保证以下前提条件。
启动时，必须配置3个环境变量ALIYUN_LOGTAIL_CONFIG，ALIYUN_LOGTAIL_USER_ID和ALIYUN_LOGTAIL_USER_DEFINED_ID。
将宿主机上的/var/run目录挂载到Logtail容器的/var/run目录。
将宿主机根目录挂载到Logtail容器的/logtail_host目录。
如果Logtail日志（/usr/local/ilogtail/ilogtail.LOG）中出现The parameter is invalid : uuid=none的错误日志，请在宿主机上创建一个product_uuid文件，在其中输入任意合法UUID（例如169E98C9-ABC0-4A92-B1D2-AA6239C0D261），并把该文件挂载到Logtail容器的/sys/class/dmi/id/product_uuid目录。
输入docker ps查看容器是否启动成功。
创建用户自定义标识机器组
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表，单击打开目标Project。
左侧导航栏中，选择资源>机器组。在打开的机器组页面中，选择机器组右侧的>创建机器组。
在创建机器组页面填写名称，机器组标识选择用户自定义标识，并在用户自定义标识中填入步骤一中参数${user_defined_id}的值，本例为user-defined-docker-1。
| 参数 | 说明 |
| --- | --- |
| 机器组 Topic | （可选） 机器组 Topic 用于区分不同服务器产生的日志数据。更多信息，请参见 [日志主题](log-topics.md) 。 |
检查机器组状态
在机器组列表中，单击目标机器组。在机器组配置页面，可查看机器组配置信息以及服务器状态。
如果心跳状态显示OK，说明配置成功，如果显示FAIL，请等待1分钟后单击刷新重试，若心跳状态仍为FAIL，请检查：
Logtail容器与Project是否同地域。
宿主机安全组是否放行Logtail出方向流量（默认端口80）。
处理操作请参见[如何排查容器日志采集异常](what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers.md)。
## 步骤二：创建Logtail采集配置
在日志存储>日志库页签中，单击目标Logstore。
展开LogStore菜单栏，单击Logtail配置，然后单击添加Logtail配置。
在快速数据接入页面，单击Docker标准输出-旧版。
由于步骤一创建了机器组，此处请单击使用现有机器组。
在机器组配置步骤中，选择步骤一中创建的机器组，单击>添加机器组到应用机器组中，并单击下一步。
在Logtail配置步骤中，输入配置名称，单击下一步。
在查询分析配置步骤中，单击刷新，可预览采集到的日志。若无日志，请确认容器是否持续产生标准输出日志，一般来说，标准输出默认在/var/lib/docker/containers/容器ID/容器ID-json.log中。若确认后仍无预览日志，请查看[如何排查容器日志采集异常](what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers.md)。
## 步骤三： 查看上传结果
重要
Logtail只采集增量日志，如果下发Logtail配置后标准输出无新日志产生，则Logtail不会采集以前的日志。更多信息，请参见[读取日志](use-logtail-to-collect-data.md)。
Docker标准输出的每条日志默认包含如下字段：
| 字段名 | 说明 |
| --- | --- |
| __source__ | Logtail 容器的 IP 地址。 |
| __tag__:__hostname__ | Logtail 所在 Docker 主机的名称。 |
| __tag__:__receive_time__ | 日志到达服务端的时间。 |
| _time_ | 数据上传时间，例如 2024-02-02T02:18:41.979147844Z 。 |
| _source_ | 输入源类型，stdout 或 stderr。 |
| _image_name_ | 镜像名。 |
| _container_name_ | 容器名。 |
| _container_ip_ | 业务容器 IP 地址。 |
## 相关文档
查看Logtail运行状态等信息，请参见[Logtail](collect-docker-container-text-logs.md)[容器信息](collect-docker-container-text-logs.md)。
Docker基本使用，请参见[安装并使用](../../ecs/documents/user-guide/install-and-use-docker.md)[Docker](../../ecs/documents/user-guide/install-and-use-docker.md)[和](../../ecs/documents/user-guide/install-and-use-docker.md)[Docker Compose](../../ecs/documents/user-guide/install-and-use-docker.md)。
采集Docker文本日志，请参见[采集](collect-docker-container-text-logs.md)[Docker](collect-docker-container-text-logs.md)[容器日志（标准输出/文件）](collect-docker-container-text-logs.md)。
采集宿主机文本日志，请参见[采集主机文本日志](collect-host-logs.md)。默认情况下，宿主机根目录会被挂载到Logtail容器的/logtail_host目录。
日志上传到LogStore后，创建索引请参见[创建索引](create-indexes.md)，查询分析请参见[查询与分析快速指引](quick-guide-to-query-and-analysis.md)。
使用Logtail采集Docker容器日志遇到异常情况时，请参见[如何排查容器日志采集异常](what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers.md)进行排查。
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
