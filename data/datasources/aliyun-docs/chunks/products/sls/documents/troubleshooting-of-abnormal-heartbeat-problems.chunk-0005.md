## 用户自定义标识
确认服务器上是否存在/etc/ilogtail/user_defined_id文件，若不存在请创建。
向该文件中写入自定义的字符串作为用户自定义标识，此处以user-defined-test-1为例。
#向指定文件写入自定义字符串 echo "user-defined-test-1" > /etc/ilogtail/user_defined_id
修改用户自定义标识的取值为自定义的字符串，此例为user-defined-test-1。
