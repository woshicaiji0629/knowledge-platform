### 编码和解码函数

| 函数 | 说明 | 过滤器 | 示例 |
| --- | --- | --- | --- |
| base64_encoding(value) | 对输入值进行 Base64 编码。 | 支持 | {{ base64_encoding("foo") }} 的结果为 Zm9v。 |
| base64_decoding(value) | 对输入值进行 Base64 解码。 | 支持 | {{ base64_decoding("Zm9v") }} 的结果为 foo。 |
| md5_encoding(value) | 对输入值进行 MD5 编码。 | 支持 | {{ md5_encoding("foo") }} 的结果为 acbd18db4cc2f85cedef654fccc4a4d8。 |
| url_encoding(value) | 对输入值进行 URL 编码。 | 支持 | {{ url_encoding("https://example.com?a=b&c=d") }} 的结果为 https%3A%2F%2Fexample.com%3Fa%3Db%26c%3Dd。 |
| url_decoding(value) | 对输入值进行 URL 解码。 | 支持 | {{ url_decoding("https%3A%2F%2Fexample.com%3Fa%3Db%26c%3Dd") }} 的结果为 https://example.com?a=b&c=d。 |
