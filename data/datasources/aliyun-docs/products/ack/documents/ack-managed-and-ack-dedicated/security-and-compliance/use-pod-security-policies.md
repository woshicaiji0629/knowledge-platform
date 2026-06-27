# 管理默认Pod安全策略与解决Pod创建失败问题-容器服务Kubernetes版ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies

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

# 【已弃用】使用Pod安全策略

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Kubernetes的Pod安全策略（Pod Security Policy）准入控制组件会基于您定义的规则验证在集群上创建和更新Pod的请求。如果创建或更新Pod的请求不符合定义的规则，系统将拒绝该请求并返回错误。本文将介绍如何在容器服务Kubernetes版ACK（Container Service for Kubernetes）中使用Pod安全策略。

## 前提条件

您已完成以下操作：

- 

[创建一个](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[Kubernetes](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。

- 

[获取集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[KubeConfig](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[并通过](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。

说明

本文档仅适用于1.26以下版本的集群。

## ACK默认的Pod安全策略

在ACK中，Kubernetes 1.16.6版本的标准专有集群和标准托管集群将默认启用Pod安全策略准入控制组件，并配置一个名为ack.privileged的Pod安全策略。这个安全策略将放行任意类型的Pod，效果等同于集群未开启Pod安全策略准入控制组件。

## 默认的Pod安全策略命令

$ kubectl get psp ack.privileged NAME PRIV CAPS SELINUX RUNASUSER FSGROUP SUPGROUP READONLYROOTFS VOLUMES ack.privileged true * RunAsAny RunAsAny RunAsAny RunAsAny false *

## 详细规则的Pod安全策略命令

$ kubectl describe psp ack.privileged Name: ack.privileged Settings: Allow Privileged: true Allow Privilege Escalation: true Default Add Capabilities: <none> Required Drop Capabilities: <none> Allowed Capabilities: * Allowed Volume Types: * Allow Host Network: true Allow Host Ports: 0-65535 Allow Host PID: true Allow Host IPC: true Read Only Root Filesystem: false SELinux Context Strategy: RunAsAny User: <none> Role: <none> Type: <none> Level: <none> Run As User Strategy: RunAsAny Ranges: <none> FSGroup Strategy: RunAsAny Ranges: <none> Supplemental Groups Strategy: RunAsAny Ranges: <none>

展开查看Pod安全策略、相应集群角色、集群角色绑定的完整YAML文件内容

--- apiVersion: policy/v1beta1 kind: PodSecurityPolicy metadata: name: ack.privileged annotations: kubernetes.io/description: 'privileged allows full unrestricted access to pod features, as if the PodSecurityPolicy controller was not enabled.' seccomp.security.alpha.kubernetes.io/allowedProfileNames: '*' labels: kubernetes.io/cluster-service: "true" ack.alicloud.com/component: pod-security-policy spec: privileged: true allowPrivilegeEscalation: true allowedCapabilities: - '*' volumes: - '*' hostNetwork: true hostPorts: - min: 0 max: 65535 hostIPC: true hostPID: true runAsUser: rule: 'RunAsAny' seLinux: rule: 'RunAsAny' supplementalGroups: rule: 'RunAsAny' fsGroup: rule: 'RunAsAny' readOnlyRootFilesystem: false --- apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRole metadata: name: ack:podsecuritypolicy:privileged labels: kubernetes.io/cluster-service: "true" ack.alicloud.com/component: pod-security-policy rules: - apiGroups: - policy resourceNames: - ack.privileged resources: - podsecuritypolicies verbs: - use --- apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRoleBinding metadata: name: ack:podsecuritypolicy:authenticated annotations: kubernetes.io/description: 'Allow all authenticated users to create privileged pods.' labels: kubernetes.io/cluster-service: "true" ack.alicloud.com/component: pod-security-policy roleRef: apiGroup: rbac.authorization.k8s.io kind: ClusterRole name: ack:podsecuritypolicy:privileged subjects: - kind: Group apiGroup: rbac.authorization.k8s.io name: system:authenticated

## 删除ACK默认Pod安全策略对应的集群角色绑定

警告

在删除ACK默认的Pod安全策略对应的集群角色绑定前必须先配置好自定义的Pod安全策略及其相应的RBAC绑定，否则所有用户、控制器、服务账号都将无法创建或更新Pod。

在配置好自定义的Pod安全策略及其相应的RBAC绑定后，您可以通过删除ACK默认Pod安全策略ack.privileged的集群角色绑定的方式来启用您自定义的Pod安全策略。

重要

请不要删除或修改名为ack.privileged的Pod安全策略以及名为ack:podsecuritypolicy:privileged的集群角色，ACK集群的正常运行需要依赖这两个资源。

展开查看删除ACK默认Pod安全策略ack.privileged的集群角色绑定命令

$ cat <<EOF | kubectl delete -f - apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRoleBinding metadata: name: ack:podsecuritypolicy:authenticated annotations: kubernetes.io/description: 'Allow all authenticated users to create privileged pods.' labels: kubernetes.io/cluster-service: "true" ack.alicloud.com/component: pod-security-policy roleRef: apiGroup: rbac.authorization.k8s.io kind: ClusterRole name: ack:podsecuritypolicy:privileged subjects: - kind: Group apiGroup: rbac.authorization.k8s.io name: system:authenticated EOF

## 配置或恢复ACK默认的Pod安全策略

展开查看配置或恢复使用ACK默认的Pod安全策略及其RBAC绑定命令

cat <<EOF | kubectl apply -f - --- apiVersion: policy/v1beta1 kind: PodSecurityPolicy metadata: name: ack.privileged annotations: kubernetes.io/description: 'privileged allows full unrestricted access to pod features, as if the PodSecurityPolicy controller was not enabled.' seccomp.security.alpha.kubernetes.io/allowedProfileNames: '*' labels: kubernetes.io/cluster-service: "true" ack.alicloud.com/component: pod-security-policy spec: privileged: true allowPrivilegeEscalation: true allowedCapabilities: - '*' volumes: - '*' hostNetwork: true hostPorts: - min: 0 max: 65535 hostIPC: true hostPID: true runAsUser: rule: 'RunAsAny' seLinux: rule: 'RunAsAny' supplementalGroups: rule: 'RunAsAny' fsGroup: rule: 'RunAsAny' readOnlyRootFilesystem: false --- apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRole metadata: name: ack:podsecuritypolicy:privileged labels: kubernetes.io/cluster-service: "true" ack.alicloud.com/component: pod-security-policy rules: - apiGroups: - policy resourceNames: - ack.privileged resources: - podsecuritypolicies verbs: - use --- apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRoleBinding metadata: name: ack:podsecuritypolicy:authenticated annotations: kubernetes.io/description: 'Allow all authenticated users to create privileged pods.' labels: kubernetes.io/cluster-service: "true" ack.alicloud.com/component: pod-security-policy roleRef: apiGroup: rbac.authorization.k8s.io kind: ClusterRole name: ack:podsecuritypolicy:privileged subjects: - kind: Group apiGroup: rbac.authorization.k8s.io name: system:authenticated EOF

## 常见问题

### Pod创建失败，报错信息包含no providers available to validate pod request

问题现象

Pod创建失败，报错信息包含no providers available to validate pod request或者unable to validate against any pod security policy。

解决方案

当前集群内预置的Pod安全策略被误删除，需手动恢复对应资源。详见[配置或恢复](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md)[默认的](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md)[Pod](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md)[安全策略](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-pod-security-policies.md)。

### Pod创建失败，报错信息包含PodSecurityPolicy: unable to admit pod: pod.spec.securityContext.sysctls[0]: Forbidden: unsafe sysctl

问题现象

Pod创建失败，报错信息包含PodSecurityPolicy: unable to admit pod: [pod.spec.securityContext.sysctls[0]: Forbidden: unsafe sysctl "***" is not allowed]。

解决方案

出于安全考量，集群默认不允许创建使用“不安全”sysctl的 Pod。如需为特定应用开启此权限，可通过创建新的 Pod 安全策略来实现。

警告

请勿修改或删除以下集群预置的核心安全资源。ACK 集群的正常运行依赖这些核心资源。擅自修改可能导致集群功能异常，且相关更改可能会被系统自动重置。

- 

名为ack.privileged的 Pod 安全策略。

- 

名称以ack:podsecuritypolicy:开头的 Role、ClusterRole、RoleBinding 和 ClusterRoleBinding。

请通过新增 Pod 安全策略的方式，来配置所需的额外sysctl策略。

- 

使用以下内容，创建unsafe-sysctl-psp.yaml文件。

可按需调整allowedUnsafeSysctls的参数取值。--- apiVersion: policy/v1beta1 kind: PodSecurityPolicy metadata: name: psp.allow-unsafe-sysctls spec: allowedUnsafeSysctls: - '*' privileged: true allowPrivilegeEscalation: true allowedCapabilities: - '*' volumes: - '*' hostNetwork: true hostPorts: - min: 0 max: 65535 hostIPC: true hostPID: true runAsUser: rule: 'RunAsAny' seLinux: rule: 'RunAsAny' supplementalGroups: rule: 'RunAsAny' fsGroup: rule: 'RunAsAny' readOnlyRootFilesystem: false --- apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRole metadata: name: podsecuritypolicy:allow-unsafe-sysctls rules: - apiGroups: - policy resourceNames: - psp.allow-unsafe-sysctls resources: - podsecuritypolicies verbs: - use --- apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRoleBinding metadata: name: podsecuritypolicy:allow-unsafe-sysctls:authenticated roleRef: apiGroup: rbac.authorization.k8s.io kind: ClusterRole name: podsecuritypolicy:allow-unsafe-sysctls subjects: - kind: Group apiGroup: rbac.authorization.k8s.io name: system:authenticated

- 

在集群内创建相应资源。

kubectl create -f unsafe-sysctl-psp.yaml

预期输出：

podsecuritypolicy.policy/psp.allow-unsafe-sysctls created clusterrole.rbac.authorization.k8s.io/podsecuritypolicy:allow-unsafe-sysctls created clusterrolebinding.rbac.authorization.k8s.io/podsecuritypolicy:allow-unsafe-sysctls:authenticated created

- 

自定义节点池的kubelet参数，允许使用不安全的sysctl。详见[支持自定义的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-the-kubelet-configurations-of-a-node-pool.md)[kubelet](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-the-kubelet-configurations-of-a-node-pool.md)[参数](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-the-kubelet-configurations-of-a-node-pool.md)。

- 

部署一个使用不安全的sysctl的测试Pod。

可按需调整sysctls参数内容。如果集群中仅有部分节点（例如特定节点池中的节点）的kubelet配置了允许不安全的sysctl，还需为 Pod 添加nodeSelector，以确保Pod可被精确调度到目标节点上。cat <<EOF | kubectl apply -f - apiVersion: v1 kind: Pod metadata: name: sysctl-example spec: # nodeSelector: # alibabacloud.com/nodepool-id: npd912756*** # 替换为目标节点池ID securityContext: sysctls: - name: net.ipv4.tcp_syncookies value: "1" - name: net.core.somaxconn value: "1024" - name: net.ipv4.tcp_max_syn_backlog value: "65536" containers: - name: test image: nginx EOF

预期输出：

如果Pod运行时提示SysctlForbidden事件，表明运行该Pod的节点上的kubelet未配置允许使用不安全的sysctl。请检查并调整 Pod 的nodeSelector，确保被调度到已正确配置kubelet参数的节点。

pod/sysctl-example created

- 

## 相关文档

- 

[Pod Security Policies](https://kubernetes.io/docs/concepts/policy/pod-security-policy/)

[上一篇：使用仅加固模式访问ECS实例元数据](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/secure-access-to-ecs-instance-metadata.md)[下一篇：容器应用安全](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/container-security.md)

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
