### 步骤三：创建采集配置
通过控制台配置
完成[LoongCollector](log-collection-supports-nanosecond-precision-timestamps.md)[安装和机器组配置](log-collection-supports-nanosecond-precision-timestamps.md)后，进入Logtail配置页面，开始定义日志采集和处理规则。
1. 开启纳秒精度支持
定义日志的采集源、采集规则，并开启纳秒精度支持。
全局配置：
配置名称：设置一个在Project内唯一的名称。创建成功后，无法修改。
其他全局配置：开启高级参数开关，并输入以下 JSON 内容以开启纳秒精度支持：
{ "EnableTimestampNanosecond": true }
输入配置：
类型：文本日志采集。
文件路径：日志采集的路径。
Linux：以“/”开头，如/data/mylogs/**/*.log，表示/data/mylogs目录下所有后缀名为.Log的文件。
Windows：以盘符开头，如C:\Program Files\Intel\**\*.Log。
最大目录监控深度：文件路径中通配符**匹配的最大目录深度。默认为0（仅监控本层目录）。
2. 配置处理插件
由于源日志为 JSON 格式，在处理配置区域，添加JSON解析插件，从原始日志中分离出包含纳秒时间戳的字符串，并将其存为一个独立的字段。
添加日志样例
假设日志文件中的日志格式如下，其中asctime字段包含了纳秒精度的时间戳。
{ "asctime": "2023-10-25 23:51:10,199999999", "filename": "generate_data.py", "levelname": "INFO", "lineno": 51, "module": "generate_data", "message": "{\"no\": 14, \"inner_loop\": 166, \"loop\": 27451, \"uuid\": \"9be98c29-22c7-40a1-b7ed-29ae6c8367af\"}", "threadName": "MainThread" }
添加JSON解析插件
单击添加处理插件，选择原生处理插件>JSON解析，单击确认。
添加时间解析插件
将上一步提取的时间字符串（asctime字段）转换为标准的纳秒时间戳，并将其作为该条日志的事件时间。
