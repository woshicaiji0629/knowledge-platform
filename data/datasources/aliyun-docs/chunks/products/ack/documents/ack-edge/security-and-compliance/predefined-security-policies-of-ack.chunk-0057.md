### ACKPSPHostNamespace
规则说明：限制在集群指定范围内部署的Pod是否允许共享主机host命名空间。
重要等级：high。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPHostNamespace metadata: name: psp-host-namespace spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper"
Allowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good namespace: test-gatekeeper spec: containers: - image: test name: test resources: {} dnsPolicy: ClusterFirst restartPolicy: Never status: {}
Disallowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: hostPID: true containers: - image: test name: test resources: {} dnsPolicy: ClusterFirst restartPolicy: Never status: {}
