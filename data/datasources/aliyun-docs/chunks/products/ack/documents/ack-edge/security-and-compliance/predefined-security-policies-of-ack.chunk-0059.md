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
