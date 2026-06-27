## denied by sts or ram, action:*[​](https://sls.aliyun.com/doc/sqlerror/denied_by_sts_ram.html#denied-by-sts-or-ram-action)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/innermost_sql_missing_from.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
您当前查询的LogStore在您当前身份下没有权限。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/innermost_sql_missing_from.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
该LogStore未授权给您当前身份。
解决方法
检查RAM权限，并授权该LogStore读权限给您当前身份，授权资源描述：
action: log:GetLogStoreLogs, resource: acs:log:<region>:<uid>:project/<project>/logstore/<logstore>
