2qhgxbmp5eh02****标签的ECS实例信息。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --ImageId m-bp12qhgxbmp5eh02**** \ --output cols=InstanceId,InstanceName,Description,ImageId,Status rows=Instances.Instance[]
返回示例
InstanceId | InstanceName | Description | ImageId | Status ---------- | ------------ | ----------- | ------- | ------ i-bp14a7xie8erwsvo**** | demo01 | desc01 | m-bp12qhgxbmp5eh02**** | Running i-bp1aq39j2yul5y01**** | demo02 | desc02 | m-bp12qhgxbmp5eh02**** | Stopped
示例4：查询指定VPC内的ECS实例
假设VPC ID为vpc-bp1vwnn14rqpyiczj****、交换机ID为vsw-bp1ddbrxdlrcbim46****。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --VpcId vpc-bp1vwnn14rqpyiczj**** \ --VSwitchId vsw-bp1ddbrxdlrcbim46**** \ --output cols=InstanceId,InstanceName,ImageId,Status rows=Instances.Instance[]
返回示例
InstanceId | InstanceName | ImageId | Status ---------- | ------------ | ------- | ------ i-bp14a7xie8erwsvo**** | namedemo01 | m-bp12qhgxbmp5eh02**** | Running i-bp1c271nqm264lwj**** | namedemo02 | P2VSImageLnx125 | Running i-bp18a6ub0vt1tvn1**** | namedemo03 | aliyun_3_x64_20G_alibase_20240528.vhd | Running i-bp1aq39j2yul5y01**** | namedemo04 | m-bp12qhgxbmp5eh02**** | Stopped
示例5：分页查询ECS实例
调用[De
