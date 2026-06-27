### 步骤三：设置私有Bucket回源
默认情况下，新创建的Bucket读写权限为私有，通过CDN访问时需要开启私有Bucket回源功能，授权CDN节点访问私有资源。如果Bucket读写权限设为公共读，CDN可直接访问，无需开启此功能。
在[CDN](https://cdnnext.console.aliyun.com/domain/list)[控制台](https://cdnnext.console.aliyun.com/domain/list)单击目标域名，然后在左侧导航栏单击回源配置。
在阿里云OSS私有Bucket回源部分开启私有Bucket回源，回源类型选择同账号回源。
重要
开启私有Bucket回源后，CDN将获得访问私有Bucket的授权，并自动在回源请求中添加签名信息。因此，客户端必须使用不包含签名参数的URL（如http://example.com/example.jpg）进行访问。若URL中仍携带Expires、Signature等签名参数，将导致OSS鉴权失败，返回403错误。
