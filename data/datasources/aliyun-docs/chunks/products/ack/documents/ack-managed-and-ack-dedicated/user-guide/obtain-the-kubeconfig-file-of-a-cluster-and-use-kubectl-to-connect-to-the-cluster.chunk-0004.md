### 2. 获取KubeConfig并连接集群
在控制台获取 KubeConfig 后，kubectl 可依据该文件连接并管理集群。
RAM用户连接集群前，除容器服务的系统权限外，还需要被授予集群操作的权限，请参见[授权](authorization-overview.md)。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称或者目标集群右侧操作列下的详情。
在集群信息页面，单击连接信息页签，选择临时或长期KubeConfig。对于临时KubeConfig，需合理设置其有效期。
选择公网访问或内网访问页签，单击复制，将复制的KubeConfig内容粘贴至客户端的$HOME/.kube/config文件中，保存并退出。
如果$HOME/.kube/config文件不存在，可通过mkdir -p $HOME/.kube和touch $HOME/.kube/config来创建。
配置完成后，执行kubectl命令以验证集群连通性。
以查询命名空间为例。
kubectl get namespaces
预期输出：
NAME STATUS AGE default Active 4h39m kube-node-lease Active 4h39m kube-public Active 4h39m kube-system Active 4h39m
