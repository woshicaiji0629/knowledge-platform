# 全链路模型服务应用构建-大模型服务平台百炼-阿里云-大模型服务平台百炼(Model Studio)-阿里云帮助中心

Source: https://help.aliyun.com/zh/model-studio/what-is-model-studio

# 什么是阿里云百炼
阿里云百炼是一站式大模型开发与应用平台，集成千问及主流第三方模型。面向开发者提供兼容 OpenAI 的API和全链路模型服务；面向业务人员提供可视化应用构建能力，可快速创建智能体、知识库问答等 AI 应用。
主要能力：
##
##
##
| 调用 API 几行代码即可调用大模型，实现内容创作、摘要生成等功能。 百炼兼容 OpenAI 接口规范，只需调整 API Key、base_url 和模型名称，即可将现有 OpenAI 代码迁移至百炼。 Python import os from openai import OpenAI # 注意: 不同地域的 base_url 不通用（下方示例使用北京地域的 base_url） # - 华北 2（北京）: https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1，请将 WorkspaceId 替换为业务空间 ID # - 新加坡: https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1 # - 德国（法兰克福）: https://{WorkspaceId}.eu-central-1.maas.aliyuncs.com/compatible-mode/v1 # - 日本（东京）: https://{WorkspaceId}.ap-northeast-1.maas.aliyuncs.com/compatible-mode/v1 # - 美国（弗吉尼亚）: https://dashscope-us.aliyuncs.com/compatible-mode/v1 client = OpenAI( api_key=os.getenv("DASHSCOPE_API_KEY"), base_url="https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1", ) completion = client.chat.completions.create( model="qwen3.7-plus", messages=[{'role': 'user', 'content': '你是谁？'}] ) print(completion.choices[0].message.content) Node.js import OpenAI from "openai"; // 注意: 不同地域的 base_url 不通用（下方示例使用北京地域的 base_url） // - 华北 2（北京）: https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1，请将 WorkspaceId 替换为业务空间 ID // - 美国（弗吉尼亚）: https://dashscope-us.aliyuncs.com/compatible-mode/v1 // - 新加坡: https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1，请将 WorkspaceId 替换为业务空间 ID // - 德国（法兰克福）: https://{WorkspaceId}.eu-central-1.maas.aliyuncs.com/compatible-mode/v1，请将 WorkspaceId 替换为业务空间 ID // - 日本（东京）: https://{WorkspaceId}.ap-northeast-1.maas.aliyuncs.com/compatible-mode/v1，请将 WorkspaceId 替换为业务空间 ID const openai = new OpenAI( { apiKey: process.env.DASHSCOPE_API_KEY, baseURL: "https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1", } ); async function main() { const completion = await openai.chat.completions.create({ model: "qwen3.7-plus", messages: [{ role: "user", content: "你是谁？"}], }); console.log(completion.choices[0].message.content) } main() curl 不同地域的 Base URL 不通用（以下示例是北京地域 Base URL） 华北 2（北京）： https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1/chat/completions ，请将 WorkspaceId 替换为业务空间 ID 美国（弗吉尼亚）： https://dashscope-us.aliyuncs.com/compatible-mode/v1/chat/completions 新加坡： https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1/chat/completions ，请将 WorkspaceId 替换为业务空间 ID 德国（法兰克福）： https://{WorkspaceId}.eu-central-1.maas.aliyuncs.com/compatible-mode/v1/chat/completions ，请将 WorkspaceId 替换为业务空间 ID 日本（东京）： https://{WorkspaceId}.ap-northeast-1.maas.aliyuncs.com/compatible-mode/v1/chat/completions ，请将 WorkspaceId 替换为业务空间 ID curl -X POST https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1/chat/completions \ -H "Authorization: Bearer $DASHSCOPE_API_KEY" \ -H "Content-Type: application/json" \ -d '{ "model": "qwen3.7-plus", "messages": [ { "role": "user", "content": "你是谁？" } ] }' |  |  |
| --- | --- | --- |
| [构建智能客服](single-agent-application.md) 通过可视化工具快速搭建 AI 助手，处理客户咨询。 | [编排流程](workflow-application.md) 可视化流程编排，无代码基础的业务人员也能独立完成工作流设计。 | [微调模型](model-training-overview.md) 可视化微调，无需编写训练代码，即可完成模型定制。 |
## 模型服务
### 开箱即用的模型
百炼提供开箱即用的模型服务，无需自行部署或运维，直接调用自研千问（Qwen）全系列模型，以及 DeepSeek、Kimi、GLM 等第三方大模型。详情请参见[选择模型](models.md)。
千问（Qwen）系列旗舰模型：
千问 Max：Qwen 系列效果最好的模型，适合处理复杂、多步骤任务。
最新的 qwen3.7-max 推理能力全面超越前代，推荐选用。
千问 Plus：效果、速度和成本均衡，是多数场景的推荐选择。
千问 Flash：高性价比、低延迟，适合需要快速响应的简单任务。
多模态覆盖：涵盖文本生成、视觉理解、图像生成、视频生成、语音识别与合成、嵌入向量等多种能力。
细分领域模型：提供长文本处理、翻译、数据挖掘、法律、意图理解、角色扮演、深入研究等多种领域模型。
### 模型调优、部署和评测
[模型调优](model-training-overview.md)：支持有监督微调（SFT）、继续预训练（CPT）和直接偏好优化（DPO），满足特定业务需求。
[模型部署](model-deployment-introduction.md)：将预置模型或调优后的自定义模型部署为资源专享的推理服务，满足高并发、低延迟等性能要求。支持按时长、包月、按 Token 量等多种计费方式。
[模型评测](model-evaluation-overview.md)：提供人工评测、自动评测和基线评测，支持快速对比不同模型表现，验证调优效果，提前发现潜在调用风险。
## 应用构建
应用类型：提供可视化和高代码两种开发模式。可视化模式可快速创建[智能体应用](single-agent-application.md)和[工作流应用](workflow-application.md)；[高代码应用](rich-code-application.md)则支持将 Python 项目部署为后端服务，具备自动化运维、可观测、日志服务等能力。
功能拓展：通过[知识库（RAG）](rag-knowledge-base.md)接入私有数据和专业领域知识；通过[插件](plug-in-overview.md)和[模型上下文协议（MCP）](mcp-introduction.md)调用外部服务。
分享与发布：支持将应用发布至网页、钉钉机器人、微信公众号及音视频互动智能体等多种平台，详见[应用分享](share-an-application.md)。
## 产品计费
开通百炼无需费用，调用、微调、部署模型时产生相应费用，详情请参见[计费项](billing-for-model-studio.md)。
### 新用户免费额度
百炼为新用户提供北京地域专属的新人免费额度，用于体验模型调用。
未认证用户免费额度用完后无法继续使用，需要完成[认证](https://myaccount.console.aliyun.com/cert-info)并[充值](https://billing-cost.console.aliyun.com/fortune/fund-management/recharge)后方能继续按量付费。
已认证用户免费额度用完后自动转为按量付费，如需避免意外扣费，可开启[免费额度用完即停](new-free-quota.md)功能，额度耗尽时服务自动停止。
详见[新人免费额度](new-free-quota.md)。
### 如何支付费用
模型调用按分钟出账，请确保阿里云账户余额充足。可前往[费用与成本](https://usercenter2.aliyun.com/home)页面充值。
### 查看账单与用量
消费明细：前往[账单详情](https://usercenter2.aliyun.com/finance/expense-report/expense-detail)和[成本分析](https://usercenter2.aliyun.com/expense-manage/expense-analyze)页面查看。
调用统计：模型调用完约一小时后，前往[阿里云百炼控制台](https://bailian.console.aliyun.com/cn-beijing?spm=5176.29619931.J__Z58Z6CX7MY__Ll8p1ZOR.1.7dd7521cmX1pAh&tab=model#/model-market)，在页面右上角选择目标地域，进入[模型监控](https://bailian.console.aliyun.com/?tab=model#/model-telemetry)页面并设置查询条件，点击目标模型操作列的监控，即可查看调用量、Token 消耗、成功率等统计数据。详情请参见[模型监控](model-telemetry.md)。
Coding Plan 用量：如已订阅 Coding Plan（AI 编码套餐），可在[Coding Plan 页面](https://bailian.console.aliyun.com/cn-beijing/?tab=model#/efm/coding_plan)查看当前套餐的请求消耗情况。Coding Plan 采用固定月费，提供月度请求额度，支持在 AI 编码工具中使用，详情请参见[Coding Plan](coding-plan.md)[概述](coding-plan.md)。
## 开始使用阿里云百炼
在线体验大模型：
打开[阿里云百炼控制台](https://bailian.console.aliyun.com/cn-beijing?spm=5176.29619931.J__Z58Z6CX7MY__Ll8p1ZOR.1.7dd7521cmX1pAh&tab=model#/model-market)，在右上角选择目标地域
进入[模型体验](https://bailian.console.aliyun.com/?tab=model#/efm/model_experience_center/text)页面，选择模型开始体验
发起第一个API请求：[首次调用千问](first-api-call-to-qwen.md)[API](first-api-call-to-qwen.md)
构建第一个大模型应用：[0](build-knowledge-base-qa-assistant-without-coding.md)[代码构建问答应用](build-knowledge-base-qa-assistant-without-coding.md)
## 常见问题
Q：我的数据安全吗？阿里云百炼会用我的数据进行训练吗？
A：不会。阿里云严格保护数据隐私，不会将您的数据用于模型训练。构建应用或训练模型时传输的所有数据均经过加密处理。详情请参见[合规资质与隐私说明](privacy-notice.md)。
Q：阿里云百炼提供哪些地域的服务？不同地域有什么区别？
A：目前提供以下地域的模型服务：
华北2（[北京](https://bailian.console.aliyun.com/?tab=model#/model-market)）、美国（[弗吉尼亚](https://modelstudio.console.aliyun.com/us-east-1)）、国际（[新加坡](https://modelstudio.console.aliyun.com/?tab=doc#/doc/?type=model&url=2840914)）、德国（[法兰克福](https://modelstudio.console.aliyun.com/eu-central-1)）和日本（[东京](https://modelstudio.console.aliyun.com/ap-northeast-1)）地域
建议选择邻近地域以降低网络延迟。各地域的接入点（Endpoint/Base URL）不同，API Key 不通用，支持的模型、平台功能与价格也有所差异，详情请参见[选择模型](models.md)。
Q：如何避免产生费用？
A：百炼采用按量付费，本身没有"自动扣费"开关。以下措施可有效控制费用：
删除API Key：前往[阿里云百炼控制台](https://bailian.console.aliyun.com/cn-beijing?spm=5176.29619931.J__Z58Z6CX7MY__Ll8p1ZOR.1.7dd7521cmX1pAh&tab=model#/model-market)，选择目标地域，进入[API-KEY](https://bailian.console.aliyun.com/?apiKey=1&tab=globalset#/efm/api_key)页面，删除所有API Key，从源头阻断调用。
停止所有调用：停止应用程序、智能体、工作流中的模型调用，并排查定时任务和后台进程。
清理计费资源：删除不再使用的知识库；前往[模型部署](https://bailian.console.aliyun.com/?tab=model#/efm/model_deploy)页面，下线按算力时长计费的部署实例。
开启"[免费额度用完即停](new-free-quota.md)"（仅限新用户且在免费额度有效期内）：在模型详情页开启此开关，免费额度耗尽后服务自动停止，不会转为付费。仅适用于华北2（北京）地域（[中国内地服务部署范围](regions.md)），且须在免费额度有效期内。
设置费用监控和预警：查看[账单详情](https://usercenter2.aliyun.com/finance/expense-report/expense-detail)和[模型监控](https://bailian.console.aliyun.com/?tab=model#/model-telemetry)，并设置[高额消费预警](https://usercenter2.aliyun.com/home/alarm-threshold)，及时发现异常消费。
订阅 Coding Plan（AI 编码套餐）：固定月费，提供月度请求额度，无按量扣费风险。注意需使用 Coding Plan 专属的 Base URL和API Key 进行调用，否则模型调用将按量付费。详情请参见[Coding Plan](coding-plan.md)[概述](coding-plan.md)。
Q：如何使用 Qwen3 系列模型或 DeepSeek？
A：
在线体验：打开[阿里云百炼控制台](https://bailian.console.aliyun.com/cn-beijing?spm=5176.29619931.J__Z58Z6CX7MY__Ll8p1ZOR.1.7dd7521cmX1pAh&tab=model#/model-market)，选择目标地域，进入[模型广场](https://bailian.console.aliyun.com/?tab=model#/model-market)页面，点击模型即可体验（DeepSeek 仅支持北京地域）。
通过API调用：请参见[首次调用千问](first-api-call-to-qwen.md)[API](first-api-call-to-qwen.md)。
通过开发工具（如 Claude Code）调用：请参考[接入客户端/开发工具](use-chat-client-or-development-tool.md)。
通过可视化界面构建大模型应用：请参考[智能体应用](single-agent-application.md)或[工作流应用](workflow-application.md)。
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
