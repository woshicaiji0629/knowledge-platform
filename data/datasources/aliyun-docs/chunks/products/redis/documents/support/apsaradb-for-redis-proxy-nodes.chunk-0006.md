| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 7.0.16 | LOW | 2024-12-10 | 功能优化 | 在 Sentinel 免密模式下，支持通过 #no_loose_sentinel-password-free-commands 参数配置更多的免密命令。 |
| 7.0.15 | LOW | 2024-12-02 | 功能优化 | 支持 JSON.MERGE 命令。 支持 TLS 服务端 CA 证书。 优化 Proxy 到 DB 之间的连接，改为使用用户账号权限并按用户账号隔离。 |
| 7.0.14 | LOW | 2024-10-09 | 功能优化 | 支持 TOUCH 命令。 优化 Private 连接（阻塞命令、SUBSCRIBE、WATCH 等命令会使用 Private 连接）的内存使用量。 |
| 缺陷修复 | 修复 TFT.MSEARCH 命令在 DB 没有 Source 信息时异常的问题。 |  |  |  |
| 7.0.13 | LOW | 2024-08-13 | 功能优化 | 支持通过 #no_loose_sentinel-password-free-access 配置项，免密执行 SUBSCRIBE 命令订阅 +switch-master Channel（仅限该 Channel）。 |
| 7.0.12 | MEDIUM | 2024-07-24 | 功能优化 | 优化 TairVector 全局索引接口的返回值。 支持通过 #no_loose_sentinel-password-free-access 配置项，免密执行 Sentinel 相关命令。 |
| 缺陷修复 | 修复 TairVector 全局索引在部分场景下删除异常的问题。 修复 SCRIPT EXISTS 命令在 Lua 存在时也返回 0 的问题。 |  |  |  |
| 7.0.11 | LOW | 2024-07-04 | 缺陷修复 | 修复了使用 JSON.SET 或 GIS.ADD 命令之后进行变配可能失败的问题。 |
| 7.0.10 | MEDIUM | 2024-06-18 | 新特性 | 支持 TairVector 全局索引功能。 |
| 功能优化 | 优化主备同步故障的恢复时间，降低异常时的影响。 |  |  |  |
| 缺陷修复 | 修复 TFT.MSEARCH 请求结果排序异常的问题。 修复单个 Tair 、 Tair 分片在 Key 数量很多（大于 2^24）时， SCAN 命令的返回结果可能不正确的问题。 |  |  |  |
| 7.0.9 | MEDIUM | 2024-04-08 | 功能优化 | 支持 RESP2、3 协议，并通过
