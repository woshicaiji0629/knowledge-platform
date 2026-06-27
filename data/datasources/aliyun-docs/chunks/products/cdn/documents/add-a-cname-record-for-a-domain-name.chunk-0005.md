## 步骤二：配置CNAME域名解析
重要
对于同一个主机记录，CNAME记录与其他多种记录类型互斥。在添加CNAME记录前，必须删除该主机记录下任何已存在的A、AAAA、MX或TXT等记录，否则会导致CNAME记录添加失败或DNS解析失败。更多关于冲突和解决方法，请参见[解析记录冲突规则](https://help.aliyun.com/zh/dns/pubz-dns-record-conflict-rules)。
使用加速域名所在的阿里云账号，登录[云解析](https://dnsnext.console.aliyun.com/authoritative/domains)[DNS](https://dnsnext.console.aliyun.com/authoritative/domains)[控制台](https://dnsnext.console.aliyun.com/authoritative/domains)。
在公网权威解析页面，找到您的域名，在域名右侧单击解析设置。
单击添加记录。可以参考以下场景进行配置：
场景一：子域名（推荐）
这是最常见的场景。例如，配置一个www.example.com加速域名，使用该加速域名可以访问被加速的源站资源。

| 配置项 | 填写内容 | 说明 |
| --- | --- | --- |
| 记录类型 | CNAME | 固定选择 CNAME 类型 |
| 主机记录 | www | 填写域名的前缀部分。 |
| TTL 时间 | 10 分钟（推荐） | 解析记录的缓存时间，可以按需调整。 |
| 记录值 | 粘贴步骤一中获取的 CNAME 地址 | 确保地址完整，无任何修改。 |

场景二：根域名（例如example.com）
重要
根域名配置CNAME记录可能对根域名下MX记录（邮件服务器地址）产生影响，导致收不到邮件。如果您的根域名承载了邮件、认证、安全策略等关键服务，建议您使用场景一的子域名作为加速域名。

| 配置项 | 填写内容 | 说明 |
| --- | --- | --- |
| 记录类型 | CNAME | 固定选择 CNAME 类型 |
| 主机记录 | @ | 当使用根域名为加速域名时，主机记录为 @ 。 |
| TTL 时间 | 10 分钟（推荐） | 解析记录的缓存时间，可以按需调整。 |
| 记录值 | 粘贴步骤一中获取的 CNAME 地址 | 确保地址完整，无任何修改。 |
