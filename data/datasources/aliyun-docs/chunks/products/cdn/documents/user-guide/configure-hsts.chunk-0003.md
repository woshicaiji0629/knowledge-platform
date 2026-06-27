## 约束限制
配置HSTS后，客户端只能使用HTTPS协议访问CDN节点，请勿同时配置HTTPS强制跳转HTTP。
HSTS策略仅对域名有效，对IP无效。
由于HSTS策略在客户端生效，关闭HSTS后无法立即生效，需要执行刷新使HSTS策略在客户端下一次HTTPS请求时下发给客户端。
