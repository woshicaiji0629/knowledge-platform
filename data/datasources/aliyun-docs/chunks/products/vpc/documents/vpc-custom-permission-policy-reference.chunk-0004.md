"Effect": "Allow", "Action": [ "rds:*Describe*" ], "Resource": [ "*" ], "Condition": { } }, { "Effect": "Allow", "Action": [ "vpc:*Describe*", "vpc:*RouteEntry*", "vpc:*RouteTable*" ], "Resource": [ "acs:vpc:cn-hangzhou:11111111:*/*" ], "Condition": { } } ] }
示例4：只允许修改特定路由表中的路由条目
假设您只希望RAM用户新增/删除特定路由表中的路由条目。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "vpc:*RouteEntry*" ], "Resource": [ "acs:vpc:cn-qingdao:*:routetable/vtb-m5e64ujkb7xn5zlq0xxxx" ] }, { "Effect": "Allow", "Action": [ "vpc:*Describe*" ], "Resource": [ "*" ] }, { "Effect": "Allow", "Action": [ "ecs:*Describe*" ], "Resource": [ "*" ] } ] }
该文章对您有帮助吗？
反馈
