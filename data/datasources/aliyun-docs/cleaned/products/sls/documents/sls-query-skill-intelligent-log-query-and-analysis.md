# SLS Query Skill 智能查询分析日志-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/sls-query-skill-intelligent-log-query-and-analysis

# 使用SLS Query Skill 智能查询分析日志
alibabacloud-sls-query 是一个 Agent Skill，支持在 AI Agent 中通过自然语言查询和分析 SLS 日志数据。安装后，Agent 自动将查询意图转换为 SLS 查询语句并执行，返回结构化分析结果。
## 适用场景
| 场景 | 说明 | 示例提示词 |
| --- | --- | --- |
| 日志检索 | 按关键字、字段、状态码、Trace ID、用户 ID 等条件查询日志明细。 | 查询最近 10 分钟 status>=500 的 NGINX 访问日志明细。 |
| SQL 统计分析 | 对日志进行聚合、分组、排序、Top-N、趋势分析或字段投影。 | 统计最近 1 小时 5xx 错误最多的接口 Top 10。 |
| 查询语句生成 | 将自然语言需求转换为 SLS 索引查询语句、SQL 语句或 SPL 语句。 | 生成按分钟统计平均延迟和 P95 延迟的查询语句。 |
| 查询优化 | 根据索引配置和字段类型优化现有查询，减少不必要的数据扫描。 | 优化现有查询语句，优先使用字段索引并减少不必要的数据扫描。 |
说明
日志服务也可通过[调用可观测](large-language-model-llm-application-calls-observable-mcp-service-to-implement-log-query-and-analysis.md)[MCP](large-language-model-llm-application-calls-observable-mcp-service-to-implement-log-query-and-analysis.md)[服务实现日志查询与分析](large-language-model-llm-application-calls-observable-mcp-service-to-implement-log-query-and-analysis.md)。
## 前提条件
已创建日志服务 Project 和 LogStore，并已采集日志数据。
已为目标 LogStore 创建索引。未配置索引SLS 查询、SQL 分析和 SPL 查询无法执行。
已获取可访问目标 Project 和 LogStore 的阿里云账号凭据。
警告
为防止凭据泄露，不要在 Agent 对话中粘贴 AccessKey ID 或 AccessKey Secret。建议通过环境变量或阿里云 CLI 配置文件管理凭据。
## 安装 Skill
alibabacloud-sls-query 已在[阿里云 Skill](https://skills.aliyun.com/skills/alibabacloud-sls-query)和[ClawHub](https://clawhub.ai/sdk-team/alibabacloud-sls-query)发布，支持以下安装方式。
## 方式一（推荐）：通过 npx 命令安装
npx 命令随 Node.js 一起提供。安装前，执行以下命令确认本地环境可用：
node -v npx -v
如果终端提示node或npx不存在，请先前往[Node.js 官网](https://nodejs.org/)下载并安装。
执行以下命令安装 alibabacloud-sls-query Skill：
npx skills add aliyun/alibabacloud-aiops-skills --skill alibabacloud-sls-query
安装完成后，确认 skills 目录下存在alibabacloud-sls-query目录，然后重启 Agent 使 Skill 生效。
## 方式二：手动下载安装
从[GitHub Release](https://github.com/aliyun/alibabacloud-aiops-skills/releases/tag/alibabacloud-sls-query-0.0.1)下载 alibabacloud-sls-query 安装包，解压后将文件复制到对应 Agent 的 skills 安装目录中。
复制完成后，确保 skills 目录下存在alibabacloud-sls-query目录，然后重启 Agent 以加载该 Skill。
常见 Agent 的 skills 安装目录如下：
| Agent | 项目级安装目录 | 用户级安装目录 |
| --- | --- | --- |
| Claude Code | .claude/skills | ~/.claude/skills |
| Codex | .agents/skills | ~/.agents/skills |
| Qoder | .qoder/skills | ~/.qoder/skills |
| QwenCode | .qwen/skills | ~/.qwen/skills |
| OpenClaw | .openclaw/skills | ~/.openclaw/skills |
## 查询和分析日志
安装完成后，在 Agent 中直接描述 SLS 查询或分析需求即可触发该 Skill。Agent 自动执行以下流程：
检查运行环境（阿里云 CLI 和 SLS 插件）。
读取目标 LogStore 的索引配置。
根据需求生成查询语句（索引查询、SQL 或 SPL）。
通过阿里云 CLI 执行查询。
输出整理后的结构化结果。
首次执行时，Agent 会引导完成阿里云 CLI 的安装和凭据配置。按提示授予执行权限并完成配置即可。
### 提示词最佳实践
提示词的质量直接影响查询结果的准确性。编写提示词时，建议包含以下信息：
Project 名称和 LogStore 名称。
明确的查询或分析意图。例如“分析请求延迟同比变化，按分钟粒度统计平均延迟”。
查询时间范围。例如“最近 15 分钟”或“2026-04-24 10：00 到 11：00，北京时间”。
期望输出格式。例如“返回原始日志"”统计 Top 10""按分钟画趋势“"只返回这些字段”。
为提高查询效率和降低成本，建议：
尽量缩小时间范围，避免全量扫描。
明确指定字段名（如status、request_uri），而非模糊描述。
需要 Top-N 结果时，在提示词中说明具体数量（如 Top 10）。
说明
以下示例场景中的 Project、LogStore、字段名和查询结果均为示例数据。实际使用时，请替换为实际的资源名称和日志字段。
### 场景一：查询最近 15 分钟的 5xx 错误日志
提示词
查询 SLS 日志库 Project=prod-web，Logstore=nginx-access，最近 15 分钟 status 大于等于 500 的请求，按时间倒序。
Agent 输出示例
查询模式：索引查询。 原因：用户需要按条件返回原始日志，不涉及聚合、排序分析或字段投影；status 字段已配置数值类型索引，可直接使用范围查询。 执行命令： aliyun sls get-logs-v2 \ --project prod-web \ --logstore nginx-access \ --from 1777016700 \ --to 1777017600 \ --query 'status>=500' \ --line 100 \ --offset 0 \ --reverse true 查询结果： | 时间 | status | request_uri | upstream_status | request_time | message | | --- | ---: | --- | ---: | ---: | --- | | 2026-04-24 15:59:31 | 502 | /api/order/create | 502 | 1.238 | upstream connect timeout | | 2026-04-24 15:58:44 | 500 | /api/pay/notify | 500 | 0.412 | internal server error | | 2026-04-24 15:57:09 | 502 | /api/order/create | 502 | 1.104 | bad gateway | 结论：已按时间倒序返回最近 15 分钟内的 5xx 原始日志，最新错误集中出现在 /api/order/create。
### 场景二：统计 5xx 错误接口 Top 10
提示词
统计 SLS 日志库 prod-web/nginx-access 中最近 1 小时内 5xx 数量 Top 10 的接口。
Agent 输出示例
查询模式：索引查询 + SQL。 原因：需要统计 5xx 数量 Top10 的接口，因此先用索引查询过滤 500 到 599 状态码，再用 SQL 按 request_uri 分组、计数并排序。 执行命令： aliyun sls get-logs-v2 \ --project prod-web \ --logstore nginx-access \ --from 1777014000 \ --to 1777017600 \ --query 'status in [500 599] | SELECT request_uri, count(*) AS errors FROM log GROUP BY request_uri ORDER BY errors DESC LIMIT 10' 查询结果： | 排名 | request_uri | errors | | --- | --- | ---: | | 1 | /api/order/create | 186 | | 2 | /api/pay/notify | 73 | ..... | 10 | /api/user/login | 1 | 结论：最近 1 小时内 5xx 数量最高的接口是 /api/order/create，其错误量明显高于其他接口，建议优先排查该接口及其后端依赖。
### 场景三：对比最近一小时与昨天同期的延迟趋势
提示词
分析 SLS 日志库 prod-web/nginx-access 中最近一小时与昨天同期相比的平均延迟变化，按分钟粒度统计平均值，分析延迟是否存在明显异常。
Agent 输出示例
查询模式：索引查询 + SQL 原因：需要对当前最近一小时和昨天同期分别按分钟聚合平均延迟，再按分钟对齐计算变化量和变化率。 执行命令（当前最近一小时）： aliyun sls get-logs-v2 \ --project prod-web \ --logstore nginx-access \ --from 1777014000 \ --to 1777017600 \ --query "* | SELECT date_trunc('minute', __time__) AS minute, avg(request_time) AS avg_latency FROM log GROUP BY minute ORDER BY minute LIMIT 60" 执行命令（昨天同期）： aliyun sls get-logs-v2 \ --project prod-web \ --logstore nginx-access \ --from 1776927600 \ --to 1776931200 \ --query "* | SELECT date_trunc('minute', __time__) AS minute, avg(request_time) AS avg_latency FROM log GROUP BY minute ORDER BY minute LIMIT 60" 查询结果： | 分钟 | 当前平均延迟 | 昨天同期平均延迟 | 变化量 | 变化率 | | --- | ---: | ---: | ---: | ---: | | 2026-04-24 15:00 | 0.132s | 0.118s | +14ms | +11.9% | | 2026-04-24 15:01 | 0.141s | 0.116s | +25ms | +21.6% | | 2026-04-24 15:02 | 0.338s | 0.129s | +209ms | +162.0% | | 2026-04-24 15:03 | 0.351s | 0.131s | +220ms | +167.9% | 结论：最近一小时平均延迟整体高于昨天同期，其中 15:02 到 15:03 上升最明显，平均延迟增加超过 160%。建议继续按 request_uri、upstream_addr 或 service 维度下钻，定位延迟上升来源。
### 场景四：基于查询结果继续追问
SLS Query Skill 支持多轮交互。可以基于前一次查询结果继续追问，逐步缩小排查范围。
第一轮提示词
统计 SLS 日志库 prod-web/nginx-access 中最近 1 小时 5xx 最多的接口 Top 5。
第二轮提示词（基于第一轮结果追问）
针对 /api/order/create 接口，按分钟粒度统计错误数量趋势，查看错误是集中爆发还是均匀分布。
第三轮提示词（进一步下钻）
查看 /api/order/create 在 15：02 到 15：05 之间的 5xx 原始日志，返回 upstream_addr 和 message 字段。
通过多轮追问，可以从宏观统计逐步下钻到具体时间段的原始日志，快速定位故障根因。
## 数据安全与隐私
SLS Query Skill 通过阿里云 CLI 执行查询，查询过程遵循以下安全原则：
查询请求通过 HTTPS 加密传输，日志数据不经过第三方服务。
Agent 在本地生成和执行查询命令，日志数据不会发送给 AI 模型提供商。
凭据信息（AccessKey）通过阿里云 CLI 配置文件或环境变量管理，不会出现在 Agent 对话记录中。
重要
不要在 Agent 对话中直接粘贴 AccessKey ID 或 AccessKey Secret。如需配置凭据，请使用aliyun configure命令。
## 使用限制
| 限制项 | 说明 |
| --- | --- |
| 索引配置 | 目标 LogStore 必须已创建索引。未配置索引时，所有查询类型均无法执行。 |
| 查询超时 | 单次查询默认超时时间为 60 秒。超时后可尝试缩小时间范围或简化查询条件。 |
| 数据扫描量 | 查询费用与数据扫描量相关。建议尽量缩小时间范围和使用字段索引，减少不必要的全量扫描。 |
| 运行环境 | 需要 Node.js 运行时（用于安装 Skill）和阿里云 CLI（用于执行查询）。 |
## 常见问题
### 是否需要手动安装阿里云 CLI 和 SLS 插件？
一般情况下不需要手动安装。在 Agent 中发起查询需求后，Agent 会自动检查环境（aliyun version）、启用 AI Mode、设置 User-Agent 并执行插件更新。
如果本机未安装阿里云 CLI 或版本过低，Agent 会给出安装或升级指引。按照 Agent 输出的命令在本机环境中完成安装即可。
### 如何配置阿里云账号凭据？
可以根据 Agent 引导提示配置账号凭据，也可以手动执行aliyun configure命令配置。支持 AK、StsToken、OAuth、RamRole 等多种凭据配置方式。详情参考[配置凭证](https://help.aliyun.com/zh/cli/configure-credentials/)。
### 是否支持内网域名、传输加速域名、自定义域名？
支持。在提示词中告知 Agent 使用--endpoint <域名>指定 Endpoint 即可。
### 查询结果不准确怎么办？
可以从以下方面排查和优化：
确认目标字段已正确配置索引，且字段类型与查询条件匹配（例如 status 应为 long 类型而非 text）。
在提示词中明确指定字段名、时间范围和期望格式，避免模糊描述。
基于 Agent 返回的查询语句检查逻辑是否符合预期，通过追问修正查询条件。
## 故障排查
### 报错 IndexConfigNotExist
该错误表示目标 LogStore 没有索引配置或索引配置为空。
解决方法：在 SLS 控制台为目标 LogStore 创建索引。创建完成后等待片刻（新数据需要短暂时间才能被索引），然后重新执行查询。
### 报错 Unauthorized
该错误表示当前账号或 RAM 用户缺少必要权限。
解决方法：为当前账号授予以下权限：
| API 名称 | Action | Resource |
| --- | --- | --- |
| GetLogsV2 | log:GetLogStoreLogs | acs:log:<account>:<region>:project/<Project>/logstore/<Logstore> |
| GetIndex | log:GetIndex | acs:log:<account>:<region>:project/<Project> |
### 报错 ProjectNotExist
该错误通常是 Project 名称错误、地域不正确或访问了错误的 Endpoint。
解决方法：确认以下信息：
Project 名称是否准确。
地域是否与 Project 所在地域一致。
网络环境是否需要使用内网 Endpoint。
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
