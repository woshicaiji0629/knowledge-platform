n1**** | namedemo03 | aliyun_3_x64_20G_alibase_20240528.vhd | Running i-bp1aq39j2yul5y01**** | namedemo04 | m-bp12qhgxbmp5eh02**** | Stopped
示例5：分页查询ECS实例
调用[DescribeInstances](../api-describeinstances.md)分页查询杭州地域的ECS实例，每页展示5条信息。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --PageNumber 2 \ --PageSize 5 \ --output cols=InstanceId,InstanceName,ImageId,Status rows=Instances.Instance[]
返回示例
InstanceId | InstanceName | ImageId | Status ---------- | ------------ | ------- | ------ i-bp1akazu9o0rm7q0**** | demoname01 | centos_8_0_x64_20G_alibase_20191225.vhd | Running i-bp134jm1g6kqyiqu**** | demoname02 | m-bp1bc3g3b032o0ja**** | Running i-bp17qwke5y0v7hk2**** | demoname03 | centos_7_02_64_20G_alibase_20170818.vhd | Running i-bp18a6ub0vt1tvn1**** | demoname04 | centos_7_02_64_20G_alibase_20170818.vhd | Running i-bp1aq39j2yul5y01**** | demoname05 | m-bp12qhgxbmp5eh02**** | Stopped
