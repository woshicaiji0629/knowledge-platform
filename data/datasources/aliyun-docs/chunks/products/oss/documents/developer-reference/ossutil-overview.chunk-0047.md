### 从非命令行中加载数据
一般情况下，参数的值都放在命令行里，当参数值比较复杂时，需要从文件加载参数值；当需要串联多个命令操作时，需要标准输中加载参数值。所以，对需要支持多种加载参数值的参数，做了如下约定：
以file://开始的，表示从文件路径中加载。
当参数值为-时，表示从标准输入中加载。
例如， 设置存储空间的跨域设置，以JSON参数格式为例，通过文件方式加载跨域参数。cors-configuration.json文件如下：
{ "CORSRule": { "AllowedOrigin": ["www.aliyun.com"], "AllowedMethod": ["PUT","GET"], "MaxAgeSeconds": 10000 } }ossutil api put-bucket-cors --bucket examplebucket --cors-configuration file://cors-configuration.json
通过选项参数值加载跨域参数，cors-configuration.json的紧凑形式如下：
{"CORSRule":{"AllowedOrigin":["www.aliyun.com"],"AllowedMethod":["PUT","GET"],"MaxAgeSeconds":10000}}ossutil api put-bucket-cors --bucket examplebucket --cors-configuration "{\"CORSRule\":{\"AllowedOrigin\":[\"www.aliyun.com\"],\"AllowedMethod\":[\"PUT\",\"GET\"],\"MaxAgeSeconds\":10000}}"
从标准输入加载参数的示例如下：
cat cors-configuration.json | ossutil api put-bucket-cors --bucket examplebucket --cors-configuration -
