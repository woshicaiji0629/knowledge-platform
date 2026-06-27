### 使用前缀列表和端口列表
当需对多个IP地址段或端口进行统一授权时，可使用前缀列表和端口列表集中管理，从而简化安全组规则配置，提升批量维护效率。
控制台
创建前缀列表/端口列表：
前往[ECS](https://ecs.console.aliyun.com/prefixList/)[控制台-前缀列表](https://ecs.console.aliyun.com/prefixList/)。
根据需求选择到目标页签，单击创建前缀列表或创建端口列表。
引用前缀/端口列表的安全组，规则数量会根据列表设置的最大条目数计算。
在目标安全组详情页访问规则区域增加或修改规则：
设置访问来源为前缀列表，选择目标前缀列表。
设置访问目的（本实例）为端口列表，选择目标端口列表。
API使用前缀列表
调用[CreatePrefixList](../developer-reference/api-ecs-2014-05-26-createprefixlist.md)，创建一个前缀列表。创建完成后，可以通过[DescribePrefixListAttributes](../developer-reference/api-ecs-2014-05-26-describeprefixlistattributes.md)查询前缀列表的详细信息。
调用[AuthorizeSecurityGroup](../developer-reference/api-ecs-2014-05-26-authorizesecuritygroup.md)在安全组入方向规则中，设置SourcePrefixListId授权已经创建的前缀列表。
调用[AuthorizeSecurityGroupEgress](../developer-reference/api-ecs-2014-05-26-authorizesecuritygroupegress.md)在安全组出方向规则中，设置DestPrefixListId授权已经创建的前缀列表。
使用端口列表
调用[CreatePortRangeList](../developer-reference/api-ecs-2014-05-26-createportrangelist.md)，创建一个端口列表。
调用[DescribePortRangeLists](../developer-reference/api-ecs-2014-05-26-describeportrangelists.md)查看端口列表信息，并且可以通过[AuthorizeSecurityGroup](../developer-reference/api-ecs-2014-05-26-authorizesecuritygroup.md)、[AuthorizeSecurityGroupEgress](..
