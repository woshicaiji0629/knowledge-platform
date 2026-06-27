### ACKImageDigests
规则说明：限制在集群指定范围内部署不符合digest格式的镜像。
重要等级：low。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKImageDigests metadata: name: container-image-must-have-digest spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper"
Allowed：
apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: containers: - image: openpolicyagent/test-webserver@sha256:12e469267d21d66ac9dcae33a4d3d202ccb2591869270b95d0aad7516c7d075b name: test-container
Disallowed：
apiVersion: v1 kind: Pod metadata: name: bad-1 namespace: test-gatekeeper spec: containers: - image: k8s.gcr.io/test-webserver name: test-container initContainers: - image: k8s.gcr.io/test-webserver name: test-container2
