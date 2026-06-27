### 报错 Unauthorized
该错误表示当前账号或 RAM 用户缺少必要权限。
解决方法：为当前账号授予以下权限：

| API 名称 | Action | Resource |
| --- | --- | --- |
| GetLogsV2 | log:GetLogStoreLogs | acs:log:<account>:<region>:project/<Project>/logstore/<Logstore> |
| GetIndex | log:GetIndex | acs:log:<account>:<region>:project/<Project> |
