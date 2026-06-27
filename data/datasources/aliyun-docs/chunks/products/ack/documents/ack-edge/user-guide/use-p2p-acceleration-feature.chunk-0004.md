## 启用P2P加速
您可以通过添加标签的方式启用P2P加速，可以为应用负载添加P2P加速标签，例如Pod、Deployment等。也可以为ACK集群的命名空间设置P2P加速标签。为命名空间设置P2P加速标签后，该命名空间内的所有符合加速条件的应用负载都会启用P2P加速，无需再修改应用负载的YAML文件。根据实际情况选择任一方式添加P2P加速标签。
说明
标签的名称为k8s.aliyun.com/image-accelerate-mode，值为p2p。
为应用负载添加P2P加速标签。
以下以Deployment为例设置标签。执行以下命令，为Deployment设置标签。
kubectl edit deploy <Deployment名称>
在Deployment文件中添加标签k8s.aliyun.com/image-accelerate-mode: p2p。
apiVersion: apps/v1 kind: Deployment metadata: name: test labels: app: nginx spec: replicas: 1 selector: matchLabels: app: nginx template: metadata: labels: # enable P2P k8s.aliyun.com/image-accelerate-mode: p2p app: nginx spec: # your ACR instacne image pull secret imagePullSecrets: - name: test-registry containers: # your ACR instacne image - image: test-registry-vpc.cn-hangzhou.cr.aliyuncs.com/docker-builder/nginx:latest name: test command: ["sleep", "3600"]
为命名空间添加P2P加速标签
通过控制台添加P2P加速标签。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择命名空间与配额。
在命名空间页面单击目标命名空间操作列的编辑。
在编辑命名空间对话框中，单击+命名空间标签，配置变量名称为k8s.aliyun.com/image-accelerate-mode，变量值为p2p，然后单击确定。
通过命令行添加P2P加速标签。
kubectl label namespaces <YOUR-NAMESPACE> k8s.aliyun.com/image-accelerate-mode=p2p
