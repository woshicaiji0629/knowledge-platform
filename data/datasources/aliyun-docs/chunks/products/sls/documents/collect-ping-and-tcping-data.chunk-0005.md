：执行 ping 命令的服务器的 IP 地址。即由 src 字段决定在机器组的哪台机器中执行 ping 命令。 method ：执行请求的 http method，默认 get。 expect_response_contains ： 预期结果包含内容。 expect_code ：预期状态码。 target ：目的地址，支持 https。 name ：名称，默认为{src}->{target}。 labels ：标签，支持增加指标标签。 "http": [ { "src": "192.XX.XX.103", "expect_code": 200, "target": "www.aliyun.com" } ] |
| interval_seconds | int | 是 | 执行 ping 命令的时间间隔，单位：秒。 默认值：60。 取值范围：[10, 86400) |
| type | string | 是 | 数据源类型，固定为 metric_input_netping。 |
