## EdgeScript边缘脚本/边缘函数
edge_function
功能说明：边缘脚本EdgeScript，该功能详细介绍请参见控制台配置说明[EdgeScript](../user-guide/edgescript-overview.md)[概述](../user-guide/edgescript-overview.md)。
功能ID（FunctionID/FuncId）：180。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| rule | String | 是 | DSL 规则。 | if eq($uri, '/') {\n rewrite('https://example.com/index.html', 'redirect')\n} |
| pri | Integer | 是 | 优先级，取值：[0,999]，数字越小优先级越高。 说明 头部执行和尾部执行的优先级互相独立。 | 0 |
| enable | String | 是 | 本条规则是否生效： on：生效。 off：无效。 | on |
| name | String | 是 | 规则名称，仅支持英文字母和下划线（_）。 | test |
| pos | String | 否 | 规则执行位置，取值： head（默认值）：请求处理流程头部介入。 foot：请求处理流程尾部介入。 | head |
| brk | String | 否 | 中断执行，取值： on：命中本条规则后，当前执行位置剩余规则均跳过。 off（默认值）：命中本条规则后，还会执行剩余规则。 | off |
| option | String | 否 | 扩展字段。 | 空 |
| grammar | String | 否 | 规则语法，取值：es2（默认值）和 js。 | / |
| jsmode | String | 否 | JS 执行模式，取值： redirect：拦截模式。 bypass（默认值）：旁路模式。 | / |
