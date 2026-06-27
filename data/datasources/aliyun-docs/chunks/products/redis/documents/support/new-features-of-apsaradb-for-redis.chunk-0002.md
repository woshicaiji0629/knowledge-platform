### 兼容性变更
Tair 扩展数据结构在从 5.0 版本升级至 6.0 版本时存在少量行为变更，6.0 和 7.0 版本之间无兼容性变更。各大版本的原生命令支持情况参见[Tair（企业版）命令支持与限制](../developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。

| 扩展数据结构 | 版本差异（5.0 vs 6.0） | 影响说明 |
| --- | --- | --- |
| TairHash ( [exHash](../developer-reference/the-tairhash-command.md) ) | 在 EXHSCAN 命令中使用 pattern 参数时： • 5.0 版本 ：仅对匹配 pattern 的 field 进行过期检查。 • 6.0 版本 ：对所有扫描到的 field（无论是否匹配）均执行过期检查。 | 在存在大量过期 field 且扫描的 count 值较大时，6.0 版本的响应时间（RT）可能会上升。 |
| TairBloom ( [Bloom](../developer-reference/tairbloom-command.md) ) | 底层使用的 Hash 算法更新。 | 可能会导致假阳率略微上升。 |
| TairTS ( [TS](../developer-reference/the-tickets-command.md) ) | EXTS.S.ALTER ：在 6.0 版本中，传入部分无效属性（如 CHUNK_SIZE ）将被静默忽略，而在 5.0 版本中会报错。 EXTS.S.INFO ：在 6.0 版本中，返回值不再包含 maxDataPoints 字段。 EXTS.S.RANGE / EXTS.P.RANGE ：在 6.0 版本中，传入不支持的 withLabels 参数将被忽略，而在 5.0 版本中会报错。 查询 ：6.0 版本查询时 bucket 可以小于 1 秒，5.0 版本不可以。 | • 检查业务代码是否依赖 EXTS.S.ALTER 和 EXTS.S.RANGE 等命令的报错逻辑。 • 调整依赖 EXTS.S.INFO 返回值中 maxDataPoints 字段的客户端代码。 |
