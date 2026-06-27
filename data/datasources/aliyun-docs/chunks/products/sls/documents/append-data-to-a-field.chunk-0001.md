## 参数说明
配置type为processor_appender，detail说明如下表所示。
表 1.插件说明

| 参数 | 类型 | 是否必选 | 参数说明 |
| --- | --- | --- | --- |
| Key | string | 是 | 字段名称。 |
| Value | string | 是 | 添加的字段值。日志服务支持在该字段值中添加模板变量。更多信息，请参见 [模板变量](append-data-to-a-field.md) 。 |
| SortLabels | boolean | 否 | 如果您要添加 __labels__ 字段，即配置 Key 为 __labels__ ，则需要设置 SortLabels 为 true ，用于对 Labels 进行重新排序，避免因为 Labels 不遵循字母序而导致查询异常。该值默认为 false。 |

表 2.模板变量

| 模板变量 | 说明 | 配置示例 | 结果示例 |
| --- | --- | --- | --- |
| {{__ip__}} | 替换为 Logtail 所在服务器的 IP 地址。 | "Value": "{{__ip__}}" | "Value": "192.0.2.1" |
| {{__host__}} | 替换为 Logtail 所在服务器的主机名。 | "Value": "{{__host__}}" | "Value": "logtail-ds-xdfaf" |
| {{$xxxx}} | 通过环境变量引用，需以美元符号（$）开头。替换为环境变量的取值。 | "Value": "{{$WORKING_GROUP}}" | "Value": "prod" |
