L] | 将 key 指定的 TairHash 中一个 field 的 value 增加 num，num 为一个浮点数。如果 TairHash 不存在则自动新创建一个，如果指定的 field 不存在，则在加之前插入该 field 并将其值设置为 0。 说明 为 Key 的 field 设置了超时时间后，再次执行该命令时如果没有设置超时时间，该 field 将被设置为永不过期。 |
| [EXHGETWITHVER](the-tairhash-command.md) | EXHGETWITHVER key field | 同时获取 key 指定的 TairHash 一个 field 的值和版本，如果 TairHash 不存在或者 field 不存在，则返回 nil。 |
| [EXHMGET](the-tairhash-command.md) | EXHMGET key field [field ...] | 同时获取 key 指定的 TairHash 多个 field 的值，如果 TairHash 不存在或者 field 不存在，则返回 nil。 |
| [EXHMGETWITHVER](the-tairhash-command.md) | EXHMGETWITHVER key field [field ...] | 同时获取 key 指定的 TairHash 多个 field 的值和版本。 |
| [EXHLEN](the-tairhash-command.md) | EXHLEN key [NOEXP] | 获取 key 指定的 TairHash 中 field 个数，该命令不会触发对过期 field 的被动淘汰，也不会将其过滤掉，所以结果中可能包含已经过期但还未被删除的 field。如果只想返回当前没有过期的 field 个数，可以在命令中设置 NOEXP 选项。 |
| [EXHEXISTS](the-tairhash-command.md) | EXHEXISTS key field | 查询 key 指定的 TairHash 中是否存在对应的 field。 |
| [EXHSTRLEN](the-tairhash-command.md) | EXHSTRLEN key field | 获取 key 指定的 TairHash 中一个 field 对应的 value 的长度。 |
| [EXHKEYS](the-tairhash-command.md) | EXHKEYS key | 获取 key 指定的 TairHash 中所有的 field。 |
| [EXHVALS](the-tairhash-command.md) | EXHVALS key | 获取 key 指定的 TairHash 中所有 field 的值。 |
| [EXHGETALL
