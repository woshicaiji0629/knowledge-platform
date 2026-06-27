## 通过nslookup命令验证
打开cmd程序（Windows）、终端（macOS/Linux）。
输入nslookup -type=CNAME加速域名（例如nslookup -type CNAME www.example.com），如果返回的解析结果和CDN控制台上该加速域名的CNAME值一致，则表示配置的CNAME已经生效。
~ % nslookup -type=CNAME www.example.com Server: 30.30.30.xxx Address: 30.30.30.xxx Non-authoritative answer: www.example.com canonical name = www.example.com.w.kunlun.com. Authoritative answers can be found from:
