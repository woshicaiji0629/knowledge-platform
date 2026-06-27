# 什么是DNS CNAME记录-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/what-is-a-dns-cname-record

# CNAME记录简介
CNAME记录，即Canonical Name Record，直译成中文就是"规范的名称记录"，是域名系统（DNS）的一种记录类型，其作用是将一个域名映射到另一个域名。
## 什么是DNS CNAME记录？
DNS的记录类型有好多种，而CNAME记录通常都是和A记录一起工作的，所以在具体介绍CNAME记录之前先简单的介绍下A记录。
### A记录
A记录，也就是Address记录，是一种映射记录，记录的是域名和IP的映射关系。
当我们访问指定的域名时，DNS会通过A记录的配置，解析出域名映射的IP，后续就会直接以这个IP进行访问。
示例（示例数据仅供理解，不具有真实性）：
记录类型 域名 记录值 A www.example.com 10.10.10.10
### CNAME记录
与A记录相比，CNAME记录保存的是域名和域名的映射关系，可以想象为给一个域名起了一个“外号”，这个“外号”和域名的映射关系就是通过CNAME记录保存的，而CNAME类型的记录值则可以通过A记录来映射到具体的服务器。
示例（示例数据仅供理解，不具有真实性）：
记录类型 域名 记录值 CNAME cname1.example.com www.example.com.w.kunlunsl.com A www.example.com.w.kunlunsl.com 10.10.10.10
当我们访问"cname1.example.com"这个域名的时候，DNS会通过CNAME记录获取到映射值"www.example.com.w.kunlunsl.com"，基于"www.example.com.w.kunlunsl.com"的A记录，"cname1.example.com"域名最终也会解析到IP地址"10.10.10.10"。
说明
在DNS的解析记录中，对于同一个主机名，A记录和CNAME记录是相互冲突的，两者不能同时存在。
## DNS CNAME的优势
### 快速实现服务器IP的更新
当服务器的IP地址发生了变化（从10.10.10.10变为10.10.10.1），只需要把A记录对应的记录值修改成新的IP（10.10.10.1），与A记录的域名存在映射关系的三个CNAME记录无需任何改动，就能实现三个域名最终指向新的服务器IP的效果。
示例（示例数据仅供理解，不具有真实性）：
服务器IP修改前：
记录类型 域名 记录值 CNAME cname1.example.com www.example.com CNAME cname2.example.com www.example.com CNAME cname3.example.com www.example.com A www.example.com 10.10.10.10
服务器IP修改后：
记录类型 域名 记录值 CNAME cname1.example.com www.example.com CNAME cname2.example.com www.example.com CNAME cname3.example.com www.example.com A www.example.com 10.10.10.1
### 结合阿里云CDN实现静态资源的加速和分发，提高资源访问速度
阿里云内容分发网络CDN（Content Delivery Network）是建立并覆盖在承载网之上，由遍布全球的边缘节点服务器群组成的分布式网络。阿里云CDN能分担源站压力，避免网络拥塞，确保在不同区域、不同场景下加速网站内容的分发，提高资源访问速度。详情参考[什么是阿里云](product-overview/what-is-alibaba-cloud-cdn.md)[CDN](product-overview/what-is-alibaba-cloud-cdn.md)。
在第三步中，云解析DNS返回的CNAME记录值即为CDN为该域名分配的CNAME域名，通过"www.example.com.cname.com"可以访问CDN的调度中心，CDN的调度中心会根据请求用户的信息为其分配最优的CDN节点，用户访问该节点从而达到加速访问的效果。
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
