n-hangzhou-internal.aliyuncs.com。
Please enter Endpoint (optional, use public endpoint by default) [None]: https://oss-cn-hangzhou-internal.aliyuncs.com
参数说明如下：

| 参数 | 是否必填 | 说明 |
| --- | --- | --- |
| accessKeyID | 是 | 账号的 AccessKey，AccessKey 的获取方式参见 [创建](../../../ram/documents/create-an-accesskey-pair-1.md) [AccessKey](../../../ram/documents/create-an-accesskey-pair-1.md) 。 使用 ROS 脚本快速创建有 OSS 管理权限的 RAM 用户 AccessKey 在资源编排 ROS 控制台的 [创建资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks/create?templateUrl=https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241114/itgrlo/createossadmin.yaml&step=1&hideTemplateSelector=false) 页面的 安全确认 下，勾选确认，然后单击 创建 。 创建完成后，在 输出 中，复制创建的 AccessKey。 |
| accessKeySecret | 是 |  |
| Region | 是 | Bucket 所在的地域 ID，本文以 杭州 地域为例，设置为 cn-hangzhou ，其他地域的 ID 参见 [地域和](../user-guide/regions-and-endpoints.md) [Endpoint](../user-guide/regions-and-endpoints.md) 。 |
| endpoint | 否 | Bucket 所在地域的 Endpoint。若未手动设置 Endpoint， Region 将自动生成对应的外网 endpoint，内网需显式指定。例如，本示例使用 华东 1（杭州） 外网 Endpoint，设置为 https://oss-cn-hangzhou.aliyuncs.com 。 如果希望通过与 OSS 同地域的其他阿里云产品访问 OSS，请使用内网 Endpoint，设置为 https://oss-cn-hangzhou-internal.aliyuncs.com 。 关于各地域 Endpoint 的更多信息，请参见 [地域和](../user-guide/regions-and-endpoints.md) [Endpoint](../user-guide/regions-and-endpoints.md) 。 |
