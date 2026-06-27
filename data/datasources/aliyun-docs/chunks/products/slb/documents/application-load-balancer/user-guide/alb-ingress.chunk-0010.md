### ALB Ingress工作原理
ALB Ingress在兼容K8s原生功能基础上，还通过AlbConfig CRD和Ingress注解项提供了多种高级特性。
AlbConfig CRD：AlbConfig CRD用于配置ALB实例和监听。一个AlbConfig对应一个ALB实例。
Ingress注解项：用于配置转发规则，可将HTTP/HTTPS请求转发到对应的Service。
Service：后端真实服务的抽象，一个Service可以代表多个相同的后端服务。
