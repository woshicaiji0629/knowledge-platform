志内容为 instance_id:nginx"01" ，您可以使用 instance_id:nginx\"01\" 进行查询。 |
| * | 通配符查询，匹配零个、单个、多个字符。例如 host:www*com 。 说明 日志服务会在所有日志中为您查询到符合条件的 100 个词，返回包含这 100 个词并满足查询条件的所有日志。 |
| ? | 通配符查询，匹配单个字符。例如 host:aliyund?c 。 |
| > | 查询某字段值大于某数值的日志。例如 request_time>100 。 |
| >= | 查询某字段值大于或等于某数值的日志。例如 request_time>=100 。 |
| < | 查询某字段值小于某数值的日志。例如 request_time<100 。 |
| <= | 查询某字段值小于或等于某数值的日志。例如 request_time<=100 。 |
| = | 查询某字段值等于某数值的日志。针对 double、long 类型的字段， = 和 : 作用相同。例如 request_time=100 等同于 request_time:100 。 |
| in | 查询某字段值处于某数值范围内的日志，中括号表示闭区间，小括号表示开区间，两个数字之间使用空格分隔。例如 request_time in [100 200] 或 request_time in (100 200] 。 重要 in 只能为小写字母。 |
| __source__ | 查询某个日志源的日志，支持通配符。例如 __source__:192.0.2.* 。 重要 日志服务中的 __source__ 为保留字段，可缩写为 source 。如果您自定义的字段中存在 source 字段，则会与日志服务保留字段 source 冲突，此时您需要使用 Source 、 SOURCE 等词查询自定义的字段。 |
| __tag__ | 通过元数据信息查询日志。例如 __tag__:__receive_time__:1609837139 。 |
| __topic__ | 查询某日志主题下的日志。例如 __topic__:nginx_access_log 。 |
