修复 | 修复在事务请求中执行多次 SELECT 命令可能导致同一连接的后续普通请求选择的 DB 错误的问题。 |  |  |  |
| 7.0.2 | MEDIUM | 2023-05-11 | 新特性 | TR.BITOP 、 TR.BITOPCARD 命令支持跨 Slot 的 Key。 针对持久内存型， INFO 、 IINFO 命令新增返回 Persistence 信息：maxpmem（最大持久内存）、used_pmem（已使用的持久内存），单位为 B（字节）。 支持 RESP 协议嵌套超过 7 层的请求结果。 |
| 功能优化 | 优化 Proxy 模式对 Lua 语法的限制。 |  |  |  |
| 7.0.1 | MEDIUM | 2023-04-11 | 新特性 | 支持在读请求超时后，自动向其他备节点（Slave）重试。 支持 TLS 1.3 协议。 支持 TairSearch 的 TFT.ANALYZER 、 TFT.EXPLAINCOST 命令。 将命令（Command）返回结果从 Proxy 的封装结果修改为 DB 的执行结果。 优化增量订阅（Subscribe）时，Channel（频道）的计算逻辑，降低 CPU 消耗。 |
| 缺陷修复 | 修复一行审计日志的末尾多一个空格的问题。 修复当客户端协议错误时，可能会导致内存泄露的问题。 |  |  |  |
| 7.0.0 | MEDIUM | 2023-03-09 | 新特性 | 支持 Redis 6.2、Redis 7.0 命令。 支持 TairSearch 的 TFT.ANALYZER 命令。 |
