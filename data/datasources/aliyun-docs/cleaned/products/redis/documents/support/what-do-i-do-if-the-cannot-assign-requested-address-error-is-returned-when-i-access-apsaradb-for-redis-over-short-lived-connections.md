# 解决因短连接导致的“Cannot assign requested address”报错-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/support/what-do-i-do-if-the-cannot-assign-requested-address-error-is-returned-when-i-access-apsaradb-for-redis-over-short-lived-connections

# Cannot assign requested address报错
本文介绍当客户端通过短连接访问云数据库 Tair（兼容 Redis）实例时，报错Cannot assign requested address的解决方案。
## 问题原因
该报错通常出现在客户端使用PHP-FPM与PhpRedis组合的架构中，这种架构在高并发场景时，处于TIME-WAIT状态下的TCP连接数较多，客户端无法分配出新的端口，则会出现Cannot assign requested address报错。
## 解决方案
### 使用Pconnect替换Connect（推荐）
用长连接替代短连接，该方案可减少TCP连接，同时可以避免每次请求都会重新建立连接的问题，减少延时。
例如Connect连接代码示例如下：
$redis->connect('[$Hostname]', [$Port]); $redis->auth('[$Inst_Password]');
参数说明：[$Hostname]、[$Port]和[$Inst_Password]分别为Redis实例的连接地址、端口号和密码，如何查看请参见[查看连接地址](../user-guide/view-endpoints.md)。
使用Pconnect替换Connect，即使用Persistent Connection的方式连接，示例如下：
$redis->pconnect('[$Hostname]', [$Port], 0, NULL, 0, 0, ['auth' => ['[$Inst_Password]']]); // 若PhpRedis版本大于等于5.3.0，建议使用Pconnect初始化方式，避免断连时出现no auth。 // timeout、persistent_id、retry_interval和read_timeout等参数根据业务实现情况修改。
### 修改客户端所在ECS实例的tcp_max_tw_buckets内核参数
对于一些特定场景，例如业务代码牵涉过多组件不易变更等，您可以使用此方案，快速实现高可用。
此方案将直接修改tcp_max_tw_buckets参数，但如果服务端因为重传对应五元组仍然处于LAST-ACK状态时，建立连接会失败。因此，更推荐您使用Pconnect连接方式的方案。
登录客户端所在ECS实例。
执行以下命令，查看ip_local_port_range和tcp_max_tw_buckets参数。
sysctl net.ipv4.tcp_max_tw_buckets net.ipv4.ip_local_port_range
预计返回示例如下。
net.ipv4.tcp_max_tw_buckets = 262144 net.ipv4.ip_local_port_range = 32768 61000
执行以下命令，修改tcp_max_tw_buckets参数，确保tcp_max_tw_buckets的值比ip_local_port_range范围的起始值小。
例如本示例中，ipv4.ip_local_port_range的范围是32768~61000，需修改tcp_max_tw_buckets的值小于32768，示例如下：
sysctl -w net.ipv4.tcp_max_tw_buckets=10000
## 注意事项
由于tcp_tw_recycle已在Linux 4.12上被弃用，请忽略所有修改tcp_tw_recycle和tcp_tw_reuse的方案，这些方案对于使用了NAT或LVS的服务均不适用。
## 适用于
[云数据库 Tair（兼容 Redis）](../product-overview/what-is-apsaradb-for-redis.md)
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
