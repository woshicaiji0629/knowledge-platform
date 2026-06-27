### 腾讯云配置CNAME方法
如果您的DNS服务商是腾讯云，您可以根据以下步骤完成CNAME配置。
登录DNSPod控制台。
在对应域名的域名解析页，单击添加记录，添加CNAME记录。

| 参数 | 说明 | 填写样例 |
| --- | --- | --- |
| 主机记录 | 加速域名为子域名的情况下，主机记录为子域名的前缀。 加速域名为泛域名的情况下，主机记录为 * 。 加速域名为根域名自身时，主机记录为 @ 。 | 子域名示例： 加速域名为 www.example.com ，主机记录为 www 。 加速域名为 www.example.aliyundoc.com ，主机记录为 www.example 。 泛域名示例： 加速域名为 .example.com ，主机记录为 * 。 加速域名为 *.example.aliyundoc.com ，主机记录为 *.example 。 根域名示例：根域名为 example.com 且配置加速域名为 example.com 时，主机记录填写 @ 。 说明 域名解析设置是针对您注册的域名（如 example.com ）或域名的左侧部分进行解析设置。配置主机记录时，您仅需要填写要解析的部分（如解析 www.example.com 时填写 www ）。 |
| 记录类型 | 选择 CNAME。 | CNAME |
| 线路类型 | 选择“默认”类型。 | 推荐保持默认 |
| 记录值 | 输入加速域名对应的 CNAME 记录值。 说明 一级域名（如 www.example.com ）和二级域名（如 www.example.aliyundoc.com ）对应的 CNAME 值不同。如果您要加速二级域名，需要将二级域名也添加到 CDN 上并解析到对应的 CNAME 记录值，或者在 CDN 上添加泛域名，泛域名的 CNAME 可以被二级域名使用。添加泛域名或二级域名，请参见 [添加加速域名](../add-a-domain-name.md) 。 | www.example.com.w.kunlunsl.com |
| 权重 | 无需填写。 | 不涉及 |
| MX | 无需填写。 | 不涉及 |
| TTL | TTL 为缓存时间，数值越小，修改记录后各地生效时间越快。 | 推荐保持默认 |

单击保存，完成添加。
验证配置的CNAME是否生效。
