### 采集日志无法正常解析纳秒时间戳
配置采集后，发现高精度时间并未正常提取。
日志查看器中索引时间为10-26 00:30:39，而日志记录的 asctime 为2023-10-26 00:30:10,199999999，两者不一致，说明高精度时间未被正常提取。日志记录详情：
__file_offset__ xxx __tag__ xxx asctime: 2023-10-26 00:30:10,199999999 filename: xxx levelname: INFO lineno: 51 message: {"no": 14, "inner_loop": 166, "loop": 27451, "uuid": "9be98c29-22c7-40a1-b7ed-29ae6c8367af"} module: generate_data threadName: MainThread
错误原因
插件模式支持%f，但是时间格式需要与源时间内容保持一致。
解决方法
登录LoongCollector（Logtail）机器，查看日志，发现大量STRPTIME_PARSE_ALARM异常日志。
tail -f /usr/local/ilogtail/logtail_plugin.LOG 2023-10-26 00:30:39 [WRN] [strptime.go:164] [processLog] [##1.0##xxxx,xxx] AlarmType:STRPTIME_PARSE_ALARM strptime(2023-10-26 00:30:10,199999999, %Y-%m-%d %H:%M:%S %f) failed: 0001-01-01 00:00:00 +0000 UTC, <nil>
修改插件日志解析格式。
原始日志时间为2023-10-26 00:30:10,199999999，秒与高精度时间（这里是毫秒）之间分隔符为半角逗号（,），解析格式为%Y-%m-%d %H:%M:%S %f，秒与高精度时间之间分隔符为空格 。修改采集配置中时间转换格式为%Y-%m-%d %H:%M:%S,%f即可。
