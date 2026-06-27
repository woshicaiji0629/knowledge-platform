### 通过实例创建自定义镜像
调用[CreateImage](../api-createimage.md)接口，基于ECS实例创建一个自定义镜像。
场景示例

| 参数 | 示例取值 |
| --- | --- |
| 实例 ID | i-bp1aq39j2yul5y01**** |
| 操作系统 | Alibaba Cloud Linux（即 Platform 为 Aliyun） |
| 地域 | cn-hangzhou |

请求示例
aliyun ecs CreateImage \ --RegionId cn-hangzhou \ --InstanceId i-bp1aq39j2yul5y01**** \ --ImageName demoimage \ --Description demoimage \ --Platform Aliyun
返回示例
{ "ImageId": "m-bp1503ydxxrppctb****", "RequestId": "011AE447-20CE-4043-81AC-7AF2BBC4****" }
