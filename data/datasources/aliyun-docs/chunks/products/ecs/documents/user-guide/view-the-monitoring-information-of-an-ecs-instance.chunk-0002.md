## 通过ECS控制台查看监控信息
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
单击目标实例ID进入实例详情页，选择监控页签。
设置监控时间范围，可以查看vCPU使用率、内存使用率等监控信息。
由于监控曲线显示的聚合方式不一样，选择时间段的长短会影响显示的精度。选择的时间范围越小，显示效果越精细。例如，1小时和6小时的平均值会显示不一样的结果，请您根据实际需要选择适合的时间范围。
说明
您也可以使用DescribeInstanceMonitorData、DescribeDiskMonitorData和DescribeEniMonitorData接口获取监控数据。
实例是否安装云监控插件会导致在ECS管理控制台查看到的监控数据不同：
实例已安装云监控插件：ECS管理控制台的监控项中，CPU、内存、系统负载数据为云监控的操作系统监控项，其他监控项与云监控的基础监控项一致。
实例未安装云监控插件：在ECS管理控制台查看到的监控项与云监控的基础监控项一致。
说明
基础监控项数据采集频率为每1分钟一次，操作系统监控项数据采集频率为每15秒一次。更多信息，请参见[操作系统监控](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/operating-system-monitoring#concept-gdq-tgc-5db)。
以下是实例未安装插件时在ECS控制台上的监控项详细列表，指标采集粒度为1分钟。
