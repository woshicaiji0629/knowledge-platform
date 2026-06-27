### 新购ECS实例
如果为新购ECS实例，可以在创建ECS实例过程中安装应用并配置性能加速。购买实例之后，可以在ECS实例详情页的相关位置进行卸载。
安装AI增强扩展程序
前往[ECS](https://ecs-buy.aliyun.com)[控制台-自定义购买](https://ecs-buy.aliyun.com)。
购买适用的GPU实例时，安装性能加速类扩展程序。购买时，请注意以下配置。其他参数配置，请参见[自定义购买实例](create-an-instance-by-using-the-wizard.md)。
实例创建成功后，系统会使用KeenTune针对该应用的业务特点进行全栈性能调优，并且提供CPFS FUSE加速等能力。
安装AI增强扩展程序将使能FUSE加速，对使用[文件存储](https://help.aliyun.com/zh/cpfs/)[CPFS](https://help.aliyun.com/zh/cpfs/)的场景非常重要，当前仅支持阿里云公共镜像Ubuntu 24.04版本。
重要
系统需要重启后才能保证所有调优项都能够正常生效。
AI增强性能加速扩展可以与GPU、eRDMA扩展一起使用。
卸载AI增强扩展程序
在ECS实例详情页的已安装扩展列表的操作列，单击卸载按钮。
