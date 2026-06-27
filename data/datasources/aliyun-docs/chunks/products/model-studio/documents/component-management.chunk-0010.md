### 3.2 删除机制
删除Assistant通过Assistants.delete(assistant_id)：会删除这个 Assistant 及其关联的资源。需要格外谨慎。
删除Thread通过Threads.delete(thread_id)：会级联删除该会话下所有Message、Run、Step记录。
单条消息 / 单次 Run / 单个 Step目前 DashScope 默认不支持单独删除，只能通过上层对象删除整条会话或整条 Assistant 的方式进行级联清理。
