在服务器上通过sudo /etc/init.d/loongcollectord status查看LoongCollector启动状态，返回loongcollector is running表示启动成功。否则执行如下命令启动LoongCollector：
若使用的是Logtail采集器，则查看Logtail启动状态命令为：sudo /etc/init.d/ilogtaild status，启动Logtail命令为：sudo /etc/init.d/ilogtaild start。sudo /etc/init.d/loongcollectord start
若是跨账号场景（Project所属阿里云账号与服务器所属账号不同）：需手动配置用户ID文件，使该账号有权限访问、采集这台服务器的日志。
检查用户ID文件内容
请检查是否存在/etc/ilogtail/users/{阿里云账号ID}文件，若不存在请创建。
登录[日志服务控制台](https://sls.console.aliyun.com/)，鼠标悬浮在右上角用户头像上，在弹出的标签页中查看并复制账号ID。注意需要复制主账号ID。
在安装了LoongCollector的服务器上，以主账号ID作为文件名，创建用户ID文件。
touch /etc/ilogtail/users/{阿里云账号ID} #以主账号ID作为文件名，无需配置文件后缀。
检查文件名是否满足下列要求，不满足请修改。
{阿里云账号ID}必须为主账号ID。
{阿里云账号ID}应为日志服务Project所属的主账号ID，而非服务器所属的账号。
确认地域与传输方式正确，并能联通访问域名：查看服务器上/usr/local/ilogtail/ilogtail_config.json文件中region信息是否与日志服务Project地域的[RegionID](loongcollector-installation-linux.md)一致。一致则排查下一步，若不一致则修改：
测试访问域名联通性并修改服务器配置
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表中，单击目标Project。
单击Project名称右侧的进入项目概览页面。
在访问域名中可查看当前Project的域名信息，替换${project名称}为Project名称，${域名信息}为公网域名后在服务器上执行命令。
curl https://${project名称}.${域名信息}
返回类似信息{"Error":{"Code":"OLSInvalidMethod","Message":"The script name is invalid : /","RequestId":"5D****09"}}，说明网络畅通。否则检查目标地址是否被拦截以及
