# 服务端加密
当您在设置了服务端加密的存储空间（Bucket）中上传文件（Object）时，OSS对收到的文件进行加密，再将得到的加密文件持久化保存。当您通过GetObject请求下载文件时，OSS自动将加密文件解密后返回给用户，并在响应头中返回x-oss-server-side-encryption，用于声明该文件进行了服务端加密。
说明
关于响应头中x-oss-server-side-encryption的更多信息，请参见[GetObject](../developer-reference/getobject.md)。
