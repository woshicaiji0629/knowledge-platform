## 6. 常见问题 (FAQ)
Q: 我如何在本地对话框中显示消息历史？
A:您可以在后端通过Messages.list(thread_id=xxx)获取所有消息，然后根据角色（user/assistant）渲染到前端。也可将它们存到自己数据库中进行分页展示。
Q: 如何对用户消息进行拦截或过滤？
A:在调用Messages.create前，对content进行文本检测或清洗；也可以在metadata中标记敏感度。
Q: 有办法只删除单条 Message 吗？
A:目前暂不支持单条删除，需要通过Threads.delete(thread_id)进行整会话级联删除。
Q: 线程（Thread）什么时候应该结束？
A:根据业务需求决定。可以在用户退出或会话超时后调用Threads.delete，或者保留一段时间以便用户再次进来继续对话。
Q:Run等待超时时有什么应对方式？
A:可以使用Runs.wait(run_id, thread_id, timeout_seconds=...)。若超时，SDK 会抛TimeoutException，可在捕获后进行重试或提示用户“请求超时”。
Q: 如何对多步骤推理场景做更详细的监控？
A:您可以查看Steps.list(run_id, thread_id)来获取每一个步骤执行信息，也可以在本地做日志记录或触发警报（如对超时步骤发送告警）。
