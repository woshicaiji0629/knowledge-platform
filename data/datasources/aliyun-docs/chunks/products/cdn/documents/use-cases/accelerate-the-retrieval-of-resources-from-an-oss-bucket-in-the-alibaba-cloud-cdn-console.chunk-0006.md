### 步骤四：配置 DNS 解析并验证生效
前往CDN 控制台的域名管理列表，找到之前添加的域名，复制域名对应的 CNAME 值（如果此处值为空，请稍等五秒之后刷新重试）。
使用加速域名所在的阿里云账号，登录[云解析 DNS 控制台](https://dnsnext.console.aliyun.com/overview?spm=5176.11785003.console-base_search-panel.dtab-product_dns.e7e4142fCBguns)，在公网权威解析页面找到目标域名并点击解析设置。
单击添加记录，创建一条 CNAME 记录：
记录类型：选择CNAME。
主机记录：填写子域名的前缀（例如www）。
记录值：粘贴从 CDN 控制台复制的 CNAME 值。
其他参数保持默认，然后单击 确认。
验证流量是否已切换至 CDN
配置 DNS 解析后，可通过以下方式确认流量已正确切换至 CDN：
使用curl -I检查响应头：在终端执行curl -I https://your-domain.com/file，观察响应头中的X-Cache字段。若返回X-Cache: HIT或X-Cache: MISS均表示请求经过 CDN；若未出现X-Cache字段，说明请求可能直接到达 OSS。
查看 CDN 控制台监控数据：登录 CDN 控制台，进入页面，检查该域名是否有流量数据。若配置生效后监控页面有数据，说明流量已通过 CDN。
检查 CNAME 状态：在 CDN 控制台，查看目标域名的 CNAME 状态是否为已配置。CNAME 状态有三种：已配置（绿色）、等待配置（黄色）、检测超时。
若域名同时解析到 OSS 和 CDN，请求可能绕过 CDN 直接访问 OSS，导致加速失效。请确保 DNS 解析中仅保留指向 CDN CNAME 的记录，删除任何直接指向 OSS 域名的 A 记录或 CNAME 记录。
