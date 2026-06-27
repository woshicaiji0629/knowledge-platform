## 自建集群升级方式
说明
建议通过安装最新Logtail组件进行更新，如果只更新部分组件（如logtail-ds、alibaba-log-controller）的镜像版本号可能导致升级失败。
重新安装Logtail组件，即可完成自动升级。具体操作，请参见[安装](install-run-upgrade-and-uninstall-logtail.md)[Logtail](install-run-upgrade-and-uninstall-logtail.md)[组件](install-run-upgrade-and-uninstall-logtail.md)。
如果您要回滚到某个版本，可参考如下步骤。
说明
升级前备份的YAML文件中包含不少冗余信息，需要您手动删除后，才能用于恢复Logtail配置。您可以使用kubectl-neat工具完成此操作。需要删除的字段为metadata.creationTimestamp、metadata.generation、metadata.resourceVersion、metadata.uid和status。
根据业务需求判断升级之后的新Logtail配置是否需要保留。
如果不需要保留，则可以删除升级之后的新Logtail配置。
删除备份文件中的冗余信息。
cat logtail-ds.yaml | kubectl-neat > neat-logtail-ds.yaml cat alibaba-log-controller.yaml | kubectl-neat > neat-alibaba-log-controller.yaml cat aliyunlogconfigs-crd.yaml | kubectl-neat > neat-aliyunlogconfigs-crd.yaml cat alibaba-log-configuration.yaml | kubectl-neat > neat-alibaba-log-configuration.yaml cat aliyunlogconfigs-cr.yaml | kubectl-neat > neat-aliyunlogconfigs-cr.yaml
应用精简后的备份文件，恢复Logtail配置。
kubectl apply -f neat-logtail-ds.yaml kubectl apply -f neat-alibaba-log-controller.yaml kubectl apply -f neat-aliyunlogconfigs-crd.yaml kubectl apply -f neat-alibaba-log-configuration.yaml kubectl apply -f neat-aliyunlogconfigs-cr.yaml
