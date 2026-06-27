## 方式二：自定义策略精细化授权
权限管理员需具备以下能力：
查看其他RAM身份信息
查看集群列表和详情
查看集群已有的RBAC配置
在集群中执行RBAC授权操作
请登录[RAM](https://ram.console.aliyun.com/)[管理控制台](https://ram.console.aliyun.com/)，参考以下代码示例，为目标RAM用户或角色授予所需的RAM权限。具体操作，请参见[使用自定义策略授权](create-a-custom-ram-policy.md)。
{ "Statement": [{ "Action": [ "ram:Get*", "ram:List*", "cs:Get*", "cs:Describe*", "cs:List*", "cs:GrantPermission" ], "Resource": "*", "Effect": "Allow" } ], "Version": "1" }
2. 获得RBAC管理员权限
使用阿里云账号登录[容器服务管理控制台](https://cs.console.aliyun.com/)，为目标RAM用户或角色在集群维度授予预置角色管理员。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择授权管理。
在授权管理页面配置管理权限。
为RAM用户授权：单击RAM 用户页签，定位目标 RAM 用户，单击操作列的管理权限，进入权限管理页面。
为RAM角色授权：单击RAM 角色页签，定位目标 RAM 角色，单击管理权限，进入权限管理页面。
单击+添加权限，按照页面提示添加集群和命名空间级别的权限配置，选择预置角色为管理员。
如果在所有集群维度进行授权，权限管理员的身份将自动应用到未来新建的集群，无需重复授权。
