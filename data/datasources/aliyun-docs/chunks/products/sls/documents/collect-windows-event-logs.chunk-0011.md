_time: 0 provider_guid: {AEA1B4FA-97D1-45F2-A64C-4D69FFFD92C9} record_number: 6908 related_activity_id: session_id: 0 source_name: Microsoft-Windows-GroupPolicy

| 字段名 | 说明 |
| --- | --- |
| activity_id | 当前事件所属活动的全局事务 ID，同一个活动的事件具有相同的全局事务 ID。 |
| computer_name | 产生当前事件的节点名。 |
| event_data | 和当前事件相关的数据。 |
| event_id | 当前事件的 ID。 |
| kernel_time | 当前事件消耗的内核时间，一般为 0 。 |
| keywords | 当前事件关联的关键字，用于事件分类。 |
| level | 当前事件的等级。 |
| log_name | 当前事件的通道名，即 Logtail 采集配置中 Name 参数。 |
| message | 当前事件关联的消息。 |
| message_error | 在解析当前事件关联消息时发生的错误信息。 |
| opcode | 当前事件关联的操作码。 |
| process_id | 当前事件的进程 ID。 |
| processor_id | 当前事件对应的处理器 ID，一般为 0 。 |
| processor_time | 当前事件消耗的处理器时间，一般为 0 。 |
| provider_guid | 当前事件来源的全局事务 ID。 |
| record_number | 当前事件关联的记录编号。事件的记录编号会随着每条事件的写入递增，当超过 2 32 （Event Logging）或 2 64 （Windows Event Log）后会重新从 0 开始。 |
| related_activity_id | 当前事件所属活动关联的其他活动的全局事务 ID。 |
| session_id | 当前事件的会话 ID，一般为 0 。 |
| source_name | 当前事件的来源，即 Logtail 采集配置中 Provider 参数。 |
| task | 当前事件关联的任务。 |
| thread_id | 当前事件的线程 ID。 |
| type | 获取当前事件使用的 API。 |
| user_data | 当前事件关联的用户数据。 |
| user_domain | 当前事件关联的用户域。 |
| user_identifier | 当前事件关联的用户 Windows 安全标识。 |
| user_name | 当前事件关联的用户名。 |
| user_time | 当前事件消耗的用户态时间，一般为 0 。 |
| user_type | 当前事件关联的用户的类型。 |
| version | 当前事件的版本号。 |
| xml | 当前事件最原始的信息，XML 格式。 |
