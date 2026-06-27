头。
确认源站实际返回的响应头中包含该字段。
在CDN控制台「修改出站响应头」中，显式添加Access-Control-Expose-Headers: <header-name>配置，以覆盖源站的CORS设置，确保前端JavaScript能获取该字段。例如，需要获取filename响应头时，添加Access-Control-Expose-Headers: filename。
使用浏览器无痕模式重新请求，确认问题是否解决。
该文章对您有帮助吗？
反馈
