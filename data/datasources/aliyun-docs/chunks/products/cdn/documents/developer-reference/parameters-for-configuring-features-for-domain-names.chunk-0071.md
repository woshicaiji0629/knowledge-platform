remote_auth_fail_code | Integer | 是 | 鉴权失败状态码，指鉴权服务器在鉴权失败之后传给 CDN 的鉴权结果。例如：403。支持配置多个状态码，多个状态码之间用英文逗号分隔。 | 403,404 |
| remote_auth_other_code_act | String | 否 | 其他状态码是否放行，表示在鉴权服务器返回的状态码既不是鉴权成功状态码，也不是鉴权失败状态码的情况下，CDN 对用户请求的处理方式，取值： pass：通过（默认值）。 reject：拒绝。 | pass |
| remote_auth_fail_resp_code | Integer | 是 | 鉴权失败 CDN 响应状态码。例如：403，CDN 传给用户的状态码。 | 403 |
| remote_auth_timeout | Integer | 是 | 鉴权超时配置，单位 ms，最大值为 3000。 | 500 |
| remote_auth_timeout_action | String | 是 | 鉴权超时行为，取值： pass：CDN 将直接通过用户请求。 reject：CDN 将响应上面配置的“鉴权失败 CDN 响应状态码”给用户。 | pass |
