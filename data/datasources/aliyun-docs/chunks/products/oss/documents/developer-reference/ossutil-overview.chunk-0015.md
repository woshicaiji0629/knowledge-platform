### 配置文件
可以利用配置文件（默认路径为~/.ossutilconfig，或通过-c选项指定自定义路径）配置ossutil。如果使用默认配置文件，则不需要额外指定配置文件路径。直接运行ossutil命令即可，例如：
ossutil ls oss://examplebucket
如果使用自定义配置文件路径，例如/path/yourconfig，则需要通过-c选项指定配置文件路径。例如：
ossutil -c /path/yourconfig ls oss://examplebucket
配置文件格式
配置文件采用INI格式结构，以节（section）和键值（key）构成，配置参数保存在指定的节里。这些配置按照节分成多个段，可以通过--profile使用某一个节的配置。 默认情况下，ossutil使用配置文件中的[default]设置。要使用其他设置，可以创建和引用其他配置。
节和键值对
配置文件中的每个节由方括号[ ]包围的名称标识，节内的设置项采用key=value形式。例如：
[default] accessKeyID = "your-access-key-id" accessKeySecret = "your-access-key-secret"
节中的设置项采用key=value形式。
节名和键值中的key不区分大小写。
配置参数的key支持多种格式，全小写、小驼峰、短划线（-）连接和下划线（_）连接，例如：accesskeyid、accessKeyId、access-key-id、access_key_id表示同一个参数名。
井号字符（#）开头的行表示注释行。
支持的节类型

| 节（Section）名称 | 说明 | 其它说明 |
| --- | --- | --- |
| [default] | 用于保存缺省设置，即当不设置--profile 选项时，使用该节里的配置。 | 为[profile default]简化形式。 |
| [profile name] | 用于配置参数，通过--profile name 来引用。 | 支持通过 source_profile 方式引用其它配置。 |
| [buckets name] | 针对具体 bucket 配置访问域名，包括 region、 endpoint 和 addressing style。 | 支持内联写法。 |

说明
可以使用config命令查看和设置配置内容。更多信息，请参见[config（管理配置文件）](config-create-configuration-file.md)。
节类型：profile
用于配置访问凭证和全局配置参数，支持的参数名如下：
访问凭证相关参数
