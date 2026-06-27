config文件中，保存并退出。
如果$HOME/.kube/config文件不存在，可通过mkdir -p $HOME/.kube和touch $HOME/.kube/config来创建。
配置完成后，执行kubectl命令以验证集群连通性。
以查询命名空间为例。
kubectl get namespaces
预期输出：
NAME STATUS AGE default Active 4h39m kube-node-lease Active 4h39m kube-public Active 4h39m kube-system Active 4h39m
