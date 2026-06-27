## 步骤三：验证CNAME配置是否生效
重要
由于阿里云CDN校验域名的DNS解析记录的服务器部署在中国内地。如果您对域名做了分区域DNS解析配置，例如仅对域名的中国内地以外区域（中国香港、中国澳门、中国台湾、其他国家和地区）配置了阿里云CDN的CNAME地址，校验服务器将无法解析到该CNAME地址，且在CDN控制台该域名的CNAME状态会显示为待配置，这种情况不影响CDN的加速服务。
方法一：检查CDN控制台状态
前往阿里云CDN控制台的[域名管理列表](https://cdn.console.aliyun.com/domain/list)。
选择目标域名，将鼠标指向加速域名的CNAME状态处，状态为已配置时，则表示CNAME配置已生效。
说明
云解析DNS上新增CNAME记录实时生效，修改CNAME记录在10分钟后生效（具体生效时间长短取决于域名DNS解析配置的TTL时长，10分钟为TTL的默认时长），在此期间控制台中状态可能仍显示待配置，请忽略。
方法二：通过nslookup命令验证
打开cmd程序（Windows）、终端（macOS/Linux）。
输入nslookup -type=CNAME加速域名，如果返回的解析结果和CDN控制台上该加速域名的CNAME值一致，则表示CDN加速已经生效。例如：
nslookup -type=CNAME www.example.com
