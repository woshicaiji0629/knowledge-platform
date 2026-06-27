T Authorization: Signature 206 (Partial Content) content-length: 500 content-range: bytes 500-999/1000 etag: "CACF99600561A31D494569C979E6FB81" x-oss-request-id: 5DA9307750EBE33332E3720A date: Fri, 18 Oct 2019 03:24:39 GMT [500 bytes of object data]
请求Object资源最后500字节的内容。
GET /ObjectName Range: bytes=-500 Host: bucket.oss-cn-hangzhou.aliyuncs.com Date: Fri, 18 Oct 2019 03:23:22 GMT Authorization: Signature 206 (Partial Content) content-length: 500 content-range: bytes 500-999/1000 etag: "CACF99600561A31D494569C979E6FB81" x-oss-request-id: 5DA9302A6646AC37397F7039 date: Fri, 18 Oct 2019 03:23:22 GMT [500 bytes of object data]
说明
建议在大文件（平均单个文件大小在20 MB以上）内容分发场景下，CDN回源OSS的配置中都进行该项配置。
如果在阿里云OSS源站上开启了访问鉴权功能，并且由客户端来实现回源请求的签算，那么客户端在签算的时候需要把回源请求头x-oss-range-behavior:standard加入签算。阿里云OSS计算签名时会包含所有x-oss-前缀的请求头。若客户端签算未包含x-oss-range-behavior请求头将导致签名不一致而被拒绝。
