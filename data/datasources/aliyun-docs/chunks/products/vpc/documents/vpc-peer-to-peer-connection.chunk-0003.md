机绑定的路由表，配置目标网段为接收端网段。
使用接收端 VPC 所属账号：单击接收端列的配置路由条目，选择该 VPC 中需连通的资源所在交换机绑定的路由表，配置目标网段为发起端网段。
验证连通性：
路径分析：分析过程不发送真实数据包，不会影响业务运行。
在目标对等连接实例的诊断列选择发起诊断>路径分析或单击目标对等连接实例ID进入路径分析页签。
配置源与目的，指定具体的协议和端口号来模拟业务访问场景，校验二者的连通性。
系统将检查路由/安全组/网络ACL的配置，并给出诊断结果。
单向路径可达时，需配置反向路径进行连通性校验。
手动验证：在发起端VPC内的ECS，执行ping <对端 ECS 的私网 IP>。
创建跨地域对等连接后，单击实例ID，支持编辑跨地域对等连接的带宽（Mbps）和链路类型。两端账号均可删除VPC对等连接。删除后，私网互访能力将会中断，且删除后无法恢复，需确保在对业务无影响的情况下谨慎操作。
API
创建对等连接
调用[CreateVpcPeerConnection](developer-reference/api-vpcpeer-2022-01-01-createvpcpeerconnection.md)创建VPC对等连接。
两端VPC属于不同账号时，需使用接收端账号调用[AcceptVpcPeerConnection](developer-reference/api-vpcpeer-2022-01-01-acceptvpcpeerconnection.md)接受VPC对等连接。
接收端可以调用[RejectVpcPeerConnection](developer-reference/api-vpcpeer-2022-01-01-rejectvpcpeerconnection.md)拒绝VPC对等连接。
使用两端 VPC 所属账号，分别调用[GetVpcPeerConnectionAttribute](developer-reference/api-vpcpeer-2022-01-01-getvpcpeerconnectionattribute.md)查询两端VPC的网段。
使用两端 VPC 所属账号，分别调用[CreateRouteEntry](developer-reference/api-vpc-2016-04-28-createrouteentry.md)创建指向对等连接的路由条目。
修改跨地域对等连接
调用[ModifyVpcPeerConnection](developer-reference/api-vpcpeer-2022-01-01-modifyvpcpeerconnection.md)修改跨地域VPC对等连接的带宽或链路类型。
删除对等连接
调用[DeleteRouteEntry](developer-referen
