## 工作原理
[CNAME](what-is-a-dns-cname-record.md)[记录](what-is-a-dns-cname-record.md)，即Canonical Name Record，直译成中文就是"规范的名称记录"。其核心是利用DNS的别名机制。将一个域名映射到另一个域名。工作流程如下：
用户访问www.example.com，用户的本地DNS解析器向公共DNS系统查询www.example.com的IP地址。
云解析DNS查询www.example.com的DNS记录，发现其为CNAME记录，指向www.example.com.w.kunlunsl.com。
云解析DNS继续查询www.example.com.w.kunlunsl.com的A记录（IP地址）。
CDN的DNS调度系统接收到解析请求，根据用户的地理位置、网络状况和节点负载，动态地返回一个最优CDN边缘节点的IP地址。
用户最终通过步骤4的IP地址与CDN边缘节点建立连接，并从节点获取缓存内容或由节点回源获取内容。
