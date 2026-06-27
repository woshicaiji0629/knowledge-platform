s-for-mysql-instance.md)[IP](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)[白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)后才能正常访问实例。设置IP白名单后才能进行后续获取内网或外网连接地址的操作。
2. 选择合适的访问类型
访问类型分为内网访问和外网访问，如果您符合内网访问条件，您需要使用实例的内网连接地址进行远程连接；如果您不符合内网访问条件或使用本地设备访问RDS MySQL实例，则需要使用实例的外网连接地址进行远程连接。内网访问条件与获取内外网连接地址的方法如下：
重要
如您需要通过内网访问实例，则需满足以下条件：
使用阿里云服务器访问，且服务器与RDS实例同一地域、同一VPC。
如果服务器与实例的网络类型均为专有网络，则专有网络ID也需要相同。
