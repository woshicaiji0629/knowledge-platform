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
