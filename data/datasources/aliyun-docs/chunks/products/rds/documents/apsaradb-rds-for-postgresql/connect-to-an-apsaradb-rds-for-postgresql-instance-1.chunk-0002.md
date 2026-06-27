### 数据管理DMS连接
数据管理DMS是一种集数据管理、结构管理、用户授权、安全审计、数据趋势、数据追踪、BI图表、性能与优化和服务器管理于一体的数据管理服务。关于数据库管理DMS的更多信息，请参见[什么是数据管理](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582)[DMS](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582)。
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在基本信息页面单击登录数据库。在实例的基本信息页面上方，单击登录数据库。
在DMS的登录实例页面，选择访问方式和管控模式。

| 配置项 | 说明 |
| --- | --- |
| 访问方式 | 通过 DMS 访问 RDS 实例的方式。本文以 账号+密码登录 为例。 账号+密码登录 ：使用 拥有目标数据库的权限 的数据库账号和密码登录。 KMS 凭据登录 ：DMS 会自动为实例开启安全托管，但您需要手动选择在 KMS 创建的 RDS 凭据以登录数据库。 说明 KMS 凭据登录 的访问方式登录 RDS 时，DMS 会自动为实例免费开启 [安全托管](https://help.aliyun.com/zh/dms/product-overview/security-hosting) 。 您也可以单击 一键开启安全托管 ，输入账号和密码，为实例免费开启 [安全托管](https://help.aliyun.com/zh/dms/product-overview/security-hosting) ，实现安全可控的 免密登录。 |
| 管控模式 | 数据管理 DMS 提供三种实例级别的 [管控模式](https://help.aliyun.com/zh/dms/product-overview/control-modes) ，您可以根据实际业务场景进行设置。 自由操作 稳定变更 安全协同 |
