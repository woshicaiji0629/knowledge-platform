### 示例3
客户端请求http://www.example.com/cdn/url/http://image.example.com/image/cat.jpg时，请求中包含/cdn/url/http://，匹配上了正则表达式^/cdn/url/http://(.*)，CDN节点会给客户端响应302状态码，并且在Location信息里写入目标URLhttp://image.example.com/image/cat.jpg，客户端收到响应之后，将会对http://image.example.com/image/cat.jpg发起请求。
配置规则：目标Path设置为http://$1，执行规则设置为redirect。
