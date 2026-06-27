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
