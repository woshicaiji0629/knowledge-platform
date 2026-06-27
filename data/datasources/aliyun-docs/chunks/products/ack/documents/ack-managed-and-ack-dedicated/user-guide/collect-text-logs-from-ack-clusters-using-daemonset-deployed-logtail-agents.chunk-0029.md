t）：指定为stdout时，表示采集容器的标准输出和标准错误输出。
每一项采集配置都会被自动创建为对应Logstore的一个采集配置，默认采用极简模式（按行）进行采集。
设置自定义Tag。
单击自定义Tag创建新的自定义Tag，每一个自定义Tag都是一个键值对，会拼接到所采集到的日志中，您可以使用它来为容器的日志数据进行标记，例如版本号。
当完成所有配置后，可单击右上角的下一步进入后续流程。
后续操作，可参见[创建无状态工作负载](create-a-stateless-application-by-using-a-deployment.md)[Deployment](create-a-stateless-application-by-using-a-deployment.md)。
通过YAML模板
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>无状态。
在无状态页面上方的命名空间下拉框中设置命名空间，然后单击页面右上角的使用YAML创建资源。
配置YAML文件。
YAML模板的语法同Kubernetes语法，但是为了给容器指定采集配置，需要使用env来为容器增加采集配置和自定义Tag，并根据采集配置，创建对应的volumeMounts和volumes。以下是一个简单的Pod示例：
apiVersion: apps/v1 kind: Deployment metadata: annotations: deployment.kubernetes.io/revision: '1' labels: app: deployment-stdout cluster_label: CLUSTER-LABEL-A name: deployment-stdout namespace: default spec: progressDeadlineSeconds: 600 replicas: 1 revisionHistoryLimit: 10 selector: matchLabels: app: deployment-stdout strategy: rollingUpdate: maxSurge: 25% maxUnavailable: 25% type: RollingUpdate template: metadata: labels: app: deployment-stdout cluster_label: CLUSTER-LABEL-A spec: containers: - args: - >- while true; do date '+%Y-%m-%d %H:%M:%S'; echo 1; echo 2; echo 3; ec
