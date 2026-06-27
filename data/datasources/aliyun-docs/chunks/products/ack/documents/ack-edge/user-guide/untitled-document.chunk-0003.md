## 释放资源
集群删除后，请根据控制台的资源提示，依次确认是否需要清除，确认资源无需使用之后，请及时通过控制台或OpenAPI手动清理这些资源。例如：
删除包年包月的ECS节点
控制台：参见[包年包月转按量付费](../../../../ecs/documents/change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1.md)将包年包月ECS实例转换为按量付费ECS实例，再[释放实例](../../../../ecs/documents/user-guide/release-an-instance.md)。
OpenAPI：通过API接口[ModifyInstanceChargeType](../../../../ecs/documents/api-modifyinstancechargetype.md)将包年包月ECS实例转换为按量付费ECS实例，再[通过](../../../../ecs/documents/user-guide/release-an-instance.md)[API](../../../../ecs/documents/user-guide/release-an-instance.md)[释放实例](../../../../ecs/documents/user-guide/release-an-instance.md)。
删除专有网络VPC，相关操作请参见：
控制台：[强制删除](../../../../vpc/documents/unable-to-delete-vpc.md)[VPC](../../../../vpc/documents/unable-to-delete-vpc.md)[实例](../../../../vpc/documents/unable-to-delete-vpc.md)。
OpenAPI：[DeleteVpc - 删除一个](../../../../vpc/documents/developer-reference/api-vpc-2016-04-28-deletevpc.md)[VPC](../../../../vpc/documents/developer-reference/api-vpc-2016-04-28-deletevpc.md)。
删除包年包月的CLB实例，需要将其转换为按量付费实例后进行删除。相关操作请参见：
控制台：参见[包年包月转为按量付费](../../../../slb/documents/classic-load-balancer/support/faq-about-billing.md)将包年包月的CLB实例转换为按量付费的CLB实例，然后再[释放负载均衡实例](../../..
