## 数据安全与隐私
SLS Query Skill 通过阿里云 CLI 执行查询，查询过程遵循以下安全原则：
查询请求通过 HTTPS 加密传输，日志数据不经过第三方服务。
Agent 在本地生成和执行查询命令，日志数据不会发送给 AI 模型提供商。
凭据信息（AccessKey）通过阿里云 CLI 配置文件或环境变量管理，不会出现在 Agent 对话记录中。
重要
不要在 Agent 对话中直接粘贴 AccessKey ID 或 AccessKey Secret。如需配置凭据，请使用aliyun configure命令。
