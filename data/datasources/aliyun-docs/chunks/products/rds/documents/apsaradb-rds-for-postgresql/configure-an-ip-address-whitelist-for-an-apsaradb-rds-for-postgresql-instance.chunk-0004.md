## 注意事项
单个实例最多支持50个IP白名单分组。
设置白名单不会影响RDS实例的正常运行。
白名单分组仅用于IP地址管理，不会影响实际访问权限。所有分组中的IP地址对RDS实例的访问权限是一致的。
默认的IP白名单分组（default ）不能删除，只能清空。
请勿修改或删除系统自动生成的分组，避免影响相关产品的使用。例如ali_dms_group（[DMS](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582)产品IP地址白名单分组）、hdm_security_ips（[DAS](https://help.aliyun.com/zh/das/product-overview/what-is-das#concept-2419191)产品IP地址白名单分组）。
重要
为防止误修改或删除白名单分组，2020年12月之后的新建实例，hdm_security_ips白名单分组对用户不可见。
默认的IP白名单仅包含127.0.0.1，表示除了本地IP 127.0.0.1之外，任何其他IP均无法访问该RDS实例。
