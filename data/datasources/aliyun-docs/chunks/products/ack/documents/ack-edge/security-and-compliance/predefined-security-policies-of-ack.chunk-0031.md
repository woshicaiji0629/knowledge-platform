### ACKBlockVolumeTypes
规则说明：限制在集群指定范围内部署的Pod禁止使用的Volume挂载类型。
重要等级：medium
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| volumes | array | 禁止使用的 Volume 挂载类型列表。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockVolumeTypes metadata: name: block-volume-types spec: enforcementAction: deny match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["test-gatekeeper"] parameters: volumes: - "gitRepo"
Allowed：
apiVersion: v1 kind: Pod metadata: name: use-empty-dir namespace: test-gatekeeper spec: containers: - name: test image: test volumes: - name: emptydir-volume emptyDir: {}
Disallowed：
apiVersion: v1 kind: Pod metadata: name: use-git-repo namespace: test-gatekeeper spec: containers: - name: test image: test volumes: - name: git-volume gitRepo: repository: "git@***:***/my-git-repository.git" revision: "22f1d8406d464b0c08***"
