# 已弃用 管理默认Pod安全策略-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/use-pod-security-policies

# 【已弃用】使用Pod安全策略
Kubernetes的Pod安全策略（Pod Security Policy）准入控制组件会基于您定义的规则验证在集群上创建和更新Pod的请求。如果创建或更新Pod的请求不符合定义的规则，系统将拒绝该请求并返回错误。本文将介绍如何在容器服务Kubernetes版ACK（Container Service for Kubernetes）中使用Pod安全策略。
## 前提条件
您已完成以下操作：
[创建一个](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[Kubernetes](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[集群](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。
[获取集群](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[KubeConfig](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[并通过](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。
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
$ cat <<EOF | kubectl apply -f - --- apiVersion: policy/v1beta1 kind: PodSecurityPolicy metadata: name: ack.privileged annotations: kubernetes.io/description: 'privileged allows full unrestricted access to pod features, as if the PodSecurityPolicy controller was not enabled.' seccomp.security.alpha.kubernetes.io/allowedProfileNames: '*' labels: kubernetes.io/cluster-service: "true" ack.alicloud.com/component: pod-security-policy spec: privileged: true allowPrivilegeEscalation: true allowedCapabilities: - '*' volumes: - '*' hostNetwork: true hostPorts: - min: 0 max: 65535 hostIPC: true hostPID: true runAsUser: rule: 'RunAsAny' seLinux: rule: 'RunAsAny' supplementalGroups: rule: 'RunAsAny' fsGroup: rule: 'RunAsAny' readOnlyRootFilesystem: false --- apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRole metadata: name: ack:podsecuritypolicy:privileged labels: kubernetes.io/cluster-service: "true" ack.alicloud.com/component: pod-security-policy rules: - apiGroups: - policy resourceNames: - ack.privileged resources: - podsecuritypolicies verbs: - use --- apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRoleBinding metadata: name: ack:podsecuritypolicy:authenticated annotations: kubernetes.io/description: 'Allow all authenticated users to create privileged pods.' labels: kubernetes.io/cluster-service: "true" ack.alicloud.com/component: pod-security-policy roleRef: apiGroup: rbac.authorization.k8s.io kind: ClusterRole name: ack:podsecuritypolicy:privileged subjects: - kind: Group apiGroup: rbac.authorization.k8s.io name: system:authenticated EOF
## 相关文档
[Pod Security Policies](https://kubernetes.io/docs/concepts/policy/pod-security-policy/)
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
