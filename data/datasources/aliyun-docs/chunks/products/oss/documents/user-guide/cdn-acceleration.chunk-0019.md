写访问](../../../cdn/documents/user-guide/create-an-access-url-rewrite-rule.md)[URL](../../../cdn/documents/user-guide/create-an-access-url-rewrite-rule.md)实现同样效果：

| 参数 | 配置值 |
| --- | --- |
| 待重写的 Path | ^/$ （匹配根目录访问） |
| 目标 Path | /index.html （或实际首页文件名） |
| 执行规则 | Redirect |

是否可以通过CDN域名上传文件到OSS？
出于安全考虑，不建议通过CDN域名上传文件到OSS。如果CDN被设置为公共写入，任何人无需身份验证即可通过CDN上传文件到OSS，容易受到恶意上传和数据篡改的攻击。建议在限制最小权限的前提下，使用OSS域名上传文件。
使用CDN加速后OSS下行流量是否会变少？
如果CDN缓存的文件被频繁命中，OSS的公网流出流量会显著降低，从而减少OSS流量成本。
CDN缓存文件被频繁命中的前提是，业务场景中的部分数据在某段时间内被频繁访问，例如网站访问、图片文件下载、游戏发行等场景。缓存命中率越高，回源流量越少，成本节省效果越明显。
如何统计文件的真实访问次数？
启用CDN加速后，OSS的访问日志将无法记录由CDN缓存直接响应的终端用户访问请求，可通过以下方式统计：

| 数据范围 | 获取方式 |
| --- | --- |
| 30 天内的日志数据 | 通过下载 CDN 的 [离线日志](../../../cdn/documents/user-guide/offline-logs-quick-start.md) 进行查看和分析。 |
| 超过 30 天的日志数据 | 在 CDN 中 [配置实时日志推送](../../../cdn/documents/user-guide/configure-real-time-log-delivery.md) 后，在 [CDN](https://cdnnext.console.aliyun.com/log/realtime/pushData) [实时日志数据统计](https://cdnnext.console.aliyun.com/log/realtime/pushData) 页面查看和分析。 |
