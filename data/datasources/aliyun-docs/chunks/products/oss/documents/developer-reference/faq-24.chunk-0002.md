rview-63.md)[发起请求](overview-63.md)。
比对响应体中的StringToSign字段与您发起请求的内容是否存在差异。
StringToSign字段表示待签字符串，即签名算法中需要使用AccessKey Secret进行加密的内容。
请求示例如下：
PUT /bucket/abc?acl Date: Wed, 24 May 2023 02:12:30 GMT Authorization: OSS qn6q**************:77Dv**************** x-oss-abc: mymeta
以上请求计算得到的待签字符串应为：
PUT\n\n\nWed, 24 May 2023 02:12:30 GMT\nx-oss-abc:mymeta\n/bucket/abc?acl
