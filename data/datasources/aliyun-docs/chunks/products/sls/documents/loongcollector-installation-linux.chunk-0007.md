### 同账号不同地域
当服务器为阿里云ECS，且ECS与Project属于同一个阿里云账号，但不属于同一个[地域](loongcollector-installation-linux.md)，此时需要手动下载安装包，并在安装命令中使用[公网传输方式或传输加速](loongcollector-installation-linux.md)。
具体操作如下：
下载安装包：在服务器上执行下载命令，示例代码中${region_id}可使用cn-hangzhou替换，若想加快安装包下载速度，请参考[RegionID](loongcollector-installation-linux.md)替换${region_id}为ECS所属地域。
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh -O loongcollector.sh;
选择传输方式并执行安装命令：替换${region_id}为Project所属地域的[RegionID](loongcollector-installation-linux.md)。
公网：适用于大多数场景，常见于跨地域或其他云/自建服务器，但受带宽限制且可能不稳定。
chmod +x loongcollector.sh; ./loongcollector.sh install ${region_id}-internet
传输加速：用于跨地域（如中国内地到海外），通过CDN加速提升性能，避免公网延迟高，传输不稳定问题，但流量需额外计费。
需要先打开Project的[日志跨域传输加速](manage-a-project.md)功能，再执行安装命令。chmod +x loongcollector.sh; ./loongcollector.sh install ${region_id}-acceleration
查看启动状态：执行命令，返回loongcollector is running表示启动成功。
sudo /etc/init.d/loongcollectord status
配置机器组：日志服务通过机器组发现用户自定义标识并与主机上的LoongCollector建立心跳连接。
在服务器上将自定义字符串user-defined-test-1写入用户自定义标识文件，该字符串将在后续步骤中使用。
#向指定文件写入自定义字符串，若目录不存在需手动创建。文件路径和名称由日志服务固定，不可自定义。 echo "user-defined-test-1" > /etc/ilogtail/user_defined_id
登录[日志服务控制台](ht
