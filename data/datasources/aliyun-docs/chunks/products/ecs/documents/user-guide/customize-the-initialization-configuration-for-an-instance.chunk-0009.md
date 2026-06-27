## Gzip压缩内容
简介
如果您的User-Data脚本、Cloud Config数据或Include文件内容的大小超过32 KB，可以采用Gzip压缩内容（.gz格式）并做成链接，然后以Include文件的形式输入。cloud-init会自动解压Gzip压缩内容，运行解压后内容的效果和直接传入后运行没有区别。
说明
您可以通过阿里云对象存储OSS，上传User-Data脚本或Cloud Config数据、获取链接、设置链接有效期等。具体操作，请参见[OSS](../../../oss/documents/user-guide/console-quick-start.md)[控制台快速入门](../../../oss/documents/user-guide/console-quick-start.md)。
运行频率
启动实例：由脚本类型和模块类型决定。例如，Gzip压缩内容链接的脚本类型为User-Data脚本，则仅在实例首次启动时运行一次。
更换操作系统：自动运行。
重新初始化系统盘：自动运行。
重要
以下情况不会自动运行脚本：
如果更换操作系统使用的是自定义镜像且来源于原实例，更换操作系统时会判断实例不是初次启动，因此不会自动运行脚本。
如果创建使用的是自定义镜像，则创建实例时系统盘就有数据，初始化系统盘时会判断实例不是首次启动，因此不会自动运行脚本。
格式
首行为#include，且起始位置不能有空格。
Gzip压缩内容示例
#include https://ecs-image-test.oss-cn-hangzhou.aliyuncs.com/userdata/myscript.gz
示例Gzip压缩内容表示Include文件包含一个Gzip压缩内容链接，cloud-init读取该Gzip压缩内容后会自动解压并运行，该Gzip压缩内容由User-Data脚本压缩得到，所以仅在实例首次启动时运行一次。
