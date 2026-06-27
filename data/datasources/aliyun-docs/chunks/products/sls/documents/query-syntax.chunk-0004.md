### 步骤二：确定字段类型
编写查询语句时需要考虑字段类型的特点，合理使用运算符，快速、精准地锁定目标日志。
字段类型

| 字段类型 | 说明 | 可用运算符 |
| --- | --- | --- |
| [text](data-types.md) [类型](data-types.md) | 字符串类型的字段。开启全文索引后，日志服务默认将整条日志（除 __time__ 以外所有字段）设置为 text 类型。 | and 、 or 、 not 、 () 、 : 、 "" 、 \ 、 * 、 ? 。 |
| [long](data-types.md) [和](data-types.md) [double](data-types.md) [类型](data-types.md) | 只有设置字段的数据类型为 long 或 double 后，才能通过数值范围查询该字段的值。 如果字段的数据类型不被设置为 double 、 long 或者查询时数值范围的语法错误，那么日志服务会按照全文查询方式进行查询，这样查询到的结果可能与期望的结果不同。 例如字段 owner_id 不是 double 、 long 类型，则执行查询语句 owner_id>100 时，会返回同时包含 owner_id 、 > （非分词符）、 100 这三个词的日志。 如果将字段的类型从 text 类型改成 double 、 long 类型，则只支持等号 = 查询。如果需要使用范围查询、大于号（>）、小于号（<）等运算符，必须 [重建索引](reindex-logs-for-a-logstore.md) 。 | and 、 or 、 not 、 () 、 > 、 >= 、 < 、 <= 、 = 、 in 。 |
| [JSON](data-types.md) [类型](data-types.md) | 针对 JSON 对象中的字段，可根据其值，将数据类型设置为 long 、 double 或 text ，并开启统计功能。 | 根据 JSON 对象中的字段的类型使用不同的运算符。 |

运算符
重要
in运算符只能小写，其他运算符不区分大小写。
日志服务保留以下运算符的使用权，如果您需要使用以下运算符作为查询关键字，请使用""（双引号）包裹：sort、asc、desc、group by、avg、sum、min、max和limit。
运算符的优先级由高到低排序如下所示：
冒号（:）
双引号（""）
圆括号（）
and、not
or
