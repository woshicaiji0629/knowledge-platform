## OSS重要特性
版本控制
版本控制是针对存储空间（Bucket）级别的数据保护功能。开启版本控制后，针对数据的覆盖和删除操作将会以历史版本的形式保存下来。您在错误覆盖或者删除文件（Object）后，能够将Bucket中存储的Object恢复到任意时刻的历史版本。更多信息，请参见[版本控制概述](overview-78.md)。
Bucket Policy
Bucket拥有者可通过Bucket Policy授权不同用户以何种权限访问指定的OSS资源。例如您需要进行跨账号或对匿名用户授权访问或管理整个Bucket或Bucket内的部分资源，或者需要对同账号下的不同RAM用户授予访问或管理Bucket资源的不同权限，例如只读、读写或完全控制的权限等。关于配置Bucket Policy的具体操作，请参见[通过](../configure-bucket-policies-to-authorize-other-users-to-access-oss-resources.md)[Bucket Policy](../configure-bucket-policies-to-authorize-other-users-to-access-oss-resources.md)[授权用户访问指定资源](../configure-bucket-policies-to-authorize-other-users-to-access-oss-resources.md)。
跨区域复制
跨区域复制（Cross-Region Replication）是跨不同OSS数据中心（地域）的Bucket自动、异步（近实时）复制Object，它会将Object的创建、更新和删除等操作从源存储空间复制到不同区域的目标存储空间。跨区域复制功能满足Bucket跨区域容灾或用户数据复制的需求。更多信息，请参见[跨区域复制概述](cross-region-replication-overview.md)。
数据加密
服务器端加密：上传文件时，OSS对收到的文件进行加密，再将得到的加密文件持久化保存；下载文件时，OSS自动将加密文件解密后返回给用户，并在返回的HTTP请求Header中，声明该文件进行了服务器端加密。更多信息，请参见[服务器端加密](server-side-encryption-8.md)。
客户端加密：将文件上传到OSS之前在本地进行加密。更多信息，请参见[客户端加密](client-side-encryption.md)。
数据永久保存
除以下情况以外，OSS默认永久保存上传到Bucket的数据：
通过OSS控制台、API、SDK、ossutil或者ossbrowser等工具手动删除数据。更多信息，请参见[删除文件](delete-objects-18.md)。
通过生命周期规则在指定时间内
