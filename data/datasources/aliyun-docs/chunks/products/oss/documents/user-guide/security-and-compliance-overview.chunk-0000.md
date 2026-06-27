# 安全合规概述
阿里云对象存储OSS（Object Storage Service）具有丰富的安全防护能力，通过多项合规认证，支持服务端加密、客户端加密、防盗链白名单、细粒度权限管控等特性。OSS为您的云端数据安全进行全方位的保驾护航，并满足您企业数据的安全与合规要求。

| 项目 | 说明 |
| --- | --- |
| [数据加密](data-encryption.md) | OSS 支持客户端加密和服务端加密，并可设置 TLS 版本以提升基于 SSL/TLS 的 HTTPS 加密传输安全性，从而有效防止数据在云端的潜在安全风险。 |
| [数据一致性校验](data-verification.md) | OSS 支持多种数据一致性校验机制（如 ETag、CRC 校验），可确保数据在上传、下载及存储过程中的完整性，帮助用户检测和避免数据在传输、存储过程中出现的损坏或丢失问题。 |
| [内容检测](content-detection.md) | OSS 提供内容安全检测的功能，方便您检测存储的图片是否包含违规内容，例如图片内容是否涉黄、涉政、涉恐、涉暴等。OSS 还支持使用恶意文件检测功能，方便您检测存储的数据是否存在 WebShell 文件、勒索病毒、木马等恶意文件的风险。 |
| [OSS](oss-sandbox.md) [沙箱](oss-sandbox.md) | 如果您的 OSS Bucket 遭受攻击或者分享了非法内容，OSS 会自动将该 Bucket 切入沙箱，防止影响您其他 Bucket 的服务。 |
| [OSS](oss-ddos-protection.md) [高防](oss-ddos-protection.md) | OSS 高防（高防护能力）为对象存储业务提供 DDoS 攻击防护服务，有效抵御大流量恶意攻击，保障服务的可用性和数据安全。 |
| [合规认证](compliance-certifications.md) | OSS 通过 Cohasset Associates 审计认证、FINRA 4511、CFTC 1.31、ISO、BS10012、CSA STAR 等多项合规认证，能够满足您的多种合规要求。 |
| [SDK](sdk-compliance-guide.md) [合规使用指南](sdk-compliance-guide.md) | OSS 为帮助开发者更好地落实用户个⼈信息保护相关要求，避免因使用第三⽅SDK 的业务⽽出现侵害最终用户个人信息权益的行为，制定了合规使用说明，供开发者在接入【对象存储 SDK】服务时参照自查和合理配置，满足监管合规要求。 |

该文章对您有帮助吗？
反馈
