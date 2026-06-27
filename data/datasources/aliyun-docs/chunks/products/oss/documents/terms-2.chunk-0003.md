## Object类型
Object包含以下三种类型：
Normal
通过简单上传生成的Object。上传结束之后内容是固定的，只能读取，不能修改。如果Object内容发生了改变，只能重新上传同名的Object来覆盖之前的内容。简单上传适用于上传小于5 GB的单个文件、一次HTTP请求交互即可完成上传的场景。更多信息，请参见[简单上传](user-guide/simple-upload.md)。
Multipart
通过分片上传生成的Object。上传结束之后内容是固定的，只能读取，不能修改。如果Object内容发生了改变，只能重新上传同名的Object来覆盖之前的内容。分片上传适用于大文件加速上传、网络环境较差、文件大小不确定的场景。更多信息，请参见[分片上传](user-guide/multipart-upload.md)。
Appendable
通过追加上传生成的Object。追加上传可在视频数据产生之后即时将数据上传至同一个Object。追加上传适用于视频监控、视频直播等领域生成的实时视频流场景。更多信息，请参见[追加上传](user-guide/append-upload-11.md)。
重要
不支持在不同类型的Object之间相互转换。例如，Normal类型的Object无法转换为Multipart或者Appendable类型。
