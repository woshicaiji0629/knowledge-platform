## 如何测试 CNAME 解析是否生效？
在CDN控制台完成CNAME配置后，使用nslookup或dig等查询工具验证。不推荐使用ping命令，其返回的解析信息可能不准确。
Windowsnslookup -type=CNAME <加速域名>
如果返回的结果和CDN提供的CNAME值相等，则证明CNAME解析生效。
Linux/Mac OS
在Linux或Mac OS系统的终端（Terminal）中，使用dig命令验证：
仅查询CNAME目标地址（推荐）：
dig +short <加速域名> CNAME
如果返回的结果和CDN提供的CNAME值相等，则证明CNAME解析生效。结果示例如下：
dig +short cdn.example.com CNAME cdn.example.com.w.alikunlun.com.
查询域名详细信息：
dig <加速域名> CNAME
如果ANSWER SECTION的CNAME值和CDN提供的CNAME值相等，则证明CNAME解析生效。
