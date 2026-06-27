### 请求参数
客户端的请求http://aliyundoc.com/a/b/image.jpg?delete_par=1&modify_par=1将按规则添加add_par=1，删除delete_par，将modify_par的值修改为2，最终转化为http://aliyundoc.com/a/b/image.jpg?modify_par=2&add_par=1。
重要
请求参数中，如对同一个变量同时进行了多个操作，则各种操作的生效优先级：新增>删除>保留>修改。
删除操作仅支持输入单个参数名，如需删除多个参数，可单击添加参数操作增补多条删除操作。
