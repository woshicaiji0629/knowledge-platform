## 工作原理
OSS 按以下逻辑处理请求：
请求中携带x-oss-request-payer头，OSS 对请求者进行身份验证，验证通过后，流量和请求等费用由请求者承担。
请求中不携带x-oss-request-payer头：
请求者为 Bucket 拥有者：请求正常处理，所有费用由Bucket拥有者承担。
请求者非 Bucket 拥有者：请求被拒绝。
