处理配置

| 配置项 | 说明 |
| --- | --- |
| 日志样例 | 待采集日志的样例，请务必使用实际场景的日志。日志样例可协助您配置日志处理相关参数，降低配置难度。支持添加多条样例，总长度不超过 1500 个字符。 [2023-10-01T10:30:01,000] [INFO] java.lang.Exception: exception happened at TestPrintStackTrace.f(TestPrintStackTrace.java:3) at TestPrintStackTrace.g(TestPrintStackTrace.java:7) at TestPrintStackTrace.main(TestPrintStackTrace.java:16) |
| 多行模式 | 多行日志的类型：多行日志是指每条日志分布在连续的多行中，需要从日志内容中区分出每一条日志。 自定义 ：通过 行首正则表达式 区分每一条日志。 多行 JSON ：每个 JSON 对象被展开为多行，例如： { "name": "John Doe", "age": 30, "address": { "city": "New York", "country": "USA" } } 切分失败处理方式： Exception in thread "main" java.lang.NullPointerException at com.example.MyClass.methodA(MyClass.java:12) at com.example.MyClass.methodB(MyClass.java:34) at com.example.MyClass.main(MyClass.java:½0) 对于以上日志内容，如果日志服务切分失败： 丢弃 ：直接丢弃这段日志。 保留单行 ：将每行日志文本单独保留为一条日志，保留为一共四条日志。 |
| 处理模式 | 处理模式 选择 SPL 。 |
| SPL 语句 | SPL 语句具体请参考 [SPL](user-guide/spl-syntax.md) [语法](user-guide/spl-syntax.md) 。解析日志前，日志默认存在 content 字段中。 |
| 超时时间 | SPL 语句执行一次的最大时间。 |

该文章对您有帮助吗？
反馈
