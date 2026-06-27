### 结果验证
使用授权的RAM用户验证标签鉴权是否生效：
前往[VPC](https://vpc.console.aliyun.com/vpc/cn-hangzhou/switches/new)[控制台 - 创建交换机页面](https://vpc.console.aliyun.com/vpc/cn-hangzhou/switches/new)，创建交换机时指定目标专有网络、标签键、标签值。
前往[VPC](https://vpc.console.aliyun.com/vpc/cn-hangzhou/switches)[控制台 - 交换机页面](https://vpc.console.aliyun.com/vpc/cn-hangzhou/switches)，删除绑定指定标签的交换机。

| 验证场景 | 结果 | 原因 |
| --- | --- | --- |
| 在 VPC-A（ department:finance ）中创建交换机，请求中携带标签 env:prod | 成功 | acs:ResourceTag 和 acs:RequestTag 条件均满足 |
| 在 VPC-B（ department:hr ）中创建交换机，请求中携带标签 env:prod | 失败 | VPC 上的 acs:ResourceTag 不满足（ department ≠ finance ） |
| 在 VPC-A 中创建交换机，不携带标签或携带其他标签 | 失败 | acs:RequestTag 不满足（未携带 env:prod ） |
| 在 VPC-B 中创建交换机，不携带标签 | 失败 | acs:ResourceTag 和 acs:RequestTag 条件均不满足 |
| 删除已绑定 env:prod 标签的交换机 | 成功 | 交换机上的 acs:ResourceTag 满足（ env = prod ） |
| 删除未绑定 env:prod 标签的交换机 | 失败 | 交换机上的 acs:ResourceTag 不满足 |

该文章对您有帮助吗？
反馈
