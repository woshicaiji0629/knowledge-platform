识别日志格式，辅助生成正则表达式和解析规则，降低配置难度。
场景一：多行日志处理（如Java堆栈日志）
由于Java异常堆栈、JSON等日志通常跨越多行，在默认采集模式下会被拆分为多条不完整的记录，导致上下文信息丢失；为此，可启用多行模式，通过配置行首正则表达式，将同一日志的连续多行内容合并为一条完整日志。
效果示例：

| 未经任何处理的原始日志 | 默认采集模式下，每行作为独立日志，堆栈信息被拆散，丢失上下文 | 开启多行模式，通过行首正则表达式识别完整日志，保留完整语义结构。 |
| --- | --- | --- |
| [2025-11-13T10:52:20,557] [ERROR] java.sql.SQLException: No suitable driver found for jdbc:mysql://db.host:3306/prod_db at com.datastore.util.DataProcessor.save(DataProcessor.java:434) at io.awesomeapp.util.PaymentGateway.fetchData(PaymentGateway.java:463) at org.awesomeapp.util.UserService.processRequest(UserService.java:252) at io.datastore.service.DatabaseConnector.fetchData(DatabaseConnector.java:172) at org.datastore.service.UserService.fetchData(UserService.java:517) | 查询结果中每条日志均携带重复元数据（IP 172.22.243.96 、主机名 iZk1a6gxbmanfckj0ai8m8Z 、日志路径 /var/log/java_app_si...n.log ），content 字段分别为堆栈单行（如 com.weblegacy.controller.DataProcessor.getUserById:81 ）或超时错误 java.util.concurrent.TimeoutException: Future task timed out after 30 seconds 。 | 日志服务控制台中，一条包含 java.sql.SQLException: No suitable driver found for jdbc:mysql://db.host:3306/prod_db 错误及 5 行堆栈（DataProcessor.save:434 → UserService.fetchData:517）的 Java 异常日志被完整识别为单条记录。 |
