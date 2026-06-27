### 注解设置示例

| 注解 | 说明 |
| --- | --- |
| nodeport.openyurt.io/listen=foo,bar | 在 foo 和 bar 节点池中的节点上启用 NodePort Service 监听。 |
| nodeport.openyurt.io/listen=foo,* | 在所有节点池中的节点上启用 NodePort Service 监听。 |
| nodeport.openyurt.io/listen=-foo,-bar | 在所有节点池中的节点上禁用 NodePort Service 监听。 |
| nodeport.openyurt.io/listen=-foo,* | 仅在 foo 节点池中的节点上禁用 NodePort Service 监听。 |
| nodeport.openyurt.io/listen=foo,-foo | 在 foo 节点池中的节点上启用 NodePort Service 监听。 |
| nodeport.openyurt.io/listen=-foo | 在所有节点池中的节点上禁用 NodePort Service 监听（包含 foo 节点池）。 |

该文章对您有帮助吗？
反馈
