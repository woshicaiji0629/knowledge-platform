爬虫拦截：用于快速拦截所有搜索引擎的Bots，可结合[合法](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#458e1fa445hit)[Bot](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#458e1fa445hit)[管理](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#458e1fa445hit)控制仅放行执行搜索引擎Bots。
针对已知Bots库：
[爬虫威胁情报库](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#8da0dac6f4aod)：来自阿里云针对已识别到的恶意 Bots 建立的攻击源 IP 地址库，建议您开启滑块校验应对它们。
[IDC](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#8da0dac6f4aod)[黑名单封禁](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#8da0dac6f4aod)：如果您的用户客户端不会来自公有云或 IDC 的机房，可以在IDC黑名单封禁中直接设置阻断 IDC的请求。
针对需要判别的请求：
[Bot](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#c3e848838dn9g)[特征识别](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#c3e848838dn9g)：对比真实的用户浏览器访问特征来识别非浏览器类 Bots。
[Bot](https://help.a
