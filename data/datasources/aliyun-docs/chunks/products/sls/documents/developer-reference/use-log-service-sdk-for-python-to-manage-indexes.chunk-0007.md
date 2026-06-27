':', '\n', '\t', '\r'], 'caseSensitive': False, 'alias': '', 'doc_value': True, 'chn': False}, 'status': {'type': 'long', 'alias': '', 'doc_value': True}}, 'log_reduce': False, 'max_text_len': 2048} print("ready to create index") index_config = IndexConfig() index_config.from_json(logstore_index) client.create_index(project_name, logstore_name, index_config) print("create index success ")
预期结果如下：
ready to create index create index success
