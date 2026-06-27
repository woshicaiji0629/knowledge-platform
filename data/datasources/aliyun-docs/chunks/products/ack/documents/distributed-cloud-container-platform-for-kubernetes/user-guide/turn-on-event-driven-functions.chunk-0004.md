## 操作步骤
获取工作流集群的ID。
通过命令行方式获取。
aliyun adcp DescribeHubClusters --Profile=XFlow
通过控制台方式获取。
登录[工作流集群控制台](https://cs.console.aliyun.com/one?spm=5176.26288914.J_2883378880.2.791c75b87xSv6P#/argowf/ccbe3ace8f2f54fbfa1c5b0005d456d5f/detail)，在工作流集群页面的基础信息页签中获取集群ID。
执行以下命令开启事件驱动功能。
aliyun adcp UpdateHubClusterFeature --ArgoEventsEnabled true --ClusterId ***
重要
请将ClusterId后的***替换为您在[步骤](turn-on-event-driven-functions.md)[1](turn-on-event-driven-functions.md)中实际获取的工作流集群ID。
等待一段时间后，执行以下命令查看集群的详细信息。
aliyun adcp DescribeHubClusterDetails --ClusterId ***
在返回结果中查看Condition类型为EnabledArgoEvents的状态为True，表示事件驱动功能开启成功。
预期结果如下：
{ "Message": "", "Reason": "", "Status": "True", "Type": "EnabledArgoEvents" }
