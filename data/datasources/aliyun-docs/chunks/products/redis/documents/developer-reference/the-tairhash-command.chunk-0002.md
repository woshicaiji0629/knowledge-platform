| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [EXHSET](the-tairhash-command.md) | EXHSET key field value [EX time] [EXAT time] [PX time] [PXAT time] [NX | XX] [VER | ABS version] [KEEPTTL] | 向 Key 指定的 TairHash 中插入一个 field。如果 TairHash 不存在则自动创建一个，如果 field 已经存在则覆盖其值。 |
| [EXHGET](the-tairhash-command.md) | EXHGET key field | 获取 key 指定的 TairHash 中一个 field 的值，如果 TairHash 不存在或者 field 不存在，则返回 nil。 |
| [EXHMSET](the-tairhash-command.md) | EXHMSET key field value [field value ...] | 同时向 key 指定的 TairHash 中插入多个 field，如果 TairHash 不存在则自动创建一个，如果 field 已经存在则覆盖其值。 |
| [EXHPEXPIREAT](the-tairhash-command.md) | EXHPEXPIREAT key field milliseconds-timestamp [VER | ABS version] | 在 key 指定的 TairHash 中为一个 field 设置绝对过期时间，精确到毫秒。 |
| [EXHPEXPIRE](the-tairhash-command.md) | EXHPEXPIRE key field milliseconds [VER | ABS version] | 在 key 指定的 TairHash 中为一个 field 设置相对过期时间，单位为毫秒。 |
| [EXHEXPIREAT](the-tairhash-command.md) | EXHEXPIREAT key field timestamp [VER | ABS version] | 在 key 指定的 TairHash 中为一个 field 设置绝对过期时间，精确到秒。 |
| [EXHEXPIRE](the-tairhash-command.md) | EXHEXPIRE key field seconds [VER | ABS version] | 在 key 指定的 TairHash 中为一个 field 设置相对过期时间，单位为秒。 |
| [EXHPTTL](the-tairhash-command.md) | EXHPTTL key field | 查看
