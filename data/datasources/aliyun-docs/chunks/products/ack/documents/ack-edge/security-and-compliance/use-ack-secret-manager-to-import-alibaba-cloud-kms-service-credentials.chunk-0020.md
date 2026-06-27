-to-a-ram-role.md)。
账号B（集群所在的阿里云账号）权限配置
在[容器服务管理控制台](https://cs.console.aliyun.com)开启集群的RRSA功能，用于创建集群的身份提供商信息。具体操作，请参见[启用](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RRSA](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[功能](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。
说明
安装ack-secret-manager时，需要将参数rrsa.enable设置为true，以启用RRSA功能。
创建可信实体为身份提供商的RAM角色，以供ack-secret-manager使用。
选择信任主体类型为身份提供商，添加主体时主要参数设置如下，具体操作，请参见[创建](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[OIDC](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[身份提供商的](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[角色](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)。
