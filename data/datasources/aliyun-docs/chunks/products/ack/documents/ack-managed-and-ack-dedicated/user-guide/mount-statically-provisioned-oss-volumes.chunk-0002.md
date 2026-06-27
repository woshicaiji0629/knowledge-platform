## 步骤一：选择鉴权方式（RRSA或AccessKey）并准备访问凭证
为确保集群能够安全、合规地访问OSS Bucket资源，需先配置一种鉴权机制。
[RRSA](mount-statically-provisioned-oss-volumes.md)[鉴权方式](mount-statically-provisioned-oss-volumes.md)：为 Pod 动态授予临时、自动轮换的 RAM 角色，实现应用级别的精细化权限隔离，安全性较高。
[AccessKey](mount-statically-provisioned-oss-volumes.md)[鉴权方式](mount-statically-provisioned-oss-volumes.md)：将静态、长期的密钥存储在 Secret 中。配置简单，但安全性较低。
重要
在1.26及以上版本的集群中，为避免因AccessKey轮转导致的ossfs重挂载和业务重启，建议使用RRSA鉴权方式。
本示例中集群与[OSS Bucket](../../../../oss/documents/user-guide/create-a-bucket-4.md)处于同一阿里云账号下。如需[跨账号挂载](faq-about-oss-volumes-1.md)[OSS Bucket](faq-about-oss-volumes-1.md)，建议使用RRSA鉴权方式。
