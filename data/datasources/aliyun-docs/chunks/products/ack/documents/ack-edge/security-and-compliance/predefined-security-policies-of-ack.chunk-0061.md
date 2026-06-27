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
