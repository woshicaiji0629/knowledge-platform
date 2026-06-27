## 通过阿里云CLI创建集群
执行以下命令，创建工作流集群。
aliyun configure set --region cn-zhangjiakou aliyun adcp CreateHubCluster --Profile XFlow --RegionId cn-zhangjiakou --VpcId vpc-xxx --VSwitches "[\"vsw-xxx\",\"vsw-xxx\"]" --Name workflow1 --ApiServerPublicEip true --IsEnterpriseSecurityGroup true

| 参数 | 说明 |
| --- | --- |
| Profile | 必选，输入 XFlow 。 |
| RegionId | 必选， 工作流集群 所在地域。本示例选择 cn-zhangjiakou 。 |
| VpcId | 必选， 工作流集群 所在专有网络 VPC ID。 |
| VSwitches | 必选，工作流运行 ECI 所在的交换机 vSwtich ID，格式为数组。请输入多可用区的交换机 ID。 |
| Name | 可选， 工作流集群 名称。 |
| IsEnterpriseSecurityGroup | 必选，使用企业安全组，输入 true 。 |
| ApiServerPublicEip | 可选，是否使用公网 EIP 暴露工作流引擎实例 APIServer 地址。 |

预期输出如下，并记录ClusterId。
{ "ClusterId": "xxx", "RequestId": "xxx", "TaskId": "xxx" }
执行以下命令，查看工作流集群的状态。
替换以下XXX为您上一步获取的ClusterId。
aliyun adcp DescribeHubClusterDetails --ClusterId XXX | jq .Cluster.ClusterInfo
等待直到预期输出的State为running状态。
执行以下命令，安装jq。
macOS：
brew install jq
CentOS：
yum install jq
Ubuntu：
apt-get install jq
执行以下命令，自动解析文本并生成KubeConfig。
aliyun adcp DescribeHubClusterKubeconfig --ClusterId <cluster id> | jq -r .Kubeconfig | tee ack-argo-workflow-kubeconfig # 设置KUBECONFIG环境变量准备运行kubectl和Argo CLI。 export KUBECONFIG=ack-argo-workflow-kubeconfig
