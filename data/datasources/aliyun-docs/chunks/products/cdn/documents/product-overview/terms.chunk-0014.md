## Referer防盗链
Referer防盗链，是基于HTTP请求头中Referer字段（例如，Referer黑白名单）来设置访问控制规则，实现对访客的身份识别和过滤，防止网站资源被非法盗用。配置Referer黑白名单后，CDN会根据名单识别请求身份，允许或拒绝访问请求。具体配置，请参见[配置](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[Referer](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[黑/白名单](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)。
说明
Referer是HTTP请求头的一部分，携带了HTTP请求的来源地址信息（协议+域名+查询参数），可用于识别请求的来源。
