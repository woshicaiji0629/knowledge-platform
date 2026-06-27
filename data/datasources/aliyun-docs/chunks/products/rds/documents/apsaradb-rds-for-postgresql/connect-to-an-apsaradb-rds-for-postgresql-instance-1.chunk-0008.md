### 第三方报表工具连接
Microsoft Power BI
RDS PostgreSQL支持接入[Power BI](https://powerbi.microsoft.com/)，在Power BI中对数据进行获取、清洗、建模和可视化展示等操作，实现数据分析。下文以Power BI 2.112.1161.0 64-bit版本为例，介绍如何连接RDS PostgreSQL实例。
下载并安装Power BI Desktop客户端。下载方法请参见[获取 Power BI Desktop](https://learn.microsoft.com/power-bi/fundamentals/desktop-get-the-desktop)。
启动Power BI Desktop客户端。
在顶部菜单栏选择主页页签，然后单击获取数据>更多...。在主页选项卡中，单击获取数据按钮，在下拉菜单底部单击更多...。
在获取数据对话框中选择数据库>PostgreSQL数据库，然后单击连接。在左侧分类列表中选择数据库，然后在右侧列表中选择PostgreSQL 数据库，单击连接。
在PostgreSQL数据库对话框中，分别设置服务器和数据库后，单击确定。在数据连接模式中选择导入，然后单击确定。

| 参数 | 说明 |
| --- | --- |
| 服务器 | RDS PostgreSQL 实例的连接地址和对应的端口。 格式： 连接地址:端口 若通过内网连接，需输入 RDS 实例的内网地址和内网端口。 若使用外网连接，需输入 RDS 实例的外网地址和外网端口。 您可以在 RDS PostgreSQL 实例的数据库连接页面查看。 更多信息，请参见 [查看或修改连接地址和端口](view-and-change-the-endpoints-and-port-numbers-of-an-apsaradb-rds-for-postgresql-instance.md) 。 |
| 数据库 | postgres 是 RDS PostgreSQL 实例默认的系统数据库，请勿在该数据库中进行任何操作，建议配置 RDS 实例下已创建的其他数据库。 如何创建和查看数据库，请参见 [创建数据库](create-a-database-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |
