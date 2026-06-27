# JSON函数
本文介绍JSON函数的基本语法及示例。
日志服务支持如下JSON函数。
重要
在日志服务分析语句中，表示字符串的字符必须使用单引号（''）包裹，无符号包裹或被双引号（""）包裹的字符表示字段名或列名。例如：'status'表示字符串status，status或"status"表示日志字段status。
如果日志字段的值为JSON类型且需要展开为多行，请使用unnest语法。更多信息，请参见[UNNEST](unnest-clause.md)[子句](unnest-clause.md)。
如果字符串被解析成JSON类型失败，则返回null。
如果在采集过程中，JSON日志被截断，则在使用JSON函数进行查询与分析时，系统将报错且中止查询与分析。针对该错误，您可以使用TRY表达式捕获异常信息，使得系统继续执行查询和分析操作。例如* | select message, try(json_parse(message))。更多信息，请参见[TRY](conditional-expressions.md)[表达式](conditional-expressions.md)。
