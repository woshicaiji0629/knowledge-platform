### 规则执行情况
您可以在[配置](add-and-manage-scripts.md)[AScript](add-and-manage-scripts.md)[规则](add-and-manage-scripts.md)时，在高级配置中选中携带_es_dbg参数，开启相应的调试响应头，以输出规则执行记录。
规则执行情况字段详细说明：
规则ID：每条规则的唯一性标识，格式为as-****。
执行情况code及说明：

| 执行情况 code | 执行情况说明 |
| --- | --- |
| 空 | 未执行。 |
| 0 | 执行命中。 当规则含有 if condition {} ，且 condition 为真。 |
| 1 | 执行未命中。 当规则含有 if condition {} ，且 condition 为假；或规则不包含 if condition {} 。 |
| 2 | 执行异常。 |

执行耗时：
单位：微秒us。
默认值：-1。
前端呈现的耗时区间分布：
第1档：0~100us
第2档：100~500us
第3档：500~1000us
第4档：1000~5000us
第5档：5000~20000us
第6档：20000~50000us
第7档：>50000us
AScript规则的中断执行：
默认值：-1。
该文章对您有帮助吗？
反馈
