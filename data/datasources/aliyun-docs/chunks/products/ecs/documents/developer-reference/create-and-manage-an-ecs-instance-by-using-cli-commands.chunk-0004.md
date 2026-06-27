### 创建ECS实例
以在杭州地域创建一个基于Alibaba Cloud Linux镜像的包年包月的ECS实例为例，指导您如何通过CLI创建ECS实例。
准备工作。
在创建ECS实例前，请确保您已经创建了专有网络VPC、交换机、安全组，并获取其ID。
说明
如果您已有上述资源且符合需求，可跳过该步骤。
调用[CreateVpc](../../../vpc/documents/developer-reference/api-vpc-2016-04-28-createvpc.md)创建VPC。
假设在华东1（杭州）创建专有网络VPC，VPC网段为192.168.0.0/16。
请求示例
aliyun vpc CreateVpc \ --RegionId cn-hangzhou \ --CidrBlock 192.168.0.0/16
返回示例
{ "RequestId": "EC94C73B-8103-4B86-B353-E65C7C9E****", "ResourceGroupId": "rg-acfmzw2jz2z****", "RouteTableId": "vtb-bp1jxpr9ji5wcn4yv****", "VRouterId": "vrt-bp1dyxemup2q4ouga****", "VpcId": "vpc-bp1d9v4763ym2hlzt****" }
调用[CreateVSwitch](../../../vpc/documents/developer-reference/api-vpc-2016-04-28-createvswitch.md)在VPC中创建交换机。
假设交换机网段为192.168.0.0/24，VPC ID为vpc-bp1d9v4763ym2hlzt****。
请求示例
aliyun vpc CreateVSwitch \ --CidrBlock 192.168.0.0/24 \ --VpcId vpc-bp1d9v4763ym2hlzt**** \ --ZoneId=cn-hangzhou-i
返回示例
{ "RequestId": "AF1787C4-0D81-44F0-A324-D5C54EA0****", "VSwitchId": "vsw-bp11hf5r945gewysp****" }
调用[CreateSecurityGroup](api-ecs-2014-05-26-createsecuritygroup.md)创建安全组。
请求示例
aliyun ecs CreateSecurityGroup \ --RegionId cn-hangzhou \ --VpcId vpc-bp1d9v4763ym2hlzt****
返回示例
{ "RequestId": "B1C25C34-9B84-49E3-9E5
