## 快速选择

| 场景 | 推荐方案 |
| --- | --- |
| 数据私有，阻止非授权用户和匿名访问 | [Bucket ACL](bucket-acl-2.md) 设为私有（默认配置） |
| 对外提供公开可读的静态资源 | [Bucket ACL](bucket-acl-2.md) 设为公共读，配合 [防盗链](hotlink-protection.md) 防止资源盗用 |
| 授权多个用户访问特定 Bucket | [Bucket Policy](use-bucket-policy-to-grant-permission-to-access-oss.md) ，仅需单条策略即可指定允许的用户列表 |
| 统一管理某个用户可访问的所有资源 | [RAM Policy](ram-policy.md) 绑定到该用户 |
| 将资源共享给其他阿里云账号 | [Bucket Policy](use-bucket-policy-to-grant-permission-to-access-oss.md) 或 [基于](cross-account-access-by-ram-role.md) [RAM](cross-account-access-by-ram-role.md) [角色实现跨账号访问](cross-account-access-by-ram-role.md) [OSS](cross-account-access-by-ram-role.md) |
| 同一 Bucket 为多个应用或团队提供差异化访问 | [接入点](access-point.md) ，每个应用或团队独立的入口和策略 |
| 防止误配置导致数据公开泄露 | [阻止公共访问](block-public-access.md) |
| 浏览器端 JavaScript 访问 OSS | [跨域设置](configure-cross-origin-resource-sharing.md) |
| 多账号场景下统一配置权限边界，例如强制开启阻止公共访问功能 | [Control Policy](control-policy.md) |
