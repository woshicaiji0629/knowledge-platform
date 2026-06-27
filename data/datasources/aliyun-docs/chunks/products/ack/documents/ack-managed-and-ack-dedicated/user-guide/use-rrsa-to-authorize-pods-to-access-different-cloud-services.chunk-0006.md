### 使用示例
本示例部署的应用将使用RRSA功能扮演指定角色，获取当前账号下集群列表信息。
示例配置
命名空间：rrsa-demo
ServiceAccount：demo-sa
RAM角色：demo-role-for-rrsa
示例流程
如果您希望通过不安装ack-pod-identity-webhook组件的方式使用RRSA功能，您可以手动修改应用模板挂载应用所需的OIDC Token文件并配置相关环境变量。具体操作，请参见[手动修改应用模板使用](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RRSA](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[功能](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。
如果您希望使用已存在的RAM角色，不创建新的RAM角色，您可以为已有RAM角色新增相关权限。具体操作，请参见[使用已存在的](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RAM](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[角色并授权](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。
安装ack-pod-identity-webhook组件。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择运维管理 > 组件管理。
在组件管理页面，单击安全页签，找到ack-pod-identity-webhook组件，单击组件右下方的安装。
在提示对话框确认组件信息后，单击确定。
创建一个名为demo-role-for-rrsa的RAM角色。主要参数说明如下，具体操作，请参见[创建](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[OIDC](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[身份提供商的](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[RAM](../../../../ram/documents/user-guide/
