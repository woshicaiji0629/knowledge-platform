### 开启过滤参数功能
- 可能由于没有开启CDN的过滤参数功能，导致URL中传递参数为变量。以如下URL为例，其对应的文件为ArrowScene.ccbi，但是每一次打开该文件时，URL中“?_t=”字段后的数字为变量，所以CDN并不会缓存该数据。http://example.com/movie/XSHD/res/ccb/ArrowScene.ccbi?_t=xxxxxxxxxxxxxx
- 登录CDN控制台，开启过滤参数功能。关于如何开启过滤参数功能，请参考[过滤参数](user-guide/ignore-parameters.md)。说明：开启该功能后，“?_t=”字段后的参数将被忽略。
