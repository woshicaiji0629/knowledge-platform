IBABA_CLOUD_OIDC_TOKEN_FILE | 包含 OIDC Token 的文件路径。 |  |
| VolumeMount | rrsa-oidc-token | 挂载 OIDC Token 的配置。 |
| Volume | rrsa-oidc-token | 挂载 OIDC Token 的配置。 |

执行以下命令，查看测试应用日志。
kubectl -n rrsa-demo logs demo
预期输出集群列表信息：
cluster id: cf***, cluster name: foo* cluster id: c8***, cluster name: bar* cluster id: c4***, cluster name: foob*
可选：移除角色被授予的AliyunCSReadOnlyAccess系统策略权限。具体操作，请参见[为](../../../../ram/documents/remove-permissions-from-a-ram-role.md)[RAM](../../../../ram/documents/remove-permissions-from-a-ram-role.md)[角色移除权限](../../../../ram/documents/remove-permissions-from-a-ram-role.md)。
等待30秒左右，执行以下命令，再次查看测试应用日志。
kubectl -n rrsa-demo logs demo
预期输出无权限的错误日志：
StatusCode: 403 Code: StatusForbidden Message: code: 403, STSToken policy Forbidden for action cs:DescribeClustersForRegion request id: E78A2E2D-*** Data: {"accessDeniedDetail":{"AuthAction":"cs:DescribeClustersForRegion","AuthPrincipalDisplayName":"demo-role-for-rrsa:ack-ram-tool","AuthPrincipalOwnerId":"11***","AuthPrincipalType":"AssumedRoleUser","NoPermissionType":"ImplicitDeny","PolicyType":"ResourceGroupLevelIdentityBasedPolicy"},"code":"StatusForbidden","message":"STSToken policy Forbidden for action cs:DescribeClustersForRegion","requestId":"E78A2E2D-***","status":403,"statusCode":403}
