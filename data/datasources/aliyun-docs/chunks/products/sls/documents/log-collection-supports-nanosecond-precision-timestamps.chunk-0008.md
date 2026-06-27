## 提取日志时间（strptime时间格式）
单击添加处理插件，选择拓展处理插件>[提取日志时间（strptime](extract-log-time.md)[时间格式）](extract-log-time.md)，进行如下配置：
原始字段：解析日志前，用于存放时间的原始字段，本示例为asctime。
原始时间格式：根据日志的时间字段内容设置对应的[时间格式](log-collection-supports-nanosecond-precision-timestamps.md)，本示例为%Y-%m-%d %H:%M:%S,%f。其中%f为秒的小数部分，精度最高支持为纳秒。
时间格式字符串必须与原始日志中的时间格式（包括秒和纳秒之间的分隔符，如,或.）完全一致，否则无法正确解析。
