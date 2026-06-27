# 配置SSL加密提升连接安全性-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/configure-ssl-encryption

# 设置SSL加密
为提高链路的安全性，您可以启用SSL（Secure Sockets Layer）加密，然后安装SSL CA证书到您的应用服务。SSL加密功能在传输层对网络连接进行加密，在提升通信数据安全性的同时，保证数据的完整性。
## 前提条件
实例部署模式为经典版。
实例版本为4.0或5.0。
实例架构类型为集群架构。
## 注意事项
2023年4月07日云数据库 Tair（兼容 Redis）将SSL加密功能升级为TLS加密功能，同时不再支持开通SSL加密功能。若您已开通SSL加密功能，您可以继续使用也可以关闭SSL，但关闭后无法再次开启，更多信息请参见[【通知】SSL](../product-overview/encryption-upgrade-from-ssl-to-tls.md)[功能升级至](../product-overview/encryption-upgrade-from-ssl-to-tls.md)[TLS](../product-overview/encryption-upgrade-from-ssl-to-tls.md)[功能](../product-overview/encryption-upgrade-from-ssl-to-tls.md)。
SSL的证书有效期为3年，请及时更新证书有效期并重新下载配置CA证书，否则使用加密连接的客户端程序将无法正常连接。
由于开通SSL加密会增加Tair（以及Redis开源版）服务的网络响应时间，建议仅在有加密需求时才开通SSL加密（例如通过公网连接实例）。
开通SSL后同时支持SSL和非SSL两种连接方式。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击TLS（SSL）设置。
根据要执行的操作，选择下述操作步骤。
| 要执行的操作 | 操作说明 |
| --- | --- |
| 开通或关闭 SSL 加密 | 打开或关闭 SSL 证书信息 右侧的开关。 |
| 更新 CA 证书 | 单击页面右上角的 更新证书 ，然后单击 确定 。 证书有效期为 3 年，您可以随时点击 更新证书 并重新下载配置 CA 证书，更新后，证书将重新获取 3 年有效期。 |
| 下载 CA 证书 | 单击页面右上角的 下载 CA 证书 。 |
警告
执行开通SSL加密和更新证书有效期的操作将触发重启实例动作。实例会出现秒级的连接闪断，请在业务低峰期执行该操作并确保应用具备重连机制。
## 常见问题
Q：出现“版本不支持”的错误提示怎么办？
A：您需要将实例的小版本升级至最新，具体操作请参见[升级小版本与代理版本](update-the-minor-version.md)。
Q：下载的CA证书有哪些文件？
A：下载的文件为压缩包，包含如下三个文件：
ApsaraDB-CA-Chain.p7b：用于Windows系统中导入CA证书。
ApsaraDB-CA-Chain.pem：用于其他系统（如Linux）或应用中导入CA证书。
ApsaraDB-CA-Chain.jks：Java中的truststore证书存储文件，用于Java程序中导入CA证书链。
## SSL连接方法参考
[通过](use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[redis-cli](use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[连接实例](use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)
[启用](use-a-client-to-connect-to-an-apsaradb-for-redis-instance-that-has-ssl-encryption-enabled.md)[TLS（SSL）加密连接实例](use-a-client-to-connect-to-an-apsaradb-for-redis-instance-that-has-ssl-encryption-enabled.md)
## 相关API
| API | 说明 |
| --- | --- |
| [ModifyInstanceSSL](../developer-reference/api-r-kvstore-2015-01-01-modifyinstancessl-redis.md) | 设置实例的 SSL 加密功能。 |
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
