## 迁移前准备工作
登录Amazon RDS控制台。
在左侧导航栏，单击数据库，然后单击目标数据库实例的数据库标识符。
在安全组规则区域框，单击入站规则对应的安全组名称，进入安全组页面，单击目标安全组ID。
在入站规则页签，单击编辑入站规则。
在编辑入站规则页面，单击添加规则，将对应区域的DTS服务器地址添加至入站规则后，单击保存规则。DTS服务的IP地址段详情，请参见[添加](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)[DTS](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)[服务器](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)[IP](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)[地址白名单](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)。
说明
您只需添加目标数据库所在区域对应的DTS IP地址段。例如，源数据库地区为新加坡，目标数据库地区为杭州，您只需要添加杭州地区的DTS IP地址段。
在加入IP地址段时，您可以一次性添加所需的IP地址，无需逐条添加入站规则。
若您有其他疑问，请查看Amazon官方文档或联系Amazon的技术支持人员。
登录Amazon RDS MySQL数据库，设置Binlog日志保存时间。如果不需要增量数据迁移，可跳过本步骤。
call mysql.rds_set_configuration('binlog retention hour
