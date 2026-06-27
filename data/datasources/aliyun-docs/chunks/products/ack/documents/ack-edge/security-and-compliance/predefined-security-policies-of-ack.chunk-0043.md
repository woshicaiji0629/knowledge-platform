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
