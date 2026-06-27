difyVpcPeerConnection](developer-reference/api-vpcpeer-2022-01-01-modifyvpcpeerconnection.md)修改跨地域VPC对等连接的带宽或链路类型。
删除对等连接
调用[DeleteRouteEntry](developer-reference/api-vpc-2016-04-28-deleterouteentry.md)删除指向对等连接的路由条目。
调用[DeleteVpcPeerConnection](developer-reference/api-vpcpeer-2022-01-01-deletevpcpeerconnection.md)删除VPC对等连接。
路径分析
依次调用以下API来使用路径分析校验连通性。
[创建网络分析路径](https://help.aliyun.com/zh/nis/developer-reference/api-nis-2021-12-16-createnetworkpath)
[创建网络可达性分析任务](https://help.aliyun.com/zh/nis/developer-reference/api-nis-2021-12-16-createnetworkreachableanalysis)
[获取网络可达性分析任务结果](https://help.aliyun.com/zh/nis/developer-reference/api-nis-2021-12-16-getnetworkreachableanalysis)
Terraform
同账号对等连接Resources：[alicloud_vpc_peer_connection](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_peer_connection)、[alicloud_route_entry](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/route_entry)Data Sources：[alicloud_account](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/account)# VPC所属账号 data "alicloud_account" "default" {} provider "alicloud" { alias = "local" region = "cn-hangzhou" #发起端VPC所属地域。 } p
