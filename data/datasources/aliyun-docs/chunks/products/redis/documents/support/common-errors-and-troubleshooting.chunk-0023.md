### Connection reset by peer
可能原因：标准架构，开启了TLS（SSL）加密连接，未带证书访问。
解决方案：
携带证书访问，参考[TLS（SSL）加密连接实例](../user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance-that-has-ssl-encryption-enabled.md)。
若无需使用TLS（SSL）加密，请[关闭](../user-guide/enable-tls-encryption.md)[TLS](../user-guide/enable-tls-encryption.md)[加密](../user-guide/enable-tls-encryption.md)后重试。
