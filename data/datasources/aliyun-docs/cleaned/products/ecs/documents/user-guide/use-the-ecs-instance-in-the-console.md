# 控制台购买Linux实例并搭建Wordpress网站-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/use-the-ecs-instance-in-the-console

# 控制台购买Linux实例并搭建Wordpress网站
WordPress 是一款主流的开源建站工具。使用 ECS 部署WordPress 后，可以快速搭建网站并发布文章。
## 操作步骤
请保证[账号已完成实名认证](https://help.aliyun.com/zh/account/ali-cloud-account-registration-process)，且阿里云账户余额（即现金余额）与代金券的总额不低于100.00元人民币的情况下执行以下操作。
重要
完成实名认证的云服务器ECS新用户，可免费试用ECS 3个月，详细限制参见[云服务器](ecs-free-trial.md)[ECS](ecs-free-trial.md)[试用攻略](ecs-free-trial.md)。
### 步骤一：创建ECS实例
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，单击创建实例。
选择自定义购买，完成购买配置。
配置示例值可供参考，未提及配置项按照默认即可。
| 配置项 | 配置示例值 |
| --- | --- |
| 付费类型 | 按量付费 |
| 地域 | 华南 2（河源） |
| 网络及可用区 | 专有网络：默认专有网络 交换机：选择可用区 B 的默认交换机。 |
| 实例 | ecs.c9i.large 为保证流畅运行，建议实例规格不低于 2 vCPU 4 GiB。 |
| 镜像 | 选择公共镜像下 Alibaba Cloud Linux 3.2104 LTS 64 位。 |
| 系统盘 | 类型：ESSD 云盘 容量：40 GiB |
| 公网 IP | 勾选 分配公网 IPv4 地址 。 |
| 带宽计费模式 | 按使用流量 建议 升级至 CDT 计费 ，升级后赠送 220GB/月公网流量（中国内地地域 20GB/月，非中国内地 200GB/月）。 |
| 安全组 | 选择 新建安全组 ，在 普通安全组 的 开通 IPv4 端口/协议 处，新增勾选 HTTP (TCP：80) 和 SSH (TCP:22) ，允许外部 HTTP 访问。 |
| 登录凭证 | 选择 创建后设置 。 |
确认配置费用，阅读并勾选服务协议，单击确认下单。
### 步骤二：连接ECS实例
返回实例列表，待实例状态为运行中，且健康状态为正常后，单击操作列的远程连接。
在对话框中，单击通过Workbench远程连接对应的立即登录。
选择免密连接后，单击登录。
远程连接会话最久维持6个小时，如果超过6小时没有任何操作，连接会自动断开，需要重新连接。
看到命令行即表示连接成功。
### 步骤三：搭建WordPress
部署 LNMP 环境。
执行以下脚本一键部署 Wordpress 所需的 LNMP 环境（Linux + Nginx + MySQL + PHP）。执行前将MYSQL_PASSWORD替换为自定义的MySQL root密码 ，后续搭建 Wordpress 数据库时需要使用。
密码长度须为8至30个字符，且必须同时包含大小写英文字母、数字和特殊符号，其中特殊符号包含()` ~!@#$%^&*-+=|{}[]:;‘<>,.?/。curl -fsSL https://help-static-aliyun-doc.aliyuncs.com/install-script/deploy-lnmp-acl3_2.sh | MYSQL_ROOT_PASS='MYSQL_PASSWORD' bash脚本仅适用于Alibaba Cloud Linux 3.2104 LTS 64位。
登录 MySQL，创建 WordPress 专用数据库和用户。
MYSQL_PASSWORD：填写为[上一步](use-the-ecs-instance-in-the-console.md)设置的MySQL密码。
WORDPRESS_PASSWORD：自定义WordPress的用户密码。
密码长度须为8至30个字符，且必须同时包含大小写英文字母、数字和特殊符号，其中特殊符号包含()` ~!@#$%^&*-+=|{}[]:;‘<>,.?/。
mysql -u root -p'MYSQL_PASSWORD' <<EOF CREATE DATABASE wordpress; CREATE USER 'wordpress_user'@'localhost' IDENTIFIED BY 'WORDPRESS_PASSWORD'; GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress_user'@'localhost'; FLUSH PRIVILEGES; EOF
指令将创建一个名为wordpress的数据库和一个具有该数据库全部权限的wordpress_user用户。
下载并解压 WordPress。
cd /usr/share/nginx/html && sudo wget https://cn.wordpress.org/wordpress-6.4.4-zh_CN.zip && sudo yum install unzip -y && sudo unzip wordpress-6.4.4-zh_CN.zip
配置数据库连接。
备份默认配置。
sudo cp /usr/share/nginx/html/wordpress/wp-config-sample.php /usr/share/nginx/html/wordpress/wp-config.php
编辑wp-config.php，将WORDPRESS_PASSWORD替换为设置的[WordPress 用户密码](use-the-ecs-instance-in-the-console.md)。
sudo sed -i "s/database_name_here/wordpress/" /usr/share/nginx/html/wordpress/wp-config.php && \sudo sed -i "s/username_here/wordpress_user/" /usr/share/nginx/html/wordpress/wp-config.php && \sudo sed -i "s/password_here/WORDPRESS_PASSWORD/" /usr/share/nginx/html/wordpress/wp-config.php
更新 Nginx 站点根目录并重启。
sudo sed -i 's|root /usr/share/nginx/html;|root /usr/share/nginx/html/wordpress;|' /etc/nginx/conf.d/default.conf && sudo nginx -t && sudo systemctl restart nginx
### 步骤四：安装WordPress并发布第一篇文章
安装并登录Wordpress。
在本地浏览器中访问http://<ECS公网IP>，进入 WordPress 安装页面。
<ECS公网IP地址>可在实例列表的IP地址列获取。
填写站点标题、管理员用户名、密码和邮箱，单击安装WordPress。
安装完成后，单击登录，输入上一步设置的用户名和密码。
发布文章验证访问。
在左侧导航栏，单击文章>新增文章。
输入标题（如"Hello from Alibaba Cloud ECS"），单击右上角发布，在确认弹窗中再次单击发布。
复制并打开文章地址，页面显示刚才发布的文章，表示网站已对外可用。
## 计费说明
### 计费项
系统盘容量费用：40 GiB（云盘容量） × 云盘单价 × 计费时长。
公网带宽计费（按流量计费）：出网流量 x 每 GB 流量单价。
[升级至](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt#5c4c3530f9bu4)[CDT](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt#5c4c3530f9bu4)[计费](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt#5c4c3530f9bu4)后，将赠送220GB/月公网流量 （中国内地地域20GB/月，非中国内地200GB/月）。
实例规格的计算资源费用：实例规格单价 × 计费时长。
可通过[配置报价器](https://www.aliyun.com/price/cpq/?sheetId=2202605207553099534)查看价格明细。
### 获取费用明细
登录[费用与成本控制台](https://billing-cost.console.aliyun.com/home)，选择账单>账单详情。在产品名称筛选框中选择产品名称云服务器ECS，获取费用明细。
## 资源清理
使用完毕后可释放实例，停止计费。
重要
释放后数据不可恢复。
在实例列表，单击目标实例操作列下的>实例状态>释放。
选择立即释放，单击下一步。
确认无即将保留的关联资源信息后，单击确认。
## 相关文档
创建实例时的安全组配置默认允许所有IP访问，存在安全风险，建议[修改安全组规则](start-using-security-groups.md)，仅保留必要IP的访问权限。
[重置实例登录密码](reset-the-logon-password-of-an-instance.md)
[ECS](../quick-reference.md)[常用操作导航](../quick-reference.md)
[搭建](manually-build-an-ftp-site-on-a-linux-instance.md)[FTP](manually-build-an-ftp-site-on-a-linux-instance.md)[站点（Linux）](manually-build-an-ftp-site-on-a-linux-instance.md)上传WordPress主题或者插件。
直接使用IP地址访问网站不专业且不安全，建议为网站[绑定域名并启用](manually-build-a-wordpress-website-on-a-centos-7-ecs-instance.md)[HTTPS](manually-build-a-wordpress-website-on-a-centos-7-ecs-instance.md)[加密](manually-build-a-wordpress-website-on-a-centos-7-ecs-instance.md)。
[手动部署](deploy-the-lnmp-environment.md)[LNMP](deploy-the-lnmp-environment.md)[环境](deploy-the-lnmp-environment.md)。
若实例规格无法满足应用需求，可以[变更实例规格](change-the-instance-type-of-a-pay-as-you-go-instance.md)。
通过ROS，云市场镜像或Terraform[快速搭建](quickly-build-a-wordpress-website.md)[WordPress](quickly-build-a-wordpress-website.md)。
[在](install-and-use-docker.md)[Docker](install-and-use-docker.md)[中部署](install-and-use-docker.md)[WordPress](install-and-use-docker.md)。
在宝塔面板中安装WordPress，请参见[手动部署宝塔面板](deploy-bt-panel-for-linux.md)。
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
