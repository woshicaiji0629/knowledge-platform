### ACKAllowedRepos
规则说明：限制在集群指定范围部署的应用Pod中拉取白名单列表外的镜像。
重要等级：high。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| repos | array | 合法的镜像仓库白名单。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKAllowedRepos metadata: name: allowed-repos spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: repos: - "registry-vpc.cn-hangzhou.aliyuncs.com/acs/" - "registry.cn-hangzhou.aliyuncs.com/acs/"
Allowed：
apiVersion: v1 kind: Pod metadata: name: pod-01 namespace: test-gatekeeper spec: containers: - image: registry.cn-hangzhou.aliyuncs.com/acs/test-webserver name: test-container-1 initContainers: - image: registry.cn-hangzhou.aliyuncs.com/acs/test-webserver name: test-container
Disallowed：
apiVersion: v1 kind: Pod metadata: name: bad-1 namespace: test-gatekeeper spec: containers: - image: k8s.gcr.io/test-webserver name: test-container initContainers: - image: k8s.gcr.io/test-webserver name: test-container-3
