## 快速构建 Assistant
您可以与 Assistant 进行多轮对话，同时可以选择启用[流式输出](streaming-output.md)。通常情况下，您需要依次完成四个主要步骤：
创建 Assistant：Assistant 配置了大模型、指令和工具列表，用于执行特定任务。
创建 Thread：Thread 将记录用户和 Assistant 的所有消息，用于实现多轮对话。
创建 Message：Message 是承载用户和 Assistant 消息的容器。
创建 Run：Run 代表 Assistant 响应多轮对话的一系列过程，包括模型推理和工具调用。在这个步骤中，可同时选择启用[流式输出](streaming-output.md)，实现自然的交互效果。
在[Assistant API 快速入门](quick-start-of-assistant-api.md)中，您可以快速上手 Assistant 的使用方法，包括模型推理、工具调用、多轮对话和流式输出。
