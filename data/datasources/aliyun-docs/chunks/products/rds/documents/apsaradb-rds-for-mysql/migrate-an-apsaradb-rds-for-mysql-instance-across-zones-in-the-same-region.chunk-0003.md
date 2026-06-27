s/product-overview/what-is-dts#concept-26592-zh)任务，可用区迁移后，需要重启相应的DTS任务。
重新创建表文件：迁移可用区会重新创建表文件，从而导致表文件的创建时间发生变化，进而引起INFORMATION_SCHEMA中表的CREATE_TIME字段发生变化。
如果迁移的目标可用区资源不足，则可能迁移可用区失败。
迁移可用区时，不支持只更改交换机。若您需要修改实例的交换机，请参见[切换专有网络](change-the-vpc-and-vswitch-for-an-apsaradb-rds-for-mysql-instance.md)[VPC](change-the-vpc-and-vswitch-for-an-apsaradb-rds-for-mysql-instance.md)[和虚拟交换机](change-the-vpc-and-vswitch-for-an-apsaradb-rds-for-mysql-instance.md)。
当实例存储类型为高性能云盘并且开启了[Buffer Pool Extension（BPE）功能](buffer-pool-extension-bpe.md)时，无法迁移至不支持Buffer Pool Extension（BPE）的可用区。Buffer Pool Extension（BPE）支持的地域及可用区请参见[适用范围](buffer-pool-extension-bpe.md)。
您可以关闭Buffer Pool Extension（BPE）后，再进行可用区迁移。
