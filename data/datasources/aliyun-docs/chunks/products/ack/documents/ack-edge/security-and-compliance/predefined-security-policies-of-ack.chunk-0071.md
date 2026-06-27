eSelector标签。
重要等级：low。
参数说明：

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
