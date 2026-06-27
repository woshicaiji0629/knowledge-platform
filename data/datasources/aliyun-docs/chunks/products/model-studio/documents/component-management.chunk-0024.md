注意：Messages.list 返回的信息是按照创建时间逆序排列的）。 thread_messages = Messages.list(thread_id=thread_id) if thread_messages.data: last_msg = thread_messages.data[0] return last_msg.content[0].text.value if last_msg.content else "No reply." return "No reply." def end_session(thread_id: str): """删除thread，级联删除所有消息和run""" Threads.delete(thread_id) # 例子演示 assistant_id = init_assistant() thread_id = start_session(assistant_id, "你好，请告诉我今天的天气如何？") reply = get_assistant_reply(assistant_id, thread_id) print("Assistant reply:", reply) end_session(thread_id)
在此示例中：
init_assistant()：先创建一个全局的 Assistant（指定模型、默认指令等）。
start_session()：创建一个新的对话Thread并添加用户消息。
get_assistant_reply()：创建一个Run来调用模型生成回复。由于是异步执行，需要Runs.wait()等待完成；完成后，新的Message就会插入到该线程里。拉取所有消息并返回最后一条（一般就是 Assistant 的回复）。
end_session()：在完成会话后删除Thread，从服务器端移除所有资源。
