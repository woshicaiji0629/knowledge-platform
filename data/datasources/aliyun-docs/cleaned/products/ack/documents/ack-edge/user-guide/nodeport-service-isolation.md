# 为NodePort服务指定监听节点池实现端口隔离-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/nodeport-service-isolation

# NodePort端口监听隔离
在边缘网络场景中，服务隔离是必需的。例如，当使用NodePort类型的Service时，您可以指定特定节点池的节点上才会监听NodePort Service中的端口，从而避免可能产生的端口冲突风险。本文介绍如何使用NodePort端口监听隔离。
## 架构原理
edge-hub组件中内置可编程数据过滤框架，可以对边缘发起请求的响应数据（云端kube-apiserver返回）实现无感知和按需转换，以满足云边协同场景的特定需求。架构如下图所示。
edge-hub中引入一个名为nodeportisolation的新过滤器来实现NodePort Service的隔离能力，同时NodePort Service添加了一个新的注解（Annotaion）nodeport.openyurt.io/listen。
## 注意事项
edge-hub组件版本使用v0.11.0及以上版本。
您在创建Service时需要确定好是否添加注解nodeport.openyurt.io/listen。若Service创建后再添加该注解，需要重启所有kube-proxy，该功能才能生效。
新增节点池后，需要在未接入节点之前，把新创建的节点池增加到Service的注解中，该功能才能在后续接入的节点上生效。
由于节点池名称支持变更，所以请使用节点池ID来指定节点池。节点池ID可通过[容器服务管理控制台](https://cs.console.aliyun.com)查看，格式一般为npxxxx。
## 使用方法
您可以为NodePort、LoadBalancer服务引入注解nodeport.openyurt.io/listen。
注解的键（key）：nodeport.openyurt.io/listen。
注解的值（value）：用英文半角逗号分隔的节点池ID列表。
foo：使指定的NodePort Service在ID为foo的节点池中的节点上监听。
-foo：禁止指定的NodePort Service在ID为foo的节点池中的节点上监听。
*：使指定的NodePort Service在所有节点池中的节点上监听。
重要
如果对同一节点池有多个配置，仅第一个配置生效。
如果未配置节点池ID，将在这些未配置的节点池中的节点上禁用此NodePort Service监听。
与原生Kubernetes一致，系统将默认监听孤儿节点（不位于节点池中的节点）NodePort Service的端口。
### 注解设置示例
| 注解 | 说明 |
| --- | --- |
| nodeport.openyurt.io/listen=foo,bar | 在 foo 和 bar 节点池中的节点上启用 NodePort Service 监听。 |
| nodeport.openyurt.io/listen=foo,* | 在所有节点池中的节点上启用 NodePort Service 监听。 |
| nodeport.openyurt.io/listen=-foo,-bar | 在所有节点池中的节点上禁用 NodePort Service 监听。 |
| nodeport.openyurt.io/listen=-foo,* | 仅在 foo 节点池中的节点上禁用 NodePort Service 监听。 |
| nodeport.openyurt.io/listen=foo,-foo | 在 foo 节点池中的节点上启用 NodePort Service 监听。 |
| nodeport.openyurt.io/listen=-foo | 在所有节点池中的节点上禁用 NodePort Service 监听（包含 foo 节点池）。 |
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
