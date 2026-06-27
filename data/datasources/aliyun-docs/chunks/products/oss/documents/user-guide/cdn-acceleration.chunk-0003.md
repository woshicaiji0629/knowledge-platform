### 步骤一：添加CDN加速域名并配置源站
前往[CDN](https://cdnnext.console.aliyun.com/domain/list)[控制台](https://cdnnext.console.aliyun.com/domain/list)，单击添加域名。
选择加速区域和业务类型，填写加速域名。加速域名支持主域名（如example.com）或自定义的子域名（如oss.example.com），建议使用子域名以便于管理和扩展。
单击新增源站信息，选择源站信息为OSS域名，并选择目标Bucket域名，单击确定，添加OSS源站。
单击下一步，完成CDN加速域名添加。
CDN加速域名添加完成后，可按照推荐配置的引导流程来添加缓存过期时间、Range回源、HTTPS证书等基础配置，或单击跳过，暂不配置，直接进入CNAME配置。
