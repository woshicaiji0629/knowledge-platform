## 使用说明
使用资源组管理ECS资源之前，您需要了解如下说明：
一个资源组可以包含不同地域的ECS资源。
例如：资源组A中可以包含华北2（北京）地域的实例和华东1（杭州）地域的实例。
同一个账号内不同资源组中，相同地域的资源可以进行关联。
例如：资源组A中华北2（北京）地域的实例可以加入到资源组B中华北2（北京）地域的VPC内。
资源组会继承RAM用户的全局权限。即如果您授权RAM用户管理所有的阿里云资源，则阿里云账号下所有的资源组都会在该RAM用户中显示出来。
使用资源组管理ECS资源的具体操作，请参见[使用资源组限制](../../../ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)[RAM](../../../ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)[用户管理指定的](../../../ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)[ECS](../../../ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)[实例](../../../ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)。
