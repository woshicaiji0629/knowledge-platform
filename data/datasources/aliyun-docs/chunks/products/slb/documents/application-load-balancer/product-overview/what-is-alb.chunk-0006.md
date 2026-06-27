## 升级前
ALB的IP模式分为动态IP和固定IP。动态IP和固定IP的ALB实例性能存在差异。
说明
ALB实例性能指标仅与ALB的IP模式相关，与ALB功能版本无关。
单ALB实例性能（以默认2个可用区为例说明）

| IP 模式 | 最大每秒请求数（QPS） | 最大新建连接数（CPS） | 最大并发连接数 | 最大私网带宽 | 默认公网带宽 |
| --- | --- | --- | --- | --- | --- |
| 动态 IP | 100 万 | 100 万 | 1000 万 | 100 Gbps | 400 Mbps，实际公网带宽以单 ALB 实例下 EIP 的带宽总和为准。 单个 [地域](https://www.aliyun.com/getting-started/what-is/what-is-a-region) 下，单个阿里云账号下所有按使用流量计费 EIP 的实际业务带宽峰值总和不能大于 5 Gbps。更多信息，请参见 [按量付费](../../../../eip/documents/pay-as-you-go.md) 中的带宽峰值限制。 如需更大带宽请购买共享带宽。关于如何购买共享带宽，请参见 [创建与管理共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/user-guide/create-an-internet-shared-bandwidth-instance#task-hjr-jlk-z2b) 。 |
| 固定 IP | 10 万 | 10 万 | 100 万 | 10 Gbps |  |

说明
多可用区地域，ALB实例QPS、CPS、并发连接数初始上限值分别为10万、10万、100万，不随可用区的增多而变化。ALB固定IP模式实例最大QPS、CPS、并发连接数分别为10万、10万、100万，ALB动态IP模式实例会随着弹性SLA自动扩容，最高QPS、CPS、并发连接数分别可达100万、100万、1000万。
建议您使用自有域名，通过CNAME方式解析至ALB实例域名，对外提供业务访问。这种方式下ALB最高可提供99.995%SLA可用性保障。
ALB支持多可用区部署，若当前地域支持2个及以上可用区，为保障业务[高可用](https://www.aliyun.com/getting-started/what-is/what-is-high-availability)，请至少选择2个可用区，且ALB不会额外收取可用区的费用。
