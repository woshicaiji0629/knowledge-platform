## 应用于生产环境
在生产环境中，可遵循以下最佳实践，保证资源安全：
强制开启释放保护：为所有生产环境实例强制开启释放保护，防止因人为误操作或恶意行为导致核心资产被意外删除。
权限控制：仅为必要人员授予释放实例的权限（ecs:DeleteInstance和ecs:DeleteInstances）。同时，将修改实例属性（关闭释放保护）的权限（ecs:ModifyInstanceAttribute）与删除实例的权限分离，交由不同角色管理。
操作审计：启用[操作审计](https://help.aliyun.com/zh/actiontrail/product-overview/what-is-actiontrail)服务，记录所有账号内的操作，为DeleteInstance和ModifyInstanceAttribute等高危事件配置告警规则，以便在发生此类操作时立即收到通知，从而进行追踪、审计和快速响应。
