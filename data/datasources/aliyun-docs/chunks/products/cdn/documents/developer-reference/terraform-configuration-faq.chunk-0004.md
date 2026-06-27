## 选择cas类型时需要哪些必填参数？
当cert_type = "cas"时，必须提供以下参数：
cert_id：阿里云证书中心的证书ID（可在证书详情页获取）。
cert_region：阿里云数字证书管理服务所在地域，根据账号类型选择（默认为cn-hangzhou）：
中国站账号：cn-hangzhou
国际站账号：ap-southeast-1
certificate_config { server_certificate_status = "on" cert_type = "cas" cert_id = "1111111" cert_region = "cn-hangzhou" }
