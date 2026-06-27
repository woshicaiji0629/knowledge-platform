## 示例
请求示例
使用默认账号删除logstore-a的索引配置。
aliyunlog log delete_index --project_name="aliyun-test-project" --logstore_name="logstore-a"
命令执行成功后，无响应消息。查询索引是否删除，命令示例如下：
aliyunlog log get_index_config --project_name="aliyun-test-project" --logstore_name="logstore-a"
返回结果如下：
{"errorCode": "IndexConfigNotExist", "errorMessage": "index config doesn't exist", "requestId": "667BA89CA3741E0D5******"}
