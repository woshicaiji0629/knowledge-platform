### ACKBlockEphemeralContainer
规则说明：限制在集群指定范围的应用Pod中启动临时容器。
重要等级：medium。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockEphemeralContainer metadata: name: block-ephemeral-container spec: enforcementAction: deny match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper"
Allowed：
apiVersion: v1 kind: Pod metadata: name: hello-pod namespace: test-gatekeeper spec: containers: - name: hello-pod image: redis
Disallowed：
基于已有Pod启动临时容器。
kubectl debug -it hello-pod -n test-gatekeeper --image=test --target=hello-pod
预期输出：
Error from server (Forbidden): admission webhook "validation.gatekeeper.sh" denied the request: [block-ephemeral-container-w5c6n] Creating ephemeral containers is disallowed, pod: hello-pod
