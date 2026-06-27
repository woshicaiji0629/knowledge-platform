### 示例一：获取支持阿里云CLI调用的ACKOpenAPI列表
以下示例将为您展示如何使用--help选项获取支持阿里云CLI调用的ACKOpenAPI列表。更多信息，请参见[API](../../ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-overview.md)[概览](../../ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-overview.md)。
执行以下命令。
aliyun cs --help
预期输出。
Product: CS (容器服务 Kubernetes版 ) Version: 2015-12-15 Available Api List: AttachInstances : POST /clusters/[ClusterId]/attach AttachInstancesToNodePool : POST /clusters/[ClusterId]/nodepools/[NodepoolId]/attach CancelClusterUpgrade : POST /api/v2/clusters/[ClusterId]/upgrade/cancel CancelComponentUpgrade : POST /clusters/[clusterId]/components/[componentId]/cancel CancelOperationPlan : DELETE /operation/plans/[plan_id] CancelTask : POST /tasks/[task_id]/cancel CancelWorkflow : PUT /gs/workflow/[workflowName] CheckControlPlaneLogEnable : GET /clusters/[ClusterId]/controlplanelog CheckServiceRole : POST /ram/check-service-role CleanClusterUserPermissions : DELETE /cluster/[ClusterId]/user/[Uid]/permissions
