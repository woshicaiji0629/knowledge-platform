## 常见问题
Q1：为什么入门级规格的性能看起来比企业级规格的性能要好？
A：因为入门级规格一般是共享/通用型规格族，企业级规格一般是独享型规格族。实际使用中企业级规格由于独享CPU和内存，会更加稳定。详细区别，请参见[实例规格族](instance-families.md)。
Q2：想查询当前售卖资源怎么办？
A：可以在售卖页查询或使用[DescribeAvailableResource](../api-query-available-resources.md)接口查询。
Q3：为什么不展示QPS和TPS？
A：QPS和TPS需要RDS上面部署相关对象测试。同一个规格的实例在不同业务系统中，根据实现方法不同，QPS和TPS也会有较大的差距。QPS和TPS的测试方法，请参见[性能测试指导](../support/test-guidelines.md)。
