# 如何采集企业内网服务器日志-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/how-do-i-collect-logs-from-servers-in-a-corporate-intranet

# 采集企业内网服务器日志
本文以Nginx为例，介绍配置正向代理服务器以及通过代理模式将企业内网服务器日志采集到日志服务的解决方案。
## 前提条件
已创建Project和LogStore。具体操作，请参见[管理](manage-a-project.md)[Project](manage-a-project.md)和[创建基础](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
已在服务器上安装Linux Logtail 1.5.0及以上版本或Window Logtail 1.5.0.0及以上版本。具体操作，请参见[安装](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)、[安装](install-logtail-on-a-windows-server.md)[Logtail（Windows](install-logtail-on-a-windows-server.md)[系统）](install-logtail-on-a-windows-server.md)。
## 背景信息
如果您的多台服务器部署在企业内网中且没有公网访问权限，但您希望将这些服务器的日志采集到日志服务进行查询与分析，您可以通过代理模式，由具备公网访问权限的内网服务器将其他内网服务器上的日志发送到日志服务。您可以通过任何方式将具备公网访问权限的内网服务器配置为正向代理服务器。
## 工作原理
Logtail与日志服务交互的数据主要包括管控数据、业务数据和监控数据。其中，管控数据包括Logtail配置下发及鉴权等信息。通信协议包括HTTP和HTTPS，默认使用HTTP协议发送业务数据和监控数据。因此，代理服务器必须能够同时代理HTTP协议数据和HTTPS协议数据。
Nginx是一款开源的高性能HTTP代理服务器，本身支持代理HTTP协议数据，但由于鉴权等原因并不能直接代理HTTPS协议数据。为此，需要为Nginx配置HTTPS补丁，从而使其能够代理HTTPS协议数据。
## 步骤一：配置代理服务器
使用Nginx将一台具有公网访问权限的企业内网服务器配置为正向代理服务器。
登录待配置为正向代理服务器的机器。
下载Nginx及HTTPS补丁。
下载HTTPS补丁。
git clone https://github.com/chobits/ngx_http_proxy_connect_module.git
下载并解压Nginx。
其中，${version}表示Nginx版本，请根据实际情况替换。最新版本，请参见[nginx: download](https://nginx.org/en/download.html)。
wget http://nginx.org/download/nginx-${version}.tar.gz tar -xzvf nginx-${version}.tar.gz cd nginx-${version}/
添加HTTPS补丁到Nginx。
其中，${patchfile}为文件路径，请根据Nginx版本选择对应的文件。更多信息，请参见[Select patch](https://github.com/chobits/ngx_http_proxy_connect_module/#select-patch)。
patch -p1 < ../ngx_http_proxy_connect_module/patch/${patchfile}.patch
安装Nginx。
./configure --add-module=../ngx_http_proxy_connect_module make && make install
在nginx.conf文件中添加如下配置。
其中，${代理服务器监听端口}和${DNS服务器地址}，请根据实际情况替换。
server { listen ${代理服务器监听端口}; resolver ${DNS服务器地址}; # 用于指定非HTTP请求的代理。 proxy_connect; proxy_connect_allow 443; proxy_connect_connect_timeout 10s; proxy_connect_data_timeout 10s; # 用于指定HTTP请求的代理。 location / { proxy_pass http://$host; proxy_set_header Host $host; } }
启动Nginx服务器。
## 步骤二：设置网络代理相关的环境变量
## Linux系统
您可以通过如下两种方案设置网络代理相关的环境变量。
| 方案 | 优点 | 缺点 | 使用场景 |
| --- | --- | --- | --- |
| 方案一 | 配置仅对 Logtail 进程生效，影响较小。 | 配置方式相对复杂。 | 适用于服务器使用者，对服务器整体网络情况不太了解。 |
| 方案二 | 配置方式简单。 | 配置对整台服务器生效，影响较大。 | 适用于服务器管理员，对服务器上所有进程的网络请求状况较为了解。 |
## 方案一
登录某台企业内网服务器。
打开/etc/init.d/ilogtaild文件，在start()函数中增加如下环境变量，然后保存文件。
关于环境变量的更多信息，请参见[附录：网络代理相关的环境变量](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)。
start() { cd $BIN_DIR umask $UMASK # 在$BIN_DIR/ilogtail前新增代理相关环境变量。 # 这里以ALL_PROXY为例，假设代理服务器地址为192.168.1.0，监听端口为9000。 # 内网服务器与代理服务器之间通过HTTP协议进行通信。 ALL_PROXY=http://192.168.1.0:9000 $BIN_DIR/ilogtail RETVAL=$? }
执行如下命令重启Logtail。
/etc/init.d/ilogtaild restart
重复执行步骤[1](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)~[3](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)，为其他内网服务器设置代理相关的环境变量。
## 方案二
重要
如果您需要对内网服务器上的所有网络请求进行代理，或者您仅需要对Logtail的网络请求进行代理，但您完全了解服务器上其他进程的网络请求发送地址，您可以考虑此方案。否则，请使用方案一。
登录某台企业内网服务器。
使用export命令在启动文件~/.bash_profile或/etc/profile中添加网络代理相关的环境变量。
关于环境变量的更多信息，请参见[附录：网络代理相关的环境变量](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)。
执行如下命令使环境变量生效。
此处，以~/.bash_profile启动文件为例。
source ~/.bash_profile
执行如下命令，重启Logtail。
/etc/init.d/ilogtaild restart
重复执行步骤[1](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)~[4](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)，为其他内网服务器配置代理相关的环境变量。
## Windows系统
打击运行窗口，输入regedit，然后单击确定。
在注册表编辑器窗口中，搜索计算机\HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\LogtailDaemon，然后单击LogtailDaemon。
单击右键，选择新建>多字符串值，然后命名该新值为Environment。
双击Environment，在数值数据文本框中，输入代理相关的环境变量，然后单击确定。
例如以ALL_PROXY为例，代理服务器地址为192.168.1.0，监听端口为9000，内网服务器与代理服务器之间通过HTTP协议进行通信。关于环境变量的更多信息，请参见[附录：网络代理相关的环境变量](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)。例如输入ALL_PROXY=http://192.168.1.0:9000。
打击运行窗口，输入services.msc，然后单击确定。
在服务窗口中，选择Logtail对应的服务。
如果是Logtail 0.x.x.x版本，选择LogtailWorker服务。
如果是Logtail 1.0.0.0及以上版本，选择LogtailDaemon服务。
单击右键，选择重新启动。
## 步骤三：验证网络
登录某台企业内网服务器。
执行如下命令。
下述命令中的${region}为目标Project所在地域，${project_name}为目标Project名称，请根据实际情况替换。
curl http://logtail.${region}.log.aliyuncs.com curl https://logtail.${region}.log.aliyuncs.com curl http://${project_name}.${region}.log.aliyuncs.com curl http://ali-${region}-sls-admin.${region}.log.aliyuncs.com
如果系统返回如下类似信息，表示网络正常。
{"Error":{"Code":"OLSInvalidMethod","Message":"The script name is invalid : /","RequestId":"62591BC7C08B7BD4AA99FCD4"}}
重复执行步骤[1](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)和[2](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)，验证其他企业内网服务器的网络。
## 附录：网络代理相关的环境变量
环境变量的配置说明如下：
重要
下述环境变量均支持小写模式，但优先级低于大写模式。
如果将HTTP和HTTPS协议数据全部发送给同一台代理服务器，可添加环境变量ALL_PROXY。
ALL_PROXY：${正向代理服务器的地址}
如果将HTTP和HTTPS协议数据分别发送至不同的代理服务器上，可添加环境变量HTTP_PROXY和HTTPS_PROXY。
HTTP_PROXY：${代理HTTP协议数据的服务器地址} HTTPS_PROXY：${代理HTTPS协议数据的服务器地址}
其中，代理服务器的地址需满足[协议://[用户名:密码@]]地址[:端口]格式。
协议（可选）：指定了当前服务器和代理服务器之间的通信协议，可设置为http、https或socks5。如果不设置，默认使用http。
用户名和密码（可选）：登录代理服务器的用户名和密码。
地址（必选）：代理服务器的IP地址。
端口（可选）：设置为您在nginx.conf文件中配置的代理服务器监听端口。更多信息，请参见配置代理服务器中的步骤[5](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)。如果不设置，默认使用80。
另外，您还可以额外增加NO_PROXY环境变量，该变量指定发往哪些地址的数据不需要经过代理服务器，多个地址之间可以用半角逗号（,）连接，支持的地址形式包括：
IP地址
域名（可以以半角句号（.）开头，支持匹配当前域名及其子域名。）
*（禁用代理服务器）
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
