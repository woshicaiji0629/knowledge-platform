-import-alibaba-cloud-kms-service-credentials.md)[地址](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)。
如需禁止ExternalSecret跨命名空间引用SecretStore，需要将参数command.enableCrossNamespaceSecretStore设置为false
如需禁止SecretStore跨命名空间引用ServiceAccount，需要将参数command.enableCrossNamespaceAuthRef设置为false
如需禁用集群维度的控制器，需要配置以下参数，crds和command参数值是相互关联的，对于集群维度的控制器说明请参考[集群级别资源说明](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)。
crds.createClusterSecretStore：控制是否安装 ClusterSecretStore CRD，默认为true安装
crds.createClusterExternalSecret：控制是否安装 ClusterExternalSecret CRD，默认为true安装
command.processClusterSecretStore：控制是否处理 ClusterSecretStore 资源，默认为true处理
command.processClusterExternalSecret：控制是否处理 ClusterExternalSecret 资源，默认为true处理
创建成功后，会自动跳转到目标集群的ack-secret-manager页面，检查安装结果。若下图中所有资源创建成功，则表明组件安装成功。
