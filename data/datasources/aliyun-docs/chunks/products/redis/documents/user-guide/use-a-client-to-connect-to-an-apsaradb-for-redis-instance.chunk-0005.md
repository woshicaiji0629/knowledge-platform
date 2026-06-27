## 如何获取连接信息
在使用客户端程序连接Tair（以及Redis开源版）实例时，通常您需要获取以下信息并设置在代码中：

| 需获取的信息 | 获取方式 |
| --- | --- |
| 实例的连接地址 | 访问 [实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou) ，在上方选择地域，然后单击目标实例 ID。 在 连接信息 区域，可查看到各连接类型的地址和端口号。 说明 实例支持多种连接地址，推荐使用专有网络连接，可获得更高的安全性和更低的网络延迟。更多信息，请参见 [查看连接地址](view-endpoints.md) 。 |
| 端口号 | 端口号默认为 6379，您也可以自定义端口号。具体操作，请参见 [修改连接地址或端口](change-the-endpoint-or-port-number-of-an-instance.md) 。 |
| 实例的账号（部分客户端程序无需设置） | 实例默认会创建一个以实例 ID 命名的账号（例如 r-bp10noxlhcoim2****），您也可以创建一个新的账号并赋予权限。更多信息，请参见 [创建与管理账号](create-and-manage-database-accounts.md) 。 |
| 账号的密码 | 根据选取账号的不同，密码的填写格式有一定区别： 默认账号（以实例 ID 命名的账号）：直接填写密码即可。 新创建的账号：密码格式为 <user>:<password> 。例如自定义账号为 testaccount ，密码为 Rp829dlwa ，密码需填写为 testaccount:Rp829dlwa 。 说明 如果通过第三方数据库管理工具（例如 RDM 等）连接实例，请在密码框中输入 user:password 进行连接。 如果忘记密码，您可以重置密码。具体操作，请参见 [修改或重置密码](change-or-reset-the-password.md) 。 |
