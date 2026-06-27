sion "***" ensure CRDs are installed first
问题原因
该问题通常发生在集群升级后旧版本API被废弃，若Helm应用中包含使用已废弃API的资源，删除时会因API版本不存在而失败。
Kubernetes不同版本的废弃API列表，请参见[Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/)。
解决方案
使用 Helm 官方[helm-mapkubeapis](https://github.com/helm/helm-mapkubeapis)插件将Release中已废弃的API版本映射到新版支持的API版本，然后重新删除。
将<RELEASE_NAME>和<NAMESPACE>替换为Helm应用名称及所在的命名空间。helm plugin install https://github.com/helm/helm-mapkubeapis helm mapkubeapis <RELEASE_NAME> -n <NAMESPACE>
预期输出...completed successfully说明API版本已映射成功。
完成API版本映射后，即可正常删除该应用。
helm uninstall <RELEASE_NAME> -n <NAMESPACE>
预期输出release "***" uninstalled，表明Helm应用删除成功。
