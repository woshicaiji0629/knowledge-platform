## 前提条件
已创建日志服务 Project 和 LogStore，并已采集日志数据。
已为目标 LogStore 创建索引。未配置索引SLS 查询、SQL 分析和 SPL 查询无法执行。
已获取可访问目标 Project 和 LogStore 的阿里云账号凭据。
警告
为防止凭据泄露，不要在 Agent 对话中粘贴 AccessKey ID 或 AccessKey Secret。建议通过环境变量或阿里云 CLI 配置文件管理凭据。
