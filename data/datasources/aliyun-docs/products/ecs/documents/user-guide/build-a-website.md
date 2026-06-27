# 搭建网站的完整步骤与全流程-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/user-guide/build-a-website

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 搭建网站

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

工作时间您会使用公司的企业官网，内部OA系统，闲暇之余，您也会逛论坛，看博客，或者网上购物，接下来我们将为您介绍如何搭建一个属于您的网站服务。

## 建站方式

您可以在云服务器ECS上自行搭建网站服务，也可使用阿里云提供的建站服务。请根据实际业务需求，选择适合您的建站方式。

| 建站方式 | 优势 | 适用人群与场景 |
| --- | --- | --- |
| 自助建站 | 从服务器购买到网站搭建及维护，全程自主操作，确保了高度的灵活性、控制力与可扩展性。 | 有丰富的建站经验，希望自行设计网站的个人或企业用户。 |
| [模板建站](https://ac.aliyun.com/application/webdesign/sumei) | 即开即用，提供千套网站模板，可视化后台管理，轻松便捷。 | 适合有一定软件应用能力的个人或小企业用户，模板建站支持 Web 站点、移动端站点、互动表单以及会员支付等场景。 |
| [定制建站](https://ac.aliyun.com/application/webdesign/yunqi) | 由专业设计师完成网站设计及搭建。 | 适合对网站有品质要求或个性化需求、希望节省人力和时间成本的企业用户。 |


## 建站步骤

- 

准备服务器。

不同网站类型需要的ECS配置不同，请您确认网站规模与访问人数。一般情况下，小型网站只需要选择基础配置即可。具体操作，请参见[自定义购买实例](products/ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)。

- 

了解实例规格族与如何选型，请参见[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)与[实例规格选型指导](products/ecs/documents/user-guide/best-practices-for-instance-type-selection.md)。

- 

您可以根据业务进展产生的不同需求，对实例做相应的升降配调整。更多信息，请参见[规格变更限制与自检](products/ecs/documents/user-guide/instance-families-that-support-instance-type-changes.md)。

- 

配置安全组规则。

远程连接实例所需的22、3389端口在创建安全组时默认为开启状态，访问网站时需要开启80、443端口，您需要确认安全组的入方向已开放这些端口。如果未开放，请手动配置。具体操作，请参见[添加安全组规则](products/ecs/documents/user-guide/add-a-security-group-rule.md)。

- 

部署网站。

当前节点下的文档包含了众多常用网站的部署方案，您可以根据需求，自行设计、开发并部署属于您的各类网站。

- 

购买域名。

- 

注册域名。

输入想要的域名，未被占用即可注册。具体操作，请参见[域名注册基本流程](https://help.aliyun.com/zh/dws/user-guide/how-to-register-a-domain-name#task-1830383)。

域名后缀通常为.com或.cn。更多后缀信息，请参见[域名区别](https://help.aliyun.com/zh/dws/support/domain-name-differences#concept-wvr-zcd-b2b)。

- 

实名认证。具体操作，请参见[域名实名认证概述](https://help.aliyun.com/zh/dws/overview-of-real-name-verification-for-domain-names#concept-uhk-w5v-12b)。

- 

备案域名。

重要

使用中国内地地域中的服务器托管您的网站时，需要进行备案。否则，请跳过此步骤。

- 

准备备案。

各省管局要求资料有所不同，请根据[各地区管局](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-regulations-of-the-miit-for-different-regions#concept-wl4-tql-zdb)[ICP](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-regulations-of-the-miit-for-different-regions#concept-wl4-tql-zdb)[备案规则](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-regulations-of-the-miit-for-different-regions#concept-wl4-tql-zdb)准备资料。更多信息，请参见[ICP](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/overview#concept-w3d-nql-zdb)[备案前准备概述](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/overview#concept-w3d-nql-zdb)。

- 

备案。

- 

若之前尚未进行过工信部备案，请先完成首次备案接入。具体操作，请参见[ICP](https://help.aliyun.com/zh/icp-filing/for-the-first-time-the-record-process#task-1580354)[备案流程](https://help.aliyun.com/zh/icp-filing/for-the-first-time-the-record-process#task-1580354)。

- 

其它备案场景，请参见[ICP](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview#task-2038407)[备案流程](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview#task-2038407)。

- 

[解析域名](https://help.aliyun.com/zh/dns/novice-guide-dns)。 设置域名解析后，外部用户可通过域名访问网站。

如需将域名指向一个IP地址，添加A记录即可。具体操作，请参见[添加解析记录](https://help.aliyun.com/zh/dns/add-a-dns-record)。

- 

（可选）开启HTTPS加密访问。

SSL证书服务帮助您以最小的成本将服务从HTTP转换成HTTPS，实现网站或移动应用的身份验证和数据加密传输。更多信息，请参见[什么是数字证书管理服务](https://help.aliyun.com/zh/ssl-certificate/product-overview/what-is-certificate-management-service#concept-xn2-52p-ydb)。如果您已经选购并下载了SSL证书，不同环境的服务器部署方式也不同。具体操作，请参见[部署](https://help.aliyun.com/zh/ssl-certificate/installation-overview/#task-2078352)[SSL](https://help.aliyun.com/zh/ssl-certificate/installation-overview/#task-2078352)[证书](https://help.aliyun.com/zh/ssl-certificate/installation-overview/#task-2078352)。

至此，自助建站操作已完成。接下来，您可以使用域名访问网站，测试服务是否正常。

## 相关文档

- 

上云前如何根据自身业务特点，选择阿里云产品和配置，请参见[架构设计&上云咨询服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_wellarchtected_public_cn)。

- 

迁移云下自建机房、托管机房等环境下的业务到阿里云，并获取专业迁云方案实施服务，请参见[迁云方案实施服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)。

- 

基于ECS，若需要专业工程师协助对系统、数据库、站点进行基础设置，请参见[云资源管理基础设置服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_landingzone_public_cn)。

[上一篇：通过OOS扩展程序安装QwenPaw](products/ecs/documents/user-guide/install-qwenpaw-on-ecs-instances-using-the-oos-extension.md)[下一篇：搭建微信、支付宝小程序](products/ecs/documents/user-guide/develop-your-wechat-mini-program-in-10-minutes.md)

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
