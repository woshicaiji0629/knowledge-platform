## 使用Argo Workflow编排Fan-out Fan-in任务
[创建](../user-guide/create-an-argo-workflow-cluster.md)[Argo](../user-guide/create-an-argo-workflow-cluster.md)[工作流集群](../user-guide/create-an-argo-workflow-cluster.md)，并[为集群开启公网访问能力](https://help.aliyun.com/zh/cs/user-guide/enable-public-network-access-for-an-existing-cluster)。
创建阿里云OSS存储卷（参考：[使用](../../ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)[ossfs 1.0](../../ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)[静态存储卷](../../ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)），将测试所需文件（[log-count-data.txt](https://github.com/AliyunContainerService/argo-workflow-examples/blob/main/log-count/python/log-count-data.txt)）拷贝到OSS存储卷的根目录下。
挂载阿里云OSS存储卷，以便工作流可以像操作本地文件一样操作OSS上的文件。
具体操作，请参见[使用存储卷](../../distributed-cloud-container-platform-for-kubernetes/user-guide/use-volumes.md)。
使用以下YAML创建一个工作流。
具体操作，请参见[创建工作流](../../distributed-cloud-container-platform-for-kubernetes/user-guide/create-a-workflow.md)。
展开查看YAML示例
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: dynamic-dag-map-reduce- spec: entrypoint: main # claim a OSS PV
