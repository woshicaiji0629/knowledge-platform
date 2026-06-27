## 步骤二：创建RAM用户并完成授权
您可以使用阿里云账号（主账号）、RAM用户、RAM角色调用该接口，有关各种身份的差异请参见[身份](https://help.aliyun.com/zh/openapi/identity)。
重要
阿里云账号拥有所有API的访问权限，建议您创建并使用RAM用户进行API访问或日常运维。
[创建](../../../../ram/documents/user-guide/create-a-ram-user.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-user.md)[用户](../../../../ram/documents/user-guide/create-a-ram-user.md)。
使用阿里云账号登录[RAM](https://ram.console.aliyun.com/)[访问控制](https://ram.console.aliyun.com/)。
在左侧导航栏，选择身份管理>用户。
在用户页面，单击创建用户。
在创建用户页面，设置登录名称和显示名称、访问方式为控制台访问。
单击确定。
创建RAM用户成功后，请记录用户登录名称和密码。在调用OpenAPI时，需要使用该RAM用户登录阿里云OpenAPI开发者门户。
为RAM用户授予AliyunCSFullAccess权限。具体操作，请参见[管理](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
说明
AliyunCSFullAccess：管理容器服务 Kubernetes 版的权限。
AliyunCSReadOnlyAccess：只读访问容器服务 Kubernetes 版的权限。
如果您需要新建自定义权限，请参见[授权信息](../../ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-ram.md)。
进入对应的RAM用户详情页，在认证管理页签，单击创建 AccessKey。具体操作，请参见[创建](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../../r
