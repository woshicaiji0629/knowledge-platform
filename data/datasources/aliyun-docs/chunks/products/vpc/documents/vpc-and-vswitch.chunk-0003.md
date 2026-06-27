## API
与控制台逻辑不同的是，使用CreateVpc仅创建一个空的专有网络，还需要使用CreateVSwitch创建交换机。
依次调用[CreateVpc](developer-reference/api-vpc-2016-04-28-createvpc.md)和[CreateVSwitch](developer-reference/api-vpc-2016-04-28-createvswitch.md)创建专有网络和交换机。
依次调用[DeleteVSwitch](developer-reference/api-vpc-2016-04-28-deletevswitch.md)和[DeleteVpc](developer-reference/api-vpc-2016-04-28-deletevpc.md)删除交换机和专有网络。
1、删除交换机前，需要确保交换机未共享、未绑定自定义路由表和网络ACL并且交换机内的云产品资源已释放。2、删除专有网络前，需要确保VPC内资源已释放完成，且已取消与云企业网等网络服务的关联。
