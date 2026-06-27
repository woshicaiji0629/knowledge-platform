跨命名空间访问控制
为了增强安全性和灵活性，ack-secret-manager提供了多种跨命名空间访问控制机制：
ExternalSecret 引用 SecretStore 控制
通过command.enableCrossNamespaceSecretStore参数控制ExternalSecret是否可以跨命名空间引用SecretStore。
默认值为true，即允许跨命名空间引用。
设置为false时，ExternalSecret只能引用同命名空间的SecretStore。
SecretStore 引用认证资源控制
通过command.enableCrossNamespaceAuthRef参数控制SecretStore是否可以跨命名空间引用认证资源（ServiceAccount、AccessKey Secret）。
默认值为true，即允许跨命名空间引用。
设置为false时，SecretStore只能引用同命名空间的认证资源。
ClusterSecretStore 访问控制
ClusterSecretStore 通过spec.conditions字段定义允许访问该资源的命名空间条件
支持三种访问控制方式，条件之间是或的关系：
namespaceSelector：使用标签选择器匹配允许访问的命名空间。
namespaces：明确列出允许访问的命名空间名称列表。
namespaceRegexes：使用正则表达式匹配允许访问的命名空间名称列表。
conditions: - namespaceSelector: matchLabels: app: myapp matchExpressions: - key: environment operator: In values: - dev - namespaces: - default - test - namespaceRegexes: - "kube-.*"
推荐使用方式
跨命名空间访问推荐方案
对于需要跨命名空间访问的场景，推荐使用以下组合：
ClusterSecretStore + ExternalSecret：当多个命名空间需要使用相同的认证配置时。
ClusterSecretStore + ClusterExternalSecret：当需要在多个命名空间中自动创建相同配置的ExternalSecret时。
安全最佳实践
最小权限原则：
在不需要跨命名空间访问的场景中，将command.enableCrossNamespaceSecretStore和command.enableCrossNamespaceAuthRef设置为false。
优先使用命名空间级别的资源（SecretStore 和 ExternalSecret）。
访问控制配置：
使用 ClusterSecretStore 时，明确配置spec
