### API
步骤一：创建和购买弹性保障
调用[CreateElasticityAssurance](../developer-reference/api-ecs-2014-05-26-createelasticityassurance.md)接口创建弹性保障或者弹性保障-分时保障。
调用[PurchaseElasticityAssurance](../developer-reference/api-ecs-2014-05-26-purchaseelasticityassurance.md)接口购买一个准备完毕且处于未激活状态的弹性保障服务。
步骤二：使用弹性保障创建实例
调用[RunInstances](../developer-reference/api-ecs-2014-05-26-runinstances.md)接口创建实例。
通过PrivatePoolOptions.MatchCriteria指定私有池类型。若私有池类型选择指定模式（Target），必须通过PrivatePoolOptions.Id设置目标私有池ID。
步骤三：查看和修改弹性保障
查询
调用[DescribeElasticityAssurances](../developer-reference/api-ecs-2014-05-26-describeelasticityassurances.md)接口查询弹性保障服务的详细信息。
调用[DescribeElasticityAssuranceInstances](../developer-reference/api-ecs-2014-05-26-describeelasticityassuranceinstances.md)接口查询弹性保障服务已匹配实例列表。
修改
调用[ModifyElasticityAssurance](../developer-reference/api-ecs-2014-05-26-modifyelasticityassurance.md)接口修改一个弹性保障服务的部分信息，包含名称、描述、容量。
调用[ModifyInstanceAttachmentAttributes](../developer-reference/api-ecs-2014-05-26-modifyinstanceattachmentattributes.md)接口修改实例的私有池匹配模式。
