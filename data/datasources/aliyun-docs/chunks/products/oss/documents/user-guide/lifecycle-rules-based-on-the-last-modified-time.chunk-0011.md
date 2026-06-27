### 不同前缀
例如，某个Bucket包含以下Object：
logs/programl/log1.txt logs/program2/log2.txt logs/program3/log3.txt doc/readme.txt
如果生命周期规则指定的前缀是logs/，则仅作用于以logs/开头的Object；如果指定的前缀是doc/readme.txt，则仅作用于doc/readme.txt。
说明
您可以为生命周期规则指定中文前缀。
对过期策略匹配的Object执行GET或HEAD操作时，OSS会在响应Header中加入x-oss-expiration头。expiry-date表示Object的过期日期；rule-id表示相匹配的规则ID。
