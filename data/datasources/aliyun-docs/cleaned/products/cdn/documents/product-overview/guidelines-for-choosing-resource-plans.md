# 如何选购CDN资源包-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/product-overview/guidelines-for-choosing-resource-plans

# 资源包选购
阿里云CDN为您提供各类资源包帮您节省使用成本。本文通过一个典型案例为您指引如何选购资源包。
## 选购指引
您可以通过业务所需服务、业务体量、以及加速区域，来选择出最适合您的资源包。
资源包购买：[点击购买](https://common-buy.aliyun.com/?spm=5176.7933777.J_3537169050.2.2429496ezmVFeY&commodityCode=dcdnpaybag#/buy)。
资源包对应服务的计费说明：[CDN](https://www.aliyun.com/price/product?spm=5176.7933777.J_3537169050.4.2de3496e3wdMkN#/cdn/detail/cdn)[定价详情](https://www.aliyun.com/price/product?spm=5176.7933777.J_3537169050.4.2de3496e3wdMkN#/cdn/detail/cdn)。
说明
如果您需要购买CDN下行流量资源包，计费方式请选择“按流量计费”。如果您目前不是“按流量计费”，可以根据需要变更计费方式，具体方法，请参见[变更计费方式](change-the-metering-method.md)。
## 资源包规格与区域说明
### 固定规格购买
CDN资源包仅提供固定规格，不支持自定义输入容量（如直接输入3T）。如需非标准容量（如3000 GB），需购买多个固定规格资源包进行组合。例如，如需约3 TB流量，可购买3个1 TB资源包。
### 区域组合购买
您可以同时购买中国大陆和非中国大陆区域的CDN资源包，两者互不冲突，适用于同时服务跨地域用户的混合加速场景。
## 成本对比与选型建议
### 资源包与按量付费对比
购买资源包通常比按量付费更划算。以下示例说明两者的费用差异：
| 计费方式 | 中国内地 10 TB 流量 | 费用 |
| --- | --- | --- |
| 按量付费 | 10 TB × 约 0.24 元/GB | 约 2,457.6 元 |
| 资源包 | 10 TB 资源包 | 1,260 元 |
在此示例中，使用资源包比按量付费节省近50%的费用。
### 大额资源包单价说明
大额流量资源包（如百TB或PB级别）的参考单价，可通过总价除以总容量得出。例如：1 PB资源包标价约94,000元，折合约0.09元/GB。实际价格随阶梯折扣变动，请以控制台显示的价格为准。
### 流量估算与选型计算
您可以使用以下公式估算每日流量消耗：
单日流量(GB) = 并发人数 × 码率(Mbps) × 时长(秒) ÷ 1024 ÷ 8
以下表格提供了不同用户规模下的月流量预估（假设平均码率2 Mbps，每用户每天观看2小时）：
| 并发用户数 | 预估日流量 | 预估月流量 | 推荐方案 |
| --- | --- | --- | --- |
| 1 万 | 约 17.6 TB | 约 527 TB | 资源包更划算 |
| 5 万 | 约 87.9 TB | 约 2,637 TB | 建议大额资源包组合 |
| 10 万 | 约 175.8 TB | 约 5,273 TB | 大额资源包享阶梯折扣 |
大规模场景下，购买资源包比按量付费显著节省成本。
## 选购示例
案例场景
假设小张需要加速一个小型的社区类网站，需求及相关信息如下：
网站加速服务：小型社区类网站，加速内容包括：图片、文字、视频点播。
加速区域：中国内地。
其他服务：使用阿里云OSS存储服务来存储图片和视频文件；使用HTTPS加密服务保障访问安全。
业务资源消耗预估：
| 资源项 | 预估资源消耗 |
| --- | --- |
| 下行流量 | 网站的日峰值带宽：约 1 Gbps 下行流量：3.16 TB/日、95 TB/月、570 TB/半年、1140 TB/年 |
| 静态 HTTPS 请求数 | 日峰值 QPS：约 3000 请求数：约 7800 万次/日、约 23.3 亿次/月、279.6 亿次/年 |
| OSS 存储流量 | 取决于 CDN 上的命中率情况，CDN 上的命中率越高，OSS 上产生的费用越低。 例如：CDN 上字节命中率和请求命中率都是 90%，这也就意味着只有 10%的流量和请求需要回源到 OSS 源站，OSS 源站对于这部分流量的收费请参见 [对象存储](https://www.aliyun.com/price/product?spm=5176.7933691.J_5253785160.4.5ea14c59aiQsLY#/oss/detail/ossbag) [OSS](https://www.aliyun.com/price/product?spm=5176.7933691.J_5253785160.4.5ea14c59aiQsLY#/oss/detail/ossbag) [详细价格信息](https://www.aliyun.com/price/product?spm=5176.7933691.J_5253785160.4.5ea14c59aiQsLY#/oss/detail/ossbag) 。 |
资源包选购分析
根据业务服务判断计费项，确定所需资源包类型
| 所需服务及计费项 | 所需资源包 |
| --- | --- |
| CDN 基础加速服务：下行流量费用 | CDN/全站加速下行流量资源包 |
| HTTPS 加密服务：静态 HTTPS 请求费用 | CDN/全站加速静态 HTTPS 请求数资源包 |
确定资源包规格和购买周期
基于自身CDN下行流量消耗和下行流量官网选项选择，多个资源包可叠加。
推荐选购的资源包
| CDN/全站加速下行流量资源包 | CDN/全站加速静态 HTTPS 请求数资源包 |
| --- | --- |
| 商品类型：CDN/全站加速资源包 资源包类型：下行流量 下行流量：200TB 加速区域：中国内地通用 购买有效期：1 年 | 商品类型：CDN/全站加速资源包 资源包类型：静态 HTTPS 请求数 静态 HTTPS 请求数：100 亿次 套餐：静态 HTTPS 请求包 购买有效期：1 年 |
## 常见问题
### 资源包到期与续费
资源包到期后能否续费？
资源包到期后不支持直接续费，需重新购买。资源包可以叠加使用。如果您的网站因资源包过期而无法正常访问，重新购买相同配置的资源包即可恢复服务。
重新购买时如何选择配置？
重新购买时，按原有资源包的商品类型、资源包类型、规格、加速区域、购买周期进行选择即可，无需额外操作。
能否叠加购买资源包扩容？
可以。如果初始规格不足或业务流量增长（例如企业官网推广期间流量激增），您可以直接叠加购买新的资源包进行扩容。系统会自动累加所有生效中资源包的可用额度。
购买资源包和配置域名接入有先后顺序吗？
没有。您可以先购买资源包再配置域名加速，也可以先完成域名加速配置再购买资源包，两者互不影响。
### 产品区分与支付
CDN/DCDN资源包和ESA资源包有什么区别？
CDN（内容分发网络）、DCDN（全站加速）和ESA（边缘安全加速）是不同的阿里云产品，各自拥有独立的资源包。如果您使用的是CDN产品，请确保购买CDN/DCDN资源包，而非ESA资源包。购买错误类型的资源包将无法抵扣CDN的用量费用。
为什么无法选择账户余额支付？
如果在购买资源包时无法选择账户余额支付，可能由以下原因导致：
账户余额不足以支付订单金额。
账户余额因欠费或争议被冻结。
有未完成的订单占用了部分可用余额。
建议您检查账户余额状态，清除未完成的订单，或尝试清除浏览器缓存并更换浏览器重试。
## 相关文档
[查询资源包明细](query-the-details-of-resource-plans-1.md)
[设置资源包预警](configure-low-capacity-alerts.md)
[购买了资源包为什么仍会扣费或欠费？](why-am-i-still-charged-for-resources-after-i-purchase-resource-plans-of-alibaba-cloud-cdn.md)
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
