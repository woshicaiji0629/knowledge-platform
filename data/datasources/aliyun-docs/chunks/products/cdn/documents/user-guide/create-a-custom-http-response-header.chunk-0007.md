| 响应头参数 | 说明 | 示例 |
| --- | --- | --- |
| 自定义 | 支持添加自定义响应头。自定义响应头名称要求如下： 由大小写字母、短划线和数字组成。 长度为 1~100 个字符。 | Test-Header |
| Cache-Control | 指定客户端程序请求和响应遵循的缓存机制。 | no-cache |
| Content-Disposition | 指定客户端程序把请求所得的内容存为一个文件时提供的默认的文件名。 | examplefile.txt |
| Content-Type | 指定客户端程序响应对象的内容类型。 | text/plain |
| Pragma | Pragma 是一个在 HTTP/1.0 中规定的通用首部，这个首部通常用于在服务器的响应中定义客户端对文件的缓存行为。 | no-cache |
| Access-Control-Allow-Origin | Access-Control-Allow-Origin 是 HTTP 响应头，用于指示哪些源可以访问资源。它是跨域资源共享（CORS, Cross-Origin Resource Sharing）机制的一部分，该机制允许服务器声明其资源是否可以被某个指定的源（域名）访问。该响应头的值支持以下类型： 通配符 * ：使用通配符表示允许任何源访问资源。这种方式非常宽松，适用于那些公开无需认证或授权即可访问的资源。不过，在生产环境中使用通配符时需要谨慎，因为它可能带来安全风险，比如跨站请求伪造攻击。 单个指定源 ：你可以指定一个具体的源（域名），表示仅允许该特定源访问资源。例如， http://example.com 或 https://api.example.com 。这要求请求必须来自指定的源，否则将被拒绝。 | * http://www.aliyun.com |
| Access-Control-Allow-Methods | 指定允许的跨域请求方法。多个方法用英文逗号 , 分隔。 | POST,GET |
| Access-Control-Allow-Headers | 指定允许的跨域请求字段。 | X-Custom-Header |
| Access-Control-Expose-Headers | 指定允许访问的自定义头信息。 | Content-Length |
| Access-Control-Allow-Credentials | 该响应头表示是否可以将对请求的响应暴露给页面。 返回 true：表示可以暴露。 返回其他值：表示不可以暴露。 | true |
| Access-Control-Max-Age | 指定客户端程序对特定资源的预请求返回结果的缓存时间，单位为秒。 | 600 |
| Content-Security-Po
