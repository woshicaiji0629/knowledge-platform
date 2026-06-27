## 启用加速镜像
设置镜像仓库访问凭证。
警告
请确保您的镜像拉取密钥权限按最小权限原则配置，仅包含拉取本集群所需业务镜像的权限。更多详情，请参见[授予](https://help.aliyun.com/zh/acr/user-guide/attach-a-custom-policy-to-a-ram-user)[RAM](https://help.aliyun.com/zh/acr/user-guide/attach-a-custom-policy-to-a-ram-user)[用户自定义策略](https://help.aliyun.com/zh/acr/user-guide/attach-a-custom-policy-to-a-ram-user)。
镜像免密插件方式。
若已使用免密插件，且企业版实例的免密配置正确，无需其他操作。
若未使用免密插件，您可使用免密插件，更多信息，请参见[使用免密组件拉取容器镜像](https://help.aliyun.com/zh/acr/use-the-aliyun-acr-credential-helper-component-to-pull-images-without-using-secrets#task-2456294)。
指定镜像拉取凭证Secret的标签方式。
说明
仅镜像加速组件的版本不小于0.2.6支持该方式。
创建kubernetes.io/dockerconfigjson的Secret，并为其打上images.alibabacloud.com/accelerated: true的标签。
kubectl create secret docker-registry <SecretName> --docker-server=<RegistryVpcDomain> --docker-username=<UserName> --docker-password=<Password>kubectl label secrets <SecretName> images.alibabacloud.com/accelerated="true"
添加镜像加速标签。
您可以为应用负载添加镜像加速标签，例如Pod、Deployment等。也可以为ACK或ACK Serverless集群的命名空间设置标签，该命名空间内的所有符合加速条件的应用负载会启用按需加载容器镜像，无需再修改所有符合加速条件的应用负载的YAML文件。根据实际情况选择任一方式添加镜像加速标签。
说明
标签的名称为k8s.aliyun.com/image-accelerate-mode，值为on-demand。
为应用负载添加镜像加速标签。
以下以Pod为例设置标签。执行以下命令，为Deployment管理的Pod设置标签。
kubectl edit dep
