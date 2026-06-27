| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ip_list | String | 是 | IP 列表，多个用半角逗号（,）分隔。 | 192.168.0.1/24 |
| customize_response_status_code | String | 否 | 自定义响应状态码，默认为空（表示响应状态码设置为 403）。可以输入 3 位数值来设置自定义响应状态码。 | 429 |
| ip_acl_xfwd | String | 否 | 使用 X-Forwarded-For 请求头中的 IP，取值范围： on：默认取值，使用用户请求中的 x-forwarded-for 请求头（从左向右取第一个 IP）作为判断依据。 off：使用 真实建连 ip 作为判断依据。 all：同时使用 x-forwarded-for 和 真实连接 ip 作为判断依据。 | all |
| ip_list_notes | String | 否 | 备注信息，用于记录 IP 列表的备注说明信息。 | 192.x.x.1（恶意 IP 地址） 192.x.x.2（灰产 IP 地址） |
