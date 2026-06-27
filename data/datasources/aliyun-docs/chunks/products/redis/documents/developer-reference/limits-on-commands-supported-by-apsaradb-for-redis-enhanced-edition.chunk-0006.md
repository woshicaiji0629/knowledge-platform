### Generic

| 命令 | 5.0 版本 | 6.0 版本 | 7.0 版本 |
| --- | --- | --- | --- |
| COPY | ➖ | ➖ | ✔️ |
| DEL | ✔️ | ✔️ | ✔️ |
| DUMP | ✔️ | ✔️ | ✔️ |
| EXISTS | ✔️ | ✔️ | ✔️ |
| EXPIRE | ✔️ | ✔️ | ✔️ |
| EXPIREAT | ✔️ | ✔️ | ✔️ |
| EXPIRETIME | ➖ | ➖ | ✔️ |
| KEYS | ✔️ | ✔️ | ✔️ |
| MIGRATE | ❌ | ❌ | ❌ |
| MOVE | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ 说明 持久内存型存在限制，详情请参见 [命令限制](limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md) 。 | ✔️ |
| OBJECT | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| OBJECT HELP | ➖ | ➖ | ✔️ |
| PERSIST | ✔️ | ✔️ | ✔️ |
| PEXPIRE | ✔️ | ✔️ | ✔️ |
| PEXPIREAT | ✔️ | ✔️ | ✔️ |
| PEXPIRETIME | ➖ | ➖ | ✔️ |
| PTTL | ✔️ | ✔️ | ✔️ |
| RANDOMKEY | ✔️ | ✔️ | ✔️ |
| RENAME | ✔️ | ✔️ 说明 持久内存型、磁盘型存在限制，详情请参见 [命令限制](limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md) 。 | ✔️ |
| RENAMENX | ✔️ | ✔️ 说明 持久内存型、磁盘型存在限制，详情请参见 [命令限制](limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md) 。 | ✔️ |
| RESTORE | ✔️ | ✔️ | ✔️ |
| SCAN | ✔️ | ✔️ | ✔️ |
| SORT | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| SORT_RO | ➖ | ➖ | ✔️ |
| TOUCH | ✔️ | 内存型、持久内存型✔️ 磁盘型❌ | ✔️ |
| TTL | ✔️ | ✔️ | ✔️ |
| TYPE | ✔️ | ✔️ | ✔️ |
| UNLINK | ✔️ | ✔️ | ✔️ |
| WAIT | ✔️ | ✔️ | ✔️ |
