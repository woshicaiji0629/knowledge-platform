## 数据安全与保护
数据存储在OSS上安全吗？
OSS本身是非常安全的。创建完成后，只有资源所有者才能访问其OSS资源。OSS提供用户身份验证，以控制对数据的访问。您可以使用各种访问控制策略，例如存储空间级别和文件级别的访问控制列表（ACL），选择性地向用户和用户组授予权限。OSS控制台会显示您可公开访问的存储空间。您可以将不希望公开访问的存储空间及文件设置为私有读写。如果您将私有读写的存储空间或文件的ACL设置为公共读或公共读写，则OSS会向您发出警告。关于OSS安全性的更多信息，请参见[OSS](user-guide/security-and-compliance-overview.md)[安全与合规白皮书](user-guide/security-and-compliance-overview.md)。
如何控制存储在OSS中数据的访问权限？
针对存放在Bucket的Object的访问，OSS提供了多种权限控制方式，包括ACL、RAM Policy和Bucket Policy。更多信息，请参见[权限与访问控制概述](user-guide/permissions-and-access-control-overview.md)。
OSS提供哪些数据加密的方式？
服务器端加密：上传文件时，OSS对收到的文件进行加密，再将得到的加密文件持久化保存；下载文件时，OSS自动将加密文件解密后返回给用户，并在返回的HTTP请求Header中，声明该文件进行了服务器端加密。更多信息，请参见[服务端加密](user-guide/server-side-encryption-8.md)。
客户端加密：将文件上传到OSS之前在本地进行加密。更多信息，请参见[客户端加密](user-guide/client-side-encryption.md)。
如何防止Bucket的数据被误删除或覆盖？
版本控制是针对存储空间（Bucket）级别的数据保护功能。开启版本控制后，针对数据的覆盖和删除操作将会以历史版本的形式保存下来。您在错误覆盖或者删除文件（Object）后，能够将Bucket中存储的Object恢复到任意时刻的历史版本。更多信息，请参见[版本控制](user-guide/overview-78.md)。
什么是合规保留策略？
OSS支持WORM（Write Once Read Many）特性，允许您以不可删除、不可篡改的方式保存和使用数据。用户可针对Bucket设置基于时间的合规保留策略。当策略锁定后，用户可以在Bucket中上传和读取Object，但是在Object的保留时间到期之前，任何用户都无法删除Object和策略。Object的保留时间到期后，才可以删除Object。
当您需要长期存储且不允许修改或删除重要数据时，例如医疗档案、技术文件、合同文书等，可以将此类数
