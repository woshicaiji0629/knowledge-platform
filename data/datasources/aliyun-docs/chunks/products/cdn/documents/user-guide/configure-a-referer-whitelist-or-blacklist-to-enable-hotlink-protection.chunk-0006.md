## Referer配置项说明

| 参数 | 说明 |  |
| --- | --- | --- |
| Referer 类型 | 黑名单 携带黑名单 Referer 的请求均无法访问当前资源。 白名单 只有携带白名单 Referer 的请求才能访问当前资源。 说明 黑名单和白名单互斥，只能选择一种。 |  |
| 规则 | 支持添加多个 Referer 名单，使用回车符分隔。 支持星号（*）作为通配符，匹配所有子域名。如 *.example.com 匹配 example.com 的所有子域名。 支持通配符（*）缺省，匹配自身及其所有子域名。如 example.com 匹配 example.com 和 *.example.com 结果集。 说明 Referer 黑/白名单规则的总长度最长不超过 60 KB。 配置规则不需要填写协议头。 |  |
| 重定向 URL | 请求被拦截后返回 302+Location 头，该项为 Location 头的值，必须以 http:// 或者 https:// 开头，例如： http://www.example.com 。 |  |
| 高级配置 | 允许通过浏览器地址栏直接访问资源 URL | 默认未勾选。勾选后，无论配置的是 Referer 黑名单还是白名单，系统不拦截空 Referer 请求，CDN 节点允许用户访问当前资源。 空 Referer 包括： 用户请求中不携带 Referer 头。 Referer 头值为空。 |
| 精确匹配 | 默认未勾选。勾选后，不再支持通配符（*）缺省。若未使用通配符， example.com 仅匹配 example.com 。 |  |
| 忽略 Scheme | 未勾选 忽略 Scheme 时，请求头中 Referer 必须携带 HTTP 或 HTTPS 协议头。 勾选 忽略 Scheme 后，请求头中 Referer 可不携带 HTTP 或 HTTPS 协议头。 |  |
| 规则条件 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 重要 引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](rules-engine.md) 中进行管理。 |  |
