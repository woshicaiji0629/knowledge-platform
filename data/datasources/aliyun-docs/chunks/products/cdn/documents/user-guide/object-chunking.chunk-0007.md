/user-guide/http-status-code-416.md)[416](../../../oss/documents/user-guide/http-status-code-416.md)[错误](../../../oss/documents/user-guide/http-status-code-416.md)进行解决，详细错误信息如下：
The requested range cannot be satisfied
Range: bytes=500-2000：末字节超出有效区间，返回500~999字节范围内容。
Range: bytes=1000-2000：首字节超出有效区间，返回错误416 (InvalidRange)。
Range: bytes=1000-：首字节超出有效区间，返回错误416 (InvalidRange)。
Range: bytes=-2000：指定范围超出有效区间，返回0~999字节，即完整的文件内容。
针对上述内容，本文提供如下HTTP Range请求示例。
说明
此处假设Object资源大小为1000字节，Range有效区间为0~999。
请求Object资源0~499字节范围内的内容。
GET /ObjectName Range: bytes=0-499 Host: bucket.oss-cn-hangzhou.aliyuncs.com Date: Fri, 18 Oct 2019 02:51:30 GMT Authorization: Sigature 206 (Partial Content) content-length: 500 content-range: bytes 0-499/1000 connection: keep-alive etag: "CACF99600561A31D494569C979E6FB81" x-oss-request-id: 5DA928B227D52731327DE078 date: Fri, 18 Oct 2019 02:51:30 GMT [500 bytes of object data]
请求Object资源第500字节到文件结尾的内容。
GET /ObjectName Range: bytes=500- Host: bucket.oss-cn-hangzhou.aliyuncs.com Date: Fri, 18 Oct 2019 03:24:39 GMT Authorization: Signature 206 (Partial Content) content-length: 500 content-range: bytes 500-999/1000 etag: "CACF99600561A31D494569C979E6FB81" x-oss-request-id
