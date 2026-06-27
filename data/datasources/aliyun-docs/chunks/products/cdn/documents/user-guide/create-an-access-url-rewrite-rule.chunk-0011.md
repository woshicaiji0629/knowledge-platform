### 示例4
客户端请求http://example.aliyundoc.com/stories/index.html#/voice/318时，URL中#/voice/318属于客户端片段标识符（Fragment Identifier），浏览器不会将该部分发送到服务端。CDN节点收到的实际请求路径仅为/stories/index.html。因此，配置重写规则时，待重写的Path应设置为^/stories/index\.html$来精确匹配#前的路径部分，目标Path设置为目标URL，执行规则设置为Redirect。
如果多个含不同#片段的旧URL需要跳转到不同的目标地址，由于服务端无法区分#后的不同内容，需要为每个不同的源路径分别配置独立的重写规则。
该文章对您有帮助吗？
反馈
