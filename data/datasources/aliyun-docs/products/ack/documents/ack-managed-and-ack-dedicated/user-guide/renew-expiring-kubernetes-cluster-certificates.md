# 更新ACK专有集群Master节点和Worker节点即将过期的证书-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/renew-expiring-kubernetes-cluster-certificates

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

# 更新ACK专有集群即将过期的证书

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍如何更新ACK专有集群即将过期的证书。您可以通过控制台或kubectl更新所有节点的证书，也可以手动更新Master和Worker节点证书。

说明

ACK会自动更新ACK托管集群中Master节点的证书，无需您手动处理。

## 通过控制台更新所有节点证书

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

单击证书即将过期集群右侧的更新证书，进入更新证书页面。

说明

如果集群证书即将在两个月左右过期，会出现更新证书。

在集群列表中找到目标集群，单击其右侧操作列中的更新证书。

- 

在更新证书页面，单击更新证书，按照页面指引完成证书的更新。

成功更新集群证书后，您可以看到以下内容：

- 

在更新证书页面，显示更新成功。

- 

在集群列表页面，目标集群没有更新证书提示。

## 通过kubectl自动更新所有节点证书

更新证书

在集群任意Master节点，执行以下命令完成集群所有节点的证书更新。

curl http://aliacs-k8s-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/public/cert-update/renew.sh | bash

