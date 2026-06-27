### SCAN命令死循环或者返回数据为空
可能原因：SCAN命令返回的Cursor值可能超过了JavaScript最大可精确表达的数值[Number.MAX_SAFE_INTEGER](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)，导致Cursor不准确，引发死循环，更多信息请参见[redis/node-redis#2561](https://github.com/redis/node-redis/issues/2561)。
解决方案：将node-redis客户端升级至5.0.0及以上版本。
该文章对您有帮助吗？
反馈
