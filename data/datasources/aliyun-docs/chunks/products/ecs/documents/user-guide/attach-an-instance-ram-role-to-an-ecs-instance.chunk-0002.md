### 步骤一：创建RAM角色
为ECS实例创建一个RAM角色，并为其分配权限。
控制台
登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)，选择身份管理 > 角色，单击创建角色，填写以下参数，单击确定。
信任主体类型：选择云服务。
信任主体名称：选择云服务器ECS / ECS。
在创建角色对话框，输入角色名称，然后单击确定。
创建成功的RAM角色默认没有任何权限，需要为该RAM角色授权。可将系统策略或已创建的[自定义权限策略](../../../ram/documents/create-a-custom-policy.md)授权给RAM角色，使其拥有相关的资源访问或操作权限。具体操作，请参见[管理](../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
API
调用[CreateRole](../../../ram/documents/developer-reference/api-ram-2015-05-01-createrole.md)接口创建RAM角色。
信任策略参数（AssumeRolePolicyDocument）：
{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": { "Service": [ "ecs.aliyuncs.com" ] } } ], "Version": "1" }
（可选）调用[CreatePolicy](../../../ram/documents/developer-reference/api-ram-2015-05-01-createpolicy.md)接口新建权限策略。如果已有可用权限策略，可跳过该步骤。PolicyDocument（权限策略）需按如下设置：
{ "Statement": [ { "Action": [ "oss:Get*", "oss:List*" ], "Effect": "Allow", "Resource": "*" } ], "Version": "1" }
调用[AttachPolicyToRole](../../../ram/documents/developer-reference/api-r
