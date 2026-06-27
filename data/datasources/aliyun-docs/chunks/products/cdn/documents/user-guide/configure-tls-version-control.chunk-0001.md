## 背景信息
TLS（Transport Layer Security）即安全传输层协议，在两个通信应用程序之间提供保密性和数据完整性，最典型的应用就是HTTPS。HTTPS即HTTP over TLS，就是更安全的HTTP，运行在HTTP层之下，TCP层之上，为HTTP层提供数据加解密服务。

| 协议 | 说明 | 支持的主流浏览器 |
| --- | --- | --- |
| TLSv1.0 | RFC2246，1999 年发布，基于 SSLv3.0，该版本易受各种攻击（如 BEAST 和 POODLE），除此之外，支持较弱加密，对当今网络连接的安全已失去应有的保护效力。不符合 PCI DSS 合规判定标准。 | IE6+ Chrome 1+ Firefox 2+ |
| TLSv1.1 | RFC4346，2006 年发布，修复 TLSv1.0 若干漏洞。 | IE 11+ Chrome 22+ Firefox 24+ Safri 7+ |
| TLSv1.2 | RFC5246，2008 年发布，是目前广泛使用的版本。 | IE 11+ Chrome 30+ Firefox 27+ Safri 7+ |
| TLSv1.3 | RFC8446，2018 年发布，最新的 TLS 版本，支持 0-RTT 模式（更快），只支持完全前向安全性密钥交换算法（更安全）。 | Chrome 70+ Firefox 63+ |
