## Range回源
Range回源，指CDN节点在回源的HTTP请求里面携带了Range信息，源站在收到CDN节点的回源请求时，根据HTTP请求头中的Range信息返回指定范围的内容数据给CDN节点，例如只返回某个文件的0-100Byte范围内的数据。
在视频点播、软件下载等大文件内容分发场景下，Range回源可有效提高文件分发效率，可以提高缓存命中率，减少回源流量消耗和源站压力，并且提升资源响应速度。具体操作，可参见[配置](../user-guide/object-chunking.md)[Range](../user-guide/object-chunking.md)[回源](../user-guide/object-chunking.md)。
说明
Range是HTTP请求头之一，可用来指定需获取的内容的范围。
