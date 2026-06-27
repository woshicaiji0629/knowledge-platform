## 背景信息
事件驱动功能基于[开源](https://argoproj.github.io/argo-events/)[Argo Event](https://argoproj.github.io/argo-events/)[项目](https://argoproj.github.io/argo-events/)构建，完全符合开源事件驱动标准，方便您将开源事件驱动迁移到工作流集群。
重点模块说明：
Event Source
Argo Event自定义资源，针对不同的事件源创建不同的Event Source资源，并触发创建Event Source Pod获取事件。
当前工作流集群支持Git、阿里云对象存储OSS、阿里云轻量消息队列（原 MNS）作为事件源，如有其他需求，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。
Event Bus
Event Source获取事件后，会缓存到Event Bus中。Event Bus支持以下两种类型：
NATS：基于[开源](https://nats.io)[NATS](https://nats.io)构建的使用ECI运行的本地消息系统。
轻量消息队列（原 MNS）：通过使用云上轻量消息队列（原 MNS）缓存事件，如果您已经使用轻量消息队列（原 MNS），可以创建一个轻量消息队列（原 MNS）作为Event Bus。
Event Sensor
从Event Bus中读取事件，按照定义的规则过滤事件，并触发工作流的运行。您可以参考[开源](https://argoproj.github.io/argo-events/sensors/trigger-conditions/)[Argo Event](https://argoproj.github.io/argo-events/sensors/trigger-conditions/)设置Sensor Trigger条件、转换、过滤器等。
Event Sensor仅支持触发创建Argo工作流，如果有其他需求，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。
