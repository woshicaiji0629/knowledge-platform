### macOS
输入配置命令。
ossutil config
根据提示设置配置文件路径。可以直接回车使用默认的配置文件路径。
Please enter the config file name,the file name can include path(default "/Users/user/.ossutilconfig", carriage return will use the default file. If you specified this option to other file, you should specify --config-file option to the file when you use other commands):
ossutil默认使用/Users/user/.ossutilconfig作为配置文件。
根据提示分别设置AccessKey ID、AccessKey Secret、地域ID信息。
输入创建的AccessKey ID。
Please enter Access Key ID [****************id]:yourAccessKeyID
输入创建的AccessKey Secret。
Please enter Access Key Secret [****************sk]:yourAccessKeySecret
输入OSS的数据中心所在的地域，如无任何输入，默认值为cn-hangzhou。
Please enter Region [cn-hangzhou]:cn-hangzhou
输入OSS的数据中心的Endpoint，如果不需要自定义 Endpoint，可以直接按回车跳过该参数的配置。
在上一步配置完地域信息后，将默认使用该地域 ID 对应的外网 Endpoint。例如，如果设置的region-id为cn-hangzhou，默认使用的外网 Endpoint 是https://oss-cn-hangzhou.aliyuncs.com。
如果需要自定义 OSS 数据中心所在地域的 Endpoint，请输入 Endpoint 信息。例如，如果希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint如https://oss-cn-hangzhou-internal.aliyuncs.com。
Please enter Endpoint (optional, use public endpoint by default) [None]: https://oss-cn-hangzhou-internal.aliyuncs.com
参数说明如下：
