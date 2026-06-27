## 相关文档
若您的业务有更高的安全需求，您可以进一步了解ALB的以下功能：
[配置全链路](end-to-end-data-transfer-over-https.md)[HTTPS](end-to-end-data-transfer-over-https.md)[访问实现加密通信](end-to-end-data-transfer-over-https.md)：ALB提供全链路HTTPS加密功能，可以实现客户端到ALB、ALB到后端服务器之间的全链路加密通信，提升敏感业务的安全性。
[使用](configure-mutual-authentication-on-an-https-listener.md)[ALB](configure-mutual-authentication-on-an-https-listener.md)[部署](configure-mutual-authentication-on-an-https-listener.md)[HTTPS](configure-mutual-authentication-on-an-https-listener.md)[业务（双向认证）](configure-mutual-authentication-on-an-https-listener.md)：ALB提供HTTPS双向认证功能，在客户端与服务端建立连接之前，双方需进行身份验证。仅在双方均成功通过认证后，方可建立安全通信通道进行数据传输，从而确保只有授权的客户端能够访问接入，有效降低中间人攻击和未授权访问等安全风险。
了解更多关于监听的转发条件以及转发动作，请参见[配置监听转发规则](../user-guide/manage-forwarding-rules-for-a-listener.md)。
通过ALB监听转发规则还可以实现以下场景需求：
[使用](use-the-traffic-mirroring-feature-to-mirror-production-traffic-to-a-staging-environment.md)[ALB](use-the-traffic-mirroring-feature-to-mirror-production-traffic-to-a-staging-environment.md)[流量镜像功能实现仿真压测](use-the-traffic-mirroring-feature-to-mirror-production-traffic-to-a-staging-environment.md)：通过ALB提供的流量镜像功能可以实现在线流量仿真，将在线流量镜像到测试环境的后端服务器，同时ALB自动丢弃镜像后端服务器返回的响应数据，保证镜像后端服务器的测试业务不会影响到线上业务。
[使用](use-alb-to
