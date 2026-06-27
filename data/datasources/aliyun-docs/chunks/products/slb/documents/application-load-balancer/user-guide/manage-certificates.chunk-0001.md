## 证书类型
ALB支持的证书类型包括国际标准证书（RSA/ECC）和国密证书（SM2）。
国际标准证书：支持RSA和ECC算法，适用于通用HTTPS加密场景。
国密证书：支持国密算法体系，包括 SM2（签名/密钥交换）、SM3（摘要）及 SM4（数据加密），适用于金融、政企及有等保三要求的行业客户。使用国密证书时，需要配合包含国密加密套件（ECC-SM2-WITH-SM4-SM3）的自定义TLS安全策略。
说明
国密证书功能默认不开放，用户可前往[配额中心](https://quotas.console.aliyun.com/white-list-products/alb/quotas)自主申请权益配额。
仅[ALB](../../product-overview/alb.md)[升级实例](../../product-overview/alb.md)支持国密证书，升级前的ALB实例不支持。可通过[ALB](../use-cases/quickly-copy-alb-configurations-by-cloning-an-alb-instance.md)[实例克隆](../use-cases/quickly-copy-alb-configurations-by-cloning-an-alb-instance.md)将存量ALB实例业务手动迁移至ALB升级实例。
仅标准版和WAF增强版ALB实例支持国密证书，基础版、扩展版不支持。
国密证书不支持双向认证（CA证书不支持SM2类型）。
不同监听类型、证书类型与认证方式的支持情况如下表所示：

| 监听类型 | 证书类型 | 证书认证方式 |  |
| --- | --- | --- | --- |
| 单向认证 | 双向认证 |  |  |
| HTTPS | RSA、ECC、SM2 单证书配置 | 支持 | 支持（RSA、ECC） 不支持（SM2） |
| RSA 和 ECC 双证书配置 | 支持 | 支持 |  |
| RSA 和 SM2 双证书配置 | 支持 | 不支持 |  |
| ECC 和 SM2 双证书配置 | 支持 | 不支持 |  |
| RSA、ECC、SM2 三证书混合配置 | 支持 | 不支持 |  |
| QUIC | RSA 和 ECC 单证书配置 | 支持 | 不支持 |
| RSA 和 ECC 双证书配置 | 支持 | 不支持 |  |
| HTTP | 不支持配置证书 |  |  |
