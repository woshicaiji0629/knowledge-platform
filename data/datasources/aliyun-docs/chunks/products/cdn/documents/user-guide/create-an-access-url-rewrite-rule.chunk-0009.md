### 示例2
客户端请求http://example.aliyundoc.com/hello时，请求中包含/hello，匹配上了正则表达式^/hello$，CDN节点会给客户端响应302状态码，并且在Location信息里写入目标URLhttps://test.aliyundoc.com/index.html，客户端收到响应之后，将会对https://test.aliyundoc.com/index.html发起请求。
配置规则：待重写的Path设置为^/hello$，目标Path设置为https://test.aliyundoc.com/index.html，执行规则设置为redirect。
