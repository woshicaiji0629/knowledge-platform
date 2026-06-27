## 监控信息说明
主要监控项说明如下所示：
vCPU：阿里云提供实例vCPU使用率监控数据，单位为百分比。百分比数值越高，实例vCPU负载越高。您可以通过ECS管理控制台、云监控管理控制台、调用ECS API或者远程连接实例后查询监控数据。
以下是远程连接实例后查看vCPU使用率的方式：
Windows实例：在任务管理器中查看vCPU使用情况，您可以按vCPU使用率排序，定位占用实例vCPU资源的进程。
Linux实例：运行top命令查看vCPU使用情况。在键盘上按下Shift+P根据vCPU使用率排序，定位占用实例vCPU资源的进程。
重要
如果CPU持续保持高使用率，则会对系统稳定性和业务运行造成影响。您可以参见以下方法进行优化：
Linux实例请参见[Linux](../support/query-and-case-analysis-linux-cpu-load.md)[系统](../support/query-and-case-analysis-linux-cpu-load.md)[CPU](../support/query-and-case-analysis-linux-cpu-load.md)[负载的查询和案例分析](../support/query-and-case-analysis-linux-cpu-load.md)。
Windows实例请参见[Windows](../what-do-i-do-if-cpu-utilization-is-high-on-a-windows-instance.md)[实例中](../what-do-i-do-if-cpu-utilization-is-high-on-a-windows-instance.md)[CPU](../what-do-i-do-if-cpu-utilization-is-high-on-a-windows-instance.md)[使用率较高问题的排查及解决方法](../what-do-i-do-if-cpu-utilization-is-high-on-a-windows-instance.md)。
网络流量：阿里云提供实例出方向和入方向的网络流量监控数据，单位为kbps。
ECS控制台一般提供公网流量监控，云监控控制台可以提供公网和内网流量监控。例如，您的公网出网带宽为1 Mbps，当出网流量达到1024 kbps，表示您的公网带宽已经满负荷。
