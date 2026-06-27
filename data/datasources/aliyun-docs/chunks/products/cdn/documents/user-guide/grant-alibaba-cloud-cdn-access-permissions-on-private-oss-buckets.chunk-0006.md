## 安全加固建议
开启私有Bucket回源后，您的源站数据是安全的，但缓存在CDN边缘节点上的资源默认是公开访问的。为防止CDN流量被盗刷，强烈建议您结合使用CDN提供的其他安全功能：
[配置](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[Referer](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[黑/白名单](configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)：限制只有特定来源网站的请求才能访问您的CDN资源。
[配置](configure-url-signing.md)[URL](configure-url-signing.md)[鉴权](configure-url-signing.md)：为您的资源URL设置动态签名和过期时间，有效抵御恶意下载。
