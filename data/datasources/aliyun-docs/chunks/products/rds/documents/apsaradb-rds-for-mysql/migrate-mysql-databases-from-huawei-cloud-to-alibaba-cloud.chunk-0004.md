ble-ssl-encryption.md) [SSL](configure-a-cloud-certificate-to-enable-ssl-encryption.md) [链路加密](configure-a-cloud-certificate-to-enable-ssl-encryption.md) 。 |  |

填写完毕后单击测试连接以进行下一步，在DTS服务器访问授权确定窗口中，再次单击测试连接以进行下一步。
在配置任务对象及高级配置步骤，选择迁移类型。
说明
为保证迁移数据的一致性，建议选择结构迁移+全量数据迁移+增量数据迁移。
勾在源库对象框中将想要迁移的数据库选中，单击，移动到已选择对象框。
单击下一步高级配置，保持默认配置即可。
当源库和目标库账号满足要求时，可以将源库的账号（包含密码和权限）迁移至目标库。迁移数据库账号的注意事项及数据库账号所需权限等更多信息请参见[数据库账号所需权限](https://help.aliyun.com/zh/dts/user-guide/permissions-for-database-accounts-to-migrate-account-information#section-account-permissions)。
单击下一步保存任务并预检查，等待预检查结束。
说明
如果检查失败，可以根据错误项的提示进行修复，然后重新启动任务。
单击下一步购买，在购买页，勾选《数据传输（按量付费）服务条款》并单击购买并启动。
如果选择了增量迁移，那么进入增量迁移阶段后，源库的更新写入都会被DTS同步到目标RDS MySQL实例。迁移任务不会自动结束。如果您只是为了迁移，那么建议在增量迁移无延迟的状态时，源库停写几分钟，等待增量迁移再次进入无延迟状态后，停止掉迁移任务，直接将业务切换到目标RDS MySQL实例上即可。
说明
结构迁移和全量迁移任务暂不收费，增量迁移根据链路规格按小时收费。
等待迁移任务完成即可。
该文章对您有帮助吗？
反馈
