## 控制台
前往ALB控制台的[TLS](https://slb.console.aliyun.com/alb/cn-hangzhou/tls)[安全策略](https://slb.console.aliyun.com/alb/cn-hangzhou/tls)页面，选择ALB实例所在地域。
单击创建自定义策略，参考以下信息进行配置，配置完成后单击创建。
选择最低版本：如业务无特殊兼容性要求，建议选择TLS 1.2及以上保障安全性。
启用TLS 1.3版本：为保障网络通信的安全性与效率，建议在业务兼容的前提下启用。
选择加密算法套件：需要与TLS协议版本匹配。
创建完成后，即可在[为监听配置](tls-security-policies.md)[TLS](tls-security-policies.md)[安全策略](tls-security-policies.md)中选择该自定义策略。
