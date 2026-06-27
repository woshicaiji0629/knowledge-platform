## 附录4：设置Go代理
如果您使用的是中国地域的ECS，可能无法正常完成[步骤二](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)的编译流程，此时需要执行如下命令以便Go使用阿里云的代理，然后重新执行编译。
go env -w GO111MODULE=on go env -w GOPROXY=https://mirrors.aliyun.com/goproxy/,direct
说明
如果设置了上述代理后还是出现编译出错的情况，则可能是代理地址暂不可用造成的。此时可以在搜索引擎中搜索其他Go的代理地址来替换上述命令中的https://mirrors.aliyun.com/goproxy/,direct部分。推荐搜索关键词：Go代理。
