## 操作步骤
确认您的应用是否已部署或将要部署在[阿里云](../../../ecs/documents/user-guide/what-is-ecs.md)[ECS](../../../ecs/documents/user-guide/what-is-ecs.md)或其它阿里云产品（本文以ECS为例）。
如果是，进入步骤2。
如果不是，且不迁移上云，本文操作结束。请前往创建RDS实例，后续通过外网连接RDS实例。
说明
外网访问的安全性、性能、稳定性都弱于内网访问。
确认具体的ECS实例。
打开[ECS](https://ecs.console.aliyun.com/server/region#/server/region/cn-hangzhou)[实例列表](https://ecs.console.aliyun.com/server/region#/server/region/cn-hangzhou)，在顶部选择地域。数字代表该地域有多少个ECS实例。
说明
如果未创建任何ECS实例，请参见[创建](../../../ecs/documents/getting-started/create-and-manage-an-ecs-instance-by-using-the-ecs-console.md)[ECS](../../../ecs/documents/getting-started/create-and-manage-an-ecs-instance-by-using-the-ecs-console.md)[实例](../../../ecs/documents/getting-started/create-and-manage-an-ecs-instance-by-using-the-ecs-console.md)。
找到已部署或将要部署应用的ECS实例，即要连接RDS的ECS实例，例如ECS实例A。
查看ECS实例的地域和网络类型。
在ECS实例列表中，地域显示在页面顶部的地域切换区域，网络类型显示在实例列表的网络类型列中。
说明
如果网络类型是经典网络，建议迁移至专有网络。具体操作参见[ECS](../../../ecs/documents/user-guide/migrate-ecs-instances-from-the-classic-network-to-a-vpc.md)[实例从经典网络迁移到专有网络](../../../ecs/documents/user-guide/migrate-ecs-instances-from-the-classic-network-to-a-vpc.md)。
查看VPC。
如果网络类型是专有网络，您还需要单击实例ID，在实例详情页的配置信息区域查看专有网络ID和名称（VPC ID和名称）。
