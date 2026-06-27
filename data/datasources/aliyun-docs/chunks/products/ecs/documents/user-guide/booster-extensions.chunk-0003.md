### 新购ECS实例
如果您是新购ECS实例，可以在创建ECS实例过程中安装应用并配置性能加速。购买实例之后，只能通过命令行方式关闭性能加速能力或卸载已安装的应用。
安装应用性能加速
前往[ECS](https://ecs-buy.aliyun.com)[控制台-自定义购买](https://ecs-buy.aliyun.com)。
购买倚天实例、AMD实例或Intel实例时，安装性能加速类扩展程序。
购买时，请注意以下配置。其他参数配置，请参见[自定义购买实例](create-an-instance-by-using-the-wizard.md)。
倚天实例
实例：选择倚天实例。具体规格请参见[适用实例](booster-extensions.md)。
镜像：选择Alibaba Cloud Linux 3镜像。
扩展程序：
驱动：如需配置eRDMA，请选中eRDMA驱动，系统会自动安装。
性能加速：选择需要安装的应用（如Nginx、MySQL、Redis等），默认版本及性能提升请参见[默认安装的应用版本及性能提升](booster-extensions.md)。
说明
支持安装的应用，以页面实际呈现为准。
Spark性能加速扩展不支持在创建实例时安装，仅支持在创建实例后在实例详情页安装。
启用eRDMA透明替换（可选）：选择Redis且内核版本≥5.10.134-16时，可启用eRDMA透明替换，将传输协议从TCP切换到RDMA，提升网络性能。
重要
eRDMA透明替换技术基于共享内存通信（SMC）实现，启用后，部分用户运维工具将不可用。更多信息，请参见[共享内存通信（SMC）常见问题](https://help.aliyun.com/zh/alinux/user-guide/faq-about-smc)和[共享内存通信（SMC）使能和配置说明](https://help.aliyun.com/zh/alinux/user-guide/use-smc)。
请勿同时选中eRDMA驱动和启动eRDMA透明替换，否则会卸载并安装新的eRDMA驱动，从而导致eRDMA透明替换失效。
关闭eRDMA透明替换：购买实例后，如不再需要该功能，关闭性能加速即可。具体操作请参见[关闭性能加速能力](booster-extensions.md)。
弹性网卡（条件必选）：若选中启用eRDMA透明替换，需在弹性网卡处，勾选弹性RDMA接口。
AMD实例
实例：选择AMD实例。具体规格请参见[适用实例](booster-extensions.md)。
镜像：选择Alibaba Cloud Linux 3镜像。
扩展程序：
驱动：如需配置eRDMA，请选中eRDMA驱动，系统会自动安装。
性能加速：选择需要安装的应用（如Nginx、MySQL、Memcached等），默认版本及性能
