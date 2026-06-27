### 控制台操作
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
单击日志存储，在日志库中，将鼠标悬浮在目标LogStore上，选择>修改。
在Logstore属性页面中，单击修改。
选择待分裂的Shard，单击分裂。
重要
分裂Shard时，需要选择一个处于readwrite状态的Shard。
在Shard管理页面的列表中，找到目标 readwrite 状态的 Shard，单击其操作列中的分裂。
选择分裂数量，单击确定。
单击保存。
