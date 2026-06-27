| 查询需求 | 查询语句 | 调试 |
| --- | --- | --- |
| 查询 GET 请求成功（状态码为 200~299）的日志。 | request_method:GET and status in [200 299] | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/waf-demo-log/logsearch/waf-log?encode%3Dbase64%26queryString%3DcmVxdWVzdF9tZXRob2Q6R0VUIGFuZCBzdGF0dXMgaW4gWzIwMCAyOTld) |
| 查询来自非杭州地域的 GET 请求的日志。 | request_method:GET not region:cn-hangzhou | 无 |
| 查询 GET 请求或 POST 请求的日志。 | request_method:GET or request_method:POST | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DcmVxdWVzdF9tZXRob2Q6R0VUIG9yIHJlcXVlc3RfbWV0aG9kOlBPU1Q%3D) |
| 查询非 GET 请求的日志。 | not request_method:GET | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3Dbm90IHJlcXVlc3RfbWV0aG9kOkdFVA%3D%3D) |
| 查询 GET 请求或 POST 请求成功的日志。 | (request_method:GET or request_method:POST) and status in [200 299] | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DKHJlcXVlc3RfbWV0aG9kOkdFVCBvciByZXF1ZXN0X21ld
