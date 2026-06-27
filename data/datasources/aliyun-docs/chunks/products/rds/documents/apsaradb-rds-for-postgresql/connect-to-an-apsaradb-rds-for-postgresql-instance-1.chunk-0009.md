es 是 RDS PostgreSQL 实例默认的系统数据库，请勿在该数据库中进行任何操作，建议配置 RDS 实例下已创建的其他数据库。 如何创建和查看数据库，请参见 [创建数据库](create-a-database-on-an-apsaradb-rds-for-postgresql-instance.md) 。 |

设置用户名和密码后，单击连接。在弹出的身份验证对话框中，输入 RDS PostgreSQL 实例的用户名和密码，然后单击连接。
说明
创建RDS实例的账号请参见[创建账号和数据库](create-a-database-and-an-account-on-an-apsaradb-rds-for-postgresql-instance.md)。
在加密支持对话框中单击确定。在弹出的加密支持对话框中，单击确定以使用不加密连接访问数据源。
连接成功后，即可在导航器窗口中查看数据库中的表信息，您可以根据业务需求，选中目标表后，选择加载或转换数据操作。在导航器对话框左侧导航树中，展开已连接的 RDS PostgreSQL 实例，勾选需要导入的目标表（例如public.tb_test2），右侧将自动预览该表的数据。确认无误后，单击加载直接导入数据，或单击转换数据在导入前进行数据编辑。
Smartbi
RDS PostgreSQL支持接入Smartbi，在Smartbi中对数据进行分析处理，满足您在企业级报表、数据可视化分析、自助探索分析、数据挖掘建模、AI 智能分析等大数据分析需求。下文以Smartbi V10.5版本为例，介绍如何连接RDS PostgreSQL实例。
根据Smartbi官方安装指导，完成申请License、Smartbi客户端的下载、安装以及启动Smartbi服务。
在开始菜单，单击访问Smartbi。在 Windows 开始菜单中找到Smartbi文件夹，单击访问Smartbi打开 Smartbi 登录页面。
输入账号和密码后，单击登录，进入Smartbi。
说明
管理员默认登录账号为admin，密码为manager。
如果是首次登录，则需要修改管理员密码。
在左侧单击
在新建关系数据库对话框中配置相关参数，然后单击测试连接(T)。驱动程序存放目录选择产品内置，链接方式选择用户名密码，验证类型选择静态，填写完成后单击测试连接(T)验证连接是否正常。
