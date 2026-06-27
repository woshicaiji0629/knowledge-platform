### ACKRestrictRoleBindings
规则说明：限制在指定命名空间下的Rolebinding使用指定范围内的Role或Clusterrole。
重要等级：high。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| restrictedRole | object | 限制使用的 Clusterrole 或 Role。 |
| allowedSubjects | array | 允许挂载的 Subjects 白名单列表。 |
