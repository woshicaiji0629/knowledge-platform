# OSS各地域的外网、内网、双栈Endpoint访问地址-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints

# 地域和Endpoint
OSS在全球多个地域部署服务，每个地域提供外网、内网和双栈等不同类型的Endpoint。以下表格列出各地域对应的Endpoint和内网VIP网段，供快速查阅。如需了解各Endpoint类型的适用场景和使用方式，请参见[通过](access-oss-via-bucket-domain-name.md)[Endpoint](access-oss-via-bucket-domain-name.md)[和](access-oss-via-bucket-domain-name.md)[Bucket](access-oss-via-bucket-domain-name.md)[域名访问](access-oss-via-bucket-domain-name.md)[OSS](access-oss-via-bucket-domain-name.md)。
重要
通过OSS提供的访问域名访问HTML、图片等文件时，浏览器会强制下载而非在线预览。如需实现文件预览功能，请[通过自定义域名访问](access-buckets-via-custom-domain-names.md)[OSS](access-buckets-via-custom-domain-names.md)。
## 公共云
适用于大多数业务场景，覆盖全球多个地域。
### 亚太-中国
| 地域 | 地域 ID | 外网 Endpoint | 内网 Endpoint | 双栈 Endpoint | 内网 VIP 网段 |
| --- | --- | --- | --- | --- | --- |
| 华东 1（杭州） | cn-hangzhou | oss-cn-hangzhou.aliyuncs.com | oss-cn-hangzhou-internal.aliyuncs.com | cn-hangzhou.oss.aliyuncs.com | 100.118.28.0/24 100.114.102.0/24 100.98.170.0/24 100.118.31.0/24 |
| 华东 2（上海） | cn-shanghai | oss-cn-shanghai.aliyuncs.com | oss-cn-shanghai-internal.aliyuncs.com | cn-shanghai.oss.aliyuncs.com | 100.98.35.0/24 100.98.110.0/24 100.98.169.0/24 100.118.102.0/24 |
| 华东 5 （南京-本地地域-关停中） | cn-nanjing | oss-cn-nanjing.aliyuncs.com | oss-cn-nanjing-internal.aliyuncs.com | 不支持 | 100.114.142.0/24 |
| 华东 6（福州-本地地域-关停中） | cn-fuzhou | oss-cn-fuzhou.aliyuncs.com | oss-cn-fuzhou-internal.aliyuncs.com | 不支持 | 100.115.21.0/24 |
| 华中 1（武汉-本地地域） | cn-wuhan-lr | oss-cn-wuhan-lr.aliyuncs.com | oss-cn-wuhan-lr-internal.aliyuncs.com | 不支持 | 100.115.89.0/24 |
| 华北 1（青岛） | cn-qingdao | oss-cn-qingdao.aliyuncs.com | oss-cn-qingdao-internal.aliyuncs.com | cn-qingdao.oss.aliyuncs.com | 100.115.173.0/24 100.99.113.0/24 100.99.114.0/24 100.99.115.0/24 |
| 华北 2（北京） | cn-beijing | oss-cn-beijing.aliyuncs.com | oss-cn-beijing-internal.aliyuncs.com | cn-beijing.oss.aliyuncs.com | 100.118.58.0/24 100.118.167.0/24 100.118.170.0/24 100.118.171.0/24 100.118.172.0/24 100.118.173.0/24 |
| 华北 3（张家口） | cn-zhangjiakou | oss-cn-zhangjiakou.aliyuncs.com | oss-cn-zhangjiakou-internal.aliyuncs.com | cn-zhangjiakou.oss.aliyuncs.com | 100.118.90.0/24 100.98.159.0/24 100.114.0.0/24 100.114.1.0/24 |
| 华北 5（呼和浩特） | cn-huhehaote | oss-cn-huhehaote.aliyuncs.com | oss-cn-huhehaote-internal.aliyuncs.com | cn-huhehaote.oss.aliyuncs.com | 100.118.195.0/24 100.99.110.0/24 100.99.111.0/24 100.99.112.0/24 |
| 华北 6（乌兰察布） | cn-wulanchabu | oss-cn-wulanchabu.aliyuncs.com | oss-cn-wulanchabu-internal.aliyuncs.com | cn-wulanchabu.oss.aliyuncs.com | 100.114.11.0/24 100.114.12.0/24 100.114.100.0/24 100.118.214.0/24 |
| 华南 1（深圳） | cn-shenzhen | oss-cn-shenzhen.aliyuncs.com | oss-cn-shenzhen-internal.aliyuncs.com | cn-shenzhen.oss.aliyuncs.com | 100.118.78.0/24 100.118.203.0/24 100.118.204.0/24 100.118.217.0/24 |
| 华南 2（河源） | cn-heyuan | oss-cn-heyuan.aliyuncs.com | oss-cn-heyuan-internal.aliyuncs.com | cn-heyuan.oss.aliyuncs.com | 100.98.83.0/24 100.118.174.0/24 |
| 华南 3（广州） | cn-guangzhou | oss-cn-guangzhou.aliyuncs.com | oss-cn-guangzhou-internal.aliyuncs.com | cn-guangzhou.oss.aliyuncs.com | 100.115.33.0/24 100.114.101.0/24 |
| 西南 1（成都） | cn-chengdu | oss-cn-chengdu.aliyuncs.com | oss-cn-chengdu-internal.aliyuncs.com | cn-chengdu.oss.aliyuncs.com | 100.115.155.0/24 100.99.107.0/24 100.99.108.0/24 100.99.109.0/24 |
| 西北 2（中卫） | cn-zhongwei | oss-cn-zhongwei.aliyuncs.com | oss-cn-zhongwei-internal.aliyuncs.com | 不支持 | 100.115.157.0/27 |
| 中国香港 | cn-hongkong | oss-cn-hongkong.aliyuncs.com | oss-cn-hongkong-internal.aliyuncs.com | cn-hongkong.oss.aliyuncs.com | 100.115.61.0/24 100.99.103.0/24 100.99.104.0/24 100.99.106.0/24 |
| [无地域属性](region-attribute-of-buckets.md) | rg-china-mainland | oss-rg-china-mainland.aliyuncs.com | 不支持 | 不支持 | 不支持 |
### 亚太-其他
| 地域 | 地域 ID | 外网 Endpoint | 内网 Endpoint | 双栈 Endpoint | 内网 VIP 网段 |
| --- | --- | --- | --- | --- | --- |
| 日本（东京） | ap-northeast-1 | oss-ap-northeast-1.aliyuncs.com | oss-ap-northeast-1-internal.aliyuncs.com | 不支持 | 100.114.211.0/24 100.114.114.0/25 |
| 韩国（首尔） | ap-northeast-2 | oss-ap-northeast-2.aliyuncs.com | oss-ap-northeast-2-internal.aliyuncs.com | 不支持 | 100.99.119.0/24 |
| 新加坡 | ap-southeast-1 | oss-ap-southeast-1.aliyuncs.com | oss-ap-southeast-1-internal.aliyuncs.com | 不支持 | 100.118.219.0/24 100.99.213.0/24 100.99.116.0/24 100.99.117.0/24 |
| 马来西亚（吉隆坡） | ap-southeast-3 | oss-ap-southeast-3.aliyuncs.com | oss-ap-southeast-3-internal.aliyuncs.com | 不支持 | 100.118.165.0/24 100.99.125.0/24 100.99.130.0/24 100.99.131.0/24 |
| 印度尼西亚（雅加达） | ap-southeast-5 | oss-ap-southeast-5.aliyuncs.com | oss-ap-southeast-5-internal.aliyuncs.com | 不支持 | 100.114.98.0/24 |
| 菲律宾（马尼拉） | ap-southeast-6 | oss-ap-southeast-6.aliyuncs.com | oss-ap-southeast-6-internal.aliyuncs.com | 不支持 | 100.115.16.0/24 |
| 泰国（曼谷） | ap-southeast-7 | oss-ap-southeast-7.aliyuncs.com | oss-ap-southeast-7-internal.aliyuncs.com | 不支持 | 100.98.249.0/24 |
| 马来西亚（柔佛州） | ap-southeast-8 | oss-ap-southeast-8.aliyuncs.com | oss-ap-southeast-8-internal.aliyuncs.com | 不支持 | 100.115.157.0/27 |
### 欧洲与美洲
| 地域 | 地域 ID | 外网 Endpoint | 内网 Endpoint | 双栈 Endpoint | 内网 VIP 网段 |
| --- | --- | --- | --- | --- | --- |
| 德国（法兰克福） | eu-central-1 | oss-eu-central-1.aliyuncs.com | oss-eu-central-1-internal.aliyuncs.com | eu-central-1.oss.aliyuncs.com | 100.115.154.0/24 |
| 英国（伦敦） | eu-west-1 | oss-eu-west-1.aliyuncs.com | oss-eu-west-1-internal.aliyuncs.com | 不支持 | 100.114.114.128/25 |
| 美国（硅谷） | us-west-1 | oss-us-west-1.aliyuncs.com | oss-us-west-1-internal.aliyuncs.com | 不支持 | 100.115.107.0/24 |
| 美国（弗吉尼亚） | us-east-1 | oss-us-east-1.aliyuncs.com | oss-us-east-1-internal.aliyuncs.com | 不支持 | 100.115.60.0/24 100.99.100.0/24 100.99.101.0/24 100.99.102.0/24 |
| 墨西哥 | na-south-1 | oss-na-south-1.aliyuncs.com | oss-na-south-1-internal.aliyuncs.com | 不支持 | 100.115.112.0/27 |
| 法国（巴黎） | eu-west-2 | oss-eu-west-2.aliyuncs.com | oss-eu-west-2-internal.aliyuncs.com | 不支持 | 100.115.159.0/27 |
### 中东
| 地域 | 地域 ID | 外网 Endpoint | 内网 Endpoint | 双栈 Endpoint | 内网 VIP 网段 |
| --- | --- | --- | --- | --- | --- |
| 阿联酋（迪拜） | me-east-1 | oss-me-east-1.aliyuncs.com | oss-me-east-1-internal.aliyuncs.com | 不支持 | 100.99.235.0/24 |
## 金融云
适用于金融行业合规场景。金融云环境默认仅支持内网访问，如需从金融云环境外部访问OSS，使用下表中的外网Endpoint。
### 内网环境
| 地域 | 地域 ID | 内网 Endpoint | 内网 VIP 网段 |
| --- | --- | --- | --- |
| 华东 1 金融云 | cn-hangzhou-finance | oss-cn-hzjbp-a-internal.aliyuncs.com oss-cn-hzjbp-b-internal.aliyuncs.com | 100.103.4.210/32 100.115.6.0/24 |
| 华东 2 金融云 | cn-shanghai-finance-1 | oss-cn-shanghai-finance-1-internal.aliyuncs.com | 100.115.105.0/24 100.100.36.8/32 |
| 华南 1 金融云 | cn-shenzhen-finance-1 | oss-cn-shenzhen-finance-1-internal.aliyuncs.com | 100.112.15.0/24 |
| 华北 2 金融云（邀测） | cn-beijing-finance-1 | oss-cn-beijing-finance-1-internal.aliyuncs.com | 100.112.52.0/24 |
### 外网环境
| 地域 | 地域 ID | 外网 Endpoint | 内网 Endpoint | 双栈 Endpoint | 内网 VIP 网段 |
| --- | --- | --- | --- | --- | --- |
| 杭州金融云外网 | cn-hangzhou-finance | oss-cn-hzfinance.aliyuncs.com | oss-cn-hzfinance-internal.aliyuncs.com | cn-hangzhou-finance.oss.aliyuncs.com | 100.103.4.95/32 100.103.5.142/32 100.103.5.143/32 100.103.5.144/32 100.115.6.0/24 |
| 上海金融云外网 | cn-shanghai-finance-1 | oss-cn-shanghai-finance-1-pub.aliyuncs.com | oss-cn-shanghai-finance-1-pub-internal.aliyuncs.com | cn-shanghai-finance.oss.aliyuncs.com | 100.100.36.24/32 100.100.36.8/32 |
| 深圳金融云外网 | cn-shenzhen-finance-1 | oss-cn-szfinance.aliyuncs.com | oss-cn-szfinance-internal.aliyuncs.com | cn-shenzhen-finance.oss.aliyuncs.com | 100.112.15.0/24 100.100.80.70/32 |
| 北京金融云外网 | cn-beijing-finance-1 | oss-cn-beijing-finance-1-pub.aliyuncs.com | oss-cn-beijing-finance-1-pub-internal.aliyuncs.com | 不支持 | 100.112.52.0/24 |
## 政务云
| 地域 | 地域 ID | 外网 Endpoint | 内网 Endpoint | 双栈 Endpoint | 内网 VIP 网段 |
| --- | --- | --- | --- | --- | --- |
| 华北 2 阿里政务云 1 | cn-north-2-gov-1 | oss-cn-north-2-gov-1.aliyuncs.com | oss-cn-north-2-gov-1-internal.aliyuncs.com | cn-north-2-gov-1.oss.aliyuncs.com | 不支持 |
## 常见问题
### 如何选择地域？
选择地域时建议综合考虑以下因素：
就近原则：选择与主要用户或应用程序距离最近的地域，可降低网络延迟，提升访问体验。
云产品互联：当其他云产品和OSS位于同一地域时，可通过内网互访，免除外网流量费用。
成本考虑：各地域的产品价格和优惠政策存在差异，详见[OSS](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)[产品定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)。
合规要求：不同地域或行业对数据合规性要求不同，需根据业务规范选择合适地域。
产品功能：新功能在发布初期通常在部分地域进行公测，如需使用最新功能，应在指定地域创建Bucket。详见[新功能发布记录](../release-notes.md)。
可通过curl命令测试本地网络到不同地域OSS Endpoint的访问延迟，辅助选择决策。较低的time_connect和time_starttransfer值通常表示更好的网络质量。
curl -o /dev/null -s -w "Connect: %{time_connect}s\nStart Transfer: %{time_starttransfer}s\nTotal: %{time_total}s\n" "https://oss-<region-id>.aliyuncs.com"
### 海外地域名称在不同页面中显示不一致？
部分海外地域名称在OSS产品定价页面和资源包购买页面中可能存在表述差异，但均指向相同的物理地理位置。例如，美国（硅谷）地域在不同页面中可能显示为美西1或美西，更多信息请参见[OSS](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)[产品定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)或[购买资源包](https://common-buy.aliyun.com/?spm=5176.7933691.1309819..68b22a66FQKm7f&commodityCode=ossbag&request=%7B%22region%22%3A%22china-common%22%7D#/buy)。
### 跨境访问 OSS 时出现延迟或连接不稳定怎么办？
跨境远距离传输（例如从中国内地访问中国香港或者新加坡节点）需经过长距离公共互联网链路及多个运营商互联节点，受物理距离、路由复杂性及公网拥塞等客观因素影响，访问可能出现延迟较高或连接不稳定的情况。
核心建议：遵循“就近部署”原则
同地域部署（首选方案）：请将您的业务应用（如 ECS、容器服务）与对象存储 Bucket 规划在同一地域。在同地域内，流量通过阿里云高速内网交互，不受公网及跨境链路影响。
避免非必要跨境直连：对于核心生产业务，请尽量避免通过公共互联网进行长距离的跨境直接读写。将业务整体迁移至数据存储所在的区域，是从架构根源上消除网络波动的最有效手段。
解决方案：使用传输加速
若您因全球业务分发、异地容灾备份等场景，确实存在不可避免的少量跨境远距离访问需求，这 部分 访问建议您使用阿里云 OSS 传输加速（Transfer Acceleration）功能。详情请参见[通过传输加速访问](transfer-acceleration.md)[OSS](transfer-acceleration.md)。
## 相关文档
[访问域名与网络连接概述](access-and-network-overview.md)
[通过](access-oss-via-bucket-domain-name.md)[Endpoint](access-oss-via-bucket-domain-name.md)[和](access-oss-via-bucket-domain-name.md)[Bucket](access-oss-via-bucket-domain-name.md)[域名访问](access-oss-via-bucket-domain-name.md)[OSS](access-oss-via-bucket-domain-name.md)
[通过传输加速访问](transfer-acceleration.md)[OSS](transfer-acceleration.md)
[无地域属性](region-attribute-of-buckets.md)[Bucket](region-attribute-of-buckets.md)
[使用限制及性能指标](limits.md)
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
