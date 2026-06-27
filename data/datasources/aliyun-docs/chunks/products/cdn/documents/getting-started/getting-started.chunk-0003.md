### 阶段二：开通并配置CDN
[开通](../activate-alibaba-cloud-cdn.md)[CDN](../activate-alibaba-cloud-cdn.md)[服务](../activate-alibaba-cloud-cdn.md)。
[配置加速域名和源站](quick-access-to-alibaba-cloud-cdn.md)：
根据网站用户来选择合适的域名加速区域。

| 用户所在位置 | 加速效果 | 加速区域选择 |
| --- | --- | --- |
| 中国内地 | 全球用户访问均会调度至中国内地加速节点进行服务（海外地区和中国香港、中国澳门、中国台湾地区的访问流量将会被调度至华东电信的 CDN 节点）。 | 仅中国内地 |
| 海外地区+中国香港、中国澳门、中国台湾地区 | 全球用户访问会调度至中国内地以外的地区的 CDN 加速节点进行服务（中国内地用户将会被调度至日本、新加坡和中国香港的 CDN 节点）。 | 全球（不包含中国内地） |
| 全球 | 全球用户访问将会择优调度至最近的加速节点进行服务。 | 全球 |

若您的域名是首次添加到CDN控制台，则需要通过域名DNS解析来[验证域名归属权](quick-access-to-alibaba-cloud-cdn.md)，验证通过后您再次添加该域名或子域名时，无需再次验证。
配置源站信息，以便在阿里云CDN未缓存数据时，能够访问您的服务器以获取资源。
[配置](quick-access-to-alibaba-cloud-cdn.md)[HTTPS](quick-access-to-alibaba-cloud-cdn.md)[证书](quick-access-to-alibaba-cloud-cdn.md)：如果您的应用在配置阿里云CDN之前已经支持HTTPS访问或者您希望新域名可以支持HTTPS访问，请务必进行HTTPS证书的配置，否则您的域名将不会支持HTTPS访问。
如果您的域名之前就不支持HTTPS访问，并且暂时也不打算支持HTTPS访问，那么您可以直接跳过该配置。
[CDN](quick-access-to-alibaba-cloud-cdn.md)[安全防护和性能优化配置](quick-access-to-alibaba-cloud-cdn.md)：
恶意攻击或流量盗刷，都会导致突发的高带宽使用或大量数据传输，进而产生高额费用，因此，强烈建议您配置适当的安全防护措施以提前避免此类风险。
进行缓存过期时间、页面优化等功能的配置，可有效提升CDN的缓存命中率和访问性能，降低回源流量。
