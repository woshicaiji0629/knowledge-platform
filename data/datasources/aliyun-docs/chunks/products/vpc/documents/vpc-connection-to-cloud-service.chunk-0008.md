### API
网关终端节点：
创建网关终端节点并配置终端节点策略：调用[CreateVpcGatewayEndpoint](developer-reference/api-vpc-2016-04-28-createvpcgatewayendpoint.md)接口。
创建时需要传入终端节点服务名称字段ServiceName，可以通过调用[ListVpcEndpointServicesByEndUser](developer-reference/api-vpc-2016-04-28-listvpcendpointservicesbyenduser.md)接口，查询可使用的终端节点服务。
PolicyDocument字段用于配置终端节点策略，语法与访问控制RAM产品的[权限策略语言](../../ram/documents/policy-elements.md)相同。
修改网关终端节点策略：调用[UpdateVpcGatewayEndpointAttribute](developer-reference/api-vpc-2016-04-28-updatevpcgatewayendpointattribute.md)接口，传入PolicyDocument字段。
绑定路由表：调用[AssociateRouteTablesWithVpcGatewayEndpoint](developer-reference/api-vpc-2016-04-28-associateroutetableswithvpcgatewayendpoint.md)接口。
解绑路由表：调用[DissociateRouteTablesFromVpcGatewayEndpoint](developer-reference/api-vpc-2016-04-28-dissociateroutetablesfromvpcgatewayendpoint.md)接口。
删除网关终端节点：调用[DeleteVpcGatewayEndpoint](developer-reference/api-vpc-2016-04-28-deletevpcgatewayendpoint.md)接口。
OSS Bucket：
配置OSS的bucket授权策略：调用[PutBucketPolicy](../../oss/documents/developer-reference/putbucketpolicy.md)接口。
修改Bucket授权策略：调用[PutBucketPolicy](../../oss/documents/developer-reference/putbucketpolicy.md)接口，传入JSON形式的权限策略。
删除Bucket授权策略：调用[DeleteBucketPolicy](../../oss/d
