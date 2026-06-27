# 启用注册集群的API Server审计-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/distributed-cloud-container-platform-for-kubernetes/user-guide/use-cluster-auditing-in-registered-clusters

# 在注册集群中启用集群API Server审计功能
审计（Auditing）产生于API Server内部，用于记录对Kubernetes API的请求以及请求结果。ACK集群提供API Server的审计日志，帮助集群管理人员排查“什么人在什么时间对什么资源做了什么操作”，可用于追溯集群操作历史、排查集群故障等，降低集群安全运维压力。
## 前提条件
已创建注册集群，并将自建Kubernetes集群接入注册集群。具体操作，请参见[创建注册集群](create-ack-one-registered-clusters.md)。
## 步骤一：在Master节点上修改审计配置策略文件
依次登录所有Master节点，在审计配置策略文件的路径/etc/kubernetes/audit-policy.yaml，请根据以下内容修改审计配置策略：
说明
若您的集群版本低于1.24，apiVersion请使用audit.k8s.io/v1beta1，若集群版本大于等于1.24，则使用audit.k8s.io/v1。更多详细信息，请参见[Kubernetes 1.24](../../ack-managed-and-ack-dedicated/user-guide/kubernetes-1-24-release-notes.md)[版本说明](../../ack-managed-and-ack-dedicated/user-guide/kubernetes-1-24-release-notes.md)。
apiVersion: audit.k8s.io/v1beta1 kind: Policy # Don't generate audit events for all requests in RequestReceived stage. omitStages: - "RequestReceived" rules: # The following requests were manually identified as high-volume and low-risk, # so drop them. - level: None users: ["system:kube-proxy"] verbs: ["watch"] resources: - group: "" # core resources: ["endpoints", "services"] - level: None users: ["system:unsecured"] namespaces: ["kube-system"] verbs: ["get"] resources: - group: "" # core resources: ["configmaps"] - level: None users: ["kubelet"] # legacy kubelet identity verbs: ["get"] resources: - group: "" # core resources: ["nodes"] - level: None userGroups: ["system:nodes"] verbs: ["get"] resources: - group: "" # core resources: ["nodes"] - level: None users: - system:kube-controller-manager - system:kube-scheduler - system:serviceaccount:kube-system:endpoint-controller verbs: ["get", "update"] namespaces: ["kube-system"] resources: - group: "" # core resources: ["endpoints"] - level: None users: ["system:apiserver"] verbs: ["get"] resources: - group: "" # core resources: ["namespaces"] # Don't log these read-only URLs. - level: None nonResourceURLs: - /healthz* - /version - /swagger* # Don't log events requests. - level: None resources: - group: "" # core resources: ["events"] # Secrets, ConfigMaps, and TokenReviews can contain sensitive & binary data, # so only log at the Metadata level. - level: Metadata resources: - group: "" # core resources: ["secrets", "configmaps"] - group: authentication.k8s.io resources: ["tokenreviews"] # Get repsonses can be large; skip them. - level: Request verbs: ["get", "list", "watch"] resources: - group: "" # core - group: "admissionregistration.k8s.io" - group: "apps" - group: "authentication.k8s.io" - group: "authorization.k8s.io" - group: "autoscaling" - group: "batch" - group: "certificates.k8s.io" - group: "extensions" - group: "networking.k8s.io" - group: "policy" - group: "rbac.authorization.k8s.io" - group: "settings.k8s.io" - group: "storage.k8s.io" # Default level for known APIs - level: RequestResponse resources: - group: "" # core - group: "admissionregistration.k8s.io" - group: "apps" - group: "authentication.k8s.io" - group: "authorization.k8s.io" - group: "autoscaling" - group: "batch" - group: "certificates.k8s.io" - group: "extensions" - group: "networking.k8s.io" - group: "policy" - group: "rbac.authorization.k8s.io" - group: "settings.k8s.io" - group: "storage.k8s.io" # Default level for all other requests. - level: Metadata
## 步骤二：在Master节点上配置Kube API Server文件
依次登录所有Master节点机器，在Kube API Server文件的路径/etc/kubernetes/manifests/kube-apiserver.yaml，请完成以下相关配置：
根据以下示例添加command参数--audit-log-*：
... spec: containers: - command: - kube-apiserver - --audit-log-maxbackup=10 - --audit-log-maxsize=100 - --audit-log-path=/var/log/kubernetes/kubernetes.audit - --audit-log-maxage=30 - --audit-policy-file=/etc/kubernetes/audit-policy.yaml ...
根据以下示例添加env参数aliyun_logs_audit-*：
... spec: containers: - command: - kube-apiserver - --audit-log-maxbackup=10 - --audit-log-maxsize=100 - --audit-log-path=/var/log/kubernetes/kubernetes.audit - --audit-log-maxage=30 - --audit-policy-file=/etc/kubernetes/audit-policy.yaml ... ... env: - name: aliyun_logs_audit-${cluster_id} value: /var/log/kubernetes/kubernetes.audit - name: aliyun_logs_audit-${cluster_id}_tags value: audit=apiserver - name: aliyun_logs_audit-${cluster_id}_product value: k8s-audit - name: aliyun_logs_audit-${cluster_id}_jsonfile value: "true" image: registry-vpc.cn-shenzhen.aliyuncs.com/acs/kube-apiserver:v1.20.4-aliyun.1
重要
需要将{cluster_id}替换为您集群的Cluster ID。关于集群ID的获取，请参见[查看集群信息](../../ack-managed-and-ack-dedicated/user-guide/view-cluster-information.md)。
根据以下示例挂载/etc/kubernetes/audit-policy.yaml到API Server Pod。
... spec: containers: - command: - kube-apiserver - --audit-log-maxbackup=10 - --audit-log-maxsize=100 - --audit-log-path=/var/log/kubernetes/kubernetes.audit - --audit-log-maxage=30 - --audit-policy-file=/etc/kubernetes/audit-policy.yaml ... ... env: - name: aliyun_logs_audit-${cluster_id} value: /var/log/kubernetes/kubernetes.audit - name: aliyun_logs_audit-${cluster_id}_tags value: audit=apiserver - name: aliyun_logs_audit-${cluster_id}_product value: k8s-audit - name: aliyun_logs_audit-${cluster_id}_jsonfile value: "true" image: registry-vpc.cn-shenzhen.aliyuncs.com/acs/kube-apiserver:v1.20.4-aliyun.1 ... ... volumeMounts: - mountPath: /var/log/kubernetes name: k8s-audit - mountPath: /etc/kubernetes/audit-policy.yaml name: audit-policy readOnly: true ... ... volumes: - hostPath: path: /var/log/kubernetes type: DirectoryOrCreate name: k8s-audit - hostPath: path: /etc/kubernetes/audit-policy.yaml type: FileOrCreate name: audit-policy ...
## 步骤三：安装logtail-ds日志组件
关于安装logtail-ds日志组件的具体操作，请参见[步骤二：安装](enable-log-service-for-an-external-kubernetes-cluster.md)[logtail-ds](enable-log-service-for-an-external-kubernetes-cluster.md)[组件](enable-log-service-for-an-external-kubernetes-cluster.md)。
## 后续步骤
关于如何使用和查看集群API Server审计功能，请参见[使用集群](../../ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md)[API Server](../../ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md)[审计功能](../../ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md)。
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
