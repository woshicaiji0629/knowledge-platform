## 步骤四：检查网络是否通畅
使用Logtail上传数据成功，至少需要保证Logtail所在服务器能够连通下列地址。
重要
如果使用内网，需要在<endpoint>后添加-intranet。
ilogtail_config.json文件中的config_server_address字段指定的地址及其HTTPS版本。
http://<project名>.<endpoint>。
Project的名称和地域，可以通过如下方式查看。
<endpoint>为ilogtail_config.json文件中data_server_list.endpoint字段指定的地址。
http://ali-<project地域>-sls-admin.<endpoint>。其中<endpoint>为ilogtail_config.json文件中data_server_list.endpoint字段指定的地址。
具体的网络检查及解决方法如下：
