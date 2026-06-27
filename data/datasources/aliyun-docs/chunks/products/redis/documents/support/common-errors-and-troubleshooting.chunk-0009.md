### NOAUTH Authentication required
可能原因：Tair实例设置了密码鉴权，但客户端没有提供密码或提供了错误的密码。
解决方法：请使用正确的账号密码进行访问，更多信息请参见[实例的登录方式](../user-guide/logon-methods.md)。
说明
若您使用Lettuce 6.4.0.RELEASE至6.4.1.RELEASE版本的客户端，即使提供了正确密码，仍可能会出现该报错。该问题是由于Lettuce在支持Client setinfo时引入的，并已在6.4.2.RELEASE版本中修复，详情请参见[redis/lettuce#3035](https://github.com/redis/lettuce/pull/3035)。
如遇到该问题，您可以选择[手动切换](common-errors-and-troubleshooting.md)[RESP](common-errors-and-troubleshooting.md)[协议为](common-errors-and-troubleshooting.md)[RESP2](common-errors-and-troubleshooting.md)，或者将客户端升级至Lettuce 6.4.2.RELEASE版本及以上，如果您仍在使用Spring Data Redis客户端，建议使用Spring Data Redis 3.4.2及以上版本。
