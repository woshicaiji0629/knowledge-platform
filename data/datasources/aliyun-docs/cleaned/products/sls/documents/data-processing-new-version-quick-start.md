# 数据加工（新版）快速入门-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/data-processing-new-version-quick-start

# 快速入门
本文以网站访问日志为例，为您介绍完整的数据加工流程，帮助您快速熟悉数据加工功能及其操作。
## 准备工作
已创建名为web-project的Project。具体操作，请参见[管理](manage-a-project.md)[Project](manage-a-project.md)。
在Project（web-project）中创建名为website_log的源LogStore。具体操作，请参见[管理](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
已采集网站访问日志到源LogStore（website_log）。具体操作，请参见[数据采集概述](data-collection-overview.md)。
在Project（web-project）中创建目标LogStore（website_fail）。
如果您使用的是RAM用户，则需要先授予RAM用户数据加工操作权限。具体操作，请参见[授权](authorized-ram-user-operation-data-processing.md)[RAM](authorized-ram-user-operation-data-processing.md)[用户操作数据加工](authorized-ram-user-operation-data-processing.md)。
已配置源LogStore和目标LogStore的索引。具体操作，请参见[创建索引](create-indexes.md)。
说明
数据加工任务不依赖索引，但若不配置索引，将无法执行查询和分析操作。
## 背景信息
某网站将其所有的访问日志存储在LogStore（website_log）中，目前为了提升用户体验，需要对用户访问错误进行分析。所以，需求是将访问状态码为4XX的访问日志筛选出来，同时过滤掉访问的用户个人信息，并将结果写入新的LogStore（website_fail）,提供给业务分析人员使用。日志样例如下：
body_bytes_sent: 1061 http_user_agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5 remote_addr: 192.0.2.2 remote_user: vd_yw request_method: GET request_uri: /request/path-1/file-5 status: 400 time_local: 10/Jun/2021:19:10:59 error: Invalid time range
## 步骤一：创建数据加工任务
登录[日志服务控制台](https://sls.console.aliyun.com)。
进入数据加工页面。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
在查询与分析页面，单击数据加工。
在页面右上角，选择数据的时间范围。
选择时间范围后，请确认原始日志页签中存在日志。
在编辑框中，输入如下加工SPL规则。
* | extend status=cast(status as BIGINT) | where status>=0 AND status<500 | project-away remote_addr, remote_user
调试SPL规则。
从原始数据中选择测试数据，或者手动填入测试数据。
[ { "body_bytes_sent": "1061", "http_user_agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5", "remote_addr": "192.0.2.2", "remote_user": "vd_yw", "request_method": "DELETE", "request_uri": "/request/path-1/file-5", "status": "400", "time_local": "10/Jun/2021:19:10:59", "error": "Invalid time range" } ]
点击▷，执行调试运行。
查看预览结果。执行完成后，切换到加工结果标签页查看结果。加工后的日志已被结构化为多个字段，例如body_bytes_sent、error、http_user_agent、request_method、request_uri、status、time_local等。
创建数据加工任务。
单击保存数据加工（新版）。
在创建数据加工任务（新版）面板中，配置如下信息，然后单击确定。
| 参数 | 说明 |
| --- | --- |
| 任务名称 | 数据加工任务的名称。 |
| 显示名称 | 数据加工显示的名称。 |
| 任务描述 | 数据加工任务的描述。 |
| 授权方式 | 您可以通过如下方式授予数据加工任务读取源 LogStore 中数据的权限。 默认角色 ：授予数据加工任务使用阿里云系统角色 AliyunLogETLRole 来读取源 LogStore 中的数据。单击 授权系统角色 AliyunLogETLRole ，根据页面提示完成授权。更多信息，请参见 [通过默认角色访问数据](access-data-by-using-a-default-role.md) 。 重要 如果您使用的是 RAM 用户，需要由阿里云账号先完成授权。 已完成授权的阿里云账号，无需再次授权。 自定义角色 ：授予数据加工任务使用自定义角色来读取源 LogStore 中的数据。您需先授予自定义角色读取源 LogStore 数据的权限，然后在 角色 ARN 中输入您自定义角色的 ARN。如何授权，请参见 [通过自定义角色访问数据](access-data-by-using-a-custom-role.md) 。 密钥 ：根据集团安全要求，不再支持 AK/SK 创建任务。 |
| 存储目标 |  |
| 目标名称 | 存储目标的名称。存储目标中包括 Project、LogStore 等配置。 |
| 目标 Region | 选择目标 Project 所在地域。 |
| 目标 Project | 用于存储数据加工结果的目标 Project 名称。目标 Project 可以通过 SPL 规则动态指定，详情请参见 [动态目标](processing-result-output-configuration.md) [Project/LogStore](processing-result-output-configuration.md) [输出](processing-result-output-configuration.md) 。如果 SPL 中动态指定，则使用该 Project，否则使用当前配置的默认 Project。 重要 SPL 规则动态指定的 Project 须与当前配置的 Region、授权相匹配。 |
| 目标库 | 用于存储数据加工结果的目标 LogStore 名称。目标 LogStore 可以通过 SPL 规则动态指定，详情请参见 [动态目标](processing-result-output-configuration.md) [Project/LogStore](processing-result-output-configuration.md) [输出](processing-result-output-configuration.md) 。如果 SPL 中动态指定，则使用该 LogStore，否则使用当前配置的默认 LogStore。 重要 SPL 规则动态指定的 LogStore 须与当前配置的 Region、授权、以及 Project 相匹配。禁止目标 LogStore 与源 LogStore 相同。 警告 请勿将目标库配置为当前源库（即同源配置），否则可能导致日志被循环写入，产生额外的存储与流量费用。由此造成的资源消耗及相关费用，将由用户自行承担。 |
| 授权方式 | 您可以通过如下方式授予数据加工任务写目标 LogStore 的权限。 默认角色 ：授予数据加工任务使用阿里云系统角色 AliyunLogETLRole 将数据加工结果写入目标 LogStore。 单击 授权系统角色 AliyunLogETLRole ，根据页面提示完成授权。更多信息，请参见 [通过默认角色访问数据](access-data-by-using-a-default-role.md) 。 重要 如果您使用的是 RAM 用户，需要由阿里云账号先完成授权。 已完成授权的阿里云账号，无需再次授权。 自定义角色 ：授予数据加工任务使用自定义角色将数据加工结果写入目标 LogStore。您需先授予自定义角色写数据到目标 LogStore 的权限，然后在 角色 ARN 中输入您自定义角色的 ARN。如何授权，请参见 [通过自定义角色访问数据](access-data-by-using-a-custom-role.md) 。 密钥 ：根据集团安全要求，不再支持 AK/SK 创建任务。 |
| 写入结果集 | 需要写入至当前目标 LogStore 的数据集，数据加工（新版）处理结果的数据集详情请参见 [加工结果输出配置](processing-result-output-configuration.md) 。一个输出目标可配置多个数据集，单个数据集也可被多个目标选中。 |
| 加工范围 |  |
| 时间范围 （数据接收时间） | 指定数据加工任务的时间范围，详细说明如下： 所有 ：从 LogStore 接收到第一条日志的时间点开始数据加工任务，直到加工任务被手动停止。 某时间开始 ：指定数据加工任务的开始时间，从该时间点开始加工，直到加工任务被手动停止。 特定时间范围 ：指定数据加工任务的起止时间，加工任务执行到指定时间后自动停止。 |
| 高级选项 |  |
| 高级参数配置 | 对于加工语句中需要使用的密码信息（例如数据库连接密码），日志服务支持使用键值对形式保存在密钥对中，即您可以在加工语句中通过 res_local("key") 进行引用。 单击 + ，可添加多个键值对。例如 config.vpc.vpc_id.test1：vpc-uf6mskb0b****n9yj，表示 RDS 实例所属的专有网络 ID。 |
进入目标LogStore（website_fail），执行查询和分析操作。具体操作，请参见[查询与分析快速指引](quick-guide-to-query-and-analysis.md)。
## 步骤二：观测数据加工任务
在左侧导航栏中，选择任务管理>数据加工。
在加工任务列表中，单击目标加工任务。
在数据加工概览（新版）页面，查看数据加工任务详情。您可以查看任务详情与状态，修改、启动、停止和删除任务等。具体操作，请参见[管理数据加工（新版）任务](manage-data-processing-new-version-job.md)。也可以观测任务运行状态和运行指标，具体操作，请参见[观测与监控数据加工（新版）任务](observation-and-monitoring-data-processing-new-edition-job.md)。
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
