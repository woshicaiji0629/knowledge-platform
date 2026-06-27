### 不同账号同地域
当服务器为阿里云ECS，且ECS与Project属于同一个[地域](loongcollector-installation-linux.md)，但不属于同一个阿里云账号时，需要手动下载安装包，并在安装命令中使用[内网传输方式](loongcollector-installation-linux.md)，且需要配置用户ID。
具体操作如下：
下载安装包：在服务器上执行下载命令，示例代码中${region_id}可使用cn-hangzhou替换，若想加快安装包下载速度，请参考[RegionID](loongcollector-installation-linux.md)替换${region_id}为ECS所属地域。
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh -O loongcollector.sh;
执行安装命令：${region_id}需替换为Project所属地域的[RegionID](loongcollector-installation-linux.md)。
若发生连接超时，可能是${region_id}替换错误，不同地域内网传输无法建立连接，因而超时。需修改后重新执行安装命令。chmod +x loongcollector.sh; ./loongcollector.sh install ${region_id}
查看启动状态：执行命令，返回loongcollector is running表示启动成功。
sudo /etc/init.d/loongcollectord status
配置用户ID：用户ID文件包含Project所属阿里云主账号的ID信息，用于标识该账号有权限访问、采集这台服务器的日志。
只有在采集非本账号ECS、自建服务器、其他云厂商服务器日志时需要配置用户ID。多个账号对同一台服务器进行日志采集时，支持在同一台服务器上创建多个用户ID文件。
登录[日志服务控制台](https://sls.console.aliyun.com/)，鼠标悬浮在右上角用户头像上，在弹出的标签页中查看并复制账号ID。注意需要复制主账号ID。
在安装了LoongCollector的服务器上，以主账号ID作为文件名，创建用户ID文件。
touch /etc/ilogtail/users/{阿里云账号ID} # 如果/etc/ilogtail/users目录不存在，请手动创建目录。用户ID文件只需配置文件名，无需配置文件后缀。
配置机器组：日志服务通过机器组发现用户自定义标识并与主机上的LoongCollector建立心
