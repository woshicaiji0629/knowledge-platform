选择地域。
选择要在哪个地域创建RDS实例。
如果您已购买[云服务器](../../../ecs/documents/user-guide/what-is-ecs.md)[ECS](../../../ecs/documents/user-guide/what-is-ecs.md)，并且期望ECS与RDS内网互通，请选择ECS实例所在地域。否则，ECS实例只能通过外网访问RDS实例，无法发挥最佳性能。
重要
RDS实例购买后，地域不支持更改，请慎重选择。
如果您要通过ECS以外的设备（例如本地服务器或电脑）连接RDS实例，则选择将RDS实例创建在离该设备较近的地域，可以降低网络时延。后续通过外网地址连接RDS。
选择引擎。
本文介绍快速创建RDS MariaDB实例，固定配置为MariaDB。
选择实例规格。
根据不同系列实例我们提供不同规格，您可以根据实际业务需要进行选择。如此规格无法满足需要，也可在购买后进行[变更配置](change-the-specifications-of-an-apsaradb-rds-for-mariadb-instance.md)或在页面顶部选择标准创建进行自定义。更多信息，请参见[创建](create-an-apsaradb-rds-for-mariadb-instance-1.md)[RDS MariaDB](create-an-apsaradb-rds-for-mariadb-instance-1.md)[实例](create-an-apsaradb-rds-for-mariadb-instance-1.md)。
选择存储空间。
存储空间范围（最小值和最大值）与前面选择的实例规格和存储类型有关。您可以调整存储空间，增减幅度最少为5 GB。
设置网络和交换机。
网络类型固定配置为专有网络，建议选择与ECS实例相同的VPC。ECS实例与RDS实例位于不同VPC时，无法内网互通。
说明
VPC相同，交换机不同，ECS实例与RDS实例也可以内网互通。
（可选）查看更多配置项。
在快捷创建中，阿里云已自动帮您默认配置了其他参数，您可以单击更多配置查看其他信息。
重要
实例创建后暂不支持变更VPC，如果您需要通过ECS内网连接RDS实例，除了需要在相同地域外，还需要确保VPC一致，如不一致，请使用标准创建方式，各参数含义及具体方法，请参见[创建](create-an-apsaradb-rds-for-mariadb-instance-1.md)[RDS MariaDB](create-an-apsaradb-rds-for-mariadb-instance-1.md)[实例](create-an-apsaradb-rds-for-mariadb-instance-1.md)。
选择购买数量。
默认1个，支持一次性最多购买10个实例，根
