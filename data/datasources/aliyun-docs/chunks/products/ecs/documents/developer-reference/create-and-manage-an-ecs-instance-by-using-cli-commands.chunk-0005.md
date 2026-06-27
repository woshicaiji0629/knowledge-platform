ritygroup.md)创建安全组。
请求示例
aliyun ecs CreateSecurityGroup \ --RegionId cn-hangzhou \ --VpcId vpc-bp1d9v4763ym2hlzt****
返回示例
{ "RequestId": "B1C25C34-9B84-49E3-9E50-FB7D7970****", "SecurityGroupId": "sg-bp18z2q1jg4gq95t****" }
调用[AuthorizeSecurityGroup](api-ecs-2014-05-26-authorizesecuritygroup.md)添加安全组规则。
假设在安全组（ID为sg-bp18z2q1jg4gq95t****）的入方向放行22端口，协议为TCP。
请求示例
aliyun ecs AuthorizeSecurityGroup \ --RegionId cn-hangzhou \ --SecurityGroupId sg-bp18z2q1jg4gq95t**** \ --IpProtocol tcp \ --SourceCidrIp 0.0.0.0/0 \ --PortRange 22/22
返回示例
{ "RequestId": "FA8B1E61-C9C9-4D91-9628-64B8E2F4****" }
创建ECS实例。
调用[RunInstances](api-ecs-2014-05-26-runinstances.md)创建一个包年包月的ECS实例。
场景示例
