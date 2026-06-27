Role", "ram:ListPoliciesForRole" ], "Resource": "*" } ], "Version": "1" }
创建RAM角色：进入[创建](https://ram.console.aliyun.com/roles/create)[RAM](https://ram.console.aliyun.com/roles/create)[角色](https://ram.console.aliyun.com/roles/create)页面。信任主体类型选择云服务，信任主体名称选择对象存储。
为RAM角色授予写入目标 Bucket 的权限：
在[创建权限策略](https://ram.console.aliyun.com/policies/create)页面，单击脚本编辑页签。将以下策略内容粘贴到策略编辑器中，并将dest-bucket替换为实际的源Bucket名称。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "oss:PutObject", "Resource": [ "acs:oss:*:*:dest-bucket/*" ] } ] }
（可选）配置 KMS 加密权限：如果清单报告需要使用 KMS 密钥加密，还需为该 RAM 角色授予AliyunKMSCryptoUserAccess权限或更精细的 KMS 相关权限。
在[授权](https://ram.console.aliyun.com/permissions)页面，单击新增授权，授权主体选择创建的RAM角色，权限策略选择刚创建的策略，然后单击确认新增授权。
记录角色ARN：在[角色](https://ram.console.aliyun.com/roles)页面找到创建RAM角色，进入基本信息页面，复制角色的ARN用于创建清单规则。格式为acs:ram::{源账号UID}:role/{角色名}。
