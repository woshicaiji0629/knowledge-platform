## 相关操作
如果您需要将阿里云账号B下的历史数据迁移到当前的LogStore中，可以在原LogStore中创建数据加工任务，将数据复制到当前LogStore中。具体操作，请参见[复制](replicate-data-from-a-logstore.md)[LogStore](replicate-data-from-a-logstore.md)[数据](replicate-data-from-a-logstore.md)。
重要
跨账号加工数据时，需使用自定义角色方式进行授权，此处以自定义角色为例。
第一个角色ARN用于授予数据加工任务使用该角色来读取源LogStore中的数据。角色权限配置说明请参见[授权](access-data-by-using-a-custom-role.md)[RAM](access-data-by-using-a-custom-role.md)[角色只读访问源](access-data-by-using-a-custom-role.md)[LogStore](access-data-by-using-a-custom-role.md)。
第二个角色ARN用于授予数据加工任务使用该角色将数据加工结果写入目标LogStore。角色权限配置说明请参见[授权](access-data-by-using-a-custom-role.md)[RAM](access-data-by-using-a-custom-role.md)[角色写数据到目标](access-data-by-using-a-custom-role.md)[LogStore（跨账号）](access-data-by-using-a-custom-role.md)。
该文章对您有帮助吗？
反馈
