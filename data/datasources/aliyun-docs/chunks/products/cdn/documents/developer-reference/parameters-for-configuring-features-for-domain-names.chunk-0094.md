匹配。 |
| \"negate\":false | negate 表示是否对条件表达式的结果取反，取值为 true 和 false。 |
| \"name\":\"example\" | name 表示规则条件的名称。 |
| \"status\":\"enable\" | status 表示规则条件的生效状态。 |

配置示例：
以下示例演示了如何通过OpenAPI来给加速域名example.com添加一个规则引擎配置，实现对客户端IP协议版本是否为IPv6的匹配和过滤。对于规则引擎功能的详细说明请参见[规则引擎](../user-guide/rules-engine.md)。
{ "Functions": [{ "functionArgs": [{ "argName": "rule", "argValue": "{\"match\":{\"logic\":\"and\",\"criteria\":[{\"matchType\":\"clientipVer\",\"matchObject\":\"CONNECTING_IP\",\"matchOperator\":\"equals\",\"matchValue\":\"v6\",\"negate\":false}]},\"name\":\"example\",\"status\":\"enable\"}" }], "functionName": "condition" }], "DomainNames": "example.com" }
创建完成的规则引擎配置，可以供其他功能配置时关联引用（当前支持引用规则引擎配置的功能列表请参见[规则引擎](../user-guide/rules-engine.md)），以实现更加灵活、更加精确地控制CDN各种配置策略的执行效果。例如：[条件源站功能](../user-guide/configure-a-conditional-origin.md)（功能函数是origin_dns_host）的配置就可以关联引用规则引擎的配置，配置示例可以参见[origin_dns_host](parameters-for-configuring-features-for-domain-names.md)。
注意事项：
其他功能在关联引用规则引擎配置的时候，需要通过设置parentid来引用已经使用规则引擎功能创建好的某个规则条件，这里的parentid等于添加规则引擎配置时生成的configid。
功能函数是condition（规则引擎）的时候，不支持设置parentId参数。
