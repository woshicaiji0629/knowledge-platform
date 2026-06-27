on-control.md)[TLS](../user-guide/configure-tls-version-control.md)[版本与加密套件](../user-guide/configure-tls-version-control.md)。
功能ID（FunctionID/FuncId）：110。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| tls10 | String | 否 | 是否开启 TLSv1.0： on（默认）：开启。 off：关闭。 | on |
| tls11 | String | 否 | 是否开启 TLSv1.1： on（默认）：开启。 off：关闭。 | on |
| tls12 | String | 否 | 是否开启 TLSv1.2： on（默认）：开启。 off：关闭。 | on |
| tls13 | String | 否 | 是否开启 TLSv1.3： on（默认）：开启。 off：关闭。 | on |
| ciphersuitegroup | String | 否 | 加密算法套件组： all（默认）：全部加密算法套件。 strict：强加密算法套件。 custom：自定义加密算法套件。 | all |
|  | String | 否 | 加密算法套件，配合 ciphersuitegroup 参数（自定义加密算法套件）使用，可以配置多个加密算法套件，中间用英文逗号分隔。 | TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 |
