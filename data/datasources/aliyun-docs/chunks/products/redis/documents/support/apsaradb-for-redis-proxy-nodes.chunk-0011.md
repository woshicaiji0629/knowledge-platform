性 | 支持部分 Tairsearch。 支持 AUTH user:password 格式的鉴权方式。 |
| 功能优化 | 修复 RESP V3 协议引入的空数组嵌套解码问题。 |  |  |  |
| 6.8.4 | MEDIUM | 2022-07-20 | 新特性 | 支持 RESP V3 协议解析与转发，支持通过 resp_version 配置切换 Proxy 到 Redis 间协议。 |
| 6.8.2 | MEDIUM | 2022-06-14 | 功能优化 | 增强稳定性，修复一些 Crash 问题。 |
| 6.8.1 | LOW | 2022-04-19 | 新特性 | 支持部分 TairSearch。 支持 TairRoaring V2.2 新增的命令。 |
| 6.8.0 | MEDIUM | 2022-04-01 | 新特性 | 支持部分 TairZset。 支持部分 TairRoaring。 SSL 证书禁用 RC4 加密算法。 |
| 缺陷修复 | 修复开启 ptod_enabled 参数后，可能导致 SDIFFSTORE、SINTERSTORE、SUNIONSTORE、ZINTERSTORE、ZUNIONSTORE 命令异常的问题。 修复 SMOVE 命令可能出现 CROSSSLOT 的错误。 |  |  |  |
