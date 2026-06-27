# 配置OCSP Stapling以提升证书验证速度-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-ocsp-stapling

# 配置OCSP Stapling
OCSP Stapling功能可实现由CDN预先缓存在线证书验证结果并下发给客户端，无需客户端直接向CA站点查询证书状态，从而减少证书验证时间，提升用户访问速度。
## 功能说明
OCSP（Online Certificate Status Protocol，在线证书状态协议）是由数字证书颁发机构CA（Certificate Authority）提供，客户端通过OCSP可实时验证证书的合法性和有效性。
未开启OCSP Stapling时：客户端的每次请求都会向CA进行OCSP查询，以确认证书未被吊销，频繁的OCSP查询请求导致TLS握手效率较低，将影响用户访问速度。
开启OCSP Stapling功能后，OCSP信息查询的工作将由CDN服务器完成。CDN通过低频次查询，将查询结果缓存到服务器中（默认缓存时间60分钟）。当客户端向服务器发起TLS握手请求时，CDN服务器将证书的OCSP信息和证书一起发送给客户端，无需再向数字证书认证机构（CA）发送查询请求。极大地提高了TLS握手效率，节省了证书验证时间。
重要
OCSP Stapling功能默认关闭。
OCSP Stapling功能默认缓存时间是1小时，缓存过期后第一个访问请求OCSP Stapling将不生效，直到重新获取OCSP Stapling信息为止。
配置了HTTPS加速的域名，可启用或者关闭OCSP Stapling功能，删除HTTPS证书配置后，OCSP Stapling功能会同步失效。
OCSP信息是无法伪造的，因此这一过程不会产生额外的安全问题。
## 前提条件
执行配置前，请您确保：
您已成功配置HTTPS证书，操作方法请参见[配置](configure-an-ssl-certificate.md)[HTTPS](configure-an-ssl-certificate.md)[证书](configure-an-ssl-certificate.md)。
客户端需支持OCSP扩展字段，如果客户端版本不支持OCSP扩展字段，则功能无法生效。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击HTTPS配置。
在OCSP Stapling区域，打开或关闭开关。开启后，CDN将预先缓存在线证书验证结果并下发给客户端，无需浏览器直接向CA站点查询证书状态，从而减少用户验证时间。
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
