例所在的每个交换机内预留至少8个IP地址。

| 单 VIP 性能指标 | 最高自动弹性性能 |
| --- | --- |
| 最大每秒请求数（QPS） | 500,000 |
| 最大新建连接数（CPS） | 200,000 |
| 最大并发连接数 | 5,000,000 |
| 最大私网带宽 | 25Gbps |

双可用区的ALB实例默认公网带宽为400Mbps，实际公网带宽以单ALB实例下EIP的带宽总和为准。
单个[地域](https://www.aliyun.com/getting-started/what-is/what-is-a-region)下，单个阿里云账号下所有按使用流量计费EIP的实际业务带宽峰值总和不能大于 5 Gbps。更多信息，请参见[按量付费](../../../../eip/documents/pay-as-you-go.md)中的带宽峰值限制。
如需更大带宽请购买共享带宽。关于如何购买共享带宽，请参见[创建与管理共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/user-guide/create-an-internet-shared-bandwidth-instance#task-hjr-jlk-z2b)。
说明
ALB的性能容量会随着分钟级弹性SLA自动扩容，若您有如下场景或需要更高的弹性能力，请使用[ALB](../user-guide/capacity-reservation.md)[资源预留](../user-guide/capacity-reservation.md)。
您准备推出系列运营活动，该活动将带来突发流量高峰，您希望确保ALB能够支持活动期间的流量高峰。
您的业务属于突发型业务，无法有效预测流量洪峰。
您上线或迁移的业务需要ALB在初始状态就具备较高性能，而不是等待自动扩容。
您需要持续保持确定性容量，以满足业务诉求。
您正在进行负载均衡之间的迁移，并希望目标负载均衡的性能规模与源负载均衡匹配。
ALB支持多可用区部署，若当前地域支持2个及以上可用区，为保障业务[高可用](https://www.aliyun.com/getting-started/what-is/what-is-high-availability)，请至少选择2个可用区，且ALB不会额外收取可用区的费用。
建议您使用自有域名，通过CNAME方式解析至ALB实例域名，对外提供业务访问。这种方式下ALB最高可提供99.995% SLA可用性保障。
上方规格表中的性能指标为ALB实例的最高自动弹性性能上限，与实例功能版本无关。
