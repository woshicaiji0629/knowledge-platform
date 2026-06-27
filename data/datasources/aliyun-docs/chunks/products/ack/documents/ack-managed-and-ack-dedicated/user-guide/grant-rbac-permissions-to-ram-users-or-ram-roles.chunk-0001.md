## 工作原理
ACK的[授权](authorization-overview.md)体系包括阿里云RAM和Kubernetes[RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)两个层级，构成了从云资源到集群资源的完整授权链路。
[RAM](create-a-custom-ram-policy.md)：决定了谁能“进入”集群的大门。负责在云资源层面进行授权，控制用户对ACK集群及其依赖云产品的OpenAPI操作权限。
RBAC：决定了用户“进入”大门后能做什么。负责在集群内部进行精细化授权，定义用户能对哪些Kubernetes资源（如Pod、Deployment）执行何种操作（如创建、删除）。
