## 步骤四：验证连通性
完成上述操作后，客户端可以通过ALB访问部署了gRPC服务的后端服务器，以下内容为您展示如何测试客户端和gRPC服务之间的连通性。
说明
浏览器无法直接访问gRPC服务。建议您通过grpcurl工具之类的测试工具验证访问。
在客户端中执行grpcurl -insecure -v <域名>:<监听端口> <gRPC服务名称>/<方法>命令尝试访问ECS中的gRPC服务。
如果收到类似以下所示的回复报文，则表示客户端可以通过ALB访问部署了gRPC服务的后端服务器ECS。
[root@iZbp1xxx.0Z ~]# grpcurl -insecure -v xxx.com:443 helloworld.Greeter/SayHello Resolved method descriptor: rpc SayHello ( .helloworld.HelloRequest ) returns ( .helloworld.HelloReply ); Request metadata to send: (empty) Response headers received: accept-encoding: identity,gzip content-type: application/grpc date: Mon, 04 Jul 2022 08:53:01 GMT grpc-accept-encoding: identity,deflate,gzip vary: Accept-Encoding Response contents: { "message": "remoteip:47.xxx.xxx.195 x-forwarded-for:47.xxx.xxx.xx5 user-agent:grpcurl/v1.8.0 grpc-go/1.30.0 hostname:iZbp12xxx0kZ server addr:192.168.1.239 " } Response trailers received: (empty) Sent 0 requests and received 1 response
