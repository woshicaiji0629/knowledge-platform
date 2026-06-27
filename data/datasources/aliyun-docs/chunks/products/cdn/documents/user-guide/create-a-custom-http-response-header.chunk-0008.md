tials | 该响应头表示是否可以将对请求的响应暴露给页面。 返回 true：表示可以暴露。 返回其他值：表示不可以暴露。 | true |
| Access-Control-Max-Age | 指定客户端程序对特定资源的预请求返回结果的缓存时间，单位为秒。 | 600 |
| Content-Security-Policy | 配置内容安全策略（CSP），用于控制页面可以加载哪些资源，防范 XSS 攻击和数据注入等安全威胁。CDN 不对 CSP 策略内容做语义校验，仅校验 HTTP 响应头基本格式。策略内容需为单行字符串，不能包含换行符、非法控制字符或未转义的引号，且不要包含外层双引号。建议先在浏览器开发者工具中验证策略正确性后再填入，或在源站配置 CSP 由 CDN 透传。 | default-src 'self'; script-src 'self' 'unsafe-inline' |
| Permissions-Policy | 配置权限策略，用于控制浏览器特定功能（如摄像头、麦克风、地理位置等）的访问权限。 | camera=(), microphone=() |
