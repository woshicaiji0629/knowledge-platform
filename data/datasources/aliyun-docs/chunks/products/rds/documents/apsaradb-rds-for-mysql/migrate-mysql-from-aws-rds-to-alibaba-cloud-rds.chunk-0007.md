条添加入站规则。
若您有其他疑问，请查看Amazon官方文档或联系Amazon的技术支持人员。
登录Amazon RDS MySQL数据库，设置Binlog日志保存时间。如果不需要增量数据迁移，可跳过本步骤。
call mysql.rds_set_configuration('binlog retention hours', 24);
说明
上述命令将binlog日志的保存设置为24小时，最大可设置为168个小时，即7天。
Amazon RDS MySQL的Binlog日志需处于开启状态，且binlog_format需设置为row；当MySQL为5.6及以上版本时，binlog_row_image需设置为full。开启方法，请查看Amazon官方文档或联系Amazon的技术支持人员。
