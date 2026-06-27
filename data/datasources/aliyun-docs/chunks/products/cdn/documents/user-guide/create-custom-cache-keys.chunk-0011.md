### 自定义变量
示例一
变量名为language，来源为Request Header，来源字段名为Accept-Language，匹配规则为([%w]+),([%w]+)，变量表达式为$1aa。自定义变量配置示例：变量名设置为language，来源选择Request Header，来源字段名填写Accept-Language，匹配规则填写([%w]+),([%w]+)，变量表达式填写$1aa。
客户端的请求http://aliyundoc.com/a/b/image.jpg且携带HTTP请求头Accept-Language=en,ch，则匹配规则将匹配到en赋值给变量表达式中的$1。变量表达式还将在末尾拼接上aa，得到enaa的变量并取别名为language，拼接在URL后方形成最终的Cache Key：http://aliyundoc.com/a/b/image.jpgenaa。
说明
变量表达式中的$n的含义是匹配规则中第n个括号所匹配到的内容。例如示例一中Accept-Language=en,ch，匹配规则为([%w]+),([%w]+)，则$1=en，$2=ch。
示例二
变量名为expired，来源为Request Cookie，来源字段名为a，匹配规则为[%w]+:(.*)，变量表达式为$1。自定义变量配置示例： -变量名：expired-来源：Request Cookie-来源字段名：a-匹配规则：[%w]+:(.*)-变量表达式：$1
客户端的请求http://aliyundoc.com/a/b/image.jpg且携带Cookie a=expired_time:12635187，则匹配规则将匹配到12635187赋值给变量表达式中的$1并取别名为expired，拼接在URL后方形成最终的Cache Key：http://aliyundoc.com/a/b/image.jpg12635187。
示例三
同时设置URI规则和自定义变量。
URI：
将所有URI符合/abc/.*/abc的请求都合并成/abc。源URI为/abc/.*/abc，目标URI为/abc。
自定义变量：
变量名为testname，来源为Path，匹配规则为/abc/xyz/(.*)，变量表达式为$1。变量名：testname；来源：Path；匹配规则：/abc/xyz/(.*)；变量表达式：$1
客户端的请求URLhttp://aliyundoc.com/abc/xyz/abc/image.jpg，按URI的配置Cache Key将被合并成http://aliyundoc.com/abc/image.jpg， 然后根据自定义变量的配置该URL将会命中/abc/xyz/(.*)，此时$1将被赋值为abc并拼接到Cache Key中，形成最终的Cache Key：htt
