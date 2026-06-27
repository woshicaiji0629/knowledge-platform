### ACKBlockAutomountToken
规则说明：要求在应用中设置automountServiceAccountToken: false字段防止自动挂载serviceaccount。
重要等级：high。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockAutomountToken metadata: name: block-auto-mount-service-account-token spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper"
Allowed：
apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: automountServiceAccountToken: false containers: - image: openpolicyagent/test-webserver:v1.0 name: test-container
Disallowed：
apiVersion: v1 kind: Pod metadata: name: bad-1 namespace: test-gatekeeper spec: containers: - image: k8s.gcr.io/test-webserver name: test-container
