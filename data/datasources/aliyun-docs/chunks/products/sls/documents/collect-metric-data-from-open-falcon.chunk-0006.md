## 步骤二：修改Open-Falcon配置
登录Open-Falcon所在服务器。
添加transfer配置。
打开配置文件。
配置文件默认为cfg.json。
将如下脚本添加到配置文件中。
address中配置的IP地址和端口号要与您在步骤[7](collect-metric-data-from-open-falcon.md)中配置的Address中的IP地址和端口号一致，详情参数说明请参见[Transfer](https://book.open-falcon.org/zh/install_from_src/transfer.html)。
"influxdb": { "enabled": true, "batch": 200, "retry": 3, "maxConns": 32, "precision": "s", "address": "http://127.0.0.1:8478", "timeout": 5000 }
