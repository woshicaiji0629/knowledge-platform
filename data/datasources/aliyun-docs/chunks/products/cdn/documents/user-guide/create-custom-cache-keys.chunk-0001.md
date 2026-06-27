## 功能对比与选择
自定义Cache Key与[忽略参数](ignore-parameters.md)存在冲突：开启忽略参数后，节点会去除URL中?之后的参数，导致自定义Cache Key中的请求参数配置失效。使用自定义Cache Key前，请关闭忽略参数。
自定义Cache Key功能更全面，可替代忽略参数缓存键配置，推荐优先使用。配置对比：

| 场景 | 忽略参数 | 自定义 Cache Key |
| --- | --- | --- |
| 在缓存键中忽略所有请求参数 | 忽略参数设置为是，保留指定参数留空 | 添加一条请求参数处理策略： 操作方式：保留 参数名：设为任意不存在的参数名，例如 example-argument |
| 在缓存键中仅保留请求参数 key1 | 忽略参数设置为是，保留指定参数设置为 key1 | 添加一条请求参数处理策略： 操作方式：保留 参数名：key1 |
| 在缓存键中仅删除请求参数 key1 | 删除指定参数设置为 key1 | 添加一条请求参数处理策略： 操作方式：删除 参数名：key1 |

回源参数改写：自定义Cache Key功能不修改回源URL，仅修改请求的缓存标识，回源请求与客户端请求内容一致。如果需要改写回源URL携带的请求参数，请使用[重写回源参数](rewrite-url-parameters-in-back-to-origin-requests.md)。
缓存刷新：配置自定义 Cache Key 后，[按](refresh-and-prefetch-resources.md)[URL](refresh-and-prefetch-resources.md)[提交刷新任务](refresh-and-prefetch-resources.md)可能无法正确匹配缓存内容，请提交经过自定义Cache Key功能处理后的缓存键作为刷新对象。
