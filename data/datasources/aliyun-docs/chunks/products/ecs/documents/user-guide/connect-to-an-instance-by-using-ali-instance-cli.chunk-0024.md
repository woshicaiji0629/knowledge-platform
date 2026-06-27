## 本机为Windows
进入命令提示符，在ali-instance-cli.exe所在目录，输入命令远程连接实例。其中<instance_id>为步骤2.1中获取的实例ID。
ali-instance-cli.exe session --instance <instance_id>
例如连接实例ID为i-bp1******的实例时，可输入以下命令完成连接操作。
ali-instance-cli.exe session --instance i-bp1******
如图所示，连接成功后，会进入对应实例的命令行界面。
