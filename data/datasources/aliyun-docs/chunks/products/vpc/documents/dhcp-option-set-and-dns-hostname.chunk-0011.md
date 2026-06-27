### API
与控制台逻辑不同的是，调用[CreateVpc](developer-reference/api-vpc-2016-04-28-createvpc.md)创建 VPC 时，可调整EnableDnsHostname参数，启用/禁用 DNS 主机名。
调整[ModifyVpcAttribute](developer-reference/api-vpc-2016-04-28-modifyvpcattribute.md)的EnableDnsHostname参数，启用/禁用 DNS 主机名。
调用[RunInstances](../../ecs/documents/developer-reference/api-ecs-2014-05-26-runinstances.md)创建实例时，指定PrivateDnsNameOptions相关参数，配置实例的私网域名解析。
调整[ModifyInstanceAttribute](../../ecs/documents/developer-reference/api-ecs-2014-05-26-modifyinstanceattribute.md)的PrivateDnsNameOptions相关参数，配置目标 ECS 的私网域名解析。
