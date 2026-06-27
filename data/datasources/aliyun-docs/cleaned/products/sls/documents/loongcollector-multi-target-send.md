# 使用LoongCollector通过单一采集配置将日志分发到多个日志库-日志服务-阿里云-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/loongcollector-multi-target-send

# LoongCollector多目标发送
本文介绍如何配置LoongCollector，通过单一采集配置将日志分发至多个日志库，解决传统方案中配置膨胀和资源浪费的问题。
## 业务场景说明
在复杂的系统环境中，经常需要将同一来源的日志根据其内容或属性分发到不同的目的地，以满足不同的存储、分析或合规要求。例如：
日志分类存储：业务服务产生的普通日志和审计日志打印在同一个日志文件中，但审计日志需要长期归档存储以满足合规要求，而普通日志只需短期保存用于问题排查。将它们发送到不同生命周期策略的日志库可以显著降低存储成本。
K8s多容器日志分离：在Kubernetes中，一个Pod内可能运行多个容器（如业务容器和Sidecar容器），需要将它们的标准输出日志分别采集到独立的日志库进行分析。
传统方法是为每个目标日志库创建一个独立的采集配置，这会导致采集配置数量膨胀，增加管理复杂度，并在Agent端启动多个重复的采集任务，造成不必要的CPU和内存资源浪费。LoongCollector的多目标发送功能旨在通过单一采集配置解决上述问题。
## 方案架构
方案的核心机制是基于Tag字段的路由分发。数据从采集到最终发送的完整生命周期在一个采集任务内完成：
多路复制：当一条日志同时满足多个输出目标的路由规则时，该日志将被复制并发送到所有匹配的目标日志库。
无匹配丢弃：当一条日志不满足任何一个输出目标的路由规则时，该日志将被丢弃，不会发送到任何地方。
默认发送：如果一个输出目标未配置任何路由规则，则所有采集到的日志都将被发送到该目标。
## 实施步骤
本节将通过两个典型场景，详细介绍如何配置和使用LoongCollector的多目标发送功能。
重要
本功能仅适用于LoongCollector 3.0.0及以上版本，Logtail不支持。
### 全局采集配置入口
与在特定日志库下创建采集配置不同，多目标发送的采集配置需要在Project的资源>配置管理页面进行：
登录[日志服务控制台](https://sls.console.aliyun.com/)，单击目标Project名称。
在目标Project页面，单击左侧导航栏资源>配置管理。
说明
此页面集中管理Project下的所有采集配置，包括那些因日志库被误删而残留的配置。
### 场景一：同文件内不同类型日志的分类存储
本场景将演示如何将同一个日志文件中的普通服务日志和审计日志分发到两个具有不同存储周期的日志库。
在配置管理页面，单击创建Logtail配置。
在快速数据接入弹窗中，单击单行 - 文本日志卡片的立即接入。
机器组配置，配置完成后单击下一步。
使用场景：主机场景
安装环境：ECS
选择机器组：选择目标主机所在的机器组并添加到应用机器组。如目标主机尚未安装LoongCollector，请参考[配置机器组（安装](host-text-log-collection-auto-install.md)[LoongCollector）](host-text-log-collection-auto-install.md)完成机器组配置。
Logtail配置，配置完成后单击下一步。
配置名称：自定义采集配置名称，在其所属Project内必须唯一。创建成功后，无法修改。
输入配置
文件路径：日志采集的路径。
Linux：以“/”开头，如/data/mylogs/**/*.log，表示/data/mylogs目录下所有后缀名为.Log的文件。
Windows：以盘符开头，如C:\Program Files\Intel\**\*.Log。
最大目录监控深度：文件路径中通配符**匹配的最大目录深度。默认为0，表示只监控本层目录。
处理配置
日志样例：单击添加日志样例，样例内容如下：其中包含action字段的为审计日志。
2025-10-28 11:22:21 INFO User test deleted a record | action=DELETE 2025-10-28 11:22:21 INFO Cache refreshed 2025-10-28 11:22:22 INFO User guest attempted unauthorized access | action=ACCESS_DENIED 2025-10-28 11:22:23 INFO Connected to database 2025-10-28 11:22:23 INFO User admin logged in | action=LOGIN 2025-10-28 11:22:24 INFO Connected to database 2025-10-28 11:22:25 INFO User guest attempted unauthorized access | action=ACCESS_DENIED 2025-10-28 11:22:26 INFO User test deleted a record | action=DELETE 2025-10-28 11:22:26 INFO Cache refreshed 2025-10-28 11:22:29 INFO Processed 200 requests in the last minute
处理模式：选择SPL。
SPL语句：输入如下SPL语句
* | parse-regexp content, '^(\d+-\d+-\d+\s\d+:\d+:\d+)\s+(\w+)\s+(.*?)\s*(?:\|\s*action=(\w+))?$' as time, level, message, action | project-away content | extend "__tag__:type" = case when action = '' then 'service_log' else 'audit_log' end
SPL语句说明：
通过正则表达式提取出日志中的字段，包括time，level，message，action，并移除content字段。
新增一个Tag字段为type，当action字段不为空时，tag值为audit_log，否则tag值为service_log。
说明
Tag命名说明：在SPL中创建或引用Tag时，字段名必须以__tag__:为前缀，如__tag__:type。但在后续的路由规则配置中，仅需填写Tag名称type。
输出配置：单击展开输出配置，添加两个输出目标。
配置输出目标1：存储普通日志，type标签值为service_log的日志。
日志库：选择用于存储普通日志的日志库（如service_log日志库）。
压缩方式：支持lz4和zstd，默认为lz4。
路由配置：
Tag名称：Tag名称填写时直接使用字段名，无需添加__tag__:前缀。此处设置tag名为type。
Tag值：配置为service_log。
是否丢弃该Tag字段：开启后上传的日志中不包含该Tag字段。
配置输出目标2：存储审计日志，type标签值为audit_log的日志。
日志库：选择用于存储审计日志的日志库（如audit_log日志库）。
压缩方式：支持lz4和zstd，默认为lz4。
路由配置：
Tag名称：type。
Tag值：audit_log。
是否丢弃该Tag字段：开启后上传的日志中不包含该Tag字段。
查询分析配置：
系统默认开启[全文索引](create-indexes.md)，支持对日志原始内容进行关键词搜索。
如需按字段进行精确查询，请在页面加载出预览数据后，单击自动生成索引，日志服务将根据预览数据中的第一条内容生成[创建索引](create-indexes.md)。
配置完成后，单击下一步，完成整个采集流程的设置。
完成配置并保存后，LoongCollector将根据日志中的action字段自动将日志分发到对应的日志库。
audit_log日志库中应只包含带有action字段的日志记录。
查询audit_log日志库的原始日志，可以看到日志记录均包含action字段，取值包括ACCESS_DENIED、DELETE、LOGIN等，验证分类存储结果符合预期。
service_log日志库中应只包含普通服务日志。
查询service_log日志库的原始日志，可以看到日志条目均为 INFO 级别的普通服务日志，例如Processed 200 requests in the last minute、Cache refreshed、Connected to database等，不包含错误日志或其他类型日志。
### 场景二：K8s同一Pod内不同容器日志的分离
本场景将演示如何将ACK集群中同一个Pod内两个不同容器（app1-container和app2-container）的标准输出日志采集到各自独立的日志库。实现在不创建多个采集配置的情况下，对同一Pod内多容器日志的精细化管理和分离。
在配置管理页面，单击创建Logtail配置。
在快速数据接入弹窗中，单击K8S - 标准输出 - 新版卡片的立即接入。
机器组配置，配置完成后单击下一步。
使用场景：K8s场景
部署方式：ACK Daemonset
选择机器组：在源机器组中将系统默认创建的机器组k8s-group-${cluster_id}添加至右侧应用机器组。
Logtail配置，配置完成后单击下一步。
配置名称：自定义采集配置名称，在其所属Project内必须唯一。创建成功后，无法修改。
输入配置
选择开启标准输出或标准错误开关（默认全部开启）。
容器过滤：根据需要设置过滤条件，以限定采集范围。
开启容器过滤，单击添加>K8s Namespace 正则匹配，输入^(app)$：只采集app命名空间下的容器数据。
输出配置：单击展开输出配置，添加两个输出目标。
K8s标准输出采集会自动为日志附加一系列包含容器元信息的Tag，例如_container_name_。本场景利用此内置Tag进行路由。
配置输出目标1：存储app1容器日志。
日志库：选择用于存储app1日志的日志库（例如app1-log）。
压缩方式：支持lz4和zstd，默认为lz4。
路由配置：
Tag名称：Tag名称填写时直接使用字段名，无需添加__tag__:前缀。此处设置tag名为_container_name_。
Tag值：配置为app1-container。
是否丢弃该Tag字段：开启后上传的日志中不包含该Tag字段。
配置输出目标2：存储app2容器日志。
日志库：选择用于存储app2日志的日志库（例如app2-log）。
压缩方式：支持lz4和zstd，默认为lz4。
路由配置：
Tag名称：_container_name_。
Tag值：app2-container。
是否丢弃该Tag字段：开启后上传的日志中不包含该Tag字段。
查询分析配置：
系统默认开启[全文索引](create-indexes.md)，支持对日志原始内容进行关键词搜索。
如需按字段进行精确查询，请在页面加载出预览数据后，单击自动生成索引，日志服务将根据预览数据中的第一条内容生成[创建索引](create-indexes.md)。
配置完成后，单击下一步，完成整个采集流程的设置。
完成配置并保存后，来自不同容器的标准输出日志被自动路由到指定的日志库。
app1-log日志库：
在日志服务 SLS 查询页面中，设置时间范围为最近 3 分钟，共查询到 1,454 条日志。日志来源为app1-container，输出类型为stdout，日志内容为每秒输出的Hello from app1，表明 app1 容器日志已成功采集到该日志库。
app2-log日志库：
查询结果显示共 1,454 条日志记录，日志来源为 app2-container 容器的 stdout，内容为周期性输出的Hello from app2消息，表明 app2 容器的日志已被正确采集并投递到该 Logstore。
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
