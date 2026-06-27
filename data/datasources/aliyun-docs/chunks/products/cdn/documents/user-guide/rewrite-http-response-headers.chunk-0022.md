### JS 文件被当成 text/html 错误处理，首次刷新必现、第二次正常的原因及解决方法？
问题原因：
源站首次返回 JS 文件时，Content-Type响应头可能被错误设置为text/html。CDN 将该错误类型缓存后，首次访问时浏览器会按照text/html解析 JS 文件，导致乱码或执行异常。第二次访问时，由于源站已修正Content-Type或 CDN 重新回源获取了正确类型，页面恢复正常。
解决方法：
在 CDN 控制台的「修改入站响应头」中配置规则，将 JS 文件的Content-Type强制替换为application/javascript。
配置完成后，前往刷新和预热页面刷新该 JS 文件的缓存，使新规则立即生效。
