### ACKServicesDeleteProtection
规则说明：限制指定Namespace中的Service实例被误删除，可以通过protectionServices参数配置受保护的Service实例名称。
重要等级：medium。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| protectionServices | array | 指定命名空间下受保护的 Service 实例名称列表。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKServicesDeleteProtection metadata: name: service-delete-protection annotations: description: "Protect to delete specific service." spec: enforcementAction: deny match: kinds: - apiGroups: [''] kinds: ['Service'] namespaces: ["test-gatekeeper"] parameters: protectionServices: - test-svc
Allowed：
apiVersion: v1 kind: Service metadata: name: good namespace: test-gatekeeper
Disallowed：
apiVersion: v1 kind: Service metadata: name: test-svc
