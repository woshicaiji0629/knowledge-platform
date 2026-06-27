## 通过内容过滤降低成本
基于日志内容的字段过滤（如仅采集 level 为 WARNING 或 ERROR 的日志）。
效果示例：

| 未经任何处理的原始日志 | 只采集 WARNING 或 ERROR 日志 |
| --- | --- |
| {"level":"WARNING","timestamp":"2025-09-23T19:11:40+0800","cluster":"yilu-cluster-0728","message":"Disk space is running low","freeSpace":"15%"} {"level":"ERROR","timestamp":"2025-09-23T19:11:42+0800","cluster":"yilu-cluster-0728","message":"Failed to connect to database","errorCode":5003} {"level":"INFO","timestamp":"2025-09-23T19:11:47+0800","cluster":"yilu-cluster-0728","message":"User logged in successfully","userId":"user-123"} | {"level":"WARNING","timestamp":"2025-09-23T19:11:40+0800","cluster":"yilu-cluster-0728","message":"Disk space is running low","freeSpace":"15%"} {"level":"ERROR","timestamp":"2025-09-23T19:11:42+0800","cluster":"yilu-cluster-0728","message":"Failed to connect to database","errorCode":5003} |

配置步骤：在Logtail配置页面的处理配置区域
单击添加处理插件，选择原生处理插件>过滤处理：
字段名：过滤的日志字段。
字段值：用于过滤的正则表达式，仅支持全文匹配，不支持关键词部分匹配。
