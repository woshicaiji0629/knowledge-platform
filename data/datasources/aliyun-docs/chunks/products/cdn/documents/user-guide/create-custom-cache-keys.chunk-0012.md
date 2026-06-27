m/abc/xyz/abc/image.jpg，按URI的配置Cache Key将被合并成http://aliyundoc.com/abc/image.jpg， 然后根据自定义变量的配置该URL将会命中/abc/xyz/(.*)，此时$1将被赋值为abc并拼接到Cache Key中，形成最终的Cache Key：http://aliyundoc.com/abc/image.jpgabc，从而达到两个规则组合使用，实现更复杂的缓存逻辑。
如果没有匹配到Cache Key的自定义变量，则变量表达式$1就不会被拼接到Cache Key中。
示例四
同时设置规则条件和自定义变量，使来自Mobile端和PC端的请求生成不同的Cache Key。
Mobile规则条件：
User-Agent包含*Mobile*,*Android*,*iPhone*,*ipad*其中任意一个
PC规则条件：
User-Agent不包含*Mobile*,*Android*,*iPhone*,*ipad*其中任意一个
Mobile自定义Cache Key：
规则条件选择Mobile，自定义变量的变量名为Mobile，来源为Path，匹配规则为/，变量表达式为+mobile。
PC自定义Cache Key：
规则条件选择PC，自定义变量的变量名为PC，来源为Path，匹配规则为/，变量表达式为+pc。
客户端的请求URLhttp://aliyundoc.com/image.jpg，根据User-Agent的值，请求分别命中Mobile端和PC端的自定义Cache Key规则。Mobile端最终生成的Cache Key为：http://aliyundoc.com/image.jpg+mobile；PC端最终生成的Cache Key为：http://aliyundoc.com/image.jpg+pc。
