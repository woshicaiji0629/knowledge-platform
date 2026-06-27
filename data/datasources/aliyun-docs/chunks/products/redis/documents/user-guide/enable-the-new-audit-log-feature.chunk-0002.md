## RAM用户权限限制
如使用阿里云账号（主账号），则可以忽略此说明。若RAM用户开通审计日志，需要具备日志服务的管理权限。
您可以为RAM用户授予系统权限策略AliyunLogFullAccess。授权后，RAM用户可以管理所有日志库（Logstore）。具体操作，请参见[授予权限](../../../ram/documents/grant-permissions-to-a-ram-user.md)。
您也可以自定义权限策略，限定RAM用户只能管理云数据库 Tair（兼容 Redis）实例的审计日志。
自定义权限策略示例
{ "Version": "1", "Statement": [ { "Action": "log:*", "Resource": "acs:log:*:*:project/nosql-*", "Effect": "Allow" } ] }
