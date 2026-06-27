## （备用方案）通过RAM手动授权
登录[RAM](https://ram.console.aliyun.com/permissions)[控制台](https://ram.console.aliyun.com/permissions)。
在左侧导航栏，单击权限管理>权限策略。
在权限策略页面，单击创建权限策略。
在脚本编辑页签，输入以下策略内容。
{ "Version": "1", "Statement": [ { "Action": [ "oss:List*", "oss:Get*" ], "Resource": "*", "Effect": "Allow" } ] }
单击确定，在创建权限策略页面输入以下信息之后单击确定。
策略名称：AliyunCDNAccessingPrivateOSSRolePolicy
备注：用于CDN/DCDN回源私有OSS Bucket角色的授权策略，包含OSS的只读权限。
在左侧导航栏，单击身份管理>角色。
在角色页面，单击创建角色。
将信任主体类型设置为云账号，信任主体名称选择当前云账号，单击确定。
在创建角色阶段，输入以下信息。
角色名称：AliyunCDNAccessingPrivateOSSRole
角色创建完成之后，在角色页面列表中单击AliyunCDNAccessingPrivateOSSRole，进入角色编辑页面。
在信任策略页签，单击编辑信任策略，输入以下信息之后单击确定。
{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": { "Service": [ "cdn.aliyuncs.com" ] } } ], "Version": "1" }
切换到权限管理页签，在授权页签中，单击新增授权。
资源范围：账号级别
授权主体：选择之前创建的AliyunCDNAccessingPrivateOSSRole
权限策略：选择自定义策略，选择之前创建的AliyunCDNAccessingPrivateOSSRolePolicy，单击确认新增授权。
确认新增授权之后，回到CDN控制台的回源配置页面，可以看到阿里云OSS私有Bucket回源功能已经完成授权，
开启阿里云OSS私有Bucket回源并配置回源类型。
找到阿里云OSS私有Bucket回源区域，打开其开关。
在弹出的阿里云OSS私有Bucket回源对话框中，选择回源类型，单击确定。
