# 配置Referer黑/白名单
Referer黑/白名单基于HTTP请求头中的Referer字段，通过设置黑名单/白名单来控制访问，防止资源被非法盗用。配置后，CDN会根据Referer信息，允许或拒绝访问请求。
重要
阿里云CDN的Referer黑/白名单功能默认不启用，即任何网站均可访问您的资源。
Referer黑/白名单只是防止CDN流量盗刷的一种方式，更多防护方式参见[防范流量盗刷最佳实践](../use-cases/best-practices-for-preventing-traffic-theft.md)。
将域名添加到Referer黑名单或白名单后，CDN会将该域名的泛域名加入规则名单。例如，填写aliyundoc.com，最终生效的是*.aliyundoc.com，即所有子域名都会生效。
