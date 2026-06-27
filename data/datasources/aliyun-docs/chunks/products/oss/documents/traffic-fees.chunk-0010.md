恶意行为，请执行[步骤](traffic-fees.md)[3](traffic-fees.md)检查相关配置。
如果发现多个IP地址访问不同对象，可能是内容被大规模分发（如社交媒体传播），请执行[步骤](traffic-fees.md)[4](traffic-fees.md)配置CDN加速访问OSS。
检查相关配置。

| 配置项 | 风险说明 | 解决方法 |
| --- | --- | --- |
| Bucket ACL 设置了公共读或公共读写 | 任何人（包括匿名访问者）都可以对该 Bucket 中的文件进行读操作，从而产生大量的下行流量费用。 | 将 Bucket ACL 设置为私有。设置为私有后，所有不带签名或者没有权限的请求都会失败。 具体步骤，请参见 [Bucket ACL](user-guide/bucket-acl-2.md) 。 |
| 高频访问的文件 ACL 设置了公共读或者公共读写 | 任何人（包括匿名访问者）都可以对该文件进行读操作，从而产生大量的下行流量费用。 | 将 Object ACL 设置为私有。具体步骤，请参见 [Object ACL](user-guide/object-acl.md) 。 完成以上配置后，用户需要通过预签名 URL 在指定有效期内才能访问该文件。 |
| Bucket Policy 没有对允许访问 Bucket 的 IP 地址进行限制 | 如果某些未知来源的 IP 地址频繁请求特定对象，也会产生大量的下行流量费用。 | 通过 Bucket Policy 限制 [步骤](traffic-fees.md) [1](traffic-fees.md) 查询到的未知来源的热门访问 IP 地址访问 Bucket。 具体步骤，请参见 [通过](user-guide/use-bucket-policy-to-grant-permission-to-access-oss.md) [Bucket Policy](user-guide/use-bucket-policy-to-grant-permission-to-access-oss.md) [授权访问](user-guide/use-bucket-policy-to-grant-permission-to-access-oss.md) [OSS](user-guide/use-bucket-policy-to-grant-permission-to-access-oss.md) 。 |
| 没有配置 Referer 防盗链来阻止其他网站引用 OSS 文件 | 其他网站可以通过直接引用 OSS 文件的 URL（如图片、视频等），将流量压力转移到您的 OSS 上。这会导致您的 OSS 下行流量激增，产生高额的带宽费用。 | 通过配置防盗链黑名单 Referer 的方式限制 [步骤](traffic-fees.md) [1](traffic-fees.md) 查询到恶意 Referer 访问 OSS，同时允许对访问来源设置白名单的机制，避免 OSS 资源被其他人盗用。具体步骤，请参见 [防盗链](user-guide/hotlink-protection.md) 。 |
