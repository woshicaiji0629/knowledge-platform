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
