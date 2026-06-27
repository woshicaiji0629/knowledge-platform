### 场景二：设置Referer规则并勾选允许通过浏览器地址栏直接访问资源URL
说明
该场景设置Referer规则为aliyun.com并勾选允许通过浏览器地址栏直接访问资源URL。高级配置其他选项不勾选，重定向URL、规则条件均不配置。
相比场景一中多匹配出空Referer的情形，即携带空Referer和直接访问也将被允许。
不携带Referer的访问测试，命令curl -I CDN加速域名。
[root@ixxxxxxxxxx ~]# curl -I http://referer.mxxxxxxxp HTTP/1.1 200 OK Server: Tengine
携带" "Referer的访问测试，命令curl -e " " -I CDN加速域名。
[root@ixxxxx7 ~]# curl -e " " -I http://referer.mxxxp HTTP/1.1 200 OK Server: Tengine
