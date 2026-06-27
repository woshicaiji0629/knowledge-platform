值、最小值的配置。更多信息，请参见 [Users and groups](https://kubernetes.io/docs/concepts/policy/pod-security-policy/?spm=a2c4g.11186623.0.0.38671d80Jvlhsj#users-and-groups) 。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPAllowedUsers metadata: name: psp-pods-allowed-user-ranges spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: runAsUser: rule: MustRunAs # MustRunAsNonRoot # RunAsAny ranges: - min: 100 max: 200 runAsGroup: rule: MustRunAs # MayRunAs # RunAsAny ranges: - min: 100 max: 200 supplementalGroups: rule: MustRunAs # MayRunAs # RunAsAny ranges: - min: 100 max: 200 fsGroup: rule: MustRunAs # MayRunAs # RunAsAny ranges: - min: 100 max: 200
Allowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good2 namespace: test-gatekeeper spec: securityContext: fsGroup: 150 supplementalGroups: - 150 containers: - image: test name: test securityContext: runAsUser: 150 runAsGroup: 150
Disallowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: containers: - image: test name: test
