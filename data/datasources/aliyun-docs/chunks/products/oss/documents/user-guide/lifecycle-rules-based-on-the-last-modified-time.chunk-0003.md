### 存储类型转换限制
不支持通过生命周期规则将Appendable类型Object转为冷归档或深度冷归档存储。需先通过[SealAppendObject](../developer-reference/sealappendobject.md)将Object变为非追加状态，然后再使用生命周期规则完成转换。
不支持通过生命周期规则将软链接（symlink）转换为低频访问、归档、冷归档以及深度冷归档存储类型。
