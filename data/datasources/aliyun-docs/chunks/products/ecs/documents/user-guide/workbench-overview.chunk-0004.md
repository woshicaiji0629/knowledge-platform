## RAM用户使用Workbench的权限设置
在开通服务关联角色后，RAM用户使用Workbench需设置如下权限策略，该策略代表用户可以使用Workbench连接所有ECS实例。
{ "Version": "1", "Statement": [ { "Action": "ecs-workbench:LoginInstance", "Resource": "*", "Effect": "Allow" } ] }
如果需要限制用户可以通过Workbench连接的实例，可通过修改Resource字段实现，格式如下：
{ "Version": "1", "Statement": [ { "Action": "ecs-workbench:LoginInstance", "Resource": [ "acs:ecs-workbench:{#regionId}:{#accountId}:workbench/{#instanceId}", "acs:ecs-workbench:{#regionId}:{#accountId}:workbench/{#instanceId}" ], "Effect": "Allow" } ] }
参数说明如下：
{#regionId}：实例所在地域ID，可设置为通配符*。
{#accountId}：主账号ID，可设置为通配符*。
{#instanceId}：目标实例ID，可设置为通配符*。
示例
例如，设置RAM用户可使用Workbench连接所有地域和账号下实例ID为i-001和i-002的实例时，可设置以下权限策略。
{ "Version": "1", "Statement": [ { "Action": "ecs-workbench:LoginInstance", "Resource": [ "acs:ecs-workbench:*:*:workbench/i-001", "acs:ecs-workbench:*:*:workbench/i-002" ], "Effect": "Allow" } ] }
