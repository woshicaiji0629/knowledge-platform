## 常见原因
用户通过HTTPS协议（443端口）访问加速域名（如https://example.aliyun.com/）。
CDN以HTTP协议（80 端口）回源（如http://example.aliyun.com/）。
源站服务器（如Nginx）配置了HTTP到HTTPS的重定向规则，通过HTTP协议回源时，服务器会返回301/302状态码，并且将请求重定向到HTTPS协议的URL（例如https://example.aliyun.com/）。随后，客户端（如浏览器）会遵循跳转规则，通过HTTPS协议（默认端口443）重新发起请求，最终访问加速域名。
上述过程形成循环，超过浏览器单次请求允许的重定向次数后，浏览器终止请求并报错。
