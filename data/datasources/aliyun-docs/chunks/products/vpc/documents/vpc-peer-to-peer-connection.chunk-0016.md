### 创建并授予策略
控制台
登录[RAM 控制台](https://ram.console.aliyun.com/)，在左侧导航栏选择权限管理>权限策略。
单击创建权限策略，在脚本编辑页签粘贴上方所选方案的策略，并替换其中的资源目录 ID、路径或账号 ID。
单击确定，填写策略名称再确定。
[将策略授权给目标 RAM 用户、用户组或角色](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
API
调用[CreatePolicy](../../ram/documents/developer-reference/api-ram-2015-05-01-createpolicy.md)创建自定义策略，将上方所选方案的策略作为PolicyDocument参数传入。
调用[AttachPolicyToUser](../../ram/documents/developer-reference/api-ram-2015-05-01-attachpolicytouser.md)、[AttachPolicyToGroup](../../ram/documents/developer-reference/api-ram-2015-05-01-attachpolicytogroup.md)或[AttachPolicyToRole](../../ram/documents/developer-reference/api-ram-2015-05-01-attachpolicytorole.md)将策略授予目标 RAM 用户、用户组或角色。
