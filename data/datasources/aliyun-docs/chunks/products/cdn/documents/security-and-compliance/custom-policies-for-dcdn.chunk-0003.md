## 常见自定义权限策略场景及示例
示例1：刷新预热权限
该权限策略通过授予RAM用户刷新和预热接口的权限，使被授权的RAM用户拥有刷新预热功能的权限，可进行刷新预热配置。
{ "Version": "1", "Statement": [ { "Action": [ "cdn:PushObjectCache", "cdn:RefreshObjectCaches", "cdn:DescribeRefreshTasks", "cdn:DescribeRefreshQuota" ], "Resource": "acs:cdn:*:*:*", "Effect": "Allow" } ] }
示例2：限制RAM用户修改计费模式
{ "Statement": [ { "Action": "cdn:*", "Resource": "*", "Effect": "Allow" }, { "Action": [ "cdn:OpenCdnService", "cdn:ModifyCdnService" ], "Resource": "*", "Effect": "Deny" }, { "Action": "ram:CreateServiceLinkedRole", "Resource": "*", "Effect": "Allow", "Condition": { "StringEquals": { "ram:ServiceName": [ "cdn-waf.cdn.aliyuncs.com", "cdn-ddos.cdn.aliyuncs.com" ] } } } ], "Version": "1" }
