pc](../../../vpc/documents/developer-reference/api-vpc-2016-04-28-deletevpc.md) | RegionId | 地域： cn-hangzhou |
| VpcId | VPC ID： vpc-bp1aag0sb9s4i92i3 **** |  |

示例代码如下：
#!/bin/bash # 定义要释放的资源信息 INSTANCE_ID='ecs_cli_demo' # ECS实例ID SECURITY_GROUP_ID='sg-bp1esyhwfbqeyudt****' # 安全组ID VSWITCH_ID='vsw-bp1nzprm8h7mmnl8t****' # VSwitchID VPC_ID='vpc-bp1aag0sb9s4i92i3****' # VPC ID REGION='cn-hangzhou' # 区域 echo "正在释放资源..." # 删除实例 aliyun ecs DeleteInstance \ --region ${REGION} \ --InstanceId ${INSTANCE_ID} # 删除安全组 aliyun ecs DeleteSecurityGroup \ --region ${REGION} \ --RegionId ${REGION} \ --SecurityGroupId ${SECURITY_GROUP_ID} # 删除 VSwitch aliyun vpc DeleteVSwitch \ --region ${REGION} \ --RegionId ${REGION} \ --VSwitchId ${VSWITCH_ID} # 删除 VPC aliyun vpc DeleteVpc \ --region ${REGION} \ --RegionId ${REGION} \ --VpcId ${VPC_ID} echo "释放完成"
