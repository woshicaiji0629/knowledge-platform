### 步骤四：在TR之间创建跨地域连接
转发路由器连接VPC后，需要在不同地域的转发路由器之间创建跨地域连接，才能实现VPC1和VPC2的跨地域私网互通。
登录[云企业网管理控制台](https://cen.console.aliyun.com/)。
在云企业网实例页面，单击已创建的云企业网实例ID。
在基本信息>转发路由器页签，找到西南1（成都）地域的转发路由器实例，在操作列单击创建网络实例连接。
在连接网络实例页面，配置以下信息，然后单击确定创建。
此处仅列出和本文强相关的配置项，其余配置项可保持默认值。更多信息，请参见[使用企业版转发路由器创建跨地域连接](../../../../cen/documents/user-guide/manage-inter-region-connections.md)。

| 配置项 | 说明 |
| --- | --- |
| 实例类型 | 选择 跨地域连接 。 |
| 地域 | 选择要互通的地域。本文选择 西南 1（成都） 。 |
| 对端地域 | 选择要互通的对端地域。本文选择 华东 1（杭州） 。 |
| 带宽分配方式 | 选择 按流量付费 。 针对转发路由器间的跨地域流量，您可使用云数据传输 CDT 降低流量成本，如您未开通该服务建议您查看 [升级至](https://help.aliyun.com/zh/cdt/user-guide/upgrade-to-cdt-billing) [CDT](https://help.aliyun.com/zh/cdt/user-guide/upgrade-to-cdt-billing) [计费](https://help.aliyun.com/zh/cdt/user-guide/upgrade-to-cdt-billing) 开通，仅开通 CDT 不收取任何费用。您也可以根据实际业务情况选择使用带宽包。 |
