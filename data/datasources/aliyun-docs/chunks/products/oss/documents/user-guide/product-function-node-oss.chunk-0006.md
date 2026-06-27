tc.md) |  |
| 定时备份 | 为了避免因误删除、误修改、误覆盖操作等情况引起的数据丢失或受损，您可以通过云备份对存储空间（Bucket）内的文件（Object）进行定期备份。当您的 Object 意外丢失时，可通过云备份进行恢复。云备份对支持配置灵活备份策略，将数据备份至云端，您可以随时查看和恢复数据。 | [定时备份](configure-scheduled-backup.md) |  |
| 安全合规 | 服务器端加密 | 当您在设置了服务器端加密的 Bucket 中上传 Object 时，OSS 对收到的文件进行加密，再将得到的加密文件持久化保存。当您通过 GetObject 请求下载文件时，OSS 自动将加密文件解密后返回给用户，并在响应头中返回 x-oss-server-side-encryption，用于声明该文件进行了服务器端加密。 | [服务器端加密](server-side-encryption-8.md) |
| 客户端加密 | OSS 客户端加密是在数据上传至 OSS 之前，由用户在本地对数据进行加密处理，确保只有密钥持有者才能解密数据，增强数据在传输和存储过程中的安全性。 | [客户端加密](client-side-encryption.md) |  |
| 合规保留策略 | OSS 保留策略具有 WORM（Write Once Read Many）特性，满足用户以不可删除、不可篡改方式保存和使用数据。如果您希望指定时间内任何用户（包括资源拥有者）均不能修改和删除 OSS 某个 Bucket 中的 Object，您可以选择为 Bucket 配置保留策略。在保留策略指定的 Object 保留时间到期之前，仅支持在 Bucket 中上传和读取 Object。Object 保留时间到期后允许修改或删除。 | [合规保留策略](oss-retention-policies.md) |  |
| 敏感数据保护 | 敏感数据保护是一款识别、分类、分级和保护 Bucket 中敏感数据的原生服务，可满足数据安全、个人信息保护等相关法规的合规要求。 | [敏感数据保护](sddp.md) |  |
| OSS 高防 | OSS 高防是 OSS 结合 DDoS 高防推出的 DDoS 攻击代理防护服务。当受保护的 Bucket 遭受大流量攻击时，OSS 高防会将攻击流量牵引至高防集群进行清洗，并将正常访问流量回源到目标 Bucket，确保业务的正常进行。 | [OSS](oss-ddos-protection.md) [高防](oss-ddos-protection.md) |  |
| 日志转存 | 访问 OSS 的过程中会产生大量的访问日志。您可以通过日志转存功能将这些日志按照固定命名规则，以小时为单位生成日志文件写入您指定的 Bucket
