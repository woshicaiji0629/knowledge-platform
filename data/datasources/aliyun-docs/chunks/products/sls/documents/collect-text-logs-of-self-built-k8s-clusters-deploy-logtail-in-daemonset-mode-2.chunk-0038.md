### 日志标签富化
核心配置：通过在[spec.config.inputs](kubernetes-cr-parameter-description.md)中配置ExternalEnvTag和ExternalK8sLabelTag，向日志中添加与容器环境变量、Pod标签相关的tag。

| 关键字段详解 | 示例 |
| --- | --- |
| ExternalEnvTag 将指定的环境变量值映射为 tag 字段，格式为： <环境变量名>: <tag 名> 。 | # ...在 spec.config 下... inputs: - Type: input_file # 或 input_container_stdio ExternalEnvTag: <环境变量名>: <tag 名> ExternalK8sLabelTag: <Pod 标签名>: <tag 名> |
| ExternalK8sLabelTag 将 Kubernetes Pod 的标签值映射为 tag 字段，格式为： <Pod 标签名>: <tag 名> 。 |  |
