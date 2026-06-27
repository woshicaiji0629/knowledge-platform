## 关闭离线日志转存
如果您之前开通了离线日志转存服务，请在删除域名之前，先关闭离线日志转存功能，并且清空已经转存到OSS产品上日志。您可以[【CDN](../user-guide/use-function-compute-to-deliver-logs.md)[控制台】通过函数计算转存离线日志](../user-guide/use-function-compute-to-deliver-logs.md)来了解更多原理离线日志的信息。
操作步骤
在CDN控制台取消关联域名。
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，选择日志管理>离线日志。
单击通过函数计算转存离线日志页签。
单击关联域名，在弹窗右侧勾选需要取消的域名，单击。
单击确认，取消关联域名。
可选：在函数计算控制台删除函数和服务。
说明
开通离线日志功能时，在函数计算中指定或者创建了函数和服务为离线日志功能服务，如果您不再需要可同步删除该函数和服务，可选择删除函数和服务，避免残留过多配置。
删除函数：请参考[删除函数](https://help.aliyun.com/zh/functioncompute/fc-2-0/user-guide/manage-functions#multiTask3514)。
删除服务：请参考[删除服务](https://help.aliyun.com/zh/functioncompute/fc-2-0/user-guide/manage-services#multiTask427)。
在OSS控制台删除对应的存储Bucket数据。
说明
日志只要存储在OSS的存储Bucket就会收取少量费用，建议您主动删除存储Bucket数据。
删除对应的存储Bucket数据：请参考[删除存储空间](../../../oss/documents/basic-settings-delete-buckets.md)。
