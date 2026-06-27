### CNAME记录
与A记录相比，CNAME记录保存的是域名和域名的映射关系，可以想象为给一个域名起了一个“外号”，这个“外号”和域名的映射关系就是通过CNAME记录保存的，而CNAME类型的记录值则可以通过A记录来映射到具体的服务器。
示例（示例数据仅供理解，不具有真实性）：
记录类型 域名 记录值 CNAME cname1.example.com www.example.com.w.kunlunsl.com A www.example.com.w.kunlunsl.com 10.10.10.10
当我们访问"cname1.example.com"这个域名的时候，DNS会通过CNAME记录获取到映射值"www.example.com.w.kunlunsl.com"，基于"www.example.com.w.kunlunsl.com"的A记录，"cname1.example.com"域名最终也会解析到IP地址"10.10.10.10"。
说明
在DNS的解析记录中，对于同一个主机名，A记录和CNAME记录是相互冲突的，两者不能同时存在。
