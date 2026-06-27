# Assistant API 功能概览-大模型服务平台百炼(Model Studio)-阿里云帮助中心

Source: https://help.aliyun.com/zh/model-studio/assistant-api

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南（模型）](products/model-studio/documents/model-user-guide.md)

- [用户指南（应用）](products/model-studio/documents/application-user-guide.md)

- [API参考（模型）](products/model-studio/documents/model-api-reference.md)

- [API参考（应用）](products/model-studio/documents/applicantion-api-reference.md)

[首页](https://help.aliyun.com/zh)

# Assistant API（下线中）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/bailian)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Assistant API 旨在帮助开发者快速开发[大模型应用](products/model-studio/documents/application-introduction.md)（Assistant），例如个人助理、智能导购、会议助手等。相比[文本生成 API](products/model-studio/documents/text-generation.md)，Assistant API 还内置了多轮对话和工具调用组件，从而降低了大模型应用的开发成本。

重要

Assistant API下线中，建议迁移至[Responses API](products/model-studio/documents/qwen-api-via-openai-responses.md)：内置多种工具，并支持多轮上下文管理，可作为替代方案。

说明

[智能体应用](products/model-studio/documents/single-agent-application.md)和 Assistant 虽然均为大模型应用，但二者的功能相互独立，使用方法也不相同。

- 

智能体应用：仅可使用控制台进行创建、查看、更新和删除，以及通过[应用调用 API](products/model-studio/documents/agent-and-workflow-application-api-reference.md)进行调用。

- 

Assistant：仅可使用 Assistant API 创建、查看、更新、删除和调用。

## 为什么选择 Assistant API

Assistant API 为您提供高效、灵活的大模型应用构建能力，具备以下核心优势：

| 内置官方工具： 提供代码执行、文生图、在线搜索等实用工具。例如，Assistant 可以直接运行 Python 代码生成结果，调用搜索功能获取实时信息，或生成图片用于创意设计。 | # 示例代码，仅供参考 def submit_message(thread, assistant, message): Messages.create( thread_id=thread.id, role="user", content=message ) run = Runs.create( thread_id=thread.id, assistant_id=assistant.id, stream=True ) for event, data in run: if event == 'thread.message.delta': yield data.delta.content.text.value if event == 'thread.message.completed': yield '\n' if event == 'thread.run.step.delta': # 第一次检测到 step.delta 时输出工具名称 if not hasattr(submit_message, 'tool_name_shown'): submit_message.tool_name_shown = True tool_name = data.delta.step_details.tool_calls[0]['type'] yield f"\n 正在使用工具: {tool_name}\n\n" formatted_output = format_tool_output(data.delta.step_details.tool_calls[0]) if formatted_output is not None: yield formatted_output |
| --- | --- |
| 内置对话管理： 提供上下文管理工具，无需手动维护对话历史。 | # 示例代码，仅供参考 while True: for event, data in run: elif event == 'thread.run.requires_action': # 工具调用 => 可能需要提交工具输出 => 导致新的 run 生成器 tool_calls = data.required_action.submit_tool_outputs.tool_calls if not tool_calls: continue tool_outputs = [] for tool_call in tool_calls: name = tool_call.function.name arguments = json.loads(tool_call.function.arguments) output = tools_map[name](**arguments) # 普通工具 tool_outputs.append({"output": output}) # 将工具输出提交给 run，会返回一个新的 run 生成器 run = Runs.submit_tool_outputs( thread_id=thread.id, # 原生的对话线程，无需手动管理 run_id=data.id, tool_outputs=tool_outputs, stream=True ) yield "转接中...\n" break # 跳出当前事件循环，用返回的 new_run 接着处理 elif event in ('thread.run.completed', 'thread.run.cancelled', 'thread.run.expired', 'thread.run.failed'): # 当前 run 结束 break else: # for 循环正常结束(没有 break)，说明 run 流耗尽 break |
| 快速搭建多智能体系统： 提供 Assistant、上下文、消息封装、流程控制等简易模板，可以灵活、高效地实现多智能体系统。例如 [具备自动规划能力的 Multi Agent 系统](products/model-studio/documents/use-multi-agent-to-query-alibaba-cloud-resource-information.md) 。 | # 示例代码，仅供参考 # 获得 Multi Agent 的回复，输入与输出需要与 Gradio 前端展示界面中的参数对齐 def get_multi_agent_response(query,history): # 处理输入为空的情况 if len(query) == 0: return "",history+[("","")],"","" # 获取 Agent 的运行顺序 assistant_order = get_agent_response(PlannerAssistant,query) try: order_stk = ast.literal_eval(assistant_order) cur_query = query # 依次运行 Agent for i in range(len(order_stk)): yield "----->".join(order_stk),history+[(query,"multi agent 正在努力工作中...")],f"{order_stk[i]}正在处理信息...","" cur_assistant = assistant_mapper[order_stk[i]] response = get_agent_response(cur_assistant,cur_query) yield "----->".join(order_stk),history+[(query,"multi agent 正在努力工作中...")],response,"" # 如果当前 Agent 为最后一个 Agent，则将其输出作为 Multi Agent 的输出 if i == len(order_stk)-1: yield "----->".join(order_stk),history+[(query,response)],"assistant 已处理完毕","" # 如果当前 Agent 不是最后一个 Agent，则将上一个 Agent 的输出 response 添加到下一轮的 query 中，作为参考信息 else: # 在参考信息前后加上特殊标识符，可以防止大模型混淆参考信息与提问 cur_query = f"你可以参考已知的信息：\n{response}\n 你要完整地回答用户的问题。问题是：{query}。" # 兜底策略，如果上述程序运行失败，则直接调用 ChatAssistant except Exception as e: yield "ChatAssistant",[(query,get_agent_response(ChatAssistant,query))],"","" |


## 快速构建 Assistant

您可以与 Assistant 进行多轮对话，同时可以选择启用[流式输出](products/model-studio/documents/streaming-output.md)。通常情况下，您需要依次完成四个主要步骤：

- 

创建 Assistant：Assistant 配置了大模型、指令和工具列表，用于执行特定任务。

- 

创建 Thread：Thread 将记录用户和 Assistant 的所有消息，用于实现多轮对话。

- 

创建 Message：Message 是承载用户和 Assistant 消息的容器。

- 

创建 Run：Run 代表 Assistant 响应多轮对话的一系列过程，包括模型推理和工具调用。在这个步骤中，可同时选择启用[流式输出](products/model-studio/documents/streaming-output.md)，实现自然的交互效果。

在[Assistant API 快速入门](products/model-studio/documents/quick-start-of-assistant-api.md)中，您可以快速上手 Assistant 的使用方法，包括模型推理、工具调用、多轮对话和流式输出。

## 兼容性

### 模型支持

Assistant API 支持千问的多款主流模型。您可以前往[模型广场](https://bailian.console.aliyun.com/#/model-market)查看和体验这些模型。

说明

千问-Turbo、千问-Plus、千问-Max 模型的快照版本（例如qwen-plus-1220）仅兼容“函数调用”及“知识检索增强”工具。模型的兼容性以实际运行结果为准。

| 模型系列 | 模型标识符 |
| --- | --- |
| 千问-Turbo | qwen-turbo |
| 千问-Plus | qwen-plus |
| 千问-Max | qwen-max |


### 工具支持

Assistant API 支持多款官方工具，以及自定义的函数调用或插件。

说明

插件的兼容性请以实际执行结果为准，更多详情可参考[插件列表](products/model-studio/documents/plug-ins.md)。

| 工具（tools） | 唯一标识符 | 用途 |
| --- | --- | --- |
| 代码解释器 | code_interpreter | 帮助执行 Python 代码，适用于编程问题、数学计算、数据分析等场景 |
| 夸克搜索 | quark_search | 用于实时检索网络信息，增强知识获取能力。 |
| 文生图 | text_to_image | 将文字描述转为图像，丰富回复形式。 |
| 计算器 | calculator | 拥有良好的计算能力，可用于执行精确运算任务。 |
| 生成二维码 | generate_qrcode | 可将文本转换为二维码。 |
| GitHub 搜索 | github_search | 可搜索 GitHub 项目的实时信息。 |
| 函数调用（Function calling） | function | 在本地设备上执行特定功能，无需依赖外部网络服务。 |
| 知识检索增强（RAG） | rag | 检索外部知识，增强大模型回答准确性。 |
| 自定义插件 | ${plugin_id} | 连接自定义业务接口，扩展 AI 业务能力。 |


[上一篇：相关协议](products/model-studio/documents/application-related-agreements.md)[下一篇：快速入门](products/model-studio/documents/quick-start-of-assistant-api.md)

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
