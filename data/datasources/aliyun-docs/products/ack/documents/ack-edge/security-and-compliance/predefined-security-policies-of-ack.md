# 集群策略管理内置规则列表与详解-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/predefined-security-policies-of-ack

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-edge/product-overview.md)

- [快速入门](products/ack/documents/ack-edge/quick-start.md)

- [操作指南](products/ack/documents/ack-edge/user-guide.md)

- [实践教程](products/ack/documents/ack-edge/use-cases.md)

- [安全合规](products/ack/documents/ack-edge/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-edge/developer-reference.md)

- [服务支持](products/ack/documents/ack-edge/support.md)

[首页](https://help.aliyun.com/zh)

# 容器安全策略规则库说明

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以为Pod配置安全策略，验证Pod部署和更新的请求是否安全。ACK集群策略管理功能提供多个内置规则库，包括Compliance、Infra、K8s-general、PSP和FinOps。

## 规则介绍

当前容器服务ACK容器安全策略规则库包含以下规则模板：

- 

Compliance：基于阿里云K8s加固等合规规范定制化的安全规则。

- 

Infra：用于增强和保护云基础设施层资源安全。

- 

K8s-general：用于约束和规范K8s集群内敏感资源配置，增强K8s集群内应用安全。

- 

PSP：用于替换K8s PSP的相关策略，使用该类策略可以实现等同于原ACK策略管理中PSP提供的安全约束能力。

- 

FinOps：用于成本治理流程中的控制与优化策略规则。

## 策略规则库说明

当前阿里云容器服务ACK内置如下类型的策略规则库，策略分类和简要说明如下：

| Category | Policy | Description | Severity |
| --- | --- | --- | --- |
| Compliance | ACKNoEnvVarSecrets | 限制 Secret 以 secretKeyRef 的形式挂载到应用 Pod 环境变量中。 | medium |
| ACKPodsRequireSecurityContext | 限制 Pod 中所有容器必须配置 securityContext 字段。 | low |  |
| ACKRestrictNamespaces | 限制资源部署在集群指定的命名空间中。 | low |  |
| ACKRestrictRoleBindings | 限制指定命名空间下的 rolebinding 使用指定范围内的 Role 或 Clusterrole。 | high |  |
| ACKNamespacesDeleteProtection | 限制指定的 Namespace 被误删除。 | medium |  |
| ACKServicesDeleteProtection | 防止 Namespace 中的 Service 实例被误删除。 | medium |  |
| ACKProtectBoundingPV | 防止绑定状态的持久化存储卷（PV）被删除。 | high |  |
| ACKBlockNodeDelete | 防止带有自定义标签的节点（Node）被删除。 | high |  |
| ACKResourceDeletionProtection | 防止带有自定义标签的多种资源（包括 Service、Namespace、Ingress 等）被删除。 | high |  |
| ACKProtectCoreDNS | 防止 kube-system 命名空间中 CoreDNS 相关资源被删除。 | high |  |
| Infra | ACKBlockProcessNamespaceSharing | 限制在集群指定范围部署的应用中使用 shareProcessNamespace 。 | high |
| ACKEmptyDirHasSizeLimit | 要求 emptyDir 类型的 Volume 必须指定 sizelimit 。 | low |  |
| ACKLocalStorageRequireSafeToEvict | 限制部署在集群指定范围内的 Pod 必须具有 "cluster-autoscaler.kubernetes.io/safe-to-evict": "true" 注释标签。默认情况下 autoscaler 在集群自动伸缩时不会驱逐使用 HostPath 或 EmptyDir 卷的 Pod。为了允许驱逐这些 Pod，必须在 Pod 上添加该注释标签。 | low |  |
| ACKOSSStorageLocationConstraint | 限制指定 Namespaces 下的部署只能使用指定 Region 中的阿里云 OSS 存储卷 | low |  |
| ACKPVSizeConstraint | 限制集群中创建的 PV 实例中能够申请的最大磁盘容量。 | medium |  |
| ACKPVCConstraint | 限制能够部署 PVC 实例的命名空间白名单列表以及限制 PVC 实例中能够申请的最大磁盘容量。 | medium |  |
| ACKBlockVolumeTypes | 限制在集群指定范围内部署的 Pod 禁止使用的 Volume 挂载类型。 | medium |  |
| ASMSidecarInjectionEnforced | 限制 Pod 必须注入 ASM Sidecar。 | high |  |
| K8s-general | ACKAllowedRepos | 限制在集群指定范围部署的应用 Pod 中拉取白名单列表外的镜像。 | high |
| ACKBlockAutoinjectServiceEnv | 要求在应用中配置 enableServiceLinks: false 防止在 Pod 环境变量中透出服务 IP。 | low |  |
| ACKBlockAutomountToken | 要求在应用中设置 automountServiceAccountToken: false 字段以防止自动挂载 serviceaccount 。 | high |  |
| ACKBlockEphemeralContainer | 限制在集群指定范围的应用 Pod 中启动临时容器。 | medium |  |
| ACKBlockLoadBalancer | 限制在集群指定范围内部署 LoadBalancer 类型的 Service。 | high |  |
| ACKBlockNodePort | 限制在集群指定范围内使用 NodePort 类型的 Service。 | high |  |
| ACKContainerLimits | 要求集群指定范围的应用 Pod 配置资源 limits 。 | low |  |
| ACKExternalIPs | 限制在集群指定范围内的 Service 实例使用白名单范围之外的 externalIPs。 | high |  |
| ACKImageDigests | 限制在集群指定范围内部署不符合 digest 格式的镜像。 | low |  |
| ACKRequiredLabels | 限制在集群指定范围内部署没有指定范式 label 标签的应用。 | low |  |
| ACKRequiredProbes | 限制在集群指定范围内部署的 Pod 配置指定类型的 readinessProbe 和 livenessProbe。 | medium |  |
| ACKCheckNginxPath | 限制在 Ingress 实例的 spec.rules[].http.paths[].path 字段中使用危险配置。Ingress-nginx 1.2.1 以下版本建议开启该策略。 | high |  |
| ACKCheckNginxAnnotation | 限制在 Ingress 实例的 metadata.annotations 字段中使用危险配置。Ingress-nginx 1.2.1 以下版本建议开启该策略。 | high |  |
| ACKBlockInternetLoadBalancer | 限制创建公网类型的 LoadBalancer Service。 | high |  |
| RatifyVerification | 您在集群中安装应用市场组件 Ratify 后，可以验证在集群指定范围内部署的 Pod 镜像中的签名或 SBOM 等安全元数据。 | high |  |
| PSP | ACKPSPAllowPrivilegeEscalationContainer | 限制在集群指定范围内部署的 Pod 配置 allowPrivilegeEscalation 参数。 | medium |
| ACKPSPAllowedUsers | 限制在集群指定范围内部署的 Pod 中的启动 user 、 group 、 supplementalGroups 以及 fsGroup 。 | medium |  |
| ACKPSPAppArmor | 限制在集群指定范围内部署的 Pod 配置 AppArmor。 | low |  |
| ACKPSPCapabilities | 限制在集群指定范围内部署的 Pod 配置 Linux Capabilities 能力。 | high |  |
| ACKPSPFSGroup | 限制在集群指定范围内部署的 Pod 配置 fsGroup。 | medium |  |
| ACKPSPFlexVolumes | 限制在集群指定范围内部署 Pod 的 FlexVolume 驱动配置。 | medium |  |
| ACKPSPForbiddenSysctls | 限制在集群指定范围内部署 Pod 的禁止的 Sysctl 范围。 | high |  |
| ACKPSPHostFilesystem | 限制在集群指定范围内部署的 Pod 允许挂载的主机 host 目录范围。 | high |  |
| ACKPSPHostNamespace | 限制在集群指定范围内部署的 Pod 是否允许共享主机 host 命名空间。 | high |  |
| ACKPSPHostNetworkingPorts | 限制在集群指定范围内部署的 Pod 使用主机网络和指定端口。 | high |  |
| ACKPSPPrivilegedContainer | 限制在集群指定范围内部署的 Pod 中启动特权容器。 | high |  |
| ACKPSPProcMount | 限制在集群指定范围内部署的 Pod 允许挂载的 Proc 类型。 | low |  |
| ACKPSPReadOnlyRootFilesystem | 限制在集群指定范围内部署的 Pod 使用只读的根文件系统。 | medium |  |
| ACKPSPSELinuxV2 | 限制在集群指定范围内部署的 Pod 必须使用 AllowedSELinuxOptions 参数中规定的 Selinux 配置。 | low |  |
| ACKPSPSeccomp | 限制在集群指定范围内部署的 Pod 使用指定的 Seccomp 配置文件。 | low |  |
| ACKPSPVolumeTypes | 限制在集群指定范围内部署的 Pod 使用指定的 Volume 挂载类型。 | medium |  |
| FinOps | ACKContainerRequests | 要求集群中某些应用 Pod 必须声明资源 requests 。 | low |
| ACKContainerResourcesWhitelist | 要求集群中某些应用 Pod 的 CPU 和内存资源配置必须从预设选项中选取。 | low |  |
| ACKContainerResourcesRange | 限制集群中某些应用 Pod 的资源配置必须在指定的上下限范围内。 | low |  |
| ACKRequiredNodeSelector | 限制集群中某些应用 Pod 必须配置指定的 nodeSelector 标签。 | low |  |
| ACKWorkloadReplicasRange | 限制应用副本数量的上下限。 | low |  |
| ACKRestrictALBCreation | 强制复用已有 ALB 实例，禁止通过 ALBConfig 创建新的 ALB 资源实例。 | low |  |


## Compliance

### ACKNoEnvVarSecrets

规则说明：限制Secret以secretKeyRef的形式挂载到应用Pod环境变量中使用。

重要等级：medium。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKNoEnvVarSecrets metadata: name: no-env-var-secrets spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["test-gatekeeper"]

Allowed：

apiVersion: v1 kind: Pod metadata: name: mypod namespace: test-gatekeeper spec: containers: - name: mypod image: redis volumeMounts: - name: foo mountPath: "/etc/foo" volumes: - name: foo secret: secretName: mysecret items: - key: username path: my-group/my-username

Disallowed：

apiVersion: v1 kind: Pod metadata: name: bad namespace: test-gatekeeper spec: containers: - name: mycontainer image: redis env: - name: SECRET_USERNAME valueFrom: secretKeyRef: name: mysecret key: username - name: SECRET_PASSWORD valueFrom: secretKeyRef: name: mysecret key: password restartPolicy: Never

### ACKPodsRequireSecurityContext

规则说明：限制Pod中所有容器必须配置securitycontext字段。

重要等级：low。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPodsRequireSecurityContext metadata: name: pods-require-security-context annotations: description: "Requires that Pods must have a `securityContext` defined." spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["test-gatekeeper"]

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: test namespace: test-gatekeeper spec: securityContext: runAsNonRoot: false containers: - image: test name: test resources: {} dnsPolicy: ClusterFirst restartPolicy: Never status: {}

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: containers: - image: test name: test2 - image: test name: test resources: {} securityContext: runAsNonRoot: false

### ACKRestrictNamespaces

规则说明：限制资源部署在集群指定的命名空间中。

重要等级：low。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| restrictedNamespaces | array | 禁止资源部署在该参数声明的列表中。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKRestrictNamespaces metadata: name: restrict-default-namespace annotations: description: "Restricts resources from using the restricted namespace." spec: match: kinds: - apiGroups: [''] kinds: ['Pod'] parameters: restrictedNamespaces: - "test-gatekeeper"

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: test namespace: non-test-gatekeeper spec: containers: - image: test name: test resources: {} dnsPolicy: ClusterFirst restartPolicy: Never status: {}

Disallowed：

apiVersion: v1 kind: Pod metadata: name: bad namespace: test-gatekeeper spec: containers: - name: mycontainer image: redis restartPolicy: Never

### ACKRestrictRoleBindings

规则说明：限制在指定命名空间下的Rolebinding使用指定范围内的Role或Clusterrole。

重要等级：high。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| restrictedRole | object | 限制使用的 Clusterrole 或 Role。 |
| allowedSubjects | array | 允许挂载的 Subjects 白名单列表。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKRestrictRoleBindings metadata: name: restrict-clusteradmin-rolebindings annotations: description: "Restricts use of sensitive role in specific rolebinding." spec: match: kinds: - apiGroups: ["rbac.authorization.k8s.io"] kinds: ["RoleBinding"] parameters: restrictedRole: apiGroup: "rbac.authorization.k8s.io" kind: "ClusterRole" name: "cluster-admin" allowedSubjects: - apiGroup: "rbac.authorization.k8s.io" kind: "Group" name: "system:masters"

Allowed：

kind: RoleBinding apiVersion: rbac.authorization.k8s.io/v1 metadata: name: good-2 namespace: test-gatekeeper subjects: - kind: Group name: 'system:masters' roleRef: kind: ClusterRole name: cluster-admin apiGroup: rbac.authorization.k8s.io

Disallowed：

kind: RoleBinding apiVersion: rbac.authorization.k8s.io/v1 metadata: name: bad-1 namespace: test-gatekeeper subjects: - kind: ServiceAccount name: policy-template-controller roleRef: kind: ClusterRole name: cluster-admin apiGroup: rbac.authorization.k8s.io

### ACKNamespacesDeleteProtection

规则说明：限制指定的Namespace被误删除。可以通过protectionNamespaces参数配置受保护命名空间的Name。

使用前提：需确保gatekeeper组件已升级至v3.10.0.130-g0e79597d-aliyun或以上版本。关于gatekeeper组件版本信息，请参见[gatekeeper](products/ack/documents/product-overview/gatekeeper.md)。

重要等级：medium。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| protectionNamespaces | array | 受保护 Namespace 的名称列表。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKNamespacesDeleteProtection metadata: name: namespace-delete-protection spec: match: kinds: - apiGroups: [''] kinds: ['Namespace'] parameters: protectionNamespaces: - test-gatekeeper

Allowed：

apiVersion: v1 kind: Namespace metadata: name: will-delete

Disallowed：

apiVersion: v1 kind: Namespace metadata: name: test-gatekeeper

### ACKServicesDeleteProtection

规则说明：限制指定Namespace中的Service实例被误删除，可以通过protectionServices参数配置受保护的Service实例名称。

重要等级：medium。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| protectionServices | array | 指定命名空间下受保护的 Service 实例名称列表。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKServicesDeleteProtection metadata: name: service-delete-protection annotations: description: "Protect to delete specific service." spec: enforcementAction: deny match: kinds: - apiGroups: [''] kinds: ['Service'] namespaces: ["test-gatekeeper"] parameters: protectionServices: - test-svc

Allowed：

apiVersion: v1 kind: Service metadata: name: good namespace: test-gatekeeper

Disallowed：

apiVersion: v1 kind: Service metadata: name: test-svc

### ACKProtectBoundingPV

规则说明：防止集群中绑定到持久化存储卷声明（PVC）的持久化存储卷（PV）被删除。

重要等级：high。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKProtectBoundingPV metadata: name: protect-pv-deletion spec: enforcementAction: deny match: kinds: - apiGroups: - "" kinds: - PersistentVolume

Allowed：

apiVersion: v1 kind: PersistentVolume metadata: name: test-pv-bound-should-be-blocked spec: accessModes: - ReadWriteOnce capacity: storage: 1Gi persistentVolumeReclaimPolicy: Retain storageClassName: manual-sc hostPath: path: /tmp/data type: DirectoryOrCreate status: phase: Released

Disallowed：

apiVersion: v1 kind: PersistentVolume metadata: name: test-pv-bound-should-be-blocked spec: accessModes: - ReadWriteOnce capacity: storage: 1Gi persistentVolumeReclaimPolicy: Retain storageClassName: manual-sc hostPath: path: /tmp/data type: DirectoryOrCreate status: phase: Bound

### ACKBlockNodeDelete

规则说明：防止集群中带有自定义标签的节点（Node）被删除。可定义多组键值对，节点只要满足其中任意一对即可受到保护。

重要等级：high。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| protectedLabels | array | 自定义标签，用于识别需要被保护的节点。 |
| protectedLabels.labelName | string | 自定义标签的键。 |
| protectedLabels.labelValue | string | 自定义标签的值。 |


示例：

Constraint:

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockNodeDelete metadata: name: block-node-delete spec: enforcementAction: deny match: kinds: - apiGroups: ["*"] kinds: ["Node"] parameters: protectedLabels: - labelName: policy.alibabacloud.vpc.com/node-delete-protection labelValue: "true" - labelName: policy.alibabacloud.com/node-delete-protection labelValue: "true"

Allowed：

apiVersion: v1 kind: Node metadata: name: cn-hangzhou-1

Disallowed：

apiVersion: v1 kind: Node metadata: labels: policy.alibabacloud.vpc.com/node-delete-protection: "true" name: cn-hangzhou-1 --- apiVersion: v1 kind: Node metadata: labels: policy.alibabacloud.vpc.com/node-delete-protection: "true" name: cn-hangzhou-2 --- apiVersion: v1 kind: Node metadata: labels: policy.alibabacloud.com/node-delete-protection: "true" policy.alibabacloud.vpc.com/node-delete-protection: "true" name: cn-hangzhou-3

### ACKResourceDeletionProtection

规则说明：防止集群中带有自定义标签的资源被删除。支持Service、Namespace、Ingress、Deployment、StatefulSet、DaemonSet、Job、CronJob等资源类型。可定义多组键值对，资源只要满足其中任意一对即可受到保护。

重要等级：high。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| labels | array | 自定义标签，用于识别需要被保护的节点。 |
| labels.labelName | string | 自定义标签的键。 |
| labels.labelValue | string | 自定义标签的值。 |


示例：

Constraint:

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKResourceDeletionProtection metadata: name: resource-deletion-protection annotations: description: "Protect resources from being accidentally deleted." spec: enforcementAction: deny match: kinds: - apiGroups: - "" kinds: - Service - Namespace - apiGroups: - extensions - networking.k8s.io kinds: - Ingress - apiGroups: - apps kinds: - Deployment - StatefulSet - DaemonSet - apiGroups: - batch kinds: - Job - CronJob parameters: labels: - labelName: policy.alibabacloud.com/delete-protection labelValue: "true"

Allowed：

apiVersion: apps/v1 kind: Deployment metadata: name: test-deployment namespace: test-gatekeeper spec: replicas: 2 selector: matchLabels: app: test-app template: metadata: labels: app: test-app spec: containers: - name: nginx image: nginx:latest ports: - containerPort: 80

Disallowed：

apiVersion: apps/v1 kind: Deployment metadata: name: test-deployment namespace: test-gatekeeper labels: policy.alibabacloud.com/delete-protection: "true" spec: replicas: 2 selector: matchLabels: app: test-app template: metadata: labels: app: test-app spec: containers: - name: nginx image: nginx:latest ports: - containerPort: 80

### ACKProtectCoreDNS

规则说明：防止kube-system命名空间中CoreDNS相关资源被删除，包括其使用的Deployment、Service和ConfigMap。

重要等级：high。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| min_replicas | int | 定义 CoreDNS Deployment 期望的最小副本数量。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKProtectCoreDNS metadata: name: coredns-protect-rule spec: enforcementAction: deny match: kinds: - apiGroups: ["*"] kinds: ["Deployment", "Service", "Scale", "ConfigMap" ] scope: "Namespaced" namespaces: ["kube-system"] parameters: min_replicas: 2

Allowed：

apiVersion: apps/v1 kind: Deployment metadata: name: coredns namespace: kube-system spec: replicas: 3 selector: matchLabels: k8s-app: kube-dns template: metadata: labels: k8s-app: kube-dns spec: containers: - name: coredns image: registry-cn-hangzhou-vpc.ack.aliyuncs.com/acs/coredns:latest imagePullPolicy: IfNotPresent

Disallowed：

apiVersion: apps/v1 kind: Deployment metadata: name: coredns namespace: kube-system spec: replicas: 1 selector: matchLabels: k8s-app: kube-dns template: metadata: labels: k8s-app: kube-dns spec: containers: - name: coredns image: registry-cn-hangzhou-vpc.ack.aliyuncs.com/acs/coredns:latest imagePullPolicy: IfNotPresent --- apiVersion: v1 data: Corefile: "" kind: ConfigMap metadata: name: coredns namespace: kube-system --- apiVersion: v1 kind: Service metadata: labels: k8s-app: kube-dns kubernetes.io/cluster-service: "true" kubernetes.io/name: KubeDNS name: kube-dns namespace: kube-system

## Infra

### ACKBlockProcessNamespaceSharing

规则说明：限制在集群指定范围部署的应用中使用shareProcessNamespace。

重要等级：high。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockProcessNamespaceSharing metadata: name: block-share-process-namespace spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["test-gatekeeper"]

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: test-3 namespace: test-gatekeeper spec: containers: - image: test name: test resources: {} dnsPolicy: ClusterFirst restartPolicy: Never status: {}

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: shareProcessNamespace: true containers: - image: test name: test resources: {} dnsPolicy: ClusterFirst restartPolicy: Never status: {}

### ACKEmptyDirHasSizeLimit

规则说明：要求emptyDir类型的Volume必须指定sizelimit。

重要等级：low。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKEmptyDirHasSizeLimit metadata: name: empty-dir-has-sizelimit spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["test-gatekeeper"]

Allowed：

apiVersion: v1 kind: Pod metadata: name: test-1 namespace: test-gatekeeper spec: containers: - image: k8s.gcr.io/test-webserver name: test-container volumeMounts: - mountPath: /cache name: cache-volume volumes: - name: cache-volume emptyDir: sizeLimit: "10Mi"

Disallowed：

apiVersion: v1 kind: Pod metadata: name: bad namespace: test-gatekeeper spec: containers: - image: k8s.gcr.io/test-webserver name: test-container volumeMounts: - mountPath: /cache name: cache-volume volumes: - name: cache-volume emptyDir: {}

### ACKLocalStorageRequireSafeToEvict

规则说明：限制部署在集群指定范围内的Pod必须具有"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"注释标签。集群自动伸缩时不会删除没有此注释标签的Pod。

重要等级：low。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKLocalStorageRequireSafeToEvict metadata: name: local-storage-require-safe-to-evict spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["test-gatekeeper"]

Allowed：

apiVersion: v1 kind: Pod metadata: name: test-1 namespace: test-gatekeeper annotations: 'cluster-autoscaler.kubernetes.io/safe-to-evict': 'true' spec: containers: - image: k8s.gcr.io/test-webserver name: test-container volumeMounts: - mountPath: /test-pd name: test-volume volumes: - name: test-volume hostPath: # directory location on host path: /data # this field is optional type: Directory

Disallowed：

apiVersion: v1 kind: Pod metadata: name: bad namespace: test-gatekeeper spec: containers: - image: k8s.gcr.io/test-webserver name: test-container volumeMounts: - mountPath: /cache name: cache-volume volumes: - name: cache-volume emptyDir: {}

### ACKOSSStorageLocationConstraint

规则说明：限制指定命名空间下的部署只能使用指定地域中的阿里云OSS存储卷。

重要等级：low。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| mode | string | 是否采用白名单模式，默认值 allowlist 为白名单模式，其他值为黑名单模式。 |
| regions | array | 指定的阿里云 Region ID 列表。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKOSSStorageLocationConstraint metadata: name: restrict-oss-location annotations: description: "Restricts location of oss storage in cluster." spec: match: kinds: - apiGroups: [""] kinds: ["PersistentVolume", "Pod"] namespaces: - "test-gatekeeper" parameters: mode: "allowlist" regions: - "cn-beijing"

Allowed：

apiVersion: v1 kind: Pod metadata: name: pod-oss-csi-good namespace: test-gatekeeper spec: containers: - name: test image: test volumes: - name: test csi: driver: ossplugin.csi.alibabacloud.com volumeAttributes: bucket: "oss" url: "oss-cn-beijing.aliyuncs.com" otherOpts: "-o max_stat_cache_size=0 -o allow_other" path: "/"

Disallowed：

apiVersion: v1 kind: Pod metadata: name: pod-oss-csi namespace: test-gatekeeper spec: containers: - name: test image: test volumes: - name: test csi: driver: ossplugin.csi.alibabacloud.com nodePublishSecretRef: name: oss-secret volumeAttributes: bucket: "oss" url: "oss-cn-hangzhou.aliyuncs.com" otherOpts: "-o max_stat_cache_size=0 -o allow_other" path: "/"

### ACKPVSizeConstraint

规则说明：限制集群中创建的PV实例中能够申请的最大磁盘容量。

重要等级：medium。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| maxSize | string | PV 实例中能申请的最大磁盘容量，默认为 50 GiB。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPVSizeConstraint metadata: name: limit-pv-size annotations: description: "Limit the pv storage capacity size within a specified maximum amount." spec: enforcementAction: deny match: kinds: - apiGroups: [ "" ] kinds: [ "PersistentVolume" ] parameters: maxSize: "50Gi"

Allowed：

apiVersion: v1 kind: PersistentVolume metadata: name: pv-oss-csi labels: alicloud-pvname: pv-oss spec: capacity: storage: 25Gi accessModes: - ReadWriteMany persistentVolumeReclaimPolicy: Retain csi: driver: ossplugin.csi.alibabacloud.com volumeHandle: pv-oss nodePublishSecretRef: name: oss-secret namespace: default volumeAttributes: bucket: "oss" url: "oss-cn-beijing.aliyuncs.com" otherOpts: "-o max_stat_cache_size=0 -o allow_other" path: "/"

Disallowed：

apiVersion: v1 kind: PersistentVolume metadata: name: pv-oss-csi-bad labels: alicloud-pvname: pv-oss spec: capacity: storage: 500Gi accessModes: - ReadWriteMany persistentVolumeReclaimPolicy: Retain csi: driver: ossplugin.csi.alibabacloud.com volumeHandle: pv-oss nodePublishSecretRef: name: oss-secret namespace: default volumeAttributes: bucket: "oss" url: "oss-cn-beijing.aliyuncs.com" otherOpts: "-o max_stat_cache_size=0 -o allow_other" path: "/"

### ACKPVCConstraint

规则说明：限制能够部署PVC实例的命名空间白名单列表以及限制PVC实例中能够申请的最大磁盘容量。

重要等级：medium

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| maxSize | string | PV 实例中能申请的最大磁盘容量，默认为 50 GiB。 |
| allowNamespaces | array | 能够部署 PVC 实例的命名空间白名单列表。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPVCConstraint metadata: name: limit-pvc-size-and-ns annotations: description: "Limit the maximum pvc storage capacity size and the namespace whitelists that can be deployed." spec: enforcementAction: deny match: kinds: - apiGroups: [ "" ] kinds: [ "PersistentVolumeClaim" ] parameters: maxSize: "50Gi" allowNamespaces: - "test-gatekeeper"

Allowed：

apiVersion: v1 kind: PersistentVolumeClaim metadata: name: disk-pvc namespace: test-gatekeeper spec: accessModes: - ReadWriteOnce resources: requests: storage: 20Gi

Disallowed：

apiVersion: v1 kind: PersistentVolumeClaim metadata: name: bad-disk-pvc namespace: test-gatekeeper spec: accessModes: - ReadWriteOnce resources: requests: storage: 200Gi --- apiVersion: v1 kind: PersistentVolumeClaim metadata: name: bad-namespace-pvc namespace: test-gatekeeper-bad spec: accessModes: - ReadWriteOnce resources: requests: storage: 20Gi

### ACKBlockVolumeTypes

规则说明：限制在集群指定范围内部署的Pod禁止使用的Volume挂载类型。

重要等级：medium

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| volumes | array | 禁止使用的 Volume 挂载类型列表。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockVolumeTypes metadata: name: block-volume-types spec: enforcementAction: deny match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["test-gatekeeper"] parameters: volumes: - "gitRepo"

Allowed：

apiVersion: v1 kind: Pod metadata: name: use-empty-dir namespace: test-gatekeeper spec: containers: - name: test image: test volumes: - name: emptydir-volume emptyDir: {}

Disallowed：

apiVersion: v1 kind: Pod metadata: name: use-git-repo namespace: test-gatekeeper spec: containers: - name: test image: test volumes: - name: git-volume gitRepo: repository: "git@***:***/my-git-repository.git" revision: "22f1d8406d464b0c08***"

### ASMSidecarInjectionEnforced

规则说明：限制Pod必须注入ASM Sidecar。

重要等级：high

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ASMSidecarInjectionEnforced metadata: name: asm-sidecar-injectionen-forced spec: enforcementAction: deny match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["test-gatekeeper"]

Allowed：

apiVersion: v1 kind: Pod metadata: name: sidecar-injection namespace: test-gatekeeper spec: containers: - name: test image: test - name: istio-proxy image: xxx/proxyv2:xxx

Disallowed：

apiVersion: v1 kind: Pod metadata: name: sidecar-injection namespace: test-gatekeeper spec: containers: - name: test image: test

## K8s-general

### ACKAllowedRepos

规则说明：限制在集群指定范围部署的应用Pod中拉取白名单列表外的镜像。

重要等级：high。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| repos | array | 合法的镜像仓库白名单。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKAllowedRepos metadata: name: allowed-repos spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: repos: - "registry-vpc.cn-hangzhou.aliyuncs.com/acs/" - "registry.cn-hangzhou.aliyuncs.com/acs/"

Allowed：

apiVersion: v1 kind: Pod metadata: name: pod-01 namespace: test-gatekeeper spec: containers: - image: registry.cn-hangzhou.aliyuncs.com/acs/test-webserver name: test-container-1 initContainers: - image: registry.cn-hangzhou.aliyuncs.com/acs/test-webserver name: test-container

Disallowed：

apiVersion: v1 kind: Pod metadata: name: bad-1 namespace: test-gatekeeper spec: containers: - image: k8s.gcr.io/test-webserver name: test-container initContainers: - image: k8s.gcr.io/test-webserver name: test-container-3

### ACKBlockAutoinjectServiceEnv

规则说明：要求在应用中配置enableServiceLinks: false防止在Pod环境变量中透出服务IP。

重要等级：low。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockAutoinjectServiceEnv metadata: name: block-auto-inject-service-env spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper"

Allowed：

apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: enableServiceLinks: false containers: - image: openpolicyagent/test-webserver:1.0 name: test-container

Disallowed：

apiVersion: v1 kind: Pod metadata: name: bad-1 namespace: test-gatekeeper spec: containers: - image: k8s.gcr.io/test-webserver name: test-container

### ACKBlockAutomountToken

规则说明：要求在应用中设置automountServiceAccountToken: false字段防止自动挂载serviceaccount。

重要等级：high。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockAutomountToken metadata: name: block-auto-mount-service-account-token spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper"

Allowed：

apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: automountServiceAccountToken: false containers: - image: openpolicyagent/test-webserver:v1.0 name: test-container

Disallowed：

apiVersion: v1 kind: Pod metadata: name: bad-1 namespace: test-gatekeeper spec: containers: - image: k8s.gcr.io/test-webserver name: test-container

### ACKBlockEphemeralContainer

规则说明：限制在集群指定范围的应用Pod中启动临时容器。

重要等级：medium。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockEphemeralContainer metadata: name: block-ephemeral-container spec: enforcementAction: deny match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper"

Allowed：

apiVersion: v1 kind: Pod metadata: name: hello-pod namespace: test-gatekeeper spec: containers: - name: hello-pod image: redis

Disallowed：

- 

基于已有Pod启动临时容器。

kubectl debug -it hello-pod -n test-gatekeeper --image=test --target=hello-pod

- 

预期输出：

Error from server (Forbidden): admission webhook "validation.gatekeeper.sh" denied the request: [block-ephemeral-container-w5c6n] Creating ephemeral containers is disallowed, pod: hello-pod

### ACKBlockLoadBalancer

规则说明：限制在指定集群范围内部署LoadBalancer类型的Service。

重要等级：high。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| restrictedNamespaces | array | 禁止资源部署在该参数声明的列表中。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockLoadBalancer metadata: name: block-load-balancer spec: match: kinds: - apiGroups: [""] kinds: ["Service"] namespaces: - "test-gatekeeper"

Allowed：

apiVersion: v1 kind: Service metadata: name: my-service-1 namespace: test-gatekeeper spec: selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376

Disallowed：

apiVersion: v1 kind: Service metadata: name: my-service namespace: test-gatekeeper spec: type: LoadBalancer selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376

### ACKBlockNodePort

规则说明：限制在集群指定范围内使用NodePort类型的Service。

重要等级：low。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockNodePort metadata: name: block-node-port spec: match: kinds: - apiGroups: [""] kinds: ["Service"] namespaces: - "test-gatekeeper"

Allowed：

apiVersion: v1 kind: Service metadata: name: my-service-1 namespace: test-gatekeeper spec: selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376

Disallowed：

apiVersion: v1 kind: Service metadata: name: my-service namespace: test-gatekeeper spec: type: NodePort selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376

### ACKContainerLimits

规则说明：要求集群指定范围的应用Pod配置资源limits。

重要等级：low。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKContainerLimits metadata: name: container-must-have-limits spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: cpu: "1000m" memory: "1Gi"

Allowed：

apiVersion: v1 kind: Pod metadata: name: pod-1 namespace: test-gatekeeper spec: containers: - image: openpolicyagent/test-webserver name: test-container resources: limits: memory: "100Mi" cpu: "500m"

Disallowed：

apiVersion: v1 kind: Pod metadata: name: pod-2 namespace: non-test-gatekeeper spec: containers: - image: openpolicyagent/test-webserver name: test-container resources: limits: memory: "100Gi" cpu: "2000m"

### ACKExternalIPs

规则说明：限制在集群指定范围内的Service实例使用白名单范围之外的externalIPs。

重要等级：high。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| allowedIPs | array | externalIPs 白名单列表。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKExternalIPs metadata: name: external-ips spec: match: kinds: - apiGroups: [""] kinds: ["Service"] namespaces: - "test-gatekeeper" parameters: allowedIPs: - "192.168.0.5"

Allowed：

apiVersion: v1 kind: Service metadata: name: my-service-3 namespace: test-gatekeeper spec: selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376

Disallowed：

apiVersion: v1 kind: Service metadata: name: my-service namespace: test-gatekeeper spec: selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376 externalIPs: - 80.11.XX.XX

### ACKImageDigests

规则说明：限制在集群指定范围内部署不符合digest格式的镜像。

重要等级：low。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKImageDigests metadata: name: container-image-must-have-digest spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper"

Allowed：

apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: containers: - image: openpolicyagent/test-webserver@sha256:12e469267d21d66ac9dcae33a4d3d202ccb2591869270b95d0aad7516c7d075b name: test-container

Disallowed：

apiVersion: v1 kind: Pod metadata: name: bad-1 namespace: test-gatekeeper spec: containers: - image: k8s.gcr.io/test-webserver name: test-container initContainers: - image: k8s.gcr.io/test-webserver name: test-container2

### ACKRequiredLabels

规则说明：校验 Pod 是否包含特定的标签（Labels），并确保标签值符合预定义格式。支持为每个标签键（Key）指定一个正则表达式，用于验证其值（Value）。还可通过optional来控制标签校验的强制性。

重要等级：low。

参数说明：

- 

- 

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| allowedRegex | string | Label 白名单的正则表达式。 |
| key | string | 待校验的标签 Key。 |
| optional | bool | 是否允许 Pod 缺少此标签。 true ：允许缺少，仅在标签存在时校验。包含时，其值必须通过正则校验。 false ：不允许缺少，标签必须存在且通过校验。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKRequiredLabels metadata: name: must-have-label-test spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: labels: - key: test allowedRegex: "^test.*$" - key: env allowedRegex: "^(dev|prod)$" optional: true

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null name: test namespace: test-gatekeeper labels: 'test': 'test_233' spec: containers: - name: mycontainer image: redis

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null name: bad2 namespace: test-gatekeeper labels: 'test': '233' 'env': 'invalid' spec: containers: - name: mycontainer image: redis

### ACKRequiredProbes

规则说明：限制在集群指定范围内部署的Pod配置指定类型的readinessProbe和livenessProbe。

重要等级：medium。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| probes | array | Pod 中需要配置的 Probe。例如， readinessProbe 和 livenessProbe 。 |
| probeTypes | array | Pod 中需要配置的 Probe 类型。例如， tcpSocket ， httpGet 和 exec 类型。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKRequiredProbes metadata: name: must-have-probes spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: probes: ["readinessProbe", "livenessProbe"] probeTypes: ["tcpSocket", "httpGet", "exec"]

Allowed：

apiVersion: v1 kind: Pod metadata: name: p4 namespace: test-gatekeeper spec: containers: - name: liveness image: k8s.gcr.io/busybox readinessProbe: exec: command: - cat - /tmp/healthy initialDelaySeconds: 5 periodSeconds: 5 livenessProbe: exec: command: - cat - /tmp/healthy initialDelaySeconds: 5 periodSeconds: 5

Disallowed：

apiVersion: v1 kind: Pod metadata: name: p1 namespace: test-gatekeeper spec: containers: - name: liveness image: k8s.gcr.io/busybox

### ACKCheckNginxPath

限制在Ingress实例spec.rules[].http.paths[].path字段中使用危险配置，Ingress-nginx 1.2.1以下版本建议开启该策略。

重要等级：high。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKCheckNginxPath metadata: name: block-nginx-path spec: enforcementAction: deny match: kinds: - apiGroups: ["extensions", "networking.k8s.io"] kinds: ["Ingress"] namespaces: - "test-gatekeeper"

Allowed：

apiVersion: networking.k8s.io/v1 kind: Ingress metadata: name: good-paths namespace: test-gatekeeper spec: rules: - host: cafe.example.com http: paths: - path: /tea pathType: Prefix backend: service: name: tea-svc port: number: 80 - path: /coffee pathType: Prefix backend: service: name: coffee-svc port: number: 80

Disallowed：

apiVersion: networking.k8s.io/v1 kind: Ingress metadata: name: bad-path-secrets namespace: test-gatekeeper spec: rules: - host: cafe.example.com http: paths: - path: /var/run/secrets pathType: Prefix backend: service: name: tea-svc port: number: 80

### ACKCheckNginxAnnotation

限制在Ingress实例metadata.annotations字段中使用危险配置，Ingress-nginx 1.2.1以下版本建议开启该策略。

重要等级：high。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKCheckNginxAnnotation metadata: name: block-nginx-annotation spec: match: kinds: - apiGroups: ["extensions", "networking.k8s.io"] kinds: ["Ingress"] namespaces: - "test-gatekeeper"

Allowed：

apiVersion: networking.k8s.io/v1 kind: Ingress metadata: name: good-annotations namespace: test-gatekeeper annotations: nginx.org/good: "value" spec: rules: - host: cafe.example.com http: paths: - path: /tea pathType: Prefix backend: service: name: tea-svc port: number: 80 - path: /coffee pathType: Prefix backend: service: name: coffee-svc port: number: 80

Disallowed：

apiVersion: networking.k8s.io/v1 kind: Ingress metadata: name: var-run-secrets namespace: test-gatekeeper annotations: nginx.org/bad: "/var/run/secrets" spec: rules: - host: cafe.example.com http: paths: - path: /tea pathType: Prefix backend: service: name: tea-svc port: number: 80 - path: /coffee pathType: Prefix backend: service: name: coffee-svc port: number: 80

### ACKBlockInternetLoadBalancer

规则说明：限制创建公网类型的LoadBalancer Service。

重要等级：high。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockInternetLoadBalancer metadata: name: block-internet-load-balancer spec: match: kinds: - apiGroups: [""] kinds: ["Service"] namespaces: ["test-gatekeeper"]

Allowed：

apiVersion: v1 kind: Service metadata: name: my-service namespace: non-test-gatekeeper annotations: 'service.beta.kubernetes.io/alibaba-cloud-loadbalancer-address-type': 'intranet' spec: selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376 type: LoadBalancer

Disallowed：

apiVersion: v1 kind: Service metadata: name: bad-service-2 namespace: test-gatekeeper annotations: 'service.beta.kubernetes.io/alibaba-cloud-loadbalancer-address-type': 'internet' spec: type: LoadBalancer selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376

### RatifyVerification

规则说明：您在集群中安装应用市场组件Ratify后，可以验证在集群指定范围内部署的Pod镜像中的签名或SBOM等安全元数据。

重要等级：high。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: RatifyVerification metadata: name: ratify-constraint spec: enforcementAction: deny match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["default"]

Allowed：

apiVersion: v1 kind: Pod metadata: name: pod-1 namespace: test-gatekeeper spec: containers: - image: registry.cn-hangzhou.aliyuncs.com/acs/signed # 部署合法签名的镜像。 name: test-container

Disallowed：

apiVersion: v1 kind: Pod metadata: name: bad-1 namespace: test-gatekeeper spec: containers: - image: registry.cn-hangzhou.aliyuncs.com/acs/unsigned # 部署不满足Ratify签名校验的非法镜像。 name: test-container

## PSP

### ACKPSPAllowedUsers

规则说明：限制在集群指定范围内部署的Pod中的启动user、group、supplementalGroups以及fsGroup。

重要等级：medium。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| runAsUser | object | 关于该参数的具体说明，请参见原 PSP 规则中对 User 的配置，支持规则类型和 UID 最大值、最小值的配置。更多信息，请参见 [Users and groups](https://kubernetes.io/docs/concepts/policy/pod-security-policy/?spm=a2c4g.11186623.0.0.38671d80Jvlhsj#users-and-groups) 。 |
| runAsGroup | object | 关于该参数的具体说明，请参见原 PSP 规则中对 Group 的配置，支持规则类型和 UID 最大值、最小值的配置。更多信息，请参见 [Users and groups](https://kubernetes.io/docs/concepts/policy/pod-security-policy/?spm=a2c4g.11186623.0.0.38671d80Jvlhsj#users-and-groups) 。 |
| supplementalGroups | object | 关于该参数的具体说明，请参见原 PSP 规则中对 SupplementalGroups 的配置，支持规则类型和 UID 最大值、最小值的配置。更多信息，请参见 [Users and groups](https://kubernetes.io/docs/concepts/policy/pod-security-policy/?spm=a2c4g.11186623.0.0.38671d80Jvlhsj#users-and-groups) 。 |
| fsGroup | object | 关于该参数的具体说明，请参见原 PSP 规则中对 fsGroup 的配置，支持规则类型和 UID 最大值、最小值的配置。更多信息，请参见 [Users and groups](https://kubernetes.io/docs/concepts/policy/pod-security-policy/?spm=a2c4g.11186623.0.0.38671d80Jvlhsj#users-and-groups) 。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPAllowedUsers metadata: name: psp-pods-allowed-user-ranges spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: runAsUser: rule: MustRunAs # MustRunAsNonRoot # RunAsAny ranges: - min: 100 max: 200 runAsGroup: rule: MustRunAs # MayRunAs # RunAsAny ranges: - min: 100 max: 200 supplementalGroups: rule: MustRunAs # MayRunAs # RunAsAny ranges: - min: 100 max: 200 fsGroup: rule: MustRunAs # MayRunAs # RunAsAny ranges: - min: 100 max: 200

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good2 namespace: test-gatekeeper spec: securityContext: fsGroup: 150 supplementalGroups: - 150 containers: - image: test name: test securityContext: runAsUser: 150 runAsGroup: 150

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: containers: - image: test name: test

### ACKPSPAllowPrivilegeEscalationContainer

规则说明：限制在集群指定范围内部署的Pod配置allowPrivilegeEscalation参数。

重要等级：medium。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPAllowPrivilegeEscalationContainer metadata: name: psp-allow-privilege-escalation-container spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper"

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good namespace: test-gatekeeper spec: containers: - image: test name: test securityContext: allowPrivilegeEscalation: false initContainers: - image: test name: test2 securityContext: allowPrivilegeEscalation: false

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: containers: - image: test name: test

### ACKPSPAppArmor

规则说明：限制在集群指定范围内部署的Pod配置AppArmor。

重要等级：low。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| probes | array | Pod 中需要配置的 Probe。例如， readinessProbe 和 livenessProbe 。 |
| probeTypes | array | Pod 中需要配置的 Probe 类型。例如， tcpSocket 、 httpGet 和 exec 类型。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPAppArmor metadata: name: psp-apparmor spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: allowedProfiles: - runtime/default

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good namespace: test-gatekeeper annotations: 'container.apparmor.security.beta.kubernetes.io/test': 'runtime/default' 'container.apparmor.security.beta.kubernetes.io/test2': 'runtime/default' spec: containers: - image: test name: test initContainers: - image: test name: test2

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: containers: - image: test name: test

### ACKPSPCapabilities

规则说明：限制在集群指定范围内部署的Pod配置Linux Capabilities能力。

重要等级：high。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| allowedCapabilities | array | 允许的 capabilities 白名单。 |
| requiredDropCapabilities | array | 需要强制 Drop 的 capabilities 。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPCapabilities metadata: name: psp-capabilities spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: allowedCapabilities: ["CHOWN"] requiredDropCapabilities: ["NET_ADMIN", "SYS_ADMIN", "NET_RAW"]

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good-4 namespace: test-gatekeeper spec: containers: - image: test name: test securityContext: capabilities: add: - CHOWN drop: - "NET_ADMIN" - "SYS_ADMIN" - "NET_RAW"

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad-1 namespace: test-gatekeeper spec: containers: - image: test name: test

### ACKPSPFlexVolumes

规则说明：限制在集群指定范围内部署Pod的FlexVolume驱动配置。

重要等级：medium。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| allowedFlexVolumes | array | 允许配置的 FlexVolume 驱动列表。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPFlexVolumes metadata: name: psp-flexvolume-drivers spec: match: kinds: - apiGroups: [""] kinds: ["Pod", "PersistentVolume"] namespaces: - "test-gatekeeper" parameters: allowedFlexVolumes: #[] - driver: "alicloud/disk" - driver: "alicloud/nas" - driver: "alicloud/oss" - driver: "alicloud/cpfs"

Allowed：

apiVersion: v1 kind: Pod metadata: name: pv-nas namespace: test-gatekeeper spec: containers: - name: test image: test volumes: - name: test flexVolume: driver: "alicloud/nas"

Disallowed：

apiVersion: v1 kind: Pod metadata: name: pv-oss-flexvolume namespace: test-gatekeeper spec: containers: - name: test image: test volumes: - name: test flexVolume: driver: "alicloud/ossxx"

### ACKPSPForbiddenSysctls

规则说明：限制在集群指定范围内部署的Pod禁止的Sysctl范围。

重要等级：high。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| forbiddenSysctls | array | Pod 中禁止的 sysctl 列表。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPForbiddenSysctls metadata: name: psp-forbidden-sysctls spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: forbiddenSysctls: # - "*" # * may be used to forbid all sysctls - "kernel.*"

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good-2 namespace: test-gatekeeper spec: securityContext: sysctls: - name: 'net.ipv4.tcp_syncookies' value: "65536" containers: - image: test name: test

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad-1 namespace: test-gatekeeper spec: securityContext: sysctls: - name: 'kernel.shm_rmid_forced' value: '1024' containers: - image: test name: test

### ACKPSPFSGroup

规则说明：限制在集群指定范围内部署的Pod的fsGroup配置。

重要等级：medium。

参数说明：

- 

- 

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| rule | string | 关于该参数的具体说明，请参见原 PSP 规则中对 fsGroup 的配置，支持 MustRunAs 、 MayRunAs 、 RunAsAny 。更多信息，请参见 [Volumes and file systems](https://kubernetes.io/docs/concepts/policy/pod-security-policy/?spm=a2c4g.11186623.0.0.38671d80Jvlhsj#volumes-and-file-systems) 。 |
| ranges | object | 包含以下取值。 min：fsGroup id 的最小值。 max：fsGroup id 的最大值。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPFSGroup metadata: name: psp-fsgroup spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: rule: "MayRunAs" #"MustRunAs" #"MayRunAs", "RunAsAny" ranges: - min: 1 max: 1000

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good namespace: test-gatekeeper spec: securityContext: fsGroup: 100 containers: - image: test name: test

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad-1 namespace: non-test-gatekeeper spec: securityContext: fsGroup: 0 shareProcessNamespace: true containers: - image: test name: test

### ACKPSPHostFilesystem

规则说明：限制在集群指定范围内部署的Pod允许挂载的主机host目录范围。

重要等级：high。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| allowedHostPaths | object | 主机路径白名单配置。 |
| readOnly | boolean | 是否只读。 |
| pathPrefix | string | 路径前缀。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPHostFilesystem metadata: name: psp-host-filesystem spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: allowedHostPaths: - readOnly: true pathPrefix: "/foo"

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good1 namespace: test-gatekeeper spec: containers: - image: test name: test volumeMounts: - name: test-volume mountPath: "/projected-volume" readOnly: true volumes: - name: test-volume hostPath: path: /foo

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: containers: - image: test name: test volumes: - name: test-volume hostPath: path: /data type: File

### ACKPSPHostNamespace

规则说明：限制在集群指定范围内部署的Pod是否允许共享主机host命名空间。

重要等级：high。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPHostNamespace metadata: name: psp-host-namespace spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper"

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good namespace: test-gatekeeper spec: containers: - image: test name: test resources: {} dnsPolicy: ClusterFirst restartPolicy: Never status: {}

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: hostPID: true containers: - image: test name: test resources: {} dnsPolicy: ClusterFirst restartPolicy: Never status: {}

### ACKPSPHostNetworkingPorts

规则说明：限制在集群指定范围内部署的Pod使用主机网络和指定端口。

重要等级：high。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| hostNetwork | boolean | 是否允许 Pod 共享使用主机网络。 |
| min | int | 最小使用的 hostPort 值。 |
| max | int | 最大使用的 hostPort 值。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPHostNetworkingPorts metadata: name: psp-host-network-ports spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: hostNetwork: true min: 80 max: 9000

Allowed：

apiVersion: v1 kind: Pod metadata: name: good-2 namespace: test-gatekeeper spec: hostNetwork: true containers: - image: k8s.gcr.io/test-webserver name: test-container ports: - hostPort: 80 containerPort: 80 initContainers: - image: k8s.gcr.io/test-webserver name: test-container2 ports: - hostPort: 8080 containerPort: 8080

Disallowed：

apiVersion: v1 kind: Pod metadata: name: bad-1 namespace: non-test-gatekeeper spec: hostNetwork: true containers: - image: k8s.gcr.io/test-webserver name: test-container ports: - hostPort: 22 containerPort: 22

### ACKPSPPrivilegedContainer

规则说明：限制在集群指定范围内部署的Pod中启动特权容器。

重要等级：high。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPPrivilegedContainer metadata: name: psp-privileged-container spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper"

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good1 namespace: test-gatekeeper spec: containers: - image: test name: test

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: containers: - image: test name: test securityContext: privileged: true dnsPolicy: ClusterFirst restartPolicy: Never

### ACKPSPProcMount

规则说明：限制在集群指定范围内部署的Pod允许挂载的proc类型。

重要等级：high。

参数说明：

- 

- 

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| procMount | string | proc 挂载类型，允许配置如下类型： Default：默认屏蔽挂载 /proc 目录。 Unmasked：不屏蔽挂载 /proc 。 关于参数配置的具体说明，请参见 [AllowedProcMountTypes](https://kubernetes.io/docs/concepts/policy/pod-security-policy/?spm=a2c4g.11186623.0.0.38671d80Jvlhsj#allowedprocmounttypes) 。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPProcMount metadata: name: psp-proc-mount spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: procMount: Default # Default or Unmasked

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good1 namespace: test-gatekeeper spec: containers: - image: test name: test securityContext: procMount: "Default"

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad3 namespace: test-gatekeeper spec: hostUsers: false containers: - image: test name: test securityContext: procMount: "Unmasked" initContainers: - image: test name: test2

### ACKPSPReadOnlyRootFilesystem

规则说明：限制在集群指定范围内部署的Pod使用只读的根文件系统。

重要等级：medium。

参数说明：无。

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPReadOnlyRootFilesystem metadata: name: psp-readonlyrootfilesystem spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper"

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good1 namespace: test-gatekeeper spec: containers: - image: test name: test securityContext: readOnlyRootFilesystem: true

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad2 namespace: non-test-gatekeeper spec: containers: - image: test name: test securityContext: readOnlyRootFilesystem: false initContainers: - image: test name: test2

### ACKPSPSeccomp

规则说明：限制在集群指定范围内部署的Pod使用指定的Seccomp配置文件。

重要等级：low。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| allowedProfileTypes | array | 允许的 Seccomp profile 类型白名单。 |
| allowedProfiles | array | 允许的 Seccomp profile。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPSeccomp metadata: name: psp-seccomp spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: allowedProfileTypes: # - Unconfined - RuntimeDefault - Localhost allowedProfiles: - runtime/default - docker/default - localhost/profiles/audit.json

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good namespace: test-gatekeeper spec: containers: - image: test name: test securityContext: seccompProfile: type: Localhost localhostProfile: profiles/audit.json initContainers: - image: test name: test2 securityContext: seccompProfile: type: Localhost localhostProfile: profiles/audit.json

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test echo-k8s-webhook-enabled: 'true' name: bad namespace: test-gatekeeper spec: containers: - image: test name: test

### ACKPSPSELinuxV2

规则说明：限制在集群指定范围内部署的Pod必须使用allowedSELinuxOptions参数中规定的SELinux配置。

重要等级：low。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| allowedSELinuxOptions | object | 允许的 SELinux 配置白名单。更多信息，请参见 [SELinuxOptions v1 core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.26/#selinuxoptions-v1-core) 。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPSELinuxV2 metadata: name: psp-selinux-v2 spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: allowedSELinuxOptions: - level: s0:c123,c456 role: object_r type: svirt_sandbox_file_t user: system_u

Allowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good namespace: test-gatekeeper spec: securityContext: seLinuxOptions: level: "s0:c123,c456" containers: - image: test name: test

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: containers: - image: test name: test securityContext: seLinuxOptions: level: "s0:c123,c455"

### ACKPSPVolumeTypes

规则说明：限制在集群指定范围内部署的Pod使用指定Volume挂载类型。

重要等级：low。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| volumes | array | 允许使用的 Volume 挂载类型列表。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPVolumeTypes metadata: name: psp-volume-types spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: volumes: # - "*" # * may be used to allow all volume types - configMap # - emptyDir - projected - secret - downwardAPI - persistentVolumeClaim # - hostPath #required for allowedHostPaths - flexVolume #required for allowedFlexVolumes

Allowed：

apiVersion: v1 kind: Pod metadata: name: pv-oss namespace: test-gatekeeper spec: containers: - name: test image: test volumes: - name: test flexVolume: driver: "alicloud/oss"

Disallowed：

apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad-1 namespace: test-gatekeeper spec: containers: - image: test name: test volumes: - name: test-volume hostPath: path: /data

## FinOps

### ACKContainerRequests

规则说明：要求集群中某些应用 Pod 必须声明资源requests。

重要等级：low。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| cpu | string | 容器 CPU requests 的最大值。 |
| memory | string | 容器内存 requests 的最大值。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKContainerRequests metadata: name: container-must-have-requests spec: enforcementAction: deny match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: cpu: "1000m" memory: "1Gi"

Allowed：

apiVersion: v1 kind: Pod metadata: name: pod-1 namespace: test-gatekeeper spec: containers: - image: openpolicyagent/test-webserver name: test-container resources: requests: memory: "100Mi" cpu: "500m"

Disallowed：

apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: containers: - image: openpolicyagent/test-webserver name: test-container

### ACKContainerResourcesWhitelist

规则说明：要求集群中某些应用 Pod 的 CPU 和内存资源配置必须从预设选项中选取。

重要等级：low。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| cpuRequests | array | 容器 CPU requests 的白名单列表。设置为空数组 [] 是否正确表示允许所有值。 |
| cpuLimits | array | 容器 CPU limits 的白名单列表。设置为空数组 [] ，表示允许所有值。 |
| memoryRequests | array | 容器内存 requests 的白名单列表。设置为空数组 [] ，表示允许所有值。 |
| memoryLimits | array | 容器内存 limits 的白名单列表。设置为空数组 [] ，表示允许所有值。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKContainerResourcesWhitelist metadata: name: container-resources-whitelist spec: enforcementAction: deny match: kinds: - apiGroups: [ "" ] kinds: [ "Pod" ] namespaces: - "test-gatekeeper" parameters: cpuRequests: - "100m" - "500m" - "1" cpuLimits: - "2" - "4000m" memoryRequests: - "256Mi" - "512Mi" memoryLimits: - "1Gi" - "2048Mi"

Allowed：

apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: containers: - image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 name: test-container resources: requests: cpu: 100m memory: 512Mi limits: cpu: "2" memory: 1Gi

Disallowed：

apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: containers: - image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 name: test-container resources: requests: cpu: 10m memory: 512Mi limits: cpu: "1" memory: 1Gi

### ACKContainerResourcesRange

规则说明：限制集群中某些应用 Pod 的资源配置必须在指定的上下限范围内。

重要等级：low。

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| cpuRequests | object | 包含以下取值。 min ：容器 CPU requests 的最小值。 max ：容器 CPU requests 的最大值。 |
| cpuLimits | object | 包含以下取值。 min ：容器 CPU limits 的最小值。 max ：容器 CPU limits 的最大值。 |
| memoryRequests | object | 包含以下取值。 min ：容器内存 requests 的最小值。 max ：容器内存 requests 的最大值。 |
| memoryLimits | object | 包含以下取值。 min ：容器内存 limits 的最小值。 max ：容器内存 limits 的最大值。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKContainerResourcesRange metadata: name: container-resources-range spec: enforcementAction: deny match: kinds: - apiGroups: [ "" ] kinds: [ "Pod" ] namespaces: - "test-gatekeeper" parameters: cpuRequests: min: "100m" max: "1" cpuLimits: min: "500m" max: "2" memoryRequests: min: "256Mi" max: "512Mi" memoryLimits: min: "1Gi" max: "2048Mi"

Allowed：

apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: containers: - image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 name: test-container resources: requests: cpu: 100m memory: 512Mi limits: cpu: "2" memory: 2Gi

Disallowed：

apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: containers: - image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 name: test-container resources: requests: cpu: 10m memory: 5Mi limits: cpu: "3" memory: 128Mi

### ACKRequiredNodeSelector

规则说明：限制集群中某些应用 Pod 必须配置指定的nodeSelector标签。

重要等级：low。

参数说明：

- 

- 

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| nodeSelector | array | 包含以下取值。 key ：指定 Label Key。 allowedRegex ：Label Value 的正则表达式。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKRequiredNodeSelector metadata: name: must-have-nodeselector spec: enforcementAction: deny match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: nodeSelector: - key: "node.alibabacloud.com/nodepool-id" allowedRegex: "^np.*$" - key: "kubernetes.io/os" allowedRegex: "^linux$"

Allowed：

apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: containers: - image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 name: test-container resources: requests: cpu: 100m memory: 512Mi limits: cpu: "2" memory: 1Gi nodeSelector: node.alibabacloud.com/nodepool-id: npd37f0e64410c41328a6282dbe5d35cae kubernetes.io/os: linux

Disallowed：

apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: containers: - image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 name: test-container resources: requests: cpu: 100m memory: 512Mi limits: cpu: "2" memory: 1Gi nodeSelector: node.alibabacloud.com/nodepool-id: npd37f0e64410c41328a6282dbe5d35cae kubernetes.io/os: windows

### ACKWorkloadReplicasRange

规则说明：限制应用副本数量的上下限。

重要等级：low。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| minReplicas | int | 应用的最小副本数。 |
| maxReplicas | int | 应用的最大副本数。 |


示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKWorkloadReplicasRange metadata: name: replica-limiter spec: enforcementAction: deny match: kinds: - apiGroups: ["*"] kinds: ["Deployment", "StatefulSet", "ReplicaSet", "Scale"] namespaces: - "test-gatekeeper" parameters: minReplicas: 2 maxReplicas: 3

Allowed：

apiVersion: apps/v1 kind: Deployment metadata: name: nginx-deployment-basic namespace: test-gatekeeper labels: app: nginx spec: replicas: 2 selector: matchLabels: app: nginx template: metadata: labels: app: nginx spec: containers: - name: nginx image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 ports: - containerPort: 80 resources: limits: cpu: "500m"

Disallowed：

apiVersion: apps/v1 kind: Deployment metadata: name: nginx-deployment-basic-0 namespace: test-gatekeeper labels: app: nginx spec: replicas: 1 selector: matchLabels: app: nginx template: metadata: labels: app: nginx spec: containers: - name: nginx image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 ports: - containerPort: 80 resources: limits: cpu: "500m" --- apiVersion: apps/v1 kind: Deployment metadata: name: nginx-deployment-basic-1 namespace: test-gatekeeper labels: app: nginx spec: replicas: 4 selector: matchLabels: app: nginx template: metadata: labels: app: nginx spec: containers: - name: nginx image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 ports: - containerPort: 80 resources: limits: cpu: "500m"

### ACKRestrictALBCreation

规则说明：强制复用已有ALB实例，禁止通过ALBConfig创建新的ALB资源实例。

重要等级：low。

参数说明：无

示例：

Constraint：

apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKRestrictALBCreation metadata: name: restrict-alb-creation spec: enforcementAction: deny match: kinds: - apiGroups: ["alibabacloud.com"] kinds: ["AlbConfig"]

Allowed：

apiVersion: alibabacloud.com/v1 kind: AlbConfig metadata: name: reuse-alb spec: config: id: 'abcdefghijklmnopqrstuvwxyz' forceOverride: false listenerForceOverride: false

Disallowed：

apiVersion: alibabacloud.com/v1 kind: AlbConfig metadata: name: alb spec: config: name: alb addressType: Internet zoneMappings: - vSwitchId: vsw-uf6ccg2a9g71hx8go**** # 替换为集群所在VPC中至少两个处于不同可用区的VSwitch IDVSwitch ID allocationId: eip-asdfas**** # 替换为EIP ID，默认选项为自动分配公网IP。 - vSwitchId: vsw-uf6nun9tql5t8nh15**** # 替换为集群所在VPC中至少两个处于不同可用区的VSwitchIDID allocationId: eip-dpfmss**** # 替换为EIP ID。EIP ID。 listeners: - port: 80 protocol: HTTP

[上一篇：启用安全策略管理](products/ack/documents/ack-edge/security-and-compliance/configure-and-enforce-ack-pod-security-policies.md)[下一篇：配置巡检检查集群工作负载](products/ack/documents/ack-edge/security-and-compliance/use-the-inspection-feature-to-detect-security-risks-in-the-workloads-of-an-ack-cluster.md)

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
