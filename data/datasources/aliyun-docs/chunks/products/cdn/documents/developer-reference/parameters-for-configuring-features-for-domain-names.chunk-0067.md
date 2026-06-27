| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| auth_m3u8 | String | 否 | 开启 m3u8 内容改写，对 m3u8 里面的 ts 补齐对应的鉴权，可以避免 ts 的访问鉴权失败，取值 on（默认值）和 off。 | on |
| auth_type | String | 是 | 鉴权类型。取值： no_auth：无鉴权。 type_a：鉴权方式 A。 type_b：鉴权方式 B。 type_c：鉴权方式 C。 type_d：鉴权方式 D。 type_e：鉴权方式 E。 type_f：鉴权方式 F。 | type_a |
| auth_key1 | String | 是 | 鉴权 key1（16~128 个字符支持大写字母、小写字母和数字）。 | 1234567890123456789 |
| auth_key2 | String | 否 | 鉴权 key2（16~128 个字符支持大写字母、小写字母和数字）。 | 1234567890123456789 |
| ali_auth_delta | Integer | 否 | 鉴权 URL 有效时长，默认 1800，单位：秒。 | 1800 |
| req_auth_ip_white | String | 否 | 白名单例外 IP 列表，白名单中的 IP 不进行鉴权校验。 支持输入多个 IP 地址，多个 IP 地址之间使用英文逗号分隔。 | 192.168.0.1 |
| req_auth_ip_acl_xfwd | String | 否 | 客户端例外 IP 的提取方式，取值支持： on：该模式为默认模式。该模式校验的是用户请求中 x-forwarded-for 请求头携带的左边第一个 IP，这个 IP 对应客户端真实 IP。 off：该模式校验的是客户端与 CDN 节点之间建立建连接用的 IP。 all：同时校验以下两个 IP 地址信息： 用户请求中 x-forwarded-for 请求头携带的左边第一个 IP，即客户端真实 IP。 客户端与 CDN 节点之间建立建连接用的 IP。 | all |
| sign_param | String | 否 | 签名参数名称。仅在鉴权类型设置为 F 方式的时候有效。 | sign |
| time_param | String | 否 | 时间戳参数名称。仅在鉴权类型设置为 F 方式的时候有效。 | time |
| time_format | String | 否 | 时间戳格式。仅在鉴权类型设置为 F 方式的时候有效。 dec：十进制 hex：十六进制 | hec |
| path_encoding | String | 否 | URL 编码开关，支持 on/of
