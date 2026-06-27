## 相关文档
[RunInstances](../api-runinstances.md)：创建一台或多台按量付费或者包年包月ECS实例。
[实例](instance-faq.md)[FAQ](instance-faq.md)
获取价格折扣信息
您可以调用[DescribePrice](../developer-reference/api-ecs-2014-05-26-describeprice.md)接口查询云服务器ECS资源的最新价格，例如活动规则、价格、折扣等信息。
CLI命令参考如下。例如，查询在华东1（杭州）地域创建一个实例规格为ecs.c6.xlarge的最新价格信息。
aliyun ecs DescribePrice --region cn-hangzhou --RegionId 'cn-hangzhou' --ResourceType instance --InstanceType 'ecs.c6.xlarge'
该文章对您有帮助吗？
反馈
