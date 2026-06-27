### Linux系统
登录Logtail所在的机器。
执行curl命令依次连接上述地址。
curl http://<project名>.cn-hangzhou-intranet.log.aliyuncs.com
所有返回结果都为如下类似信息，说明网络畅通。
{"Error":{"Code":"OLSInvalidMethod","Message":"The script name is invalid : /","RequestId":"5D****09"}}
如果网络不畅通，请检查网络环境中80和443端口是否已经开放、目标地址是否被拦截以及其他网络方面的检查（例如DNS配置、安全组等）。
