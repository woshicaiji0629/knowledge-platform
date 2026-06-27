, '\t', '\r'], 'caseSensitive': True, 'alias': '', 'doc_value': True, 'chn': False}, 'status': {'type': 'long', 'alias': '', 'doc_value': True}}, 'log_reduce': False, 'max_text_len': 2048} print("ready to update index") index_config = IndexConfig() index_config.from_json(logstore_index) client.update_index(project_name, logstore_name, index_config) print("update index success ")
预期结果如下：
ready to update index update index success
