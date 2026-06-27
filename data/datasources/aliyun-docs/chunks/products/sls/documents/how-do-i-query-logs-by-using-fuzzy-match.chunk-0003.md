## 通过SQL的正则式函数进行模糊查询
通过正则式函数，可以在一个正则式中查询多个词。并且正则式的表达语义比like语法更强大，可以搜索满足数字的词以及满足特定字符的词等，详情请参见[正则式函数](regular-expression-functions-1.md)。
示例：
* | select * from log where regexp_like(key, abc*)表示查询以abc开头的词。
* | select * from log where regexp_like(key, abc\d+)表示查询以abc开头且后面跟着数字的词。
* | select * from log where regexp_like(key, abc[xyz])表示查询以abc开头且后面跟着xyz中的某个字符的词。
该文章对您有帮助吗？
反馈
