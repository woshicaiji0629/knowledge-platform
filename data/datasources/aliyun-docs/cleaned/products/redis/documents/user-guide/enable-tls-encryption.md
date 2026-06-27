# 开启TLS加密,有哪些注意事项和前提条件-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/enable-tls-encryption

# 开启TLS加密
云数据库 Tair（兼容 Redis）支持TLS（Transport Layer Security）加密协议，TLS协议具有比SSL（Secure Sockets Layer）协议更好的加密技术和更高级别的安全性，可进一步保障数据通信安全。
## 背景信息
TLS协议是SSL协议的升级版，当前已成为互联网加密通信的标准协议，在现代网络中被广泛使用。以下是TLS相对SSL的一些优势：
加密强度：TLS协议使用更强大的加密技术，例如AES（Advanced Encryption Standard）算法。
安全性：TLS协议采用更安全的算法和协议，例如SHA-2（Secure Hash Algorithm 2）算法。
兼容性：TLS协议是更现代化的协议，更加兼容现代浏览器和服务器，且支持更广泛的加密协议和密码套件。
安全更新：TLS协议支持实时升级加密算法和协议。
因此，若您希望在传输层对网络连接进行加密，推荐您使用更安全、更新的TLS加密功能（该功能默认关闭）。
## 前提条件
实例满足如下条件：
实例版本为Tair（企业版）内存型、持久内存型或Redis开源版5.0、6.0、7.0。
实例类型为高可用（双副本）。
若实例已申请公网连接地址，请释放公网连接地址，释放后才能开启TLS加密功能。
说明
若经典版集群架构实例已申请直连地址，也请释放直连地址。
## 注意事项
创建TLS连接需要经历多次握手过程，包括认证和密钥交换，这些步骤会占用显著的计算资源和时间，创建TLS连接的速度显著低于创建普通连接。在短时间内无法快速创建大量TLS连接，且频繁创建TLS连接会显著影响正常请求的延迟。因此，建议通过使用TLS长连接来减少这些开销，尽量避免频繁创建和销毁TLS连接，以降低对性能的影响。
建立TLS连接后，使用TLS连接传输数据，由于所有的数据都需要加密、解密，也会产生额外开销，这些额外开销会伴随传输内容大小增长。
说明
具体的性能影响因业务场景而异，需要进行实际测试来评估在特定业务环境下的影响程度。
开启TLS加密功能后，实例将不支持申请公网连接地址，同时经典版集群实例也无法申请直连地址，客户端只能通过专有网络、TLS加密方式连接实例。连接示例请参见[启用](use-a-client-to-connect-to-an-apsaradb-for-redis-instance-that-has-ssl-encryption-enabled.md)[TLS（SSL）加密连接实例](use-a-client-to-connect-to-an-apsaradb-for-redis-instance-that-has-ssl-encryption-enabled.md)。
开启TLS加密功能后，实例将不支持迁移可用区。
开启TLS加密功能后，若修改了实例的连接地址或端口号，请更新实例TLS证书，再进行连接。否则会报错No subject alternative DNS name matching xxx found。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击TLS（SSL）设置。
单击一键开通。
在弹出的对话框中，选择TLS版本。
参数说明：
TLSv1.3（默认推荐）：RFC8446，2018年发布，相比较TLSv1.2，TLSv1.3具有更快、更安全的特性。要求Redis引擎版本5.5及以上，Proxy小版本7.0.1及以上。若控制台无法选择TLSv1.3，请先升级实例小版本。
TLSv1.2：RFC5246，2008年发布，具有强大的加密技术，能提供更好的安全保护。
TLSv1.1：RFC4346，2006年发布，修复TLSv1.0若干漏洞。
TLSv1.0：RFC2246，1999年发布，基于SSLv3.0，该版本易受各种攻击（如BEAST和POODLE）。
单击确定。
警告
本操作将触发重启实例，实例会出现秒级的连接闪断，请在业务低峰期执行该操作并确保应用具备重连机制。
此时，您可以通过刷新控制台页面，更新TLS的开通状态。
开通TLS后，您可以单击页面中的下载CA证书，将CA证书导入至客户端中。下载的文件为压缩包，包含如下三个文件：
ApsaraDB-CA-Chain.p7b：用于Windows系统中导入CA证书。
ApsaraDB-CA-Chain.pem：用于其他系统（如Linux）或应用中导入CA证书。
ApsaraDB-CA-Chain.jks：Java中的truststore证书存储文件，用于Java程序中导入CA证书链。
不同实例下载的CA证书均相同，且证书文件没有密码，可以用于连接账号下所有Tair实例。
## 管理TLS加密设置
以下操作需要在实例已开通TLS加密后进行。
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击TLS（SSL）设置。
根据要执行的操作，选择下述操作步骤。
| 要执行的操作 | 操作说明 |
| --- | --- |
| 更新 CA 证书 | 单击页面中的 更新证书 ，然后单击 确定 。 开通 TLS 加密时，证书的默认有效期为 3 年，且不支持自定义有效期。在证书到期前 20 天，实例会发起主动运维，更新证书有效期。届时，您可以在 事件管理 > 计划内事件 中修改运维时间。或者您也可以随时单击 更新证书 ，更新后证书将重新获取 3 年有效期。 警告 本操作会使实例出现秒级的连接闪断，请在业务低峰期执行该操作并确保应用具备重连机制。 |
| 修改 TLS 版本 | 单击 TLS 版本 右侧的 图标，然后在下拉列表中选择要更换的 TLS 版本。推荐使用 TLSv1.3 版本。若控制台无法选择 TLSv1.3，请先升级实例小版本（要求 Redis 引擎版本 5.5 及以上，Proxy 小版本 7.0.1 及以上）。 说明 如果 TLS 最低版本 下拉列表处于不可用状态，请升级实例的小版本后重试，具体操作请参见 [升级小版本与代理版本](update-the-minor-version.md) 。 |
| 关闭 TLS 加密 | 关闭 TLS 状态 右侧的开关。 警告 本操作将触发重启实例，实例会出现秒级的连接闪断，请在业务低峰期执行该操作并确保应用具备重连机制。 |
更新证书或修改TLS版本后，无需重新下载证书文件，可继续使用。
## 相关API
| API | 说明 |
| --- | --- |
| [ModifyInstanceTLS(SSL)](../developer-reference/api-r-kvstore-2015-01-01-modifyinstancessl-redis.md) | 设置实例的 TLS（SSL）加密功能。 |
## 后续步骤
[启用](use-a-client-to-connect-to-an-apsaradb-for-redis-instance-that-has-ssl-encryption-enabled.md)[TLS（SSL）加密连接实例](use-a-client-to-connect-to-an-apsaradb-for-redis-instance-that-has-ssl-encryption-enabled.md)
## 常见问题
为什么我的实例无法开启TLS功能？
若实例为经典版读写分离架构实例，不支持开启TLS功能。
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
