### 方式二：创建自定义权限策略进行授权
使用阿里云账号（主账号）或RAM管理员登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
创建一个自定义权限策略，其中在脚本编辑页签，请使用以下脚本替换配置框中的原有内容。具体操作，请参见[通过脚本编辑模式创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)。
重要
Project名称表示用于管理告警数据的Project，请根据实际情况替换。
sls-alert-*表示当前阿里云账号下所有的全局告警中心Project。全局告警中心Project中包含该账号下所有告警规则的评估数据、发送的日志和告警相关的全局报表等。如果您只想授权RAM用户操作单个全局告警中心Project的权限，您可以将sls-alert-*配置为单个Project的名称，格式为sls-alert-${uid}-${region}，例如sls-alert-148****6461-cn-hangzhou。
创建LogStore、创建索引及更新索引的权限策略，用于RAM用户操作告警相关的系统日志库（告警历史日志库、全局告警中心日志库），从而进行告警历史等报表的查看。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "log:GetLogStore", "log:UpdateLogStore", "log:CreateLogStore", "log:CreateIndex", "log:UpdateIndex" ], "Resource": [ "acs:log:*:*:project/Project名称/logstore/internal-alert-history", "acs:log:*:*:project/sls-alert-*/logstore/internal-alert-center-log" ] }, { "Effect": "Allow", "Action": [ "log:*" ], "Resource": "acs:log:*:*:project/Project名称/job/*" }, { "Effect": "Allow", "Action": [ "log:GetProject", "log:CreateProject" ], "Resource": [ "acs:log:*:*:project/sls-alert-*" ] }, { "Effect": "Allow", "Action": [ "log:GetLogStoreLogs", "log:ListLogStores"
