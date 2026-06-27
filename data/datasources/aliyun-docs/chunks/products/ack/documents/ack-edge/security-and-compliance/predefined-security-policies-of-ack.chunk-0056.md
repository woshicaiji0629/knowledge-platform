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
