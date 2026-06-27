### 报错 IndexConfigNotExist
该错误表示目标 LogStore 没有索引配置或索引配置为空。
解决方法：在 SLS 控制台为目标 LogStore 创建索引。创建完成后等待片刻（新数据需要短暂时间才能被索引），然后重新执行查询。
