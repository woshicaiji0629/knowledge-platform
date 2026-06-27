例如，对原图example.jpg添加图片缩放resize以及质量变换quality参数后，文件URL为https://oss-console-img-demo-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/example.jpg?x-oss-process=image/resize,w_300/quality,q_90。您可以通过配置不同的规则，实现CDN回源原图或者经图片处理参数后的图片。
回源原图
通过CDN开启过滤参数后，文件URL请求中问号（?）之后的参数将全部去除，即直接命中原图example.jpg。
回源处理后的图片
通过CDN开启保留回源参数后，文件URL请求中问号（?）之后的所有参数将全部保留，即直接命中经图片处理参数后的图片。
关于CDN回源规则的配置详情，请参见[忽略参数](../../../cdn/documents/user-guide/ignore-parameters.md)。
