## 规则引擎
condition
功能说明：规则引擎，该功能能够使用图形化的方式来配置各种条件规则。条件规则支持对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效，可用于更加灵活、更加精确地控制CDN的各种配置策略的执行效果。该功能详细介绍请参见控制台配置说明[规则引擎](../user-guide/rules-engine.md)。
功能ID（FunctionID/FuncId）：250。
该功能需要申请再开通，您需要[填写信息](https://page.aliyun.com/form/act2017566026/index.htm)申请开通该功能。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| rule | Array | 是 | 规则条件的具体内容，包括名称、状态、逻辑判断、条件表达式。 | 规则条件内容： {\"match\":{\"logic\":\"and\",\"criteria\":[{\"matchType\":\"clientipVer\",\"matchObject\":\"CONNECTING_IP\",\"matchOperator\":\"equals\",\"matchValue\":\"v6\",\"negate\":false}]},\"name\":\"example\",\"status\":\"enable\"} 实现效果： 规则名称：example 状态：enable 逻辑判断：and 条件表达式：客户端建联 IP 的协议版本等于 v6 |

条件表达式的格式（即argValue的格式）说明如下：
