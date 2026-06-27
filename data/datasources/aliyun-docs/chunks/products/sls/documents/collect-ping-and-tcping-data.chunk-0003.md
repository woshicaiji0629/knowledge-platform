，设置配置名称和插件配置，然后单击下一步。
重要
inputs为数据源配置，必选项。一个inputs中只允许配置一个类型的数据源。
{{ "inputs": [ { "detail": { "tcp": [ { "port": 80, "src": "192.XX.XX.103", "count": 3, "target": "www.aliyun.com" } ], "interval_seconds": 60, "icmp": [ { "src": "192.XX.XX.103", "count": 3, "target": "www.aliyun.com" } ], "http": [ { "src": "192.XX.XX.103", "expect_code": 200, "target": "www.aliyun.com" } ] }, "type": "metric_input_netping" } ] }
