### 3. 验证自定义数据运行效果
您需要结合自定义脚本的实际内容进行运行效果的验证，以下以在Linux实例中传入如下User-Data脚本为例，为您演示如何进行脚本运行效果验证。
#!/bin/sh echo "Hello World. The time is now $(date -R)!" | tee /root/userdata_test.txt
该示例中，User-Data脚本的效果是在实例首次启动时，向userdata_test.txt文件写入系统时间。为验证该脚本的执行效果，您可以运行cat userdata_test.txt命令来查看效果，系统已经向userdata_test.txt文件写入系统时间。
说明
当User-Data执行遇到问题时，可以通过云助手公共命令ACS-ECS-UserData-Check-for-linux.sh来获取失败相关的错误日志。如果返回有错误信息表示脚本执行有问题，如果没有返回错误信息表示执行没有报错，需要排查其他方面。关于云助手公共命令的更多信息，请参见[查看和执行公共命令](view-and-run-common-cloud-assistant-commands.md)。
