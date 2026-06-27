## 控制台
创建ECS实例的具体操作，请参见[自定义购买实例](create-an-instance-by-using-the-wizard.md)。在创建ECS实例时，您需要完成如下配置：
购买实例数量：在自定义购买页面右侧的购买实例数量调整框中，单击加号，将购买数量调整为3。
批量设置实例名称或主机名：指定排序的输入格式为name_prefix[begin_number,bits]name_suffix，具体规则，请参见[指定排序](batch-configure-sequential-names-or-hostnames-for-multiple-instances.md)。
重要
本示例仅用于指定排序，此处不选中有序后缀。
实例名称：输入需要设置的实例名称。本文指定新创建的3台ECS实例名称以k8s-node-开头，从0006开始排序，因此，实例名称配置为k8s-node-[6,4]。
主机名：选中主机名下方的自定义有序主机名，然后再输入需要设置的主机名。本文指定新创建的3台ECS主机名称以k8s-node-开头，从0006开始排序，且以-ecshost结尾，因此，主机名配置为k8s-node-[6,4]-ecshost。
当您完成ECS实例配置，并确认下单后，可以单击管理控制台，然后查看实例信息：
您可以在实例列表中查看新增的实例。按照本文示例，生成的实例名分别为k8s-node-0006、k8s-node-0007、k8s-node-0008。
您可以在实例详情页面的其他信息区域，查看新增实例的主机名，按照本文实例，生成的主机名分别为k8s-node-0006-ecshost、k8s-node-0007-ecshost、k8s-node-0008-ecshost。
