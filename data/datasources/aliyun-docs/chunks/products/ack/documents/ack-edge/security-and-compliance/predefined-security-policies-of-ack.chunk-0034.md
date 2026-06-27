### ACKBlockAutoinjectServiceEnv
规则说明：要求在应用中配置enableServiceLinks: false防止在Pod环境变量中透出服务IP。
重要等级：low。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockAutoinjectServiceEnv metadata: name: block-auto-inject-service-env spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper"
Allowed：
apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: enableServiceLinks: false containers: - image: openpolicyagent/test-webserver:1.0 name: test-container
Disallowed：
apiVersion: v1 kind: Pod metadata: name: bad-1 namespace: test-gatekeeper spec: containers: - image: k8s.gcr.io/test-webserver name: test-container
