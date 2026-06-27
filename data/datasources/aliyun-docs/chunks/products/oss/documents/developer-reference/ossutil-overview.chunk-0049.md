例如：以get-bucket-cors为例，原始内容如下：
ossutil api get-bucket-cors --bucket bucketexample <?xml version="1.0" encoding="UTF-8"?> <CORSConfiguration> <CORSRule> <AllowedOrigin>www.aliyun.com</AllowedOrigin> <AllowedMethod>PUT</AllowedMethod> <AllowedMethod>GET</AllowedMethod> <MaxAgeSeconds>10000</MaxAgeSeconds> </CORSRule> <ResponseVary>false</ResponseVary> </CORSConfiguration>
转成JSON如下：
ossutil api get-bucket-cors --bucket bucketexample --output-format json { "CORSRule": { "AllowedMethod": [ "PUT", "GET" ], "AllowedOrigin": "www.aliyun.com", "MaxAgeSeconds": "10000" }, "ResponseVary": "false" }筛选输出
ossutil提供了基于JSON的内置客户端筛选功能，通过--output-query value选项使用。
说明
该选项仅支持ossutil api下的子命令。
该功能基于JMESPath语法，当使用该功能时，会把返回的内容转成JSON，然后再使用JMESPath进行筛查，最后按照指定的输出格式输出。有关JMESPath 语法的说明，请参见[JMESPath Specification](https://jmespath.org/specification.html)。
例如：以get-bucket-cors为例，只输出AllowedMethod内容，示例如下：
ossutil api get-bucket-cors --bucket bucketexample --output-query CORSRule.AllowedMethod --output-format json [ "PUT", "GET" ]友好显示
对于高级命令（du、stat），提供了--human-readable选项，对字节、数量数据，提供了以人类可读方式输出信息。即字节数据转成Ki|Mi|Gi|Ti|Pi后缀格式（1024 base），数量数据转成k|m|g|t|p后缀格式(1000 base)。
例如：原始模式
ossutil stat oss://bucketexample ACL : private
