# Logtail（旧版采集器）-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/use-logtail-to-collect-data

# Logtail（旧版采集器）
Logtail是日志服务提供的日志采集Agent，用于采集阿里云ECS、自建IDC或其他云厂商等服务器上的日志。本文介绍Logtail的采集流程、功能、优势、使用限制及配置流程等信息。
Logtail多年来一直承载着阿里巴巴集团重要服务的数据采集。每天采集数百万服务器上的实时数据，日流量数十PB，并历经多次双十一挑战。
相关性能指标，请参见[Logtail](https://yq.aliyun.com/articles/703229)[提升采集性能](https://yq.aliyun.com/articles/703229)。
相关技术分享，请参见[Logtail](https://yq.aliyun.com/articles/204554)[技术分享一](https://yq.aliyun.com/articles/204554)和[Logtail](https://yq.aliyun.com/articles/251629)[技术分享二](https://yq.aliyun.com/articles/251629)。
## 采集流程
### 监听日志
在服务器上安装Logtail及在日志服务控制台上创建Logtail采集配置后，日志服务会实时下发Logtail采集配置到Logtail，Logtail根据Logtail采集配置开始监听文件。Logtail根据Logtail采集配置中的日志路径和最大监控目录深度，逐层扫描符合规则的日志目录和文件。
将Logtail采集配置应用到机器组后，对应服务器上没有发生修改事件的日志文件会被判定为历史日志文件，Logtail监听到历史日志文件，并不会采集。当日志文件产生了修改事件，才会触发采集流程，Logtail开始读取文件。如果您要采集历史日志文件，请参见[导入历史日志文件](import-historical-logs.md)。
为保证采集日志的时效性以及稳定性，Logtail会对待采集的目录注册事件监听（Linux下使用[Inotify](http://man7.org/linux/man-pages/man7/inotify.7.html)）以及定期轮询。
### 读取日志
Logtail监听到日志文件，并确认有更新后，开始读取。
首次读取日志文件时，日志服务默认首次读取大小为1024 KB。
如果文件小于1024 KB，则从文件内容起始位置开始读取。
如果文件大于1024 KB，则从距离文件末尾1024 KB的位置开始读取。
说明
日志服务支持自定义首次读取大小。
控制台方式：在Logtail配置中修改首次采集大小参数。具体操作，请参见[高级配置](collect-logs-in-simple-mode.md)。
API方式：在Logtail配置中修改tail_size_kb参数。具体操作，请参见[advanced](developer-reference/logtail-configurations.md)[参数说明](developer-reference/logtail-configurations.md)。
如果Logtail已读取过该日志文件，则从上次读取的Checkpoint处继续读取。
读取日志文件时，每次最多可以读取512 KB，因此每条日志的大小请控制在512 KB以内，否则无法正常读取。
说明
如果您修改了服务器上的时间，请手动重启Logtail，否则会导致日志时间不正确、意外丢弃日志等现象。
### 处理日志
Logtail读取日志后，对日志内容进行分行、解析、设置时间字段。
分行
如果Logtail采集配置中指定了行首正则表达式，则Logtail根据行首正则表达式对每次读取的日志进行分行，切分成多条日志；如果没有指定行首正则表达式，则将一行日志作为一条日志处理。
解析
根据Logtail采集配置中配置的采集模式，对每条日志内容进行解析。
说明
如果您的正则表达式比较复杂，可能会导致CPU占用率过高，请使用合理高效的正则表达式。
如果解析失败，会根据Logtail采集配置中是否开启丢弃解析失败日志的功能进行处理。
开启丢弃解析失败日志，则直接丢弃该日志，并上报解析失败的报错信息。
关闭丢弃解析失败日志，则上传解析失败的原始日志，其中Key为raw_log、Value为日志内容。
设置日志时间字段
如果未配置时间字段，则日志时间为当前解析日志的时间。
如果配置了时间字段：
日志中记录的时间距离当前时间12小时以内，则从解析的日志字段中提取时间。
日志中记录的时间距离当前时间12小时以上，则丢弃该日志并上传错误信息。
### 过滤日志
处理日志后，根据Logtail采集配置中的过滤器配置过滤日志。
在Logtail采集配置中未设置过滤器配置，则不过滤日志，执行下一个步骤。
Logtail采集配置已设置过滤器配置，则对每条日志中的所有字段进行遍历并验证。
只有符合过滤器配置的日志被采集。
### 聚合日志
为降低网络请求次数，在日志处理、过滤完毕后，会在Logtail内部缓存一段时间后进行聚合打包，再发送到日志服务。缓存数据后，触发打包日志发送到日志服务的条件如下：
日志聚合时间超过3秒。
日志聚合条数超过4000条。
日志聚合总大小超过512 KB。
### 发送日志
Logtail将采集到的日志聚合并发送到日志服务。如果数据发送失败，Logtail自动根据错误信息决定重试或放弃发送。
| 错误信息 | 说明 | Logtail 处理方式 |
| --- | --- | --- |
| 401 错误 | 当前账号没有权限采集数据。为该账号授予数据接入相关权限。具体操作，请参见 [配置权限助手](configure-the-permission-assistant-feature.md) 。 | 直接丢弃日志包。 |
| 404 错误 | Logtail 采集配置中指定的 Project 或 LogStore 不存在。 | 直接丢弃日志包。 |
| 403 错误 | Shard Quota 超出限制。 | 等待 3 秒后重试。 |
| 500 错误 | 服务端异常。 | 等待 3 秒后重试。 |
说明
如果要调整数据的发送速度和最大并发数，您可以设置启动参数配置文件中的max_bytes_per_sec参数和send_request_concurrency参数。具体操作，请参见[设置](configure-the-startup-parameters-of-logtail.md)[Logtail](configure-the-startup-parameters-of-logtail.md)[启动参数](configure-the-startup-parameters-of-logtail.md)。
## 功能优势
基于日志文件，无侵入式采集日志。您无需修改应用程序代码，且采集日志不会影响您的应用程序运行。
除采集文本日志外，还支持采集binlog、http数据、容器日志等。
支持Docker、Kubernetes集群等容器集群的数据采集。
阿里云容器服务Kubernetes：请参见[K8s](overview-of-log-collection-from-containers.md)[容器日志提取](overview-of-log-collection-from-containers.md)。
自建Kubernetes：请参见[K8s](overview-of-log-collection-from-containers.md)[容器日志提取](overview-of-log-collection-from-containers.md)。
自建Docker集群：请参见[采集](collect-docker-container-text-logs.md)[Docker](collect-docker-container-text-logs.md)[容器日志（标准输出/文件）](collect-docker-container-text-logs.md)。
稳定处理日志采集过程中的各种异常。当遇到网络异常、服务端异常等问题时会采取主动重试、本地缓存数据等措施保障数据安全。
基于日志服务的集中管理能力。安装Logtail后，只需要在日志服务上配置机器组、Logtail采集配置等信息即可。
完善的自我保护机制。为保证运行在服务器上的Logtail不会明显影响您服务器上其他服务的性能，Logtail在CPU、内存及网络使用方面都做了严格的限制和保护机制。
## 配置流程
[安装](install.md)[Logtail](install.md)
[创建机器组](manage-machine-groups.md)
日志服务Project支持使用IP地址或用户自定义标识创建机器组。
创建Logtail采集配置
您可以通过日志服务控制台配置向导完成操作。具体操作，请参见[采集文本日志](overview-10.md)和[采集容器日志](overview-of-log-collection-from-containers.md)。
完成上述操作后，Logtail开始采集您服务器上的日志，并发送到对应的LogStore中。您可以通过日志服务控制台、API、SDK或CLI查询日志。
## 核心概念
机器组：一个机器组包含一台或多台待采集同类日志的服务器。将Logtail采集配置应用到机器组后，日志服务会根据Logtail采集配置采集机器组内所有服务器上的日志。
日志服务通过机器组管理所有需要通过Logtail采集日志的服务器，支持通过IP地址或者用户自定义标识的方式定义机器组。您可以通过日志服务控制台管理机器组（包括创建、删除机器组，添加、移除机器等操作）。 更多信息，请参见[机器组](machine-group-overview.md)。
Logtail：日志服务提供的日志采集Agent，运行在待采集日志的服务器上。
Linux操作系统：Logtail安装在/usr/local/ilogtail目录下，启动两个以ilogtail开头的独立进程，一个为采集进程，另外一个为守护进程，程序运行日志保存在/usr/local/ilogtail/ilogtail.LOG文件中。更多信息，请参见[安装](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)。
Windows操作系统
Logtail（32位程序）
安装在Windows 32位操作系统中时，对应的安装目录为C:\Program Files\Alibaba\Logtail。
安装在Windows 64位操作系统中时，对应的安装目录为C:\Program Files (x86)\Alibaba\Logtail。
说明
Windows 64位操作系统支持运行32/64位应用程序，但是出于兼容性考虑，在Windows 64位操作系统上，Windows会使用单独的x86目录来存放32位应用程序。
Logtail（64位程序）
只支持安装在Windows 64位操作系统中，对应的安装目录为C:\Program Files\Alibaba\Logtail。
您可以通过控制面板>管理工具>服务，查看LogtailDaemon服务（Logtail 1.0.0.0及以上版本）或LogtailWorker服务（Logtail 0.x.x.x版本），确认Logtail的运行状态。程序运行日志保存在安装目录下的ilogtail.LOG文件中。更多信息，请参见[安装](install-logtail-on-a-windows-server.md)[Logtail（Windows](install-logtail-on-a-windows-server.md)[系统）](install-logtail-on-a-windows-server.md)。
Logtail配置：Logtail采集日志的策略集合。通过在创建Logtail采集配置时设置数据源、采集模式等参数，实现定制化的采集策略。Logtail采集配置定义了如何在服务器上采集同类日志并解析、发送到指定的日志服务LogStore上。
## 基本功能
| 功能 | 说明 |
| --- | --- |
| 实时采集日志 | 动态监控日志文件，实时读取、解析增量日志。日志从生成到发送到日志服务的延迟一般在 3 秒内。更多信息，请参见 [采集流程](use-logtail-to-collect-data.md) 。 说明 Logtail 不支持采集历史日志，对于一条日志，读取该日志的时间减去日志中记录的时间，差值超过 12 小时会被丢弃。如果您要采集历史日志文件，请参见 [导入历史日志文件](import-historical-logs.md) 。 |
| 自动处理日志轮转 | 很多应用会按照文件大小或者日期对日志文件进行轮转（rotation），把原日志文件重命名，并新建一个空日志文件等待写入。例如： app.LOG 文件，通过日志轮转会生成 app.LOG.1 、 app.LOG.2 等。您可以指定采集日志写入的文件，如 app.LOG ，Logtail 会自动检测到日志轮转过程，保证这个过程中不会丢失日志数据。 |
| 多种采集输入源 | Logtail 除支持采集文本日志外，还支持 syslog、http、MySQL binlog 等数据源。更多信息，请参见 [数据采集概述](data-collection-overview.md) 。 |
| 兼容开源采集 Agent | Logtail 支持 Logstash、Beats 等开源软件采集的数据作为数据源。更多信息，请参见 [数据采集概述](data-collection-overview.md) 。 |
| 自动处理采集异常 | 因为服务端错误、网络措施、配额超限等各种异常导致数据发送失败，Logtail 会按场景主动重试。如果重试失败则将数据写入本地缓存，等待 3 秒自动重发。更多信息，请参见 [Logtail](use-the-automatic-diagnostic-tool-of-logtail.md) [自动诊断工具](use-the-automatic-diagnostic-tool-of-logtail.md) 。 |
| 灵活配置采集策略 | 可以通过 Logtail 采集配置非常灵活地采集日志。您可以根据实际场景指定日志目录和文件，支持精确匹配，也支持通配符模糊匹配。您也可以自定义提取日志的方式和提取字段的名称，日志服务支持通过正则表达式提取日志。 由于日志服务中的日志数据模型要求每条日志必须有精确的时间戳信息，Logtail 提供了自定义的日志时间格式，方便您从不同格式的日志数据中提取必要的日志时间戳信息。 |
| 自动同步 Logtail 采集配置 | 您在日志服务控制台上新建或更新 Logtail 采集配置，一般情况下，Logtail 在 3 分钟内即可接收并生效。更新过程中不会丢失日志数据。 |
| 自我监控状态 | Logtail 会实时监控自身 CPU 和内存消耗，避免 Logtail 消耗您太多资源而影响您的其他服务。Logtail 在运行过程中，如果资源使用超出限制将会自动重启，避免影响服务器上的其他服务。同时，Logtail 有主动的网络限流保护措施，防止过度消耗带宽。更多信息，请参见 [启动参数配置文件（ilogtail_config.json）](logtail-configuration-files-and-record-files.md) 。 |
| 签名数据发送 | 为保证您的数据在发送过程中不会被篡改，Logtail 会通过可信通道从服务端获取私密 Token，并对所有发送日志的数据包进行数据签名。 说明 Logtail 在获取私密 Token 时采用 HTTPS 通道，保障相关安全性。 |
## 数据采集可靠性
Logtail在采集日志时，定期将采集的点位（CheckPoint）信息保存到本地，如果遇到服务器意外关闭、进程崩溃等异常情况时，Logtail重启后会从上一次记录的位置开始采集数据，尽可能保证数据不丢失。Logtail会根据启动参数配置文件中配置进行工作，如果资源占用超过限定值5分钟以上，则Logtail会强制重启。重启后可能会产生一定的数据重复。
Logtail内部采用了很多机制提升日志采集可靠性，但并不能保证日志一定不会丢失。以下情况可能造成日志丢失：
Logtail未运行且日志轮转多次。
日志轮转速度极快，例如1秒轮转1次。
日志采集速度长期无法达到日志产生速度。
## 相关文档
[Logtail](logtail-diagnostics.md)[诊断](logtail-diagnostics.md)
[Logtail](faq-about-logtail-46.md)[常见问题](faq-about-logtail-46.md)
[Logtail](logtail-limits.md)[限制说明](logtail-limits.md)
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
