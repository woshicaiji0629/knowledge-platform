not remote_user:"null" | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3Dbm90IHJlbW90ZV91c2VyOiJudWxsIg%3D%3D) |
| 查询不存在 remote_user 字段的日志。 | not remote_user:* | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3Dbm90IHJlbW90ZV91c2VyOio%3D) |
| 查询存在 remote_user 字段的日志。 | remote_user:* | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DcmVtb3RlX3VzZXI6Kg%3D%3D) |
| 查询 城市 字段值不为 上海 的日志。 | not 城市:上海 说明 当查询中文字符串时，需要在配置索引时，打开 包含中文 开关。更多信息，请参见 [创建索引](create-indexes.md) 。 | 无 |
