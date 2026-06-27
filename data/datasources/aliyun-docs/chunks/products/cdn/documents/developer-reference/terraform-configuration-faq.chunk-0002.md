## cert_type支持的证书类型有哪些？分别代表什么？
证书类型通过cert_type参数指定，支持两种类型：
upload：手动上传证书（需提供公钥和私钥，分别填写server_certificate和private_key）。
cas：使用阿里云数字证书管理服务的SSL证书（需填写cert_id证书ID和cert_region证书地域）。
说明
free类型的免费证书已不再支持。
