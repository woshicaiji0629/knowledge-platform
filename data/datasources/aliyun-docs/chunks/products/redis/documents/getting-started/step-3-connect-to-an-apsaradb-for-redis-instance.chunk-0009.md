## 常见报错

| 报错信息 | 原因及解决方法 |
| --- | --- |
| (error) ERR illegal address | 未设置正确的白名单，可依次排查如下事项： 是否已将客户端的 IP 地址添加至实例的白名单中，详情请参见 [设置白名单](step-2-configure-whitelists.md) 。 是否选择正确的实例连接地址，例如通过公网连接实例，需连接实例的公网连接地址，若此时选择实例的专有网络连接地址会导致连接失败。 使用 ECS 通过专有网络连接时，检查 ECS 是否与实例为同一 VPC，若两者不是同一 VPC，则可使用公网的方式进行访问。 排查后，可通过 ping 实例地址 进行测试，例如 ping r-bp1zxszhcgatnx****.redis.rds.aliyuncs.com ，若返回正常，则表示客户端与实例可正常连接。 |
| (error) ERR client ip is not in whitelist |  |
| Could not connect to Redis |  |
| (error) ERR invalid password (error) WRONGPASS invalid username-password pair | 密码错误，请使用正确的密码和密码格式。根据选取账号的不同，密码格式有一定区别。 使用默认账号：直接填写密码即可。例如实例默认账号为 r-bp1zxszhcgatnx**** ，自定义密码为 Password21 ，密码验证命令为 AUTH Password21 。 使用新创建的账号：密码格式为 user:password 。例如自定义账号为 testaccount ，密码为 Rp829dlwa ，密码验证命令为 AUTH testaccount:Rp829dlwa 。 说明 如果通过第三方数据库管理工具（例如 RDM 等）连接实例，请在密码框中输入 user:password 进行连接，请不要在 用户名 框中输入任何信息，否则会导致连接失败。 如果忘记密码，您可以重置密码。具体操作，请参见 [修改或重置密码](../user-guide/change-or-reset-the-password.md) 。 |

该文章对您有帮助吗？
反馈
