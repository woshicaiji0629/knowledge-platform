如果已在阿里云数字证书管理服务购买了证书，选择云盾（SSL）证书中心中选择已购买的证书。
如果无法选择已购买的证书，请检查已购买证书绑定的域名和加速域名是否相同。如果使用的是第三方服务商签发的证书，选择自定义上传（证书+私钥）后，上传证书（公钥），该证书将保存至阿里云数字证书管理服务。可前往我的证书查看。
授权 CDN 访问私有 Bucket
如果 OSS Bucket 为私有权限，则必须完成以下授权，否则所有回源请求都将因无权限而失败。
前往阿里云 CDN 控制台的域名管理列表，点击之前添加的域名，进入域名配置页面。
在回源配置中打开阿里云OSS私有Bucket回源，然后选择同账号回源。如果涉及到跨账号回源，请参考[OSS](../user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[私有](../user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[Bucket](../user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[回源](../user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)进行配置。
配置 URL 鉴权
URL 鉴权（也称时间戳防盗链）通过为访问 URL 添加签名和过期时间，防止资源被恶意盗用。
前往阿里云 CDN 控制台的域名管理列表，点击之前添加的域名，进入域名配置页面。
在访问控制页签中，选择URL鉴权，点击修改配置。
在配置页中，选择A方式，设置一个主KEY和一个备KEY（主、备KEY至少要填写一个），并妥善保管。这些密钥将用于在服务端验证带有签名的 URL，使用示例请参考[鉴权方式](../user-guide/type-a-signing.md)[A](../user-guide/type-a-signing.md)[说明](../user-guide/type-a-signing.md)。
根据业务需求设置鉴权 URL 的有效时间，例如 1800 秒。
配置用量封顶
为防止域名被攻击或盗刷产生突发高带宽导致高额账单，可通过用量封顶控制用户访问该域名的带宽、流量、HTTPS 请求数上限值，减少因突发流量导致的损失。
在往阿里云 CDN 控制台域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击流量限制。
在用量封顶页签中，参考[功能介绍](../user-guide/config
