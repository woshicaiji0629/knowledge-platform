## 常见问题
Q：开启免密访问后，为什么仍会返回WRONGPASS invalid username-password pair报错？
A：Redis开源版6.0实例开启免密访问后，若输入错误的账号密码，系统会返回以上报错。请输入正确的账号密码或不输入账号密码。
说明
密码格式：
默认账号（即以实例ID命名的账号）：直接填写密码。
新创建的账号：密码格式为<user>:<password>，例如testaccount:Rp829dlwa。
Q：开启免密访问后，为什么使用同一专有网络的客户端连接Tair实例，仍报错(error) ERR illegal address？
A：该客户端的IP地址未添加至实例的白名单。您可以将客户端的IP地址添加至实例的白名单中后重试。
该文章对您有帮助吗？
反馈
