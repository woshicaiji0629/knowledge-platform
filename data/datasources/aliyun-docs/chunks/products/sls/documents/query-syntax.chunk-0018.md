| 查询需求 | 查询语句 | 调试 |
| --- | --- | --- |
| 查询 http_user_agent 字段值中包含 Chrome 的日志。 | http_user_agent:Chrome | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DaHR0cF91c2VyX2FnZW50OkNocm9tZQ%3D%3D) |
| 查询 http_user_agent 字段值中包含 Linux 和 Chrome 的日志。 | http_user_agent:Linux and http_user_agent:Chrome | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DaHR0cF91c2VyX2FnZW50OkxpbnV4IGFuZCBodHRwX3VzZXJfYWdlbnQ6Q2hyb21l) |
| http_user_agent:"Linux Chrome" | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DaHR0cF91c2VyX2FnZW50OiJMaW51eCBDaHJvbWUi) |  |
| 查询 http_user_agent 字段值中包含 Firefox 或 Chrome 的日志。 | http_user_agent:Firefox or http_user_agent:Chrome | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DaHR0cF91c2VyX2FnZW50OkZpcmVmb3ggb3IgaHR0cF91c2VyX2FnZW50OkNocm9tZQ%3D%3D) |
| 查询 request_uri 字段值包含 /r
