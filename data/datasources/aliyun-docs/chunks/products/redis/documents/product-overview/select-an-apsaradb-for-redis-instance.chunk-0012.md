### 选择实例规格
您需要综合业务预估量（容量、带宽、连接数、QPS等）选择合适的实例规格购买量（分片规格和分片数）。建议安全规格：（预估量÷购买量）< 80%。
在预估容量时，无需考虑持久化Fork写时复制占用的内存开销以及增强功能（如安全白名单、审计、大Key、热Key等）的内存开销，这些开销由阿里云承担，不会占用购买的实例规格容量。
重要
[大](../user-guide/identify-and-handle-large-keys-and-hotkeys.md)[Key](../user-guide/identify-and-handle-large-keys-and-hotkeys.md)是Redis使用中的常见问题。如果集群总容量较大而单分片容量较小，当业务产生大Key时，更容易造成大Key所在分片容量用尽。
集群架构的分片规格选择建议：

| 实例总容量 | 建议分片规格 |
| --- | --- |
| 16 GB～64 GB | 2 GB 及以上 |
| 64 GB～256 GB | 4 GB 及以上 |
| 大于 256 GB | 8 GB 及以上 |

说明
在购买后，如果您的业务变动导致当前所选规格不满足业务需求，可随时[变更实例配置](../user-guide/change-the-configurations-of-an-instance.md)。
