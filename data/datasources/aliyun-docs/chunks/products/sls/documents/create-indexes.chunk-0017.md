### 示例2
日志内容中有request_time字段，执行全文查询语句request_time。
只建立double、long类型的字段索引，无法查询到相关日志。
只建立全文索引，从所有日志文本中查询包括request_time的日志。
只建立text类型的字段索引，从字段索引是text类型的字段中查询包括request_time的日志。
