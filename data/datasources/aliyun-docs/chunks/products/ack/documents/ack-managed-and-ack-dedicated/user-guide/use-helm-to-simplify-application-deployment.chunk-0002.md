## 管理Helm应用
在控制台Helm应用列表页面，可对目标应用执行更新、删除等管理操作。

| 操作 | 说明 |
| --- | --- |
| 查看应用 | 单击目标应用名称或 详情 ，查看该应用的资源、YAML 文件、历史版本等信息。 |
| 更新应用 | 单击 更新 ，在 更新发布 面板中修改相关参数，然后单击 确定 。 重要 更新将直接影响关联应用的运行状态，导致服务重启或功能异常。建议在变更前充分评估影响范围，并在业务低峰期执行操作。 |
| 删除应用 | 单击 删除 ，在 删除应用 对话框中，选中 清除发布记录 ，然后单击 确定 ，删除应用以及包含的 Service、Deployment 等资源。 本示例删除 Dify 应用时，不会自动同步删除 NAS 资源，需手动 [删除](https://help.aliyun.com/zh/nas/user-guide/delete-a-file-system) [NAS](https://help.aliyun.com/zh/nas/user-guide/delete-a-file-system) [文件系统](https://help.aliyun.com/zh/nas/user-guide/delete-a-file-system) 。 重要 如果删除时未选中 清除发布记录 ，此时该应用会保留在发布列表中，后续部署同名应用时，会因命名冲突而失败。 |