结果验证需已通过kubectl连接集群，请参见[通过](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[连接](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[Kubernetes](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。

- 

执行以下命令，查看集群Master和Worker节点状态。

kubectl get nodes[root@xxx ~]# kubectl get nodes NAME STATUS ROLES AGE VERSION cn-hangzhou.xxx Ready <none> 23d v1.11.2 cn-hangzhou.xxx Ready <none> 23d v1.11.2 cn-hangzhou.xxx Ready master 47d v1.11.2 cn-hangzhou.xxx Ready master 47d v1.11.2 cn-hangzhou.xxx Ready master 47d v1.11.2 cn-hangzhou.xxx Ready <none> 47d v1.11.2 cn-hangzhou.xxx Ready <none> 47d v1.11.2 [root@xxx ~]#

- 

执行以下命令，当Master节点对应的COMPLETIONS均为1，Worker节点对应的COMPLETIONS为集群Worker节点数时，所有证书完成更新。

kubectl -n kube-system get job[root@ ~]# kubectl get job -nkube-system NAME COMPLETIONS DURATION AGE aliyun-cert-renew-master-1 1/1 46s 4m49s aliyun-cert-renew-master-2 1/1 28s 4m19s aliyun-cert-renew-master-3 1/1 26s 3m48s aliyun-cert-renew-worker 6/6 46s 3m18s ingress-nginx-admission-create 1/1 29s 3d ingress-nginx-admission-patch 1/1 43s 3d kube-eventer-init-1.5-5e0e7cl-aliyun 1/1 31s 3d

## 手动更新Master节点证书

- 

任意路径下，复制以下内容，创建job-master.yml文件。

apiVersion: batch/v1 kind: Job metadata: name: ${jobname} namespace: kube-system spec: backoffLimit: 0 completions: 1 parallelism: 1 template: spec: activeDeadlineSeconds: 3600 affinity: nodeAffinity: requiredDuringSchedulingIgnoredDuringExecution: nodeSelectorTerms: - matchExpressions: - key: kubernetes.io/hostname operator: In values: - ${hostname} containers: - command: - /renew/upgrade-k8s.sh - --role - master image: registry.cn-hangzhou.aliyuncs.com/acs/cert-rotate:v1.0.0 imagePullPolicy: Always name: ${jobname} securityContext: privileged: true volumeMounts: - mountPath: /alicoud-k8s-host name: ${jobname} hostNetwork: true hostPID: true restartPolicy: Never schedulerName: default-scheduler securityContext: {} tolerations: - effect: NoSchedule key: node-role.kubernetes.io/master volumes: - hostPath: path: / type: Directory name: ${jobname}

- 

获取集群Master节点个数和节点名称等信息。

- 

方法一：通过命令行

执行以下命令：

kubectl get nodes[root@xxx ~]# kubectl get nodes NAME STATUS ROLES AGE VERSION cn-hangzhou.ixxx Ready <none> 22d v1.11.2 cn-hangzhou.ixxx Ready <none> 22d v1.11.2 cn-hangzhou.ixxx Ready master 46d v1.11.2 cn-hangzhou.ixxx Ready master 46d v1.11.2 cn-hangzhou.ixxx Ready master 46d v1.11.2 cn-hangzhou.ixxx Ready <none> 46d v1.11.2 cn-hangzhou.ixxx Ready <none> 46d v1.11.2 [root@xxx ~]#

- 

方法二：通过控制台

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面中，单击目标集群名称或者目标集群右侧操作列下的详情。

- 

在集群管理页的左侧导航栏中，选择节点管理>节点获取Master个数和对应的名称、IP地址、实例ID。

- 

执行以下命令替换job-master.yml文件中指定的变量${jobname}和${hostname}。

sed 's/${jobname}/cert-job-2/g; s/${hostname}/hostname/g' job-master.yml > job-master2.yml

其中：

- 

${jobname}为Job的名称，此处设置为cert-job-2。

- 

${hostname}为集群Master节点的名称，此处请将hostname替换为步骤2中查看到的Master名称。

- 

执行以下命令创建Job。

kubectl create -f job-master2.yml

- 

执行以下命令查看Job状态，当COMPLETIONS均为1时，证书完成更新。

kubectl get job -nkube-system

- 

重复执行步骤3~5，完成所有Master节点的证书更新。

[root@xxx ~]# kubectl get job -nkube-system NAME COMPLETIONS DURATION AGE cert-job-2 1/1 46s 22m cert-job-3 1/1 28s 2m cert-job-4 1/1 26s 1m [root@xxx ~]#

## 手动更新Worker节点证书

- 

任意路径下，复制以下内容，创建job-node.yml文件。

apiVersion: batch/v1 kind: Job metadata: name: ${jobname} namespace: kube-system spec: backoffLimit: 0 completions: ${nodesize} parallelism: ${nodesize} template: spec: activeDeadlineSeconds: 3600 affinity: podAntiAffinity: requiredDuringSchedulingIgnoredDuringExecution: - labelSelector: matchExpressions: - key: job-name operator: In values: - ${jobname} topologyKey: kubernetes.io/hostname containers: - command: - /renew/upgrade-k8s.sh - --role - node - --rootkey - ${key} image: registry.cn-hangzhou.aliyuncs.com/acs/cert-rotate:v1.0.0 imagePullPolicy: Always name: ${jobname} securityContext: privileged: true volumeMounts: - mountPath: /alicoud-k8s-host name: ${jobname} hostNetwork: true hostPID: true restartPolicy: Never schedulerName: default-scheduler securityContext: {} volumes: - hostPath: path: / type: Directory name: ${jobname}

说明

如果Worker节点带有Taint，需要在job-node.yml文件中增加对该Taint的tolerations，即在securityContext: {}与volumes:之间增加以下内容（若有n个带有Taint的Worker节点，请复制n次）：

tolerations: - effect: NoSchedule key: ${key} operator: Equal value: ${value}

获取${name}和${value}的方法如下：

- 

任意路径下，复制以下内容，创建taint.tml文件。

{{printf "%-50s %-12s\n" "Node" "Taint"}} {{- range .items}} {{- if $taint := (index .spec "taints") }} {{- .metadata.name }}{{ "\t" }} {{- range $taint }} {{- .key }}={{ .value }}:{{ .effect }}{{ "\t" }} {{- end }} {{- "\n" }} {{- end}} {{- end}}

- 

执行以下命令，查询带有Taint的Worker节点的${name}和${value}。

kubectl get nodes -o go-template-file="taint.tml"[root@xxx ~]# kubectl get nodes -o go-template-file="taint.tml" Node Taint cn-hangzhou.i-xxx key1=value1:NoSchedule cn-hangzhou.i-xxx node-role.kubernetes.io/master=<no value>:NoSchedule cn-hangzhou.i-xxx node-role.kubernetes.io/master=<no value>:NoSchedule cn-hangzhou.i-xxx node-role.kubernetes.io/master=<no value>:NoSchedule

- 

执行以下命令，获取集群的CAKey。

sed '1d' /etc/kubernetes/pki/ca.key | base64 -w 0

- 

执行以下命令替换job-node.yml文件中指定的变量${jobname}、${nodesize}和${key}。

sed 's/${jobname}/cert-node-2/g; s/${nodesize}/nodesize/g; s/${key}/key/g' job-node.yml > job-node2.yml

其中：

- 

${jobname}为Job的名称，此处设置为cert-node-2。

- 

${nodesize}为Worker节点个数，获取方法可参见[手动更新](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/renew-expiring-kubernetes-cluster-certificates.md)[Worker](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/renew-expiring-kubernetes-cluster-certificates.md)[节点证书](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/renew-expiring-kubernetes-cluster-certificates.md)的步骤1。此处请将nodesize替换为集群的Worker个数。

- 

${key}为集群的CAKey，此处请将key替换为[手动更新](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/renew-expiring-kubernetes-cluster-certificates.md)[Worker](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/renew-expiring-kubernetes-cluster-certificates.md)[节点证书](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/renew-expiring-kubernetes-cluster-certificates.md)步骤2获取到的CAKey。

- 

执行以下命令创建Job。

kubectl create -f job-node2.yml

- 

执行以下命令查看Job状态，当COMPLETIONS为集群Worker节点数时，证书完成更新。

kubectl get job -nkube-system[root@xxx ~]# kubectl get job -nkube-system NAME COMPLETIONS DURATION AGE cert-job-2 1/1 46s 1h cert-job-3 1/1 28s 47m cert-job-4 1/1 26s 46m cert-node-2 4/4 46s 1m [root@xxx ~]#

[上一篇：ACK专有集群证书更新说明](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/renew-cluster-certificates.md)[下一篇：更新ACK专有集群已过期的证书](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-expired-certificates-of-a-kubernetes-cluster.md)

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
