### 场景一：仅设置Referer规则
说明
该场景仅设置Referer规则为aliyun.com，重定向URL、高级配置、规则条件均不配置。
将匹配携带形如http(s)://aliyun.com及其子域名的请求，其他非白名单Referer将被拒绝。
携带主域名的Referer访问测试，命令curl -e http://aliyun.com -I CDN加速域名。
[root@xxx ~]# curl -e http://aliyun.com -I http://referer.n p HTTP/1.1 200 OK Server: Tengine
携带子域名的Referer访问测试，命令curl -e http://sub.aliyun.com -I CDN加速域名。
[root@xxx ~]# curl -e http://sub.aliyun.com -I http://referer.xxx HTTP/1.1 200 OK Server: Tengine
携带其他域名的Referer访问测试，命令curl -e http://aIiyun.com -I CDN加速域名。
[root@xxx ~]# curl -e http://aIiyun.com -I http://referer.xxx HTTP/1.1 403 Forbidden Server: Tengine
空Referer的测试，命令curl -e " " -I CDN加速域名。
[root@ixxxxx ~]# curl -e " " -I http://referer.nxxxxx p HTTP/1.1 403 Forbidden Server: Tengine
仅域名的Referer访问测试，命令curl -e aliyun.com -I CDN加速域名。
[root@i-xxx ~]# curl -e aliyun.com -I http://referer.mxxx HTTP/1.1 403 Forbidden Server: Tengine
