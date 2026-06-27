### 步骤一：创建自定义授权策略
使用RAM管理员登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
在左侧导航栏，选择权限管理>权限策略。
在权限策略页面，单击创建权限策略。
在创建权限策略页面，单击脚本编辑页签，输入权限策略内容。
请将YOUR_CLUSTER_ID替换为目标集群ID。{"Statement":[{"Action":["cs:Get*","cs:List*","cs:Describe*","cs:ScaleCluster","cs:DeleteCluster"],"Effect":"Allow","Resource":["acs:cs:*:*:cluster/YOUR_CLUSTER_ID"]}],"Version":"1"}

| 参数 | 说明 |
| --- | --- |
| Action | 所需授予的权限，所有的 Action 均支持通配符。 |
| Resource | 授予单集群权限 "Resource" : [ "acs:cs:*:*:cluster/ YOUR_CLUSTER_ID " ] 授予多个集群权限 "Resource" : [ "acs:cs:*:*:cluster/ YOUR_CLUSTER_ID_1 " , "acs:cs:*:*:cluster/ YOUR_CLUSTER_ID_2 " ] 授予所有集群的权限 "Resource": [ "*" ] |

在创建权限策略页面，单击确定。
在创建权限策略对话框，输入策略名称和备注，然后单击确定。
