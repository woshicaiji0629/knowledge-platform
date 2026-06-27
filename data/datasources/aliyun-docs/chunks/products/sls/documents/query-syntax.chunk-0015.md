| 查询需求 | 查询语句 | 调试 |
| --- | --- | --- |
| 查询包含以 cn 开头的词的日志。 | cn* | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DY24q) |
| 查询 region 字段值是以 cn 开头的日志。 | region:cn* | 无 |
| 查询 region 字段值包含 cn* 的日志。 | region:"cn*" 说明 此处的 cn* 为一个独立词。例如： 如果日志内容为 region:cn*,en ，分词符为半角逗号（,），则该日志内容被拆分为 region 、 cn* 和 en ，您可以通过上述语句查询到该日志。 如果日志内容为 region:cn*hangzhou ，则 cn*hangzhou 为一个整体，您执行上述语句无法查询到该日志。 | 无 |
| 查询包含以 mozi 开头，以 la 结尾，中间还有一个字符的词的日志。 | mozi?la | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DbW96aT9sYQ%3D%3D) |
| 查询包含以 mo 开头，以 la 结尾，中间包含零个、单个或多个字符的词的日志。 | mo*la | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DbW8qbGE%3D%26queryTimeType%3D99) |
| 查询包含以 moz 开头的词和以 sa 开头的词的日志。 | moz* and sa* | [调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DbW96KiBhbmQgc2Eq) |
| 查询 region 字段值以 hai 结尾的所有日志。 | 目前使用
