## 注意事项
创建TLS连接需要经历多次握手过程，包括认证和密钥交换，这些步骤会占用显著的计算资源和时间，创建TLS连接的速度显著低于创建普通连接。在短时间内无法快速创建大量TLS连接，且频繁创建TLS连接会显著影响正常请求的延迟。因此，建议通过使用TLS长连接来减少这些开销，尽量避免频繁创建和销毁TLS连接，以降低对性能的影响。
建立TLS连接后，使用TLS连接传输数据，由于所有的数据都需要加密、解密，也会产生额外开销，这些额外开销会伴随传输内容大小增长。
说明
具体的性能影响因业务场景而异，需要进行实际测试来评估在特定业务环境下的影响程度。
开启TLS加密功能后，实例将不支持申请公网连接地址，同时经典版集群实例也无法申请直连地址，客户端只能通过专有网络、TLS加密方式连接实例。连接示例请参见[启用](use-a-client-to-connect-to-an-apsaradb-for-redis-instance-that-has-ssl-encryption-enabled.md)[TLS（SSL）加密连接实例](use-a-client-to-connect-to-an-apsaradb-for-redis-instance-that-has-ssl-encryption-enabled.md)。
开启TLS加密功能后，实例将不支持迁移可用区。
开启TLS加密功能后，若修改了实例的连接地址或端口号，请更新实例TLS证书，再进行连接。否则会报错No subject alternative DNS name matching xxx found。
