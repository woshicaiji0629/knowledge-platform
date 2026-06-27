### 使用STS临时访问凭证
如果应用程序需要临时访问OSS，可以使用通过STS服务获取的临时身份凭证（Access Key ID、Access Key Secret和Security Token）初始化凭证提供者。需要注意的是，该方式需要手动维护一个STS Token，存在安全性风险和维护复杂度增加的风险。此外，如果需要多次临时访问OSS，需要手动刷新STS Token。
