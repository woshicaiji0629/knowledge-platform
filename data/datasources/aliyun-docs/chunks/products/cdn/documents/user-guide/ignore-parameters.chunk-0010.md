### 如何利用忽略参数应对通过 URL 参数绕过缓存的请求？
当攻击者或爬虫通过添加随机无意义参数（如?timestamp=xxx、?random=xxx）请求同一资源时，CDN 会将每个带不同参数的请求视为独立资源，导致缓存命中率降低和回源流量激增。
此时应开启忽略参数功能（或配置忽略所有参数），使携带不同随机参数的请求命中同一缓存，从而有效降低回源压力。例如，配置忽略参数后，以下请求将命中同一缓存：
http://example.com/page.html?t=123456
http://example.com/page.html?t=789012
http://example.com/page.html?random=abc
上述请求在开启忽略参数后，统一使用http://example.com/page.html匹配缓存，有效防御通过 URL 参数绕过缓存的攻击行为。
