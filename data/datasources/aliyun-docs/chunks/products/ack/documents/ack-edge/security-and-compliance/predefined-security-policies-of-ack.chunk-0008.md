### ACKPodsRequireSecurityContext
规则说明：限制Pod中所有容器必须配置securitycontext字段。
重要等级：low。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPodsRequireSecurityContext metadata: name: pods-require-security-context annotations: description: "Requires that Pods must have a `securityContext` defined." spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["test-gatekeeper"]
Allowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: test namespace: test-gatekeeper spec: securityContext: runAsNonRoot: false containers: - image: test name: test resources: {} dnsPolicy: ClusterFirst restartPolicy: Never status: {}
Disallowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: containers: - image: test name: test2 - image: test name: test resources: {} securityContext: runAsNonRoot: false
