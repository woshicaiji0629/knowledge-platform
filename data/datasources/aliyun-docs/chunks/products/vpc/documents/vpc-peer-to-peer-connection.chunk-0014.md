### Condition Key
鉴权时，RAM 会根据请求中的AcceptingAliUid（创建对等连接时）或RequestingAliUid（接受对等连接时）反查对端账号所属的[资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)，并将以下 Condition Key 注入鉴权上下文，由您自定义策略中的 Condition 进行匹配。

| Condition Key | 类型 | 说明 | 典型场景 |
| --- | --- | --- | --- |
| acs:TargetRDId | String | 对端账号所属的 资源目录 ID ，例如 rd-xxxxxx 。 | 限定对端账号必须属于指定资源目录。 |
| acs:TargetRDPath | String | 对端账号所属的 资源目录路径 ，格式为 {RDId}/{RootFolderId}/{FolderId}/{AccountId} ，支持通配符匹配。 | 限定对端账号必须位于指定资源夹（Folder）下，满足分层治理需求。 |

使用约束：仅vpc:CreateVpcPeerConnection与vpc:AcceptVpcPeerConnection会注入上述 Condition Key，对等连接的查询、修改、删除等其他操作不生效。命中策略后请求返回错误码Forbidden.NoPermission，错误明细中NoPermissionType为ExplicitDeny，可通过 RequestId 在[操作审计](https://help.aliyun.com/zh/actiontrail/product-overview/what-is-actiontrail)中追溯命中过程。
