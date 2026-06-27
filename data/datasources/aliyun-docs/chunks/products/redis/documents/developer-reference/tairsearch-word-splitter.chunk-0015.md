### Mapping Character Filter
可通过mappings参数配置Key-Value映射关系，当匹配到Key字符，则用对应Value进行替换，例如":) =>_happy_"，表示":)"会被"_happy_"替换。支持配置多个过滤器。
参数说明：
mappings（必填）：数组类型，每个元素必须包含=>，例如"&=>and"。
配置示例：
{ "mappings":{ "properties":{ "f0":{ "type":"text", "analyzer":"my_custom_analyzer" } } }, "settings":{ "analysis":{ "analyzer":{ "my_custom_analyzer":{ "type":"custom", "tokenizer":"standard", "char_filter": [ "emoticons" ] } }, "char_filter":{ "emoticons":{ "type":"mapping", "mappings":[ ":) => _happy_", ":( => _sad_" ] } } } } }
