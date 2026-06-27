## 1. 什么是核心组件
在使用 Assistant API 构建对话式应用时，一般需要管理以下几种核心对象：
Assistant：大模型对话应用的“主体”，包括所使用的语言模型（model）、系统指令（instructions）、工具（tools）、名称（name）等。
Thread：独立的对话上下文容器。所有与该对话相关的消息与调用都属于同一个Thread。
Message：对话中的单条消息，包含角色（role）、内容（content）、元数据（metadata）等。
Run：一次具体的模型调用请求。当您让 Assistant 生成回复时，就会触发一个Run。
Step：一次Run中更细粒度的执行步骤（如先检索资料，再生成答案；或多次外部工具调用等）。
对象间关系示意：
Assistant ┣─ (manages multiple) Thread ┣─ (has many) Message ┗─ (has many) Run ┗─ (has multiple) Step
这些对象在阿里云百炼服务器端保存，都有唯一的id。您可以使用它们各自的retrieve（或get）方法检索，或使用delete方法删除。
