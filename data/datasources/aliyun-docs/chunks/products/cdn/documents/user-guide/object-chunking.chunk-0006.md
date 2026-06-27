## HTTP Range超出有效区间的兼容性配置
CDN回源OSS源站获取大文件的场景下，如果OSS响应了cache-control:no-cache不缓存策略，或者客户端请求访问CDN触发Range请求回源OSS时，可能会出现异常，具体表现为：下载异常缓慢甚至超时（30秒左右）、下载至超Range片时触发连接中断（如文件末尾的最后一片）。
未设置兼容策略情况下的行为
如果HTTP Range请求合法，响应返回值为206并在响应头中包含Content-Range。如果HTTP Range请求不合法，或者指定范围不在有效区间，会导致Range不生效，响应返回值为200，并传送整个Object内容。如下为HTTP Range请求不合法的示例及错误说明。
说明
此处假设Object资源大小为1000字节，Range有效区间为0~999。为避免指定的Range超出范围，可在Range读取前进行[HeadObject](../../../oss/documents/developer-reference/headobject.md)请求，获取对象大小。
Range: byte=0-499：格式错误，byte应为bytes。
Range: bytes=0-1000：末字节1000超出有效区间。
Range: bytes=1000-2000：指定范围超出有效区间。
Range: bytes=1000-：首字节超出有效区间。
Range: bytes=-2000：指定范围超出有效区间。
可以通过如下命令测试Range参数的有效性：
curl -r 0-100 http://xxxx.oss-cn-hangzhou.aliyuncs.com/xx.zip -o /tmp/xx1.zip -v
设置兼容策略以后的行为
使用HTTP Range时，增加请求头x-oss-range-behavior:standard，可以改变指定范围不在有效区间时OSS的行为。行为改变的示例如下：
说明
此处假设Object资源大小为1000字节，Range有效区间为0~999。如通过HTTP Range请求获取大文件的部分内容时，因选取了无效的范围，导致OSS返回InvalidRange错误码，请参见[OSS](../../../oss/documents/user-guide/http-status-code-416.md)[返回](../../../oss/documents/user-guide/http-status-code-416.md)[416](../../../oss/documents/user-guide/http-status-code-416.md)[错误](../../../oss/documents/user-guide/http-status-code-416.
