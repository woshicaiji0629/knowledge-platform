6.4.x

| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 6.3.9 | MEDIUM | 2020-08-14 | 新特性 | 慢日志支持记录真实的客户端 IP 地址，帮助您更好地定位慢日志，更多信息，请参见 [查询慢日志](../user-guide/view-slow-logs.md) 。 |
| 功能优化 | 提升了 Proxy 节点的短连接处理能力。 |  |  |  |
| 6.3.8 | HIGH | 2020-07-24 | 缺陷修复 | 修复 Vector Clear 不释放内存导致的内存上涨的问题。 |
| 6.3.7 | HIGH | 2020-07-13 | 缺陷修复 | 修复开启 SSL 加密功能后，建立连接时可能出现的崩溃问题。 |
| 6.3.5 | HIGH | 2020-07-10 | 新特性 | 为审计日志中的二进制数据执行编码，提升日志易读性。 增加 no_loose_statistics-ip-enable 、 no_loose_statistics-keys 、 no_loose_statistics-cmds 参数，可实现对 IP、Key 和命令维度的统计，更多详细介绍请参见 [Redis](../user-guide/supported-parameters.md) [开源版配置参数列表](../user-guide/supported-parameters.md) 。 |
| 缺陷修复 | 修复连接被释放后，执行 CheckExceedLimitAndClose 可能导致的崩溃问题。 修复 SSL 加密功能开启失败的问题。 |  |  |  |
| 6.3.4 | HIGH | 2020-05-21 | 缺陷修复 | 修复 \r\n 等空包可能导致后续请求不返回的问题。 |

该文章对您有帮助吗？
反馈
