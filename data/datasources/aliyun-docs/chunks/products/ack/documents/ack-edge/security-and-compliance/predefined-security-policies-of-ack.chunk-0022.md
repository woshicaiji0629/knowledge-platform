### ACKBlockProcessNamespaceSharing
规则说明：限制在集群指定范围部署的应用中使用shareProcessNamespace。
重要等级：high。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockProcessNamespaceSharing metadata: name: block-share-process-namespace spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["test-gatekeeper"]
Allowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: test-3 namespace: test-gatekeeper spec: containers: - image: test name: test resources: {} dnsPolicy: ClusterFirst restartPolicy: Never status: {}
Disallowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: shareProcessNamespace: true containers: - image: test name: test resources: {} dnsPolicy: ClusterFirst restartPolicy: Never status: {}
