### 安全扫描发现缺失 Required HTTP Header Fields，如何在 CDN 侧直接配置修复该漏洞？
CDN 作为中间代理，无法直接在响应中插入缺失的 HTTP 响应头（如 Cache-Control 等）来修复安全扫描漏洞，只能配置修改回源请求头。
建议通过 CDN 控制台配置自定义回源请求头，将所需参数透传至源站（如 CLB），由源站接收并处理。若源站不支持或无法修改，CDN 侧无其他直接添加响应头的方式。
说明
如果您需要在 CDN 返回给客户端的响应中添加 HTTP 响应头，请参见[修改出站响应头](create-a-custom-http-response-header.md)。
