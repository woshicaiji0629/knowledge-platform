## 示例
请求示例
使用默认账号获取logstore-a的索引配置。
aliyunlog log get_index_config --project_name="aliyun-test-project" --logstore_name="logstore-a"
如果您需要将查询到的索引配置保存到指定文件，可参考如下示例：
aliyunlog log get_index_config --project_name="aliyun-test-project" --logstore_name="logstore-a" >>export_index_config.json
返回示例
{ "index_mode": "v2", "keys": { "key1": { "caseSensitive": false, "doc_value": true, "token": [ ",", " ", "'", "\"", ";", "=", "(", ")", "[", "]", "{", "}", "?", "@", "&", "<", ">", "/", ":", "\n", "\t" ], "type": "text" }, "key2": { "caseSensitive": false, "doc_value": true, "token": [ ",", " ", "'", "\"", ";", "=", "(", ")", "[", "]", "{", "}", "?", "@", "&", "<", ">", "/", ":", "\n", "\t" ], "type": "text" }, "key3": { "caseSensitive": false, "doc_value": true, "token": [ ",", " ", "'", "\"", ";", "=", "(", ")", "[", "]", "{", "}", "?", "@", "&", "<", ">", "/", ":", "\n", "\t" ], "type": "text" }, "key4": { "caseSensitive": false, "doc_value": true, "token": [ ",", " ", "'", "\"", ";", "=", "(", ")", "[", "]", "{", "}", "?", "@", "&", "<", ">", "/", ":", "\n", "\t" ], "type": "text" } }, "lastModifyTime": 0, "line": { "caseSensitive": false, "chn": false, "token": [ ",", " ", "'", "\"", ";",
