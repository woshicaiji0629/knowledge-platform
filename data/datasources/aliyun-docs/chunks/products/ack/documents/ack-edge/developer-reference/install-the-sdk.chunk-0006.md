### 运行SDK示例代码
打开IntelliJ IDEA，单击File->Open，选择解压后的工程文件夹，等待Maven自动安装依赖信息。
运行示例代码。
双击打开Sample，确认无报错后，运行代码。
查看运行结果。
在底部控制台搜索statusCode，如果看到"statusCode":202表示调用成功已开始创建集群。您可以在[容器服务管理控制台](https://cs.console.aliyun.com)的集群列表页面看到新创建的集群。
{ "headers": { "content-type": "application/json;charset=utf-8", "access-control-expose-headers": "*", "x-acs-trace-id": "30c74bc83a7fae0a081e5f5846be703e" }, "statusCode": 202, "body": { "clusterId": "c6104ee21d6304ef8..." } }
该文章对您有帮助吗？
反馈
