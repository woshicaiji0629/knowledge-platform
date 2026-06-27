hOut | 公网 IP 带宽： 1 |
| Password | 实例登录密码： <yourPassword> 说明 您需要自定义复杂密码以保护 ECS 实例的安全。 |
| SystemDisk.Category | 系统盘类型：cloud_essd |
| SystemDisk.Size | 系统盘大小：40 |

请求示例
aliyun ecs RunInstances \ --RegionId cn-hangzhou \ --ImageId aliyun_3_x64_20G_alibase_20240528.vhd \ --InstanceType ecs.c7.large \ --SecurityGroupId sg-bp18z2q1jg4gq95t**** \ --VSwitchId vsw-bp11hf5r945gewysp**** \ --InstanceName ecs_cli_demo \ --InstanceChargeType PrePaid \ --PeriodUnit Month \ --Period 1 \ --InternetMaxBandwidthOut 1 \ --Password <yourPassword> \ --SystemDisk.Category cloud_essd \ --SystemDisk.Size 40
返回示例
{ "InstanceIdSets": { "InstanceIdSet": [ "i-bp1de173dp87k5uv****" ] }, "OrderId": 23577729747****, "RequestId": "B0855F1A-279F-5153-BAA9-C245E073****", "TradePrice": **** }
