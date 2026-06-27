### 获取集群中OIDC提供商的URL和ARN信息
集群中RRSA功能开启后，在基本信息页签的安全与审计区域，将鼠标悬浮至RRSA OIDC右侧已开启上面，即可查看提供商的URL链接和ARN信息。
集群开启RRSA功能后，ACK将在后台执行如下操作。
自动创建一个集群专用的OIDC Issuer服务。该服务由ACK托管，无需您运维。更多信息，请参见[OIDC Issuer](https://openid.net/specs/openid-connect-discovery-1_0.html)。
修改当前集群的服务账户令牌卷投影功能的配置，使用本次创建的OIDC Issuer配置合并集群已有的service-account-issuer参数的值。更多信息，请参见[使用](../security-and-compliance/enable-service-account-token-volume-projection.md)[ServiceAccount Token](../security-and-compliance/enable-service-account-token-volume-projection.md)[卷投影](../security-and-compliance/enable-service-account-token-volume-projection.md)。
在您的账号下创建一个使用该OIDC Issuer的OIDC身份提供商，名称为ack-rrsa-<cluster_id>，其中<cluster_id>为您的集群ID。更多信息，请参见[管理](../../../../ram/documents/manage-an-oidc-idp.md)[OIDC](../../../../ram/documents/manage-an-oidc-idp.md)[身份提供商](../../../../ram/documents/manage-an-oidc-idp.md)。
