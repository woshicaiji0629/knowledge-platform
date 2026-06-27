### 重写回源路径示意图
客户端向CDN发起请求，请求的URL为cdn.example.com/files/hello.txt。
CDN接收到请求后，检查缓存，如果缓存中有请求URL的内容，直接返回给客户端；如果没有，则CDN节点根据重写回源URL规则，将回源URL重写为origin.example.com/secret/files/hello.txt，向源站发起请求。
源站接收到请求后，向CDN节点返回响应内容。
CDN节点将响应内容缓存，并返回给客户端。
