### 什么是QUIC
QUIC（Quick UDP Internet Connections）是一种实验性传输层网络协议，提供与TLS/SSL相当的安全性，同时具有更低的连接和传输延迟。QUIC基于UDP，因此拥有极佳的弱网性能，在丢包和网络延迟严重的情况下仍可提供可用的服务。QUIC在应用程序层面就能实现不同的拥塞控制算法，不需要操作系统和内核支持，这相比于传统的TCP协议，拥有了更好的改造灵活性，非常适合在TCP协议优化上遇到瓶颈的业务。
目前，阿里云CDN开放使用的是七层协议的QUIC。
QUIC的类型
阿里云CDN支持互联网标准版本 IETF QUIC。
对客户端的要求
QUIC协议对客户端的要求如下：
如果您使用Chrome浏览器，当前阿里云CDN已经支持HTTP/3的标准协议，Chrome支持直接对阿里云CDN发起QUIC请求。
如果您使用自研App，则App必须集成支持QUIC协议的网络库，例如：lsquic-client、cronet网络库、ngtcp2和quiche等。
