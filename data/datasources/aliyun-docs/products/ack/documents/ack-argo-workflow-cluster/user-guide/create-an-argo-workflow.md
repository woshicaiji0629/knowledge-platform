# 创建Argo工作流-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/user-guide/create-an-argo-workflow

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-argo-workflow-cluster/product-overview.md)

- [服务支持](products/ack/documents/ack-argo-workflow-cluster/support.md)

- [实践教程](products/ack/documents/ack-argo-workflow-cluster/use-cases.md)

- [操作指南](products/ack/documents/ack-argo-workflow-cluster/user-guide.md)

[首页](https://help.aliyun.com/zh)

# 创建Argo工作流

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

工作流集群基于开源Argo Workflow项目构建，适用于CI/CD流水线、数据处理、机器学习和仿真计算等。本文通过示例介绍如何创建Argo工作流。

## 适用范围

已[创建](products/ack/documents/ack-argo-workflow-cluster/user-guide/create-an-argo-workflow-cluster.md)[Argo](products/ack/documents/ack-argo-workflow-cluster/user-guide/create-an-argo-workflow-cluster.md)[工作流集群](products/ack/documents/ack-argo-workflow-cluster/user-guide/create-an-argo-workflow-cluster.md)。

## 工作流ServiceAccount

工作流可指定ServiceAccount用于运行中访问其他Kubernetes资源，您可以创建自己的ServiceAccount，工作流集群会为ServiceAccount自动绑定权限，

## 操作步骤

工作流集群支持通过Argo CLI或Argo UI创建工作流。

## 通过Argo CLI创建

### 步骤一：安装Argo CLI

阿里云Argo CLI完全兼容开源Argo CLI，并增强了Metrics能力和日志能力。阿里云Argo CLI支持查看工作流的CPU、内存资源消耗及运行成本，并获取已删除Pod的日志。

- 

下载阿里云Argo CLI。

以下步骤以Linux系统为例，Darwin（macOS）版Argo CLI的下载链接是[https://ack-one.oss-cn-hangzhou.aliyuncs.com/cli/v3.4.12/argo-cli-aliyun-darwin](https://ack-one.oss-cn-hangzhou.aliyuncs.com/cli/v3.4.12/argo-cli-aliyun-darwin)。wget https://ack-one.oss-cn-hangzhou.aliyuncs.com/cli/v3.4.12/argo-cli-aliyun-linux

- 

为argo-cli-aliyun-linux授予可执行权限。

chmod +x argo-cli-aliyun-linux

- 

将执行文件移动到环境变量包含的目录下，例如：/usr/local/bin/。

mv argo-cli-aliyun-linux /usr/local/bin/argo

### 步骤二：创建工作流

- 

创建并复制下方示例到helloworld-workflow.yaml文件。

apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: helloworld-- # 工作流名称前缀 spec: entrypoint: helloworld # 指定入口工作流模板 templates: - name: helloworld container: image: mirrors-ssl.aliyuncs.com/busybox:latest command: - sh - -c args: - echo "Hello, world!"; sleep 60;

- 

提交工作流。

argo submit helloworld-workflow.yaml

- 

查看工作流状态。

- 

获取工作流列表。

argo list

预期输出：

NAME STATUS AGE DURATION PRIORITY helloworld-lgdpp Succeeded 2m 37s 0

- 

查看工作流状态。

argo get helloworld-lgdpp

预期输出：

Name: hello-world-lgdpp Namespace: default ServiceAccount: unset (will run with the default ServiceAccount) Status: Succeeded Conditions: PodRunning False Completed True .... Duration: 1 minute 46 seconds Progress: 1/1 ResourcesDuration: 17s*(1 cpu),17s*(100Mi memory) STEP TEMPLATE PODNAME DURATION MESSAGE ✔ hello-world-lgdpp helloworld hello-world-lgdpp 1m

## 通过Argo UI创建

- 

登录[容器](https://csnew.console.aliyun.com/#/next/argowf)[Argo](https://csnew.console.aliyun.com/#/next/argowf)[工作流集群控制台](https://csnew.console.aliyun.com/#/next/argowf)，单击目标集群名称。

- 

在集群信息页面中，选择基础信息页签，单击下方工作流控制台（Argo）卡片，访问Argo UI。

- 

单击左侧workflow template选项，在NAMESPACE中输入default，查看预制的工作流模板。

页面显示三个预制工作流模板：dag-diamond、loops、steps。

- 

选择任意工作流模板，单击SUBMIT，运行工作流。

[上一篇：管理Argo工作流](products/ack/documents/ack-argo-workflow-cluster/user-guide/manage-argo-workflows.md)[下一篇：配置Argo工作流ACS Pod算力](products/ack/documents/ack-argo-workflow-cluster/user-guide/configure-computing-resources-for-the-argo-workflow-acs-pods.md)

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
