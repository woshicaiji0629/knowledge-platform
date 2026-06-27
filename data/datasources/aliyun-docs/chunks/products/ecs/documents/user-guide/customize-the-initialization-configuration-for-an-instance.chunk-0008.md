## Include文件
简介
通过Include文件指向一个或多个User-Data脚本或Cloud Config数据的链接，多个链接按行分隔。实例启动时，cloud-init会逐个解析并读取链接里的内容。如果在读取某一个链接的内容时出错，则停止读取剩余的链接。
说明
您可以通过阿里云对象存储OSS，上传User-Data脚本或Cloud Config数据、获取链接、设置链接有效期等。具体操作，请参见[OSS](../../../oss/documents/user-guide/console-quick-start.md)[控制台快速入门](../../../oss/documents/user-guide/console-quick-start.md)。
运行频率
启动实例：执行频率由链接里的内容决定。例如，链接的内容为User-Data脚本，则仅在实例首次启动时运行一次；脚本类型链接的内容为Cloud Config数据，则遵循Cloud Config数据的运行频率。
更换操作系统：自动运行。
重新初始化系统盘：自动运行。
重要
以下情况不会自动运行脚本：
如果更换操作系统使用的是自定义镜像且来源于原实例，更换操作系统时会判断实例不是初次启动，因此不会自动运行脚本。
如果创建使用的是自定义镜像，则创建实例时系统盘就有数据，初始化系统盘时会判断实例不是首次启动，因此不会自动运行脚本。
格式
首行为#include，且起始位置不能有空格。
Include文件示例
#include https://ecs-image-test.oss-cn-hangzhou.aliyuncs.com/userdata/myscript.sh
示例Include文件包含一个脚本链接，该脚本为User-Data脚本，则仅在实例首次启动时运行一次。
说明
如果您采用Include文件或Gzip压缩内容的方式，需要使用存储服务上传脚本、获取脚本链接、设置链接有效期等操作，推荐您使用阿里云对象存储OSS。具体操作，请参见[OSS](../../../oss/documents/user-guide/console-quick-start.md)[控制台快速入门](../../../oss/documents/user-guide/console-quick-start.md)。
