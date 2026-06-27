### 重写访问URL示意图
客户端向CDN发起请求，请求的URL为old.example.com/hello。
CDN接收到请求后，根据重写访问URL规则，CDN节点会在给客户端发送的302状态码响应信息的HTTP Location头部中放置新的URL地址信息，将请求的URL重写为new.example.com/hello。
客户端收到302状态码响应之后，将会向新的URL地址发起请求。
CDN节点检查缓存，如果缓存中有重写后URL的内容，直接返回给客户端；如果没有，则CDN节点向源站发起请求，请求的URL为重写后的new.example.com/hello。
源站接收到请求，返回响应内容给CDN节点。
CDN节点将响应内容缓存，并返回给客户端。
