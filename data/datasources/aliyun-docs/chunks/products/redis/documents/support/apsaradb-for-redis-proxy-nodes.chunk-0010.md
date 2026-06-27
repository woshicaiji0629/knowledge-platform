请求所记录的 RT（Response Time）值 ，避免记录慢日志。 支持 TairSearch 的 TFT.EXPLAINSCORE 命令。 |
| 6.8.13 | MEDIUM | 2023-07-24 | 缺陷修复 | 修复在事务中执行多次 SELECT 命令可能导致同连接中后续普通请求选择 DB 错误的问题。 |
| 6.8.12 | MEDIUM | 2023-05-17 | 新特性 | TR.BITOP 、 TR.BITOPCARD 命令支持跨 Slot 的 Key。 |
| 功能优化 | 优化 Proxy 模式对 Lua 语法的限制。 |  |  |  |
| 缺陷修复 | 修复当客户端协议错误时，可能导致的内存泄露问题。 |  |  |  |
| 6.8.11 | MEDIUM | 2023-04-04 | 新特性 | 支持 TLS 1.3 协议。 支持 TairSearch 的 TFT.ANALYZER 、 TFT.EXPLAINCOST 命令。 |
| 缺陷修复 | 修复一行审计日志的末尾多一个空格的问题。 |  |  |  |
| 6.8.10 | MEDIUM | 2023-01-06 | 新特性 | 支持 TairVector。 |
| 缺陷修复 | 修复 TairSearch 中 Filter Aggregation 聚合错误的问题。 修复开启 ptod_enabled 参数后，审计日志中客户端 IP 地址不准确的问题。 |  |  |  |
| 6.8.9 | MEDIUM | 2022-12-14 | 新特性 | INFO 命令返回值中添加 OS 字段。 支持 CLIENT KILL user 命令。 |
| 缺陷修复 | 修复 MOVED 返回数据可能不完整的问题，避免客户端协议解析失败。 |  |  |  |
| 6.8.8 | MEDIUM | 2022-11-15 | 新特性 | 支持 BF.INFO 命令。 支持 TairHash 的 EXHSCANUNORDER 命令。 单条审计日志的最大长度从 4KB 改为 2KB。 |
| 缺陷修复 | 修复 云原生 版 Proxy 实例的审计日志功能中客户端 IP 不准确的问题。 |  |  |  |
| 6.8.7 | LOW | 2022-08-22 | 功能优化 | 增强稳定性。 |
| 6.8.6 | MEDIUM | 2022-08-16 | 新特性 | 支持部分 Tairsearch。 支持 AUTH user:password 格式的鉴权方式。 |
| 功能优化 | 修复 RESP V3 协议引入的空数组嵌套解码问题。 |  |  |  |
| 6.8.4 | MEDIUM | 2022-07-20 | 新特性 | 支持 RESP V3 协议解析与转发，支持
