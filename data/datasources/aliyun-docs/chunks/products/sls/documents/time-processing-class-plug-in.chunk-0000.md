## 插件效果示例
表格展示该原始日志在分别使用时间解析插件（原生）与不使用插件的情况下，保存到日志服务后的数据结构。

| 原始日志 | 不使用插件 | 使用时间解析插件（原生） |
| --- | --- | --- |
| 秒级时间： { "level":"INFO", "timestamp":"2025-09-29T09:56:01+0800", "cluster":"yilu-cluster-0728", "message":"User logged in successfully", "userId":"user-123" } | Content：" {"level":"INFO","timestamp":"2025-09-29T09:56:01+0800","cluster":"yilu-cluster-0728","message":"User logged in successfully","userId":"user-123"} " |  |
| 毫秒时间： { "time": "2026-01-05T11:58:40,647Z", "filename": "out_data.py", "levelname": "INFO", "threadName": "MainThread" } | Content：" {"time":"2026-01-05T11:58:40,647Z", "filename":"out_data.py","levelname": "INFO", "threadName":"MainThread"} " |  |
| 纳秒时间： { "time": "2026-01-05T11:40:22,298837465Z07:00", "filename": "out_data.py", "levelname": "INFO", "threadName": "MainThread" } | Content：" {"time": "2026-01-05T11:40:22,298837465Z07:00","filename":"out_data.py","levelname":"INFO","threadName": "MainThread"} " |  |
