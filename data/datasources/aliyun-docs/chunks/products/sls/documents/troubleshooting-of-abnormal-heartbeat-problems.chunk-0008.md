### 切换机器组标识类型后心跳FAIL
出现IP地址冲突或IP改变等情况时，不再适合使用IP型机器组，需切换为用户自定义标识型机器组。切换机器组类型并不影响网络联通情况，阿里云主账号信息，地域与传输方式等信息，因此仅需关注用户自定义标识取值是否正确。
确认是否存在/etc/ilogtail/user_defined_id文件，若不存在请创建。
向该文件中写入自定义的字符串作为用户自定义标识，此处以user-defined-test-1为例。
#向指定文件写入自定义字符串 echo "user-defined-test-1" > /etc/ilogtail/user_defined_id
登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表中，单击目标Project。
单击资源，单击机器组，在机器组中单击目标机器组。
查看机器组配置页面，并确认以下两项参数取值，若不正确请单击右上角修改，修改后保存。
机器组标识：用户自定义标识。
用户自定义标识：自定义的字符串，此例为user-defined-test-1。
