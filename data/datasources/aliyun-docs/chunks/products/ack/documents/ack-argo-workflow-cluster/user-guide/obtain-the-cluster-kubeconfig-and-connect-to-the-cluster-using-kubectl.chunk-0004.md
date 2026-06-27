## 为RAM用户授予RBAC权限
登录[容器](https://csnew.console.aliyun.com/#/next/argowf)[Argo](https://csnew.console.aliyun.com/#/next/argowf)[工作流集群控制台](https://csnew.console.aliyun.com/#/next/argowf)，单击目标集群名称。
在权限管理页面，在目标RAM用户右侧单击管理授权，为RAM用户授予下列权限：

| RBAC 权限 | 权限说明 |
| --- | --- |
| admin（管理员） | 具有集群范围和所有命名空间下资源的读写权限。 |
| dev（开发人员） | 具有所选命名空间下的资源读写权限。 |

展开查看集群及命名空间资源列表
集群范围资源列表

| Kind | apiVersion |
| --- | --- |
| Namespace | v1 |
| PersistentVolumes | v1 |
| ImageCaches | eci.alibabacloud.com |

命名空间下资源列表

| Kind | apiVersion |
| --- | --- |
| ConfigMap | v1 |
| Secret | v1 |
| ServiceAccount | v1 |
| PersistentVolumeClaim | v1 |
| Pod | v1 |
| Workflow WorkflowTemplate CronWorkflow | argoproj.io |
| EventSource EventBus Sensor | argoproj.io |
