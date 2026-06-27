### 更多功能&适用场景
通过端口转发访问无公网服务
使用会话管理客户端的端口转发功能，将实例的某个服务端口映射到您的本机，然后您可以直接通过访问本机的对应端口访问在ECS上的服务。比如访问内网部署的Web后端服务、通过SSH连接内网实例。会话管理是基于WebSocket建立连接，工作在TCP上，因此只支持TCP端口转发，不支持UDP。具体操作，请参见[通过会话管理](perform-port-forwarding-by-using-ali-instance-cli.md)[CLI](perform-port-forwarding-by-using-ali-instance-cli.md)[的端口转发访问无公网实例](perform-port-forwarding-by-using-ali-instance-cli.md)。
向实例添加临时SSH公钥
在您使用SSH连接实例时，您可以使用会话管理向实例内添加有效时间60s的临时公钥，然后通过密钥对的验证方式连接到实例。具体操作，请参见[通过会话管理](register-a-public-key-and-connect-to-an-instance-with-the-key-by-using-ali-instance-cli.md)[CLI](register-a-public-key-and-connect-to-an-instance-with-the-key-by-using-ali-instance-cli.md)[注册临时公钥免密登录实例](register-a-public-key-and-connect-to-an-instance-with-the-key-by-using-ali-instance-cli.md)。
会话操作记录投递
如果您是多人使用场景，可以通过会话操作记录投递功能，查看某个人的操作记录，便于您在后续进行操作审计。开启会话操作记录投递功能，请参见[会话操作记录投递](use-the-session-record-delivery-feature.md)。
