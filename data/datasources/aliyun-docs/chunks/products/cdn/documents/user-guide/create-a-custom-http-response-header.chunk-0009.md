说明
响应头值支持配置为“*”，表示任意来源。
响应头值非“*”的情况下，支持配置单个或者多个IP、域名、或者IP和域名混合。相互间用英文（,）分隔。
响应头值非“*”的情况下，必须包含协议头“http:// ”或者“https://”。
响应头值支持携带端口。
响应头值支持泛域名。
说明
CDN支持通过自定义响应头配置 Content-Security-Policy（CSP）和 Permissions-Policy 安全响应头。ALB（应用型负载均衡）本身不支持直接添加这两个安全响应头，如需配置，建议通过CDN或WAF等产品实现。
CSP响应头值不要包含外层双引号，这是常见的配置报错原因。正确格式示例：default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:
浏览器F12开发者工具中的CSP语法提示属于浏览器自身的限制，与实际请求无关，不影响响应头的实际生效，请通过实际请求验证。
