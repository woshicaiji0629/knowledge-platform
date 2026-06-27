### Pod创建失败，报错信息包含PodSecurityPolicy: unable to admit pod: pod.spec.securityContext.sysctls[0]: Forbidden: unsafe sysctl
问题现象
Pod创建失败，报错信息包含PodSecurityPolicy: unable to admit pod: [pod.spec.securityContext.sysctls[0]: Forbidden: unsafe sysctl "***" is not allowed]。
解决方案
出于安全考量，集群默认不允许创建使用“不安全”sysctl的 Pod。如需为特定应用开启此权限，可通过创建新的 Pod 安全策略来实现。
警告
请勿修改或删除以下集群预置的核心安全资源。ACK 集群的正常运行依赖这些核心资源。擅自修改可能导致集群功能异常，且相关更改可能会被系统自动重置。
名为ack.privileged的 Pod 安全策略。
名称以ack:podsecuritypolicy:开头的 Role、ClusterRole、RoleBinding 和 ClusterRoleBinding。
请通过新增 Pod 安全策略的方式，来配置所需的额外sysctl策略。
使用以下内容，创建unsafe-sysctl-psp.yaml文件。
可按需调整allowedUnsafeSysctls的参数取值。--- apiVersion: policy/v1beta1 kind: PodSecurityPolicy metadata: name: psp.allow-unsafe-sysctls spec: allowedUnsafeSysctls: - '*' privileged: true allowPrivilegeEscalation: true allowedCapabilities: - '*' volumes: - '*' hostNetwork: true hostPorts: - min: 0 max: 65535 hostIPC: true hostPID: true runAsUser: rule: 'RunAsAny' seLinux: rule: 'RunAsAny' supplementalGroups: rule: 'RunAsAny' fsGroup: rule: 'RunAsAny' readOnlyRootFilesystem: false --- apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRole metadata: name: podsecuritypolicy:allow-unsafe-sysctls rules: - apiG
