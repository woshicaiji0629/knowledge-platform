### 场景三：设置Referer规则并勾选忽略Scheme
说明
该场景设置Referer规则为aliyun.com并勾选忽略scheme。高级配置其他选项不勾选，重定向URL、规则条件均不配置。
同场景一的情形，但允许出现不携带协议头，如仅域名aliyun.com的Referer请求。
不带协议头的Referer访问测试，命令curl -e aliyun.com -I CDN加速域名。
[root@i-xxx z ~]# curl -e aliyun.com -I http://referer.xxx HTTP/1.1 200 OK Server: Tengine
