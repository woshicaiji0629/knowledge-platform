## 合并Shard
当数据读写流量远达不到Shard的最大读写能力时，建议您合并Shard，降低活跃Shard租用费用。您可以通过合并操作减少Shard数量，日志服务会找到指定Shard右侧相邻的Shard，并将两个Shard合并。合并Shard只支持手动操作，无法自动合并。
重要
合并Shard时，必须指定一个处于readwrite状态的Shard，且不能是最后一个readwrite状态的Shard。
单击日志存储，在日志库中，将鼠标悬浮在目标LogStore上，选择>修改。
在Logstore属性页面中，单击修改。
选择待合并的Shard，单击合并。
在Shard 管理页面，顶部展示 Shard 总数及读写、只读个数统计。下方表格包含Id、状态、BeginKey/EndKey、创建时间、操作列。状态为readwrite的 Shard 支持分裂或合并操作，状态为readonly的 Shard 无可用操作。
单击保存。
合并完成后，所指定的Shard及其右侧相邻Shard的状态变成readonly。同时新生成一个readwrite状态的Shard，新Shard的MD5范围覆盖原来两个Shard的范围。
