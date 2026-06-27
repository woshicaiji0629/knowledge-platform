## TairDoc简介
主要特性
完整地支持JSON标准。
部分兼容[JSONPath](https://datatracker.ietf.org/doc/draft-ietf-jsonpath-base/)RFC draft-4标准。
说明
仅JSON.GET命令支持。
完整地支持[JSONPointer](https://datatracker.ietf.org/doc/html/rfc6901)语法。
文档作为二进制树存储，可以快速访问JSON数据的子元素。
支持JSON到XML或YAML格式的转换。
发布记录
随Tair内存型同时发布TairDoc，支持完整的JSONPointer语法与部分JSONPath语法（仅JSON.GET命令支持JSONPath语法）。
2022年5月17号发布1.8.4版，JSON.GET命令全面支持JSONPath语法，请将小版本升级至1.8.4及以上。
该版本新增支持Dot Wild Card Selector（节点通配符选择器）、Index Selector（索引选择器）与Filter Selector（条件过滤选择器）等。
