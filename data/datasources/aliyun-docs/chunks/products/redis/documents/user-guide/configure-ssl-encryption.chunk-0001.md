## 注意事项
2023年4月07日云数据库 Tair（兼容 Redis）将SSL加密功能升级为TLS加密功能，同时不再支持开通SSL加密功能。若您已开通SSL加密功能，您可以继续使用也可以关闭SSL，但关闭后无法再次开启，更多信息请参见[【通知】SSL](../product-overview/encryption-upgrade-from-ssl-to-tls.md)[功能升级至](../product-overview/encryption-upgrade-from-ssl-to-tls.md)[TLS](../product-overview/encryption-upgrade-from-ssl-to-tls.md)[功能](../product-overview/encryption-upgrade-from-ssl-to-tls.md)。
SSL的证书有效期为3年，请及时更新证书有效期并重新下载配置CA证书，否则使用加密连接的客户端程序将无法正常连接。
由于开通SSL加密会增加Tair（以及Redis开源版）服务的网络响应时间，建议仅在有加密需求时才开通SSL加密（例如通过公网连接实例）。
开通SSL后同时支持SSL和非SSL两种连接方式。
