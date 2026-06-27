ack-ram-authenticator-to-help-the-api-server-in-ack-managed-clusters-complete-webhook-authentication.md)实现更加灵活可控的RBAC授权体验，实现删除RAM用户或RAM角色时数据面KubeConfig凭据的自动吊销。
重要
请务必确认不存在风险后，再执行KubeConfig清除操作，否则，您将无法使用该用户的KubeConfig访问集群API Server。
KubeConfig的运维和管理是用户的职责，请您务必及时清除有安全风险的KubeConfig。
