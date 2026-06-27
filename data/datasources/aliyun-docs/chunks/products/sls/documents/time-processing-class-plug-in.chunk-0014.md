## 常见日志时间格式
processor_gotime扩展插件支持的常见日志时间格式请参见[https://pkg.go.dev/time#pkg-constants](https://pkg.go.dev/time#pkg-constants)。processor_parse_timestamp_native原生插件与 processor_strptime 扩展插件支持的常见日志时间格式如下表所示：
说明
在Linux服务器中，Logtail支持strftime函数提供的所有时间格式。即能被strftime函数格式化的日志时间字符串都能被Logtail解析并使用。
