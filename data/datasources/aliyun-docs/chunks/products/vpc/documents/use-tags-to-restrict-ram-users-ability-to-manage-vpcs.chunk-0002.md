### Condition Key 说明
标签鉴权通过权限策略中的条件（Condition）实现，支持以下两种Condition Key：

| 对比维度 | acs:ResourceTag | acs:RequestTag |
| --- | --- | --- |
| 检查对象 | 被操作的资源上已绑定的标签 | API 请求中传递的标签信息 |
| 典型场景 | 控制 可以操作哪些资源 | 控制 调用 API 操作资源时必须带什么标签 |
| 效果 | 限制操作范围（只能操作特定资源） | 限制操作行为（调用 API 时，请求参数里面必须携带的标签） |

通过组合使用acs:ResourceTag和acs:RequestTag，可以同时控制在哪个资源下操作和调用 API 操作资源时必须带什么标签，实现更精细的权限管理。
