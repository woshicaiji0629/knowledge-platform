# 下载日志方式及操作步骤-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/download-logs

# 下载日志
日志服务支持将日志或查询分析结果下载到本地，本文介绍下载方式及操作步骤。
## 下载方式说明
日志服务提供控制台、Cloud Shell、日志服务CLI或SDK下载方式下载日志或查询分析结果。
重要
日志服务CLI或SDK下载方式无数量限制，但可能由于网络等不确定因素，出现下载中断问题。
仅控制台方式支持压缩下载。
若当前LogStore的计费模式为按写入数据量计费时，下载查询和分析结果（SQL结果）时不产生费用。具体内容，可参见[按写入数据量计费](billing-per-amount-of-data-written.md)。
若当前LogStore的计费模式为按使用功能计费时，下载查询和分析结果（SQL结果）时，会使用SQL独享版，因此会产生SQL独享版相关的费用。费用说明，请参见[按使用功能计费模式计费项](billable-items.md)。
| 比较项 | 通过控制台直接下载（推荐） | 通过 OpenAPI 下载 | 通过命令行工具（CLI）下载 | 通过 Cloud Shell 下载 | 通过 SDK 下载 |
| --- | --- | --- | --- | --- | --- |
| 数据量限制 | 仅查询：华东 1（杭州）、华东 2（上海）、华北 2（北京）、华南 1（深圳）和新加坡地域最多支持下载 2000 万行数据，其他地域最多支持下载 100 万行数据。数据量不超过 20 GB。 SQL 分析：数据量不超过 2GB。 | 仅查询：华东 1（杭州）、华东 2（上海）、华北 2（北京）、华南 1（深圳）和新加坡地域最多支持下载 2000 万行数据，其他地域最多支持下载 100 万行数据。数据量不超过 20 GB。 SQL 分析：数据量不超过 2GB。 | 仅查询：无限制 SQL 分析：数据量不超过 2GB。 | 仅查询：无限制 SQL 分析：数据量不超过 2 GB。 | 仅查询：无限制 SQL 分析：数据量不超过 2 GB。 |
| 依赖部署 | 无 | 无 | 手动安装日志服务 CLI。 | 自动部署，首次运行时需要等待初始化。 | 手动安装日志服务 SDK，并需要自定义代码。 |
| 授权 | [下载权限配置](download-logs.md) | [下载权限配置](download-logs.md) | 手动配置 | 自动配置 | 手动配置 |
| SQL 独享版 | 下载 SQL 分析结果时，使用 SQL 独享版 | 下载 SQL 分析结果时，使用 SQL 独享版 | 不使用 | 不使用 | 按实际需求，设置参数配置。 |
| 外网读取流量 | 无 | 无 | 部署在与 Project 相同地域的 ECS 上且使用日志服务私网域名时，不会产生外网读取流量费用。 | 当 Project 在华东 2（上海）地域时，不会产生外网读取流量费用。 | 部署在与 Project 相同地域的 ECS 上且使用日志服务私网域名时，不会产生外网读取流量费用。 |
| NAS 集成 | 无 | 无 | 必要时，手动配置 | 自动配置 | 必要时，手动配置 |
您也可以将日志投递到OSS，通过OSS进行下载。关于投递的具体操作，请参见[创建](create-oss-shipping-tasks-new-version.md)[OSS](create-oss-shipping-tasks-new-version.md)[投递任务（新版）](create-oss-shipping-tasks-new-version.md)。
下载权限配置（点击查看）
{ "Version": "1", "Statement": [ { "Action": [ "log:ListDownloadJobs", "log:CreateDownloadJob", "log:GetDownloadJob", "log:DeleteDownloadJob" ], "Resource": [ "acs:log:*:*:project/Project名称/downloadjob/*" ], "Effect": "Allow" } ] }
## 操作步骤
### 通过控制台直接下载
日志服务支持通过控制台直接将日志或查询分析结果下载到本地，两者的下载操作类似，本文以下载日志为例进行说明。如果您要下载查询分析结果，可在执行查询分析操作后，在统计图表页签中，单击下载日志。
重要
超过单次下载的最大数量时，仅下载最大支持的数量。如果您需要下载全量日志，可缩小查询的时间范围，分多次下载。
单个阿里云账号最多支持3个并发下载操作（总下载次数无限制）。超出3个并发下载操作或多个RAM用户同时操作时，可能报错，此时您可等待其他操作完成后，再重试。
支持保存最近1天内的导出记录，超过1天的导出记录被自动清除。
在遇到网络错误或者查询不精确时，系统会自动重试下载任务。如果重试3次后，仍无法完成下载，则下载任务为失败状态。
在线下载（另存为）与离线下载（任务管理）的区别：
另存为：直接下载当前页面查询到的精确结果，适用于小数据量场景。若导出数据量过大（如几十万条），可能导致浏览器页面无响应或崩溃。此时建议改用任务管理中的离线下载功能，或缩小查询时间范围减少单次下载量。
任务管理（离线下载）：适用于大数据量场景，后台异步处理，性能更优。下载任务创建后可关闭页面，任务完成后在任务管理中下载文件。
离线下载任务的实际下载条数可能与前端查询显示的条数存在细微差异，此属正常现象。
若页面刷新导致复制失效或在线下载失败，请优先使用日志下载功能而非手动复制粘贴。
在线下载失败但离线下载成功的排查建议：
检查网络是否稳定，查询条件是否过于复杂。
优先尝试使用离线下载（任务管理）或 CLI/SDK 方式，这些方式更稳定，适用于大数据量场景。
若必须使用在线下载且持续失败，建议缩小时间范围，分多次下载。
如果下载日志按钮显示为灰色不可用，请按以下步骤排查：
确认当前处于原始日志页签。统计图表等其他视图不支持下载操作。
确认查询有返回结果。若查询结果为空，下载按钮将置灰不可用。请调整查询语句或时间范围后重新查询。
确认 RAM 用户已授予下载相关权限。需要log:CreateDownloadJob、log:ListDownloadJobs等权限，详见本文档"下载权限配置"部分。
确认当前账号的并发下载任务数未达到上限。单个阿里云账号最多支持 3 个并发下载任务，超出限制时需等待已有任务完成后重试。
若查询返回条数过少（如仅 20 条），可能是过滤条件过于严格。建议放宽时间范围或调整查询语句。
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标LogStore。
输入查询语句，然后选择时间范围。
在原始日志页签中，选择>下载日志。
在日志下载对话框中，完成如下配置，然后单击确定。
| 参数 | 说明 |
| --- | --- |
| 任务名 | 下载任务的名称。 |
| 日志数量 | 选择要下载的日志数量。 |
| 数据格式 | 支持 CSV 格式和 JSON 格式。 采用 CSV 格式时，文件中的列名将根据前 100 条日志的字段生成。如果后续日志存在新的字段，则所有新的字段将以 JSON 格式存放在 CSV 文件的最后一列（列名为空）。 采用 JSON 格式时，单条日志的内容会转换为 JSON 格式，然后以单行形式写入文件。 |
| quote 字符 | 选择 Quote 字符，用于包裹日志中的特殊字符，避免被转义。 |
| 是否允许下载不精确的结果 | 如果选择 否 ，则当出现查询结果不精确时，会导致下载失败。 |
| 压缩方式 | 支持 gzip、lz4、zstd 等压缩方式，也支持不压缩。 当下载的日志数量较多时，强烈建议采用压缩方式，可显著降低下载量，减少文件的下载时间。 |
在下载任务对话框中，等待任务状态为任务成功后，单击下载，将日志下载到本地。
您也可以在原始日志页签中，选择>下载任务，打开下载任务对话框，查看下载记录。
## 通过OpenAPI下载
[CreateDownloadJob - 创建日志下载任务](developer-reference/api-sls-2020-12-30-createdownloadjob.md)：
重要
超过单次下载的最大数量时，仅下载最大支持的数量。如果您需要下载全量日志，可缩小查询的时间范围，分多次下载。
单个阿里云账号最多支持3个并发下载操作（总下载次数无限制）。超出3个并发下载操作或多个RAM用户同时操作时，可能报错，此时您可等待其他操作完成后，再重试。
支持保存最近1天内的导出记录，超过1天的导出记录被自动清除。
在遇到网络错误或者查询不精确时，系统会自动重试下载任务。如果重试3次后，仍无法完成下载，则下载任务为失败状态。
OpenAPI 批量下载注意事项：
索引配置要求：调用 GetLogs API 或执行 SQL 查询时，需确保查询字段已在 LogStore 的索引属性中配置。如果查询字段未配置索引，将报ParameterInvalid错误。索引配置方法请参见[创建索引](developer-reference/api-sls-2020-12-30-createdownloadjob.md)。
下载指定字段：若只需下载特定字段（如 message），应在 SQL 中使用 SELECT 语句过滤，例如* | SELECT message，然后执行下载操作，以减少不必要的数据量。
### 通过Cloud Shell下载
目前 Cloud Shell 位于上海地域，如果当前 LogStore 不在上海地域，下载日志会产生一定的外网读取流量费用。价格详情请参见[产品定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.11.66cd2aab6wAn6p#/sls/detail)。
海量日志导出：当需要导出大量日志（如亿级数据量）时，推荐使用 Cloud Shell 或 CLI/SDK 方式下载，避免通过控制台分批次下载的繁琐操作。Cloud Shell 无需手动安装依赖，适合快速执行大规模导出任务。
操作步骤，参见[使用](developer-reference/use-cloud-shell-to-download-logs-from-log-service.md)[Cloud Shell](developer-reference/use-cloud-shell-to-download-logs-from-log-service.md)[下载日志数据](developer-reference/use-cloud-shell-to-download-logs-from-log-service.md)。
### 通过命令行工具下载
当您需要下载更大数量的日志时，可以通过命令行工具进行下载。
安装命令行工具。具体操作，请参见[安装](developer-reference/install-log-service-cli.md)[CLI](developer-reference/install-log-service-cli.md)。
获取当前账号的AccessKey。具体操作，请参见[访问密钥](developer-reference/access-key.md)。
获取下载日志的命令。具体步骤，请参见[get_log_all](developer-reference/get-log-all.md)。
例如：在命令行工具中执行下载命令，执行成功后自动下载到运行命令行的当前目录下的downloaded_data.txt。
aliyunlog log get_log_all --project="aliyun-test-project" --logstore="aliyun-test-logstore" --from_time="2024-07-01 15:33:00+8:00" --to_time="2024-07-09 15:23:00+8:00" --query="status:200|select request_method as method,COUNT(*) as pv group by method order by pv" --region-endpoint="cn-hangzhou.log.aliyuncs.com" --format-output=json --access-id="LT***CyGg" --access-key="8P***zi" >> ./downloaded_data.txt
更多信息，请参见[使用日志服务](developer-reference/overview-of-log-service-cli.md)[CLI](developer-reference/overview-of-log-service-cli.md)。
### 通过SDK下载
当您需要下载更大数量的日志时，可通过SDK下载。
说明
SDK下载日志接口就是查询日志的接口。
Python SDK示例如下：
import os import time from aliyun.log import LogClient from aliyun.log import GetLogsRequest # 日志服务的服务接入点。 endpoint = 'cn-qingdao.log.aliyuncs.com' # 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 accessKeyId = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID', '') accessKey = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET', '') # Project名称。 project = 'Project名称' # Logstore名称。 logstore = 'Logstore名称' client = LogClient(endpoint, accessKeyId, accessKey) request = GetLogsRequest("project1", "logstore1", fromTime=int(time()-3600), toTime=int(time()), topic='', query="*", line=100, offset=0, reverse=False) # 或者 # request = GetLogsRequest("project1", "logstore1", fromTime="2018-1-1 10:10:10", toTime="2018-1-1 10:20:10", topic='', query="*", line=100, offset=0, reverse=False) res = client.get_logs(request) res.log_print()
更多信息，请参见[SDK](developer-reference/overview-of-log-service-sdk.md)[参考概述](developer-reference/overview-of-log-service-sdk.md)。
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
