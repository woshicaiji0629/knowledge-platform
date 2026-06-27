### 控制台
确保[已开通资源目录并创建多账号体系](https://help.aliyun.com/zh/resource-management/resource-directory/getting-started/use-a-resource-directory-to-quickly-establish-a-structure-for-the-accounts-and-resources-of-an-enterprise)。
使用资源目录的管理账号，前往[资源管理-可信服务列表页](https://resourcemanager.console.aliyun.com/resource-directory/services)，单击IP地址管理操作列的管理，在委派管理员账号区域，添加资源目录的成员为 IPAM 委派管理员。
使用 IPAM 委派管理员账号[创建 IPAM](address-planning.md)后，可前往[IPAM - 多账号管理页面](https://ipam.console.aliyun.com/cn-hangzhou/member)添加成员。添加后，委派管理员即可使用资源发现查看 IPAM 生效地域中所有纳管成员账号下的 IP 地址使用情况。
资源发现更新频率为 5 分钟。IPAM 委派管理员纳管成员时，IPAM 会给纳管成员所包含的成员账号创建[服务关联角色](../../ram/documents/user-guide/service-linked-roles.md)，并配置以下权限策略。
为服务关联角色配置的权限策略
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ecs:DescribeNetworkInterfaces", "ecs:DescribeSecurityGroups", "vpc:DescribeEipAddresses", "vpc:DescribeHaVips", "vpc:DescribeIpv6Addresses", "vpc:DescribeVpcs", "vpc:DescribeVSwitches" ], "Resource": "*" }, { "Action": "ram:DeleteServiceLinkedRole", "Resource": "*", "Effect": "Allow", "Condition": { "StringEquals": { "ram:ServiceName": "vpcipam.vpc.aliyuncs.com" } } } ] }
