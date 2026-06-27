## 计费说明
ossbrowser软件本身免费，但通过ossbrowser执行相关操作时，其计费方式与在控制台操作相同，都会遵循OSS计费逻辑收取相应费用。例如：
本地环境中上传下载文件：在本地环境中使用ossbrowser上传和下载文件时，涉及PUT类[请求费用](../api-operation-calling-fees.md)，GET类的[请求费用](../api-operation-calling-fees.md)和下行[流量费用](../traffic-fees.md)。上传文件到OSS后需要根据文件存储类型收取[存储费用](../storage-fees.md)。
内网环境中上传下载文件：在阿里云内网环境中，使用ossbrowser上传和下载文件，只涉及PUT和GET类[请求费用](../api-operation-calling-fees.md)以及文件[存储费用](../storage-fees.md)。无流量费用。例如可以通过创建ECS实例，并在其上安装ossbrowser后实现在阿里云内网中上传和下载文件。
此外，如果您的业务需要在中国内地与海外地域之间传输数据，使用内外网可能无法满足预期的传输效率。建议开启传输加速服务来提升数据上传下载速度。使用传输加速服务会产生[传输加速费用](../transfer-acceleration-fees.md)。有关OSS更多增值相关费用，请参见[增值计费项](../value-added-billing-item.md)。
