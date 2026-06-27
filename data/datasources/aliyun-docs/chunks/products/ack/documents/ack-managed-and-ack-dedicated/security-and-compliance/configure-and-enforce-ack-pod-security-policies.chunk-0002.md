## 前提条件
集群版本为1.16及以上。如需升级集群，请参见[手动升级集群](../user-guide/update-the-kubernetes-version-of-an-ack-cluster.md)。
如需使用RAM用户进行策略管理时，请确保该RAM用户拥有以下授权：
cs:DescribePolicies：列举策略治理规则库列表
cs:DescribePoliceDetails：获取策略规则模板详情
cs:DescribePolicyGovernanceInCluster：获取集群策略治理详情
cs:DescribePolicyInstances：获取集群中当前部署的策略实例列表
cs:DescribePolicyInstancesStatus：获取集群当前不同策略类型对应的实例部署状态
cs:DeployPolicyInstance：在指定集群中部署策略规则实例
cs:DeletePolicyInstance：在指定集群中删除策略规则实例
cs:ModifyPolicyInstance：在指定集群中修改策略规则实例
关于如何自定义RAM授权策略，请参见[使用](../user-guide/create-a-custom-ram-policy.md)[RAM](../user-guide/create-a-custom-ram-policy.md)[授予集群及云资源访问权限](../user-guide/create-a-custom-ram-policy.md)。
