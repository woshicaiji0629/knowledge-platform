### ACKNamespacesDeleteProtection
规则说明：限制指定的Namespace被误删除。可以通过protectionNamespaces参数配置受保护命名空间的Name。
使用前提：需确保gatekeeper组件已升级至v3.10.0.130-g0e79597d-aliyun或以上版本。关于gatekeeper组件版本信息，请参见[gatekeeper](../../product-overview/gatekeeper.md)。
重要等级：medium。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| protectionNamespaces | array | 受保护 Namespace 的名称列表。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKNamespacesDeleteProtection metadata: name: namespace-delete-protection spec: match: kinds: - apiGroups: [''] kinds: ['Namespace'] parameters: protectionNamespaces: - test-gatekeeper
Allowed：
apiVersion: v1 kind: Namespace metadata: name: will-delete
Disallowed：
apiVersion: v1 kind: Namespace metadata: name: test-gatekeeper
