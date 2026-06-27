| 功能集 | 功能 | 功能描述 | 参考文档 |
| --- | --- | --- | --- |
| 访问控制 | Bucket ACL | 当您希望粗粒度地控制某个 Bucket 的读写权限，即 Bucket 内的所有 Object 均为统一的读写权限时，您可以选择使用 Bucket ACL 的方式。Bucket ACL 包含公共读、公共读写和私有。您可以在创建 Bucket 时设置 Bucket ACL，也可以在创建 Bucket 后根据自身的业务需求修改 Bucket ACL。 | [Bucket ACL](bucket-acl-2.md) |
| Object ACL | 当您希望针对 Bucket 中的某个具体的 Object 设置特定的读写权限时，可以使用 Object ACL。通过设置 Object ACL，可以精确控制某个 Object 的访问权限，且不影响 Bucket 中其他 Object 的访问权限。Object ACL 包含公共读、公共读写、私有。您可以在上传 Object 时设置 ACL，也可以在 Object 上传后根据自己的业务需求随时修改 ACL。 | [Object ACL](object-acl.md) |  |
| Bucket Policy | OSS 支持面向资源的授权方式，允许在 Bucket 级别而不是用户级别设置权限策略。使用 Bucket Policy 可以授权当前云账号或者其他阿里云账号下单个或多个 RAM 用户、RAM 角色等访问 Bucket 内的指定资源。Bucket Policy 除提供策略语法的授权方式以外，还提供了图形化界面的授权方式，助力您结合业务场景，快速完成授权。 | [Bucket Policy](use-bucket-policy-to-grant-permission-to-access-oss.md) |  |
| 防盗链 | 通过在 OSS 中配置基于请求标头 Referer 的访问规则，可以阻止某些 Referer 访问您的 OSS 文件，从而防止其他网站盗用您的文件，并避免由此引起的不必要的流量费用增加。 | [防盗链](hotlink-protection.md) |  |
| 跨域资源共享 CORS | 默认情况下，由于同源策略（Same-Origin Policy）的限制，网页浏览器在执行 JavaScript 时会限制跨域请求，只允许请求同一域或源的资源。跨域资源共享 CORS（Cross-Origin Resource Sharing）简称跨域访问，允许网页浏览器向不同域或源的服务器发起跨域请求。通过跨域设置可以实现在您的网站上使用 JavaScript 请求非同源的 OSS 对象链接而不会出现跨域问题。 | [跨域资源共享](configure-cross
