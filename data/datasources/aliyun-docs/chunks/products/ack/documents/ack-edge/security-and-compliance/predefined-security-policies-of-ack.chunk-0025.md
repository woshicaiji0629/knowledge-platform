### ACKOSSStorageLocationConstraint
规则说明：限制指定命名空间下的部署只能使用指定地域中的阿里云OSS存储卷。
重要等级：low。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| mode | string | 是否采用白名单模式，默认值 allowlist 为白名单模式，其他值为黑名单模式。 |
| regions | array | 指定的阿里云 Region ID 列表。 |
