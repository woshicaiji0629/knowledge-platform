### 自动排序
自动排序是一种自动为实例名称和主机名称添加3位有序后缀的方式。开启自动排序功能后，实例名称和主机名称后缀从001开始递增，最大不能超过999。因此，该有序后缀是多台ECS实例的实例名称或者主机名称的区别部分。
自动排序功能默认关闭。您只需要在创建ECS实例时，手动开启该功能，然后输入实例名称和主机名称，即可自动在实例名称和主机名称后添加有序的后缀，生成新的实例名称和主机名称。
当您开启自动排序时，支持输入实例名称与主机名称的命名格式如下。
重要
如果您需要搭配使用指定排序命名实例名称与主机名称，则您输入的指定排序命名格式必须指定name_suffix，否则将只生效自动排序。指定排序的具体规则，请参见[指定排序](batch-configure-sequential-names-or-hostnames-for-multiple-instances.md)。
自动排序命名格式

| 命名格式（实例名称或主机名称） | 输入参数示例 | 生成名称（以 3 台 ECS 实例为例） |
| --- | --- | --- |
| 普通名称（未使用指定排序） | ecs | ecs001 ecs002 ecs003 |
| 指定排序：name_prefix[begin_number,bits]name_suffix | k8s-node-[]-ecshost 或 k8s-node-[,]-ecshost | k8s-node-000000-ecshost001 k8s-node-000001-ecshost002 k8s-node-000002-ecshost003 说明 指定排序和自动排序同时生效。 |
| 指定排序：name_prefix[begin_number,bits] | k8s-node-[0,4] | k8s-node-0000 k8s-node-0001 k8s-node-0002 说明 指定排序格式未设置命名后缀 name_suffix ，自动排序不生效。 |
