### ACKBlockNodeDelete
规则说明：防止集群中带有自定义标签的节点（Node）被删除。可定义多组键值对，节点只要满足其中任意一对即可受到保护。
重要等级：high。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| protectedLabels | array | 自定义标签，用于识别需要被保护的节点。 |
| protectedLabels.labelName | string | 自定义标签的键。 |
| protectedLabels.labelValue | string | 自定义标签的值。 |

示例：
Constraint:
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockNodeDelete metadata: name: block-node-delete spec: enforcementAction: deny match: kinds: - apiGroups: ["*"] kinds: ["Node"] parameters: protectedLabels: - labelName: policy.alibabacloud.vpc.com/node-delete-protection labelValue: "true" - labelName: policy.alibabacloud.com/node-delete-protection labelValue: "true"
Allowed：
apiVersion: v1 kind: Node metadata: name: cn-hangzhou-1
Disallowed：
apiVersion: v1 kind: Node metadata: labels: policy.alibabacloud.vpc.com/node-delete-protection: "true" name: cn-hangzhou-1 --- apiVersion: v1 kind: Node metadata: labels: policy.alibabacloud.vpc.com/node-delete-protection: "true" name: cn-hangzhou-2 --- apiVersion: v1 kind: Node metadata: labels: policy.alibabacloud.com/node-delete-protection: "true" policy.alibabacloud.vpc.com/node-delete-protection: "true" name: cn-hangzhou-3
