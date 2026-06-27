### 步骤四：在应用程序中集成
在应用程序中，可通过阿里云Credentials工具配合各语言的云产品SDK自动获取STS临时凭证。STS临时凭证每15分钟自动刷新，Credentials SDK内置刷新逻辑，应用无需处理过期逻辑。
如果使用加固模式，请确保您使用的SDK版本满足以下最低要求。

| 语言 | 包名/工具 | 加固模式最低版本 |
| --- | --- | --- |
| Python | alibabacloud_credentials | 0.3.6 |
| Java | credentials-java | 0.3.10 |
| Go | github.com/aliyun/credentials-go | 1.3.10 |
| Node.js | @alicloud/credentials | 2.3.1 |
| .NET | Aliyun.Credentials | 1.4.2 |
| PHP | alibabacloud/credentials | 1.2.0 |
| 阿里云 CLI | aliyun | 3.0.248 |
