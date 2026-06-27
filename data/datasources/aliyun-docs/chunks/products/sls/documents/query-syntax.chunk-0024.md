### 示例

| 查询需求 | 查询语句 |
| --- | --- |
| 查询请求错误的日志。 | level:error |
| 查询用户 ID 为 usr-9a2b3c4d 的所有请求。 | user.id:usr-9a2b3c4d |
| 查询用户 ID 为 usr-9a2b3c4d ，并且查看错误状态。 | user.id:usr-9a2b3c4d and error.details.last_response.status_code :504 |
