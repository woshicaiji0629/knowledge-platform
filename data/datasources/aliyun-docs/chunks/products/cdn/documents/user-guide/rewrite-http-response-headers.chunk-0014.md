### 怎么检查源站上正确设置了Access-Control-Allow-Origin等响应头？
如果您的源站为阿里云服务器ECS
您需要确保在ECS上运行的Web服务器或应用程序正确设置了Access-Control-Allow-Origin以及其他CORS（跨源资源共享）相关的响应头，可以按照以下步骤进行：
登录[ECS](https://ecs.console.aliyun.com)[管理控制台](https://ecs.console.aliyun.com)访问您的ECS实例。
检查Web服务器跨域配置。
跨域响应头的配置可能因您使用的Web服务器或应用程序而异。常见的Web服务器有Apache、Nginx等。
