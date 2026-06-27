# Assistant API（下线中）
Assistant API 旨在帮助开发者快速开发[大模型应用](application-introduction.md)（Assistant），例如个人助理、智能导购、会议助手等。相比[文本生成 API](text-generation.md)，Assistant API 还内置了多轮对话和工具调用组件，从而降低了大模型应用的开发成本。
重要
Assistant API下线中，建议迁移至[Responses API](qwen-api-via-openai-responses.md)：内置多种工具，并支持多轮上下文管理，可作为替代方案。
说明
[智能体应用](single-agent-application.md)和 Assistant 虽然均为大模型应用，但二者的功能相互独立，使用方法也不相同。
智能体应用：仅可使用控制台进行创建、查看、更新和删除，以及通过[应用调用 API](agent-and-workflow-application-api-reference.md)进行调用。
Assistant：仅可使用 Assistant API 创建、查看、更新、删除和调用。
