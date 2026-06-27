## 什么是AccessKey
访问密钥AccessKey（简称AK）是阿里云提供给用户的永久访问凭据，由AccessKey ID和AccessKey Secret组成的一组密钥对。
AccessKey ID：用于标识用户。
AccessKey Secret：是一个用于验证您拥有该AccessKey ID的密码。
AccessKey ID和AccessKey Secret根据算法由访问控制（RAM）生成，阿里云对AccessKey ID和AccessKey Secret的存储及传输均进行加密。
AccessKey不用于控制台登录，而是用于通过开发工具（API、CLI、SDK、Terraform等）访问阿里云时，发起的请求会携带AccessKey ID和AccessKey Secret加密请求内容生成的签名，进行身份验证及请求合法性校验。
