## 演示示例
在浏览器中访问经过CDN加速的M3U8文件，并在请求最后加上MtsHlsUriToken=tokenxxxxx。例如：http://<CDN 加速域名>/video.m3u8?MtsHlsUriToken=tokenxxxxx
通过Chrome浏览器开发者工具，在Network（网络）面板，可以看到请求M3U8文件是带上了自定义参数，但是请求密钥地址时没有携带该参数。
在CDN控制台开启M3U8标准加密改写，如果需要，可以设置自定义参数名（本次演示中使用默认参数MtsHlsUriToken）。在CDN控制台开启M3U8标准加密改写功能，自定义参数名设置为MtsHlsUriToken。
重复步骤1，在浏览器中访问经过CDN加速的M3U8文件，并在请求最后加上MtsHlsUriToken=tokenxxxxx。
通过浏览器开发者工具，在Network（网络）面板，可以看到在请求密钥地址时，带上了自定义的参数。
密钥文件encryption_key.key的请求 URL 中已附带MtsHlsUriToken=tokenxxxxx参数，返回状态码为 206，Content-Length 为 16 字节。
