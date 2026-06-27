## 配置对等连接
控制台
前置检查：
确保两端VPC的网段不重叠。若重叠，需将业务迁移到网段不重叠的VPC中。
如果初次使用VPC对等连接，需要确保两端VPC所属账号都开通CDT功能。
创建对等连接：
前往[专有网络控制台 - VPC](https://vpc.console.aliyun.com/vpcpeer/cn-hangzhou/vpcpeers)[对等连接](https://vpc.console.aliyun.com/vpcpeer/cn-hangzhou/vpcpeers)，在页面上方选择VPC所在的地域，单击创建对等连接。
创建对等连接：根据两端VPC实例所属的账号和地域，选择接收端账号类型和接收端地域类型。
接收端账号类型：
同账号：系统会自动接受请求并建立连接。可勾选VPC系统路由表添加对端VPC CIDR路由，将由系统配置双向路由。
跨账号：需要使用接收端账号前往[专有网络控制台 - VPC](https://vpc.console.aliyun.com/vpcpeer/cn-hangzhou/vpcpeers)[对等连接](https://vpc.console.aliyun.com/vpcpeer/cn-hangzhou/vpcpeers)，在页面上方选择 VPC 所在的地域，在目标对等连接的操作列单击接收。
接收端也可以拒绝或删除连接请求，可以参考[VPC](vpc-peer-to-peer-connection.md)[对等连接的状态机](vpc-peer-to-peer-connection.md)了解完整流程。
接收端地域类型为跨地域时，需配置链路类型和接收端地域。
支持铂金、金两种链路类型，提供不同质量的流量传输服务，对应不同的[计费单价](https://help.aliyun.com/zh/cdt/inter-region-data-transfers#d0450e8c0bzxe)。
铂金（服务可用性承诺：99.995%）：适用于对链路抖动、时延敏感，对链路质量要求较高的业务。例如证券交易、在线语音、视频会议、实时游戏等。
金（服务可用性承诺：99.95%）：适用于对链路质量不敏感的业务。例如数据同步、文件传输等。
双向路由配置：
如需使用IPv6地址互访，需配置指向对端VPC实例的IPv6网段的路由条目。
使用发起端 VPC 所属账号：单击发起端列的配置路由条目，选择该 VPC 中需连通的资源所在交换机绑定的路由表，配置目标网段为接收端网段。
使用接收端 VPC 所属账号：单击接收端列的配置路由条目，选择该 VPC 中需连通的资源所在交换机绑定的路由表，配置目标网段为发起端网段。
验证连通性：
路径分析：分析过程不发送真实数据包，不会影响业务运行。
在目标对等连接实例的诊断列选择发起诊断>路径分析或单击目标对等连接
