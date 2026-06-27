### 原因描述
开源Redis集群不支持多DB功能，用户在从主备架构变配至集群架构后，无法执行SELECT命令。而云数据库 Tair（兼容 Redis）的代理模式支持多DB功能。通过代理模式，您可以在集群架构、读写分离架构中使用SELECT命令，切换至其他DB。该功能可以帮助您更平滑地从单机版升级至集群架构或读写分离架构，更多信息请参见[Tair Proxy](features-of-proxy-nodes.md)[特性说明](features-of-proxy-nodes.md)。
StackExchange.Redis 2.7.20（不包含）之前的版本在识别阿里云Tair的代理节点时，将其识别为Cluster，从而导致SELECT命令无法执行，该问题已经在StackExchange.Redis 2.7.20版本进行了修复。
