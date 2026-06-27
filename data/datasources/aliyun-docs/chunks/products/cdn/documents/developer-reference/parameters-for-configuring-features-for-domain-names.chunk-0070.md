| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启远程鉴权： on：开启。 off：关闭。 | on |
| remote_auth_addr | String | 是 | 鉴权服务器地址。格式： https://cdn.aliyun.com/auth 或者 http://10.10.10.10/auth 。 | https://example.aliyundoc.com/auth |
| remote_auth_method | String | 是 | 请求方法，支持 GET/POST/HEAD。 | get |
| remote_auth_type | String | 是 | 鉴权文件类型。all 表示所有类型，多个文件类型用竖线分隔、区分大小写（jpg 不等同于 JPG）。 | all |
| remote_auth_reserve_args | String | 是 | 保留参数设置，多个请求头用竖线分隔，不区分大小写（key 等同于 KEY）。 all：保留所有参数。 ali_delete_all_args：表示删除所有 URL 参数。 | all |
| remote_auth_custom_args | String | 否 | 添加自定义参数，多个参数用竖线分隔、区分大小写（key 不等同于 KEY）。 | 空 |
| remote_auth_reserve_header | String | 是 | 保留请求头设置，多个请求头用竖线分隔，不区分大小写（http_remote_addr 等同于 HTTP_Remote_Addr）。 all：保留所有请求头。 ali_delete_all_headers：删除所有请求头。 | all |
| remote_auth_custom_header | String | 否 | 添加自定义请求头，多个请求头用竖线分隔、不区分大小写（http_remote_addr 等同于 HTTP_Remote_Addr）。 | 空 |
| remote_auth_success_code | Integer | 是 | 鉴权成功状态码，指鉴权服务器在鉴权成功之后传给 CDN 的鉴权结果。例如：200。支持配置多个状态码，多个状态码之间用英文逗号分隔。 | 200 |
| remote_auth_fail_code | Integer | 是 | 鉴权失败状态码，指鉴权服务器在鉴权失败之后传给 CDN 的鉴权结果。例如：403。支持配置多个状态码，多个状态码之间用英文逗号分隔。 | 403,404 |
| remote_auth_other_code_act | String | 否
