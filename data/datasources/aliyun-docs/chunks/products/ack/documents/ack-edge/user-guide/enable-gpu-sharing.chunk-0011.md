## 步骤四：在云端节点安装和使用GPU资源查询工具
下载kubectl-inspect-cgpu。需将执行文件下载至PATH环境变量包含目录下，本文以/usr/local/bin/为例。
如果您使用的是Linux系统，您可以通过以下命令下载kubectl-inspect-cgpu。
wget http://aliacs-k8s-cn-beijing.oss-cn-beijing.aliyuncs.com/gpushare/kubectl-inspect-cgpu-linux -O /usr/local/bin/kubectl-inspect-cgpu
如果您使用的是macOS系统，您可以通过以下命令下载kubectl-inspect-cgpu。
wget http://aliacs-k8s-cn-beijing.oss-cn-beijing.aliyuncs.com/gpushare/kubectl-inspect-cgpu-darwin -O /usr/local/bin/kubectl-inspect-cgpu
执行以下命令，为kubectl-inspect-cgpu添加执行权限。
chmod +x /usr/local/bin/kubectl-inspect-cgpu
执行以下命令，查看集群GPU使用情况。
kubectl inspect cgpu
预期输出：
NAME IPADDRESS GPU0(Allocated/Total) GPU Memory(GiB) cn-shanghai.192.168.6.104 192.168.6.104 0/15 0/15 ---------------------------------------------------------------------- Allocated/Total GPU Memory In Cluster: 0/15 (0%)
