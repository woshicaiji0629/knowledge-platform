# 使用CLI根据集群ID查看集群详细信息-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/developer-reference/view-information-about-a-cluster

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-managed-and-ack-dedicated/product-overview.md)

- [快速入门](products/ack/documents/ack-managed-and-ack-dedicated/getting-started.md)

- [操作指南](products/ack/documents/ack-managed-and-ack-dedicated/user-guide.md)

- [实践教程](products/ack/documents/ack-managed-and-ack-dedicated/use-cases.md)

- [安全合规](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference.md)

- [服务支持](products/ack/documents/ack-managed-and-ack-dedicated/support.md)

[首页](https://help.aliyun.com/zh)

# 查看集群实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

根据集群ID，查看集群的详细信息。

有关具体的API描述，请参见[DescribeClusterDetail - 查询指定集群的信息](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-describeclusterdetail.md)。

## API请求响应

请求格式

aliyun cs GET /clusters/<cluster_id>

响应结果

{ "name": "sian-devk8s", "cluster_id": "cdde1f21ae22e483ebcb068a6eb7f****", "size": 1, "region_id": "cn-bei****", "state": "running", "cluster_type": "ManagedKubernetes", "created": "2019-11-25T15:50:20+08:00", "updated": "2020-01-13T23:01:03+08:00", "init_version": "1.14.8-aliyun.1", "current_version": "1.14.8-aliyun.1", "meta_data": "{\"Addons\":[{\"name\":\"flannel\",\"version\":\"\",\"disabled\":false,\"required\":\"\",\"config\":\"\"},{\"name\":\"flexvolume\",\"version\":\"\",\"disabled\":false,\"required\":\"\",\"config\":\"\"},{\"name\":\"alicloud-disk-controller\",\"version\":\"\",\"disabled\":false,\"required\":\"\",\"config\":\"\"},{\"name\":\"logtail-ds\",\"version\":\"\",\"disabled\":false,\"required\":\"\",\"config\":\"{\\\"IngressDashboardEnabled\\\":\\\"true\\\"}\"},{\"name\":\"nginx-ingress-controller\",\"version\":\"\",\"disabled\":false,\"required\":\"\",\"config\":\"{\\\"IngressSlbNetworkType\\\":\\\"internet\\\"}\"},{\"name\":\"kube-flannel-ds\",\"version\":\"\",\"disabled\":false,\"required\":\"\",\"config\":\"\"}],\"Capabilities\":{\"AnyAZ\":true,\"CSI\":true,\"CpuPolicy\":true,\"DeploymentSet\":true,\"HpcCluster\":true,\"Network\":\"Flannel\",\"NodeCIDRMask\":\"25\",\"NodeNameMode\":true,\"ProxyMode\":\"ipvs\",\"PublicSLB\":true,\"SLSProjectName\":true,\"SandboxRuntime\":false,\"Taint\":true,\"TerwayEniip\":true,\"UserData\":true},\"ClusterDomain\":\"\",\"DockerVersion\":\"18.09.2\",\"EtcdVersion\":\"v3.3.8\",\"HasSandboxRuntime\":false,\"KubernetesVersion\":\"1.14.8-aliyun.1\",\"MultiAZ\":false,\"NameMode\":\"\",\"OSType\":\"Linux\",\"Platform\":\"CentOS\",\"PodVswitchId\":\"\",\"Provider\":\"\",\"ResourceGroupId\":\"rg-acfmyvw3wjmb3uq\",\"SubClass\":\"default\",\"SupportPlatforms\":null,\"VersionSpec\":null,\"VpcCidr\":\"192.168.0.0/16\"}", "resource_group_id": "rg-acfmyvw3wjm****", "instance_type": "", "vpc_id": "vpc-2zecuu62b9zw7a7qn****", "vswitch_id": "vsw-2zete8s4qocqg0mf****", "vswitch_cidr": "", "data_disk_size": 0, "data_disk_category": "cloud", "security_group_id": "sg-2zedf74ifulatvx0z2ag", "tags": [ { "key": "ack.aliyun.com", "value": "cdde1f21ae22e483ebcb068a6eb7f358d" } ], "zone_id": "cn-beiji****", "-": "PayByTraffic", "network_mode": "vpc", "subnet_cidr": "172.20.0.0/16", "master_url": "{\"api_server_endpoint\":\"https://47.93.19X.XXX:XXXXhttps://mirana.cs-cn-beijing.aliyuncx.xxx:xxxxhttps://192.168.X.XX:XXXX\"}", "external_loadbalancer_id": "lb-2ze3buguz3gx9920zwf24", "port": 0, "node_status": "", "cluster_healthy": "", "docker_version": "18.09.2", "swarm_mode": false, "gw_bridge": "", "upgrade_components": { "Kubernetes": { "component_name": "Kubernetes", "version": "1.14.8-aliyun.1", "next_version": "", "changed": "", "can_upgrade": false, "force": false, "policy": "", "ExtraVars": null, "ready_to_upgrade": "", "message": "", "exist": false, "required": false } }, "private_zone": false, "profile": "", "deletion_protection": true, "capabilities": null, "enabled_migration": false, "need_update_agent": false, "outputs": [ { "Description": "Log Info Output", "OutputKey": "LastKnownError", "OutputValue": null }, { "Description": "Error msg of ess scaling instance", "OutputKey": "NodesScalingErrorInfo", "OutputValue": null }, { "Description": "The mode we use in kube-proxy.", "OutputKey": "ProxyMode", "OutputValue": "ipvs" }, { "Description": "ScalingGroup ID", "OutputKey": "ScalingGroupID", "OutputValue": "asg-2zebrr08gt5uluh7u5ar" }, { "Description": "Ids of worker node", "OutputKey": "NodeInstanceIDs", "OutputValue": [ "i-2ze4ymrjuocpbc0cftdj", "i-2ze4ymrjuocpbc0cftdk", "i-2ze4ymrjuocpbc0cftdl" ] }, { "Description": "Count of ess scaling instance", "OutputKey": "NodesScalingAddedInstances", "OutputValue": 3 } ] }

[上一篇：查看所有集群实例](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/view-all-clusters-1.md)[下一篇：创建集群](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/create-a-cluster-2.md)

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
