## 注意事项
配置回源301/302跟随之前，请先确认CDN是否配置了[默认回源](configure-the-default-origin-host.md)[HOST](configure-the-default-origin-host.md)或者[指定源站回源](specify-an-origin-host-for-each-origin.md)[HOST](specify-an-origin-host-for-each-origin.md)：
未配置默认回源HOST或指定源站回源HOST：当源站响应“301/302状态码+Location URL”给CDN节点时，回源请求的HOST头将使用Location域名。
配置了默认回源HOST：当源站响应“301/302状态码+Location URL”给CDN节点时，回源请求的HOST头将使用CDN配置的HOST头。如果源站要求使用Location域名作为回源HOST，请使用[指定源站回源](specify-an-origin-host-for-each-origin.md)[HOST](specify-an-origin-host-for-each-origin.md)功能。
源站响应给CDN节点的Location头部的格式支持以下3种：
Location: http://www.example.net/index.html：CDN节点将使用Location中的完整URL。
Location: //www.example.net/index.htmL：CDN节点将使用302前的回源协议加上Location中的信息拼接成一个URL。
Location: /index.html：CDN节点将使用302前的回源协议和域名加上Location中的信息拼接成一个URL。
