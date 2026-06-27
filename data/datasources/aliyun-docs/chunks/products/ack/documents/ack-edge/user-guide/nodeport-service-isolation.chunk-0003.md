## 使用方法
您可以为NodePort、LoadBalancer服务引入注解nodeport.openyurt.io/listen。
注解的键（key）：nodeport.openyurt.io/listen。
注解的值（value）：用英文半角逗号分隔的节点池ID列表。
foo：使指定的NodePort Service在ID为foo的节点池中的节点上监听。
-foo：禁止指定的NodePort Service在ID为foo的节点池中的节点上监听。
*：使指定的NodePort Service在所有节点池中的节点上监听。
重要
如果对同一节点池有多个配置，仅第一个配置生效。
如果未配置节点池ID，将在这些未配置的节点池中的节点上禁用此NodePort Service监听。
与原生Kubernetes一致，系统将默认监听孤儿节点（不位于节点池中的节点）NodePort Service的端口。
