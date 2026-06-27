配置示例：
默认配置，开启TLS1.0、1.1、1.2，使用全部加密算法套件。
{ "Functions": [{ "functionArgs": [ { "ArgValue": "on", "ArgName": "tls10" }, { "ArgValue": "on", "ArgName": "tls11" }, { "ArgValue": "on", "ArgName": "tls12" }, { "ArgValue": "off", "ArgName": "tls13" }, { "ArgValue": "all", "ArgName": "ciphersuitegroup" } ], "functionName": "https_tls_version" }], "DomainNames": "example.com" }
开启TLS1.2、1.3，使用强加密算法套件。
{ "Functions": [{ "functionArgs": [ { "ArgValue": "off", "ArgName": "tls10" }, { "ArgValue": "off", "ArgName": "tls11" }, { "ArgValue": "on", "ArgName": "tls12" }, { "ArgValue": "on", "ArgName": "tls13" }, { "ArgValue": "strict", "ArgName": "ciphersuitegroup" } ], "functionName": "https_tls_version" }], "DomainNames": "example.com" }
开启TLS1.2、1.3，使用自定义加密算法套件。
{ "Functions": [{ "functionArgs": [ { "ArgValue": "off", "ArgName": "tls10" }, { "ArgValue": "off", "ArgName": "tls11" }, { "ArgValue": "on", "ArgName": "tls12" }, { "ArgValue": "on", "ArgName": "tls13" }, { "ArgValue": "custom", "ArgName": "ciphersuitegroup" }, { "ArgValue": "TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8,TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
