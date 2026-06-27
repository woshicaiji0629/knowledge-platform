### Windows系统
登录Logtail所在的机器。
调用telnet命令依次尝试连接上述地址。
telnet <project名>.cn-hangzhou-intranet.log.aliyuncs.com 80 # 如果是HTTPS协议，则端口号为443。
所有返回结果都为如下类似信息，说明网络畅通。
Trying 100*0*7*5... Connected to xxx. Escape character is '^]'.
如果网络不畅通，请检查网络环境中80和443端口是否已经开放、目标地址是否被拦截以及其他网络方面的检查（例如DNS配置、安全组等）。
