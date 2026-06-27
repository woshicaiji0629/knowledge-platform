## 步骤七：测试连通性
说明
测试连通性时，请确保您的客户端已支持IPv6功能，您可以在浏览器地址栏输入网址http://test-ipv6.com/测试您的客户端是否支持IPv6功能。
以任意一台可以访问IPv6客户端的终端为例，测试IPv6客户端与ECS01和ECS02服务器的连通性。
打开终端的cmd窗口。
多次执行以下命令，测试IPv6客户端是否可以通过ALB以轮询的方式访问IPv4 ECS以及IPv6 ECS。
curl -6 http://<域名> -v
如果收到如下所示的回复报文，则表示IPv6客户端可以访问IPv4 ECS。
C:\Users\w***g>curl -6 http://xxx.com -v * Rebuilt URL to: http://xxx.com/ * Trying 2408:xxx:d3:c2b:df22:bc09... * TCP_NODELAY set * Connected to xxx.com (2408:xxx:f22:bc09) port 80 (#0) > GET / HTTP/1.1 > Host: xxx.com > User-Agent: curl/7.55.1 > Accept: */* > < HTTP/1.1 200 OK < Date: Wed, 07 Sep 2022 06:52:47 GMT < Content-Type: text/html < Content-Length: 31 < Connection: keep-alive < Last-Modified: Wed, 07 Sep 2022 03:13:10 GMT < ETag: "63180c46-1f" < Accept-Ranges: bytes < Hello World ! this is ipv4 rs.
如果收到如下所示的回复报文，则表示IPv6客户端可以访问IPv6 ECS。
C:\Users\wxxx>curl -6 http://xxx.s.com -v * Rebuilt URL to: http://xxx.com/ * Trying 2408:40xxx:df22:bc09... * TCP_NODELAY set * Connected to xxx.s.com (2408:xxx:22:bc09) port 80 (#0) > GET / HTTP/1.1 > Host: xxx > User-Agent: curl/7.55.1 > Accept: */* > < HTTP/1.1 200 OK < Date: Wed, 07 Sep 2022 06:53:04 GMT < Content-Type: text/html < Content-Length: 31 < Connection:
