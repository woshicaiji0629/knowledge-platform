## 注意事项
您可以修改或清空默认的IP白名单，但是不能删除。
单个实例最多支持50个IP白名单分组。
单个实例最多添加1000个IP或IP段。建议将零散的IP合并为IP段，例如10.10.10.0/24（[CIDR](../../../vpc/documents/faq-about-cidr-blocks.md)[模式](../../../vpc/documents/faq-about-cidr-blocks.md)）。
ali_dms_group（[DMS](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582)产品IP地址白名单分组）、hdm_security_ips（[DAS](https://help.aliyun.com/zh/das/product-overview/what-is-das#concept-2419191)产品IP地址白名单分组）等分组为系统自动生成，请勿修改或删除，避免影响相关产品的使用。
重要
请勿在这些分组里增加自己的业务IP，避免相关产品更新时覆盖您的业务IP，影响业务正常运行。
为防止误修改或删除白名单分组，2020年12月之后的新建实例，hdm_security_ips白名单分组对用户不可见。
