ML文件。根据实际情况选择任一方式添加镜像加速标签。
说明
标签的名称为k8s.aliyun.com/image-accelerate-mode，值为on-demand。
为应用负载添加镜像加速标签。
以下以Pod为例设置标签。执行以下命令，为Deployment管理的Pod设置标签。
kubectl edit deployment <Deployment名称> -n <Deployment命名空间>
在Deployment的YAML描述文件中添加标签k8s.aliyun.com/image-accelerate-mode: on-demand。
apiVersion: apps/v1 kind: Deployment metadata: name: nginx-deployment labels: app: nginx spec: replicas: 1 selector: matchLabels: app: nginx template: metadata: labels: app: nginx # enable on-demand mode k8s.aliyun.com/image-accelerate-mode: on-demand spec: containers: # your ACR instacne image - image: test-registry-vpc.cn-hangzhou.cr.aliyuncs.com/test/nginx:latest name: test command: ["sleep", "3600"]
为命名空间添加镜像加速标签
通过控制台添加镜像加速标签。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择命名空间与配额。
在命名空间页面单击目标命名空间操作列的编辑。
在编辑命名空间对话框中设置标签的变量名称为k8s.aliyun.com/image-accelerate-mode，标签的变量值为on-demand，然后单击确定。
通过命令行添加镜像加速标签。
kubectl label namespaces <YOUR-NAMESPACE> k8s.aliyun.com/image-accelerate-mode=on-demand
设置加速标签后，如果您已完成普通镜像到加速镜像的转换，在相应命名空间内创建和更新Pod时，加速组件会自动将Pod的原始镜像地址替换为加速镜像地址，并添加nodeSelector，将Pod调度到加速节点。
该文章对您有帮助吗？
反馈
