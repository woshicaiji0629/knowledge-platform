### 数据脱敏
使用processor_desensitize_native插件对日志中的敏感数据进行脱敏处理。

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定值 processor_desensitize_native 。 | # ...在 spec.config 下... processors: # 配置原生日志脱敏插件 - Type: processor_desensitize_native # 原始字段名 SourceKey: content # 脱敏方式：const 表示用固定字符串替换敏感内容 Method: const # 替换敏感内容的目标字符串 ReplacingString: '********' # 被替换内容前的内容表达式 ContentPatternBeforeReplacedString: 'password'':''' # 敏感内容本身的正则表达式，匹配要被替换的内容 ReplacedContentPattern: '[^'']*' # 是否替换所有匹配项，默认为 true ReplacingAll: true |
| SourceKey String （必选） 源字段名。 |  |
| Method String （必选） 脱敏方式。可选值包括： const ：用常量替换敏感内容。 md5 ：用敏感内容的 MD5 值替换相应内容。 |  |
| ReplacingString String （可选） 用于替换敏感内容的常量字符串。当 Method 取值为 const 时必选。 |  |
| ContentPatternBeforeReplacedString String （必选） 敏感内容的前缀正则表达式。 |  |
| ReplacedContentPattern String （必选） 敏感内容的正则表达式。 |  |
| ReplacingAll boolean （可选） 解析成功时是否保留原始字段，默认为 true 。 |  |
