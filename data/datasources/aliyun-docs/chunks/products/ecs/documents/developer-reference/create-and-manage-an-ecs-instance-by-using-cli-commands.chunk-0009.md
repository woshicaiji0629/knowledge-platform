### 启动实例
调用[StartInstance](../api-startinstance.md)接口启动一台ECS实例。
场景示例：实例ID为i-bp1aq39j2yul5y01****，地域为华东1（杭州）（cn-hangzhou），启动实例时不进行故障处理，并且预检查后直接启动ECS实例。
请求示例
aliyun ecs StartInstance \ --RegionId cn-hangzhou \ --InstanceId i-bp1aq39j2yul5y01**** \ --InitLocalDisk false \ --DryRun false
返回示例
{ "RequestId": "2DD09CBD-1F4D-4923-94C7-F3BD67137BBE" }
