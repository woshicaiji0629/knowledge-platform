### 阿里云配置CNAME方法
如果您的DNS服务商是阿里云，您可以根据以下步骤完成CNAME配置。
使用加速域名所在的阿里云账号，登录[云解析](https://dns.console.aliyun.com)[DNS](https://dns.console.aliyun.com)[控制台](https://dns.console.aliyun.com)
在公网权威解析页面，找到加速域名的主域名example.com，并单击右侧的解析设置。
单击添加记录，添加CNAME记录。
记录类型选择CNAME。
主机记录输入www，解析请求来源选择默认，记录值输入CNAME地址（例如www.example.com.w.kunlun.com），TTL保持默认10分钟，然后单击确定。
重要
主机记录就是域名的前缀。www.example.com的主机记录是www；如果您的加速域名就是主域名example.com，那么对应的主机记录填写@。
对于同一个主机名，CNAME记录和A记录是相互冲突，只能有一个存在。如果您要加速的域名存在相同主机记录的A记录，需要将A记录暂停或删除，才能配置CNAME记录。
暂停A记录，配置CNAME的时候，会导致域名短暂的不可访问，为减少对您域名的影响，请根据您日常流量的变化情况，在合适的时间进行配置。
单击确认，完成添加。
