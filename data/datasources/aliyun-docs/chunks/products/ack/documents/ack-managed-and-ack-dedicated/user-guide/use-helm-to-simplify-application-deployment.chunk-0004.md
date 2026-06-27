## 本地
[获取集群](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[KubeConfig](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[并通过](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。
[安装](https://helm.sh/docs/intro/install/)[Helm CLI](https://helm.sh/docs/intro/install/)。
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
添加Chart仓库。
将<REPO_NAME>替换为仓库别名，<REPO_URL>替换为仓库地址。helm repo add <REPO_NAME> <REPO_URL>
更新仓库信息。
helm repo update
第三方库部署应用。
将<APP_NAME>替换为应用实例名，<CHART_NAME>替换为要安装的 Chart 名称。helm install <APP_NAME> <REPO_NAME>/<CHART_NAME>
Helm更多命令请参见[Helm 官方文档](https://helm.sh/docs/intro/using_helm/)。
为什么Helm应用无法删除？
问题现象
在控制台删除Helm应用时，应用长时间停留在“卸载”状态。
通过Helm CLI删除应用时，命令行返回以下错误：
no matches for kind "***" in version "***" ensure CRDs are installed first
问题原因
该问题通常发生在集群升级后旧版本API被废弃，若Helm应用中包含使用已废弃API的资源，删除时会因API版本不存在而失败。
Kubernetes不同版本的废弃API列表，请参见[Deprecated API Migrati
