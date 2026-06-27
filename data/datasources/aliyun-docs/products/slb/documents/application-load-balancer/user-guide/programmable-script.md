# ALB可编程脚本AScript-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/user-guide/programmable-script/

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/slb/documents/application-load-balancer/product-overview.md)

- [快速入门](products/slb/documents/application-load-balancer/getting-started.md)

- [操作指南](products/slb/documents/application-load-balancer/user-guide.md)

- [实践教程](products/slb/documents/application-load-balancer/use-cases.md)

- [开发参考](products/slb/documents/application-load-balancer/developer-reference.md)

- [服务支持](products/slb/documents/application-load-balancer/support.md)

[首页](https://help.aliyun.com/zh)

# ALB可编程脚本AScript

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/slb)

[我的收藏](https://help.aliyun.com/my_favorites.html)

AScript具备转发规则自定义能力，当ALB控制台上的标准配置无法满足您的业务需求时，可通过简单的可编程脚本AScript来实现功能的二次开发。

## AScript简介

AScript通过简单易学的语法和庞大的函数库，能够积木式地组合出个性化的ALB配置。

AScript内置了可以识别的变量、简单的判断语句，同时提供了可直接调用的封装好的函数。通过简单的变量判断并调用现成的函数，即可满足您对转发规则的各类定制需求，有效地解决配置需求无法实现、业务变更不敏捷的问题。

关于AScript的语法的更多信息，请参见[AScript](products/slb/documents/application-load-balancer/user-guide/ascript-syntax.md)[语法规则](products/slb/documents/application-load-balancer/user-guide/ascript-syntax.md)。

## 应用场景

| 场景 | 描述 |
| --- | --- |
| 防盗链需求 | 应用于自定义鉴权算法、User-Agent 黑名单和 Referer 白名单等场景需求。基于请求参数、Cookie 或其他复杂算法等各类鉴权需求，帮您快速实现鉴权，从而完成对资源的保护。 |
| 黑白名单管控 | 通过设置客户端 IP 的黑白名单，来完成权限管控。 |
| 请求头和响应头控制 | 可以使用 AScript 脚本对请求参数和请求头等变量进行灵活修改。 |
| 改写和重定向 | 通过改写 URI、文件后缀、添加 URI 前缀、302 重定向等操作，实现您的改写和重定向目标。多应用在多语言版本的网站之上，例如中文网站可能会 302 重定向到 1 个位置，英文网站或者德文网站可能会 302 重定向到不同的位置。 |


## 功能计费

关于规则评估数如何影响LCU费，更多信息，请参见[ALB](products/slb/documents/application-load-balancer/product-overview/alb-billing-rules.md)[计费规则](products/slb/documents/application-load-balancer/product-overview/alb-billing-rules.md)。

## 工作原理

### 运行原理

您配置的AScript规则与ALB控制台上的标准配置一样，均用于处理ALB请求。

当客户端请求到达ALB监听后，ALB监听会根据您在控制台上配置的转发规则对请求进行处理。以ALB控制台上的标准配置为参照物，AScript可选择在规则处理前或规则处理后生效。

### 规则模型

AScript的规则模型如下：

- 

核心出发点是将不同业务功能隔离至不同规则，以及控制规则的执行流。

- 

每条规则可以各自选择规则的执行位置。

- 

以监听维度来进行设计的。

### 规则执行位置

AScript规则的执行位置包含请求方向规则执行前、请求方向规则执行后和响应方向规则执行前。

- 

请求方向规则执行前/后：常用文件自动重命名、文件后缀小写化、添加URI前缀和文件后缀名改写等场景。

- 

响应方向规则执行前：常用文件自动重命名等场景。

### 规则执行情况

您可以在[配置](products/slb/documents/application-load-balancer/user-guide/add-and-manage-scripts.md)[AScript](products/slb/documents/application-load-balancer/user-guide/add-and-manage-scripts.md)[规则](products/slb/documents/application-load-balancer/user-guide/add-and-manage-scripts.md)时，在高级配置中选中携带_es_dbg参数，开启相应的调试响应头，以输出规则执行记录。

规则执行情况字段详细说明：

- 

规则ID：每条规则的唯一性标识，格式为as-****。

- 

执行情况code及说明：

| 执行情况 code | 执行情况说明 |
| --- | --- |
| 空 | 未执行。 |
| 0 | 执行命中。 当规则含有 if condition {} ，且 condition 为真。 |
| 1 | 执行未命中。 当规则含有 if condition {} ，且 condition 为假；或规则不包含 if condition {} 。 |
| 2 | 执行异常。 |


- 

执行耗时：

- 

单位：微秒us。

- 

默认值：-1。

- 

前端呈现的耗时区间分布：

- 

第1档：0~100us

- 

第2档：100~500us

- 

第3档：500~1000us

- 

第4档：1000~5000us

- 

第5档：5000~20000us

- 

第6档：20000~50000us

- 

第7档：>50000us

- 

AScript规则的中断执行：

默认值：-1。

[上一篇：ALB Ingress功能操作指导](products/slb/documents/application-load-balancer/user-guide/functions-and-features-of-alb-ingresses.md)[下一篇：在ALB控制台配置AScript](products/slb/documents/application-load-balancer/user-guide/add-and-manage-scripts.md)

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
