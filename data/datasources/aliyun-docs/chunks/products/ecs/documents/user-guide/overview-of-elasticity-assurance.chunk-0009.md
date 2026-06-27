## 应用于生产环境的建议
与弹性伸缩集成：建议将弹性保障与弹性伸缩（ESS）结合使用，实现自动化资源调度。
在[创建](https://help.aliyun.com/zh/auto-scaling/user-guide/create-an-ecs-scaling-group)或[修改伸缩组](https://help.aliyun.com/zh/auto-scaling/modify-a-scaling-group#concept-qkz-nkx-rfb)时，设置的资源池策略以优先使用弹性保障的私有池容量。
资源池策略选项：
私有池优先：优先使用指定的私有池，如果私有池容量不足，则自动匹配开放类型的私有池或公共池。
仅限私有池：必须使用私有池容量，否则实例启动失败。
配置步骤：
登录[弹性伸缩控制台](https://essnew.console.aliyun.com/)。
创建或修改伸缩组。
在[伸缩配置](https://help.aliyun.com/zh/auto-scaling/user-guide/manage-scaling-configurations#9f06c1bc759oq)的高级设置中选择资源池策略，并指定一个弹性保障的私有池。
监控与告警：建议通过云监控（CloudMonitor）[创建报警规则](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/create-an-alert-rule)对关键指标设置告警，及时掌握容量使用情况。例如当可用容量低于总容量的 20% 时触发告警：
产品选择ECS私有资源池。
指标选择实例个数使用率，报警级别选择警告（Warn），阈值设置20%。
