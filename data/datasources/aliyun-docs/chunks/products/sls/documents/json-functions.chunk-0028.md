### 示例
将content字段JSON内容压缩为1层键值对。
字段样例
content: '{"Time":1626314920,"Info":[{"count":"1"}],"Body":"this is test"}'
查询和分析语句
select json_object_flatten(content) as data from (values '{"Time":1626314920,"Info":[{"count":"1"}],"Body":"this is test"}') t (content) limit 1;
输出数据
如下，data字段的值为{"Time":"1626314920","Info":"[{\"count\":\"1\"}]","Body":"this is test"}，即原始JSON对象已被压缩为单层键值结构。
该文章对您有帮助吗？
反馈
