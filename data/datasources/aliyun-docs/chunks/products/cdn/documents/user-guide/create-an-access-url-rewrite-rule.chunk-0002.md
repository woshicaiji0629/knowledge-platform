## 重写访问URL和重写回源路径的区别

| 功能 | 作用对象 | 客户端体验 | 应用场景 |
| --- | --- | --- | --- |
| [重写访问](create-an-access-url-rewrite-rule.md) [URL](create-an-access-url-rewrite-rule.md) | 影响的是客户端访问的 URL，同时也会改变 CDN 节点回源的 URL。 | 执行规则为 redirect 的情况下，客户端将会使用重定向以后的 URL 重新发起访问请求。 执行规则为 break 的情况下，客户端看到的 URL 与实际访问的 URL 一致，没有变化。 | 常用于将旧域名的 URL 迁移、映射到新域名；或者为移动端和 PC 端提供不同的 URL。 示例 ：访问 old.example.com/hello 时，重写访问 URL 为 new.example.com/hello 。 |
| [重写回源路径](rewrite-urls-in-back-to-origin-requests.md) | 影响的是 CDN 节点回源时访问的 URL，而客户端访问的 URL 不变。 | 客户端看到的 URL 与实际访问的 URL 一致，没有变化。 | 常用于隐藏源站的真实 URL 结构，保护源站信息；或者通过 URL 映射，让 CDN 节点回源到不同的源站目录。 示例 ：访问 cdn.example.com/hello 时重写回源 URL 为 origin.example.com/source/hello 。 |
