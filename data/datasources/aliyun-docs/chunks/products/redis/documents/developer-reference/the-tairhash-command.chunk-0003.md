EXHEXPIRE key field seconds [VER | ABS version] | 在 key 指定的 TairHash 中为一个 field 设置相对过期时间，单位为秒。 |
| [EXHPTTL](the-tairhash-command.md) | EXHPTTL key field | 查看 key 指定的 TairHash 中一个 field 的剩余过期时间，结果精确到毫秒。 |
| [EXHTTL](the-tairhash-command.md) | EXHTTL key field | 查看 key 指定的 TairHash 中一个 field 的过期时间，结果精确到秒。 |
| [EXHVER](the-tairhash-command.md) | EXHVER key field | 查看 key 指定的 TairHash 中一个 field 的当前版本号。 |
| [EXHSETVER](the-tairhash-command.md) | EXHSETVER key field version | 设置 key 指定的 TairHash 中一个 field 的版本号。 |
| [EXHINCRBY](the-tairhash-command.md) | EXHINCRBY key field num [EX time] [EXAT time] [PX time] [PXAT time] [VER | ABS version] [MIN minval] [MAX maxval] [KEEPTTL] | 将 key 指定的 TairHash 中一个 field 的 value 增加 num，num 为一个整数。如果 TairHash 不存在则自动新创建一个，如果指定的 field 不存在，则在加之前插入该 field 并将其值设置为 0。 说明 为 Key 的 field 设置了超时时间后，再次执行该命令时如果没有设置超时时间，该 field 将被设置为永不过期。 |
| [EXHINCRBYFLOAT](the-tairhash-command.md) | EXHINCRBYFLOAT key field num [EX time] [EXAT time] [PX time] [PXAT time] [VER | ABS version] [MIN minval] [MAX maxval] [KEEPTTL] | 将 key 指定的 TairHash 中一个 field 的 value 增加 num，num 为一个浮点数。如果 TairHash 不存在则自动新创建一个，如果指定的 field 不存在，则在加之前插入该 field 并将其值设置为 0。 说明 为 Key 的 field 设置了超时时间后，再次执行该命令时
