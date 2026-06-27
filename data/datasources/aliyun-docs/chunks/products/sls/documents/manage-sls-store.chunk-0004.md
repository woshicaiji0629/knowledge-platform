### 事件库（EventStore）
[事件库（EventStore）](manage-an-eventstore.md)是日志服务中事件数据存储和查询的单元。每个EventStore隶属于一个Project，每个Project中可创建多个EventStore。根据实际需求为某个项目创建多个EventStore，一般是为不同类型的事件数据创建不同的EventStore。例如可以根据基础设施异常事件、业务应用事件、自定义事件等进行分类，通过不同的EventStore来进行存储和分析。
在执行写入、查询和分析、消费事件数据时，都需要指定EventStore。具体说明如下：
以EventStore为采集单元采集事件数据。
以EventStore为存储单元存储事件数据以及执行消费操作。
