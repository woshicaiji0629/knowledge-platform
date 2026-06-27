### 示例1
客户端请求http://example.aliyundoc.com/hello时，请求中包含/hello，CDN节点会在302状态码的Location信息里写入新的URL地址http://example.aliyundoc.com/index.html，并返回给客户端，客户端对http://example.aliyundoc.com/index.html发起请求。
该规则配置中，待重写的Path为^/hello$，目标Path为/index.html，执行规则选择redirect。
说明
客户端在302重定向的时候，如果Location中不包含协议头和域名，那么会默认使用原始请求的协议头和域名。
