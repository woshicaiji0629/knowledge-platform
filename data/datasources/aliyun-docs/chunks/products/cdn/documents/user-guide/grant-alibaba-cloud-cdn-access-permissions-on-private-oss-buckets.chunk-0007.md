## 关闭OSS私有Bucket回源
如果您不希望加速域名能够访问您同账号下的私有Bucket内资源，您可以通过访问控制RAM（Resource Access Management）控制台，取消对应角色名称的授权，关闭CDN回源OSS私有Bucket的权限。
在CDN控制台关闭该功能。
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，单击目标域名对应的管理。
在指定域名的左侧导航栏，单击回源配置。
在阿里云OSS私有Bucket回源区域，关闭阿里云OSS私有Bucket回源开关。
在RAM控制台彻底删除授权。
登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
在左侧导航栏，单击
在角色名称列表下，单击AliyunCDNAccessingPrivateOSSRole角色。
进入角色详情页，在权限管理页签下可查看到已授权的系统策略（备注：用于CDN回源私有OSS Bucket角色的授权策略，包含OSS的只读权限），资源范围为账号级别。操作列提供解除授权链接，页面右上角有删除角色按钮。
移除角色AliyunCDNAccessingPrivateOSSRole中的所有权限。
单击权限对应的解除授权。
在移除权限的确认对话框中，单击解除授权。
返回
单击AliyunCDNAccessingPrivateOSSRole角色对应的删除角色。
在删除角色的确认对话框中，单击删除角色。
返回
单击AliyunCDNAccessingPrivateOSSRolePolic策略对应的删除权限策略按钮。
在删除权限策略的确认对话框中，输入策略名称，单击删除权限策略。
