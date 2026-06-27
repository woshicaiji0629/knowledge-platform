## VPC授权样例
示例1：对VPC的管理权限
假设您的账号为1234567，授权管理该账号下的所有VPC，使某个RAM用户具有操作所有VPC的权限。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "vpc:*" ], "Resource": [ "acs:vpc:*:1234567:*/*" ] }, { "Effect": "Allow", "Action": [ "ecs:*Describe*" ], "Resource": [ "*" ] } ] }
示例2：对VPC中vSwitch的管理授权
假设您只想授权青岛Region下的vSwitch的管理权限，使某个RAM用户可以对青岛Region下的vSwitch进行创建/删除/绑定子网路由/解绑子网路由的操作，对于其它地域的vSwitch只有查看权限。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "vpc:*Describe*", "vpc:*vSwitch*", "vpc:*RouteTable*" ], "Resource": [ "acs:vpc:cn-qingdao:*:*/*" ] }, { "Effect": "Allow", "Action": [ "ecs:*Describe*" ], "Resource": [ "acs:ecs:cn-qingdao:*:*/*" ] } ] }
示例3：只允许操作特定地域下的路由表以及路由表中的路由条目
假设您的账号为11111111，在多个地域创建了VPC，该权限只授予某个RAM用户对杭州地域VPC的操作权限，且操作权限仅限于：允许新增/删除路由条目，允许创建子网路由并绑定vSwitch，对于其它地域的云产品只有查看权限。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ecs:*Describe*" ], "Resource": [ "*" ], "Condition": { } }, { "Effect": "Allow", "Action": [ "slb:*Describe*" ], "Resource": [ "*" ], "Condition": { } }, { "Effect": "Allow", "Action": [ "rds:*Describe*" ], "Resource": [ "*" ], "Condition": { } }, { "Effect": "Allow", "Action": [ "vpc:*Describe*", "vpc:*RouteEntry*
