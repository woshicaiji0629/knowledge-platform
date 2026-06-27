## 创建并授权服务角色
OSS 清单服务需要通过扮演 RAM 角色来获得读取源 Bucket和写入目标 Bucket的权限。为确保账户安全，建议遵循最小权限原则，为清单功能创建专用的服务角色。
通过控制台快速配置清单时，系统会引导自动创建名为AliyunOSSRole的角色，可直接使用默认角色，无需自行创建服务角色。但此角色拥有对账户下所有 Bucket 的完全管理权限，不建议在生产环境中使用AliyunOSSRole。
以下是手动创建最小权限角色的步骤：
（可选）为RAM 用户授予配置清单的权限
阿里云账号默认拥有全部权限，可跳过此步骤。
此步骤旨在授权 RAM 用户（例如运维管理员）去配置清单规则，而不是为清单服务本身授权。为遵循安全最佳实践，推荐由阿里云账号或具备高权限的管理员预先创建好清单服务所需的 RAM 角色。然后，普通 RAM 用户在配置清单时，只需被授予使用该角色的权限即可，无需自行创建角色。
如果需要授予 RAM 用户创建和管理清单规则的权限，请[为其授予](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)包含以下权限的自定义策略：
以下策略中的oss:ListBuckets权限仅在通过控制台操作时需要。如果通过 SDK 或 ossutil 等工具访问，则无需此权限。{ "Statement": [ { "Effect": "Allow", "Action": [ "oss:PutBucketInventory", "oss:GetBucketInventory", "oss:DeleteBucketInventory", "oss:ListBuckets", "ram:CreateRole", "ram:AttachPolicyToRole", "ram:GetRole", "ram:ListPoliciesForRole" ], "Resource": "*" } ], "Version": "1" }
提示：如果当前 RAM 用户已拥有AliyunOSSFullAccess系统权限，则仅需为其补充授予角色管理的相关权限即可：
{ "Statement": [ { "Effect": "Allow", "Action": [ "ram:CreateRole", "ram:AttachPolicyToRole", "ram:GetRole", "ram:ListPoliciesForRole" ], "Resource": "*" } ], "Version": "1" }
创建RAM角色：进入[创建](https://ram.console.aliyun.com/roles/create)[RAM](https://ram.console.a
