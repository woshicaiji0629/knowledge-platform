包含 / 的任意字符序列）。示例： cdn.aliyun.com/.* 匹配该域名下所有资源。 说明： 此方式为标记刷新。若需强制刷新整个目录，请使用刷新缓存 API 并设置 Force=true 。建议尽量使用更精确的匹配规则，避免非预期的大范围缓存失效。一个账号每日最多可提交 20 条包含正则表达式的 URL。 |

如何实现全站刷新（全局/根目录刷新）
CDN 不支持一键全站刷新，但您可以通过以下方式实现全站刷新：
目录刷新：在操作方式中选择目录，输入域名根目录 URL（如https://www.example.com/）。URL 必须以/结尾。
强制刷新（API）：若目录刷新后部分节点仍返回旧缓存，建议调用[刷新缓存 API](../developer-reference/api-cdn-2018-05-10-refreshobjectcaches.md)（RefreshObjectCaches），将Force参数设置为true进行强制刷新。强制刷新将无条件删除节点上的缓存资源，确保下次访问回源获取最新内容。
说明
控制台的刷新表单不支持设置Force参数，如需使用强制刷新，请通过 API 或 SDK 调用。
单击提交，系统开始执行刷新任务。
刷新任务一旦提交成功，无法中止。
刷新任务通常需要 5~6 分钟在全网生效。如果缓存过期时间小于此值，则无需手动刷新。
如果在OSS控制台开启了[CDN](../../../oss/documents/user-guide/cdn-acceleration.md)[缓存自动刷新](../../../oss/documents/user-guide/cdn-acceleration.md)，则无法通过 CDN 控制台查看 OSS 的缓存自动刷新任务。
