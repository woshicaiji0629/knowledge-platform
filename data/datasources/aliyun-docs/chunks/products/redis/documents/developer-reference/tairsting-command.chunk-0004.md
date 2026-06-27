## 命令列表
表 1.TairString命令

| 命令 | 语法 | 简介 |
| --- | --- | --- |
| [EXSET](tairsting-command.md) | EXSET key value [EX|PX|EXAT|PXAT time] [NX|XX] [VER|ABS version] [KEEPTTL] | 若 key 不存在，则创建新的 key，并将 value 保存到 key 中；若 key 已存在，则覆盖原来 value 的值。 |
| [EXGET](tairsting-command.md) | EXGET key | 获取 TairString 的 value 和 version。 |
| [EXSETVER](tairsting-command.md) | EXSETVER key version | 设置目标 key 的 version。 |
| [EXINCRBY](tairsting-command.md) | EXINCRBY key num [EX|PX|EXAT|PXAT time] [NX|XX] [VER|ABS version] [MIN minval] [MAX maxval] [KEEPTTL] | 对 TairString 的 value 进行自增自减操作，num 的范围为 long。 |
| [EXINCRBYFLOAT](tairsting-command.md) | EXINCRBYFLOAT key num [EX|PX|EXAT|PXAT time] [NX|XX] [VER|ABS version] [MIN minval] [MAX maxval] [KEEPTTL] | 对 TairString 的 value 进行自增自减操作，num 的范围为 double。 |
| [EXCAS](tairsting-command.md) | EXCAS key newvalue version | 当目标 key 的 version 值与指定的 version 相等时，则更新 key 的 value 值；version 不相等，则返回旧的 value 和 version。 |
| [EXCAD](tairsting-command.md) | EXCAD key version | 当目标 key 的 version 值与指定的 version 相等时，则删除 Key。 |
| [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairString 数据。 |
