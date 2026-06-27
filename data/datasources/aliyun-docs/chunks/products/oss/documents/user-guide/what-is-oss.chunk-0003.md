## OSS工作原理
数据以对象（Object）的形式存储在OSS的存储空间（Bucket ）中。如果要使用OSS存储数据，您需要先创建Bucket，并指定Bucket的地域、访问权限、存储类型等属性。创建Bucket后，您可以将数据以Object的形式上传到Bucket，并指定Object的文件名（Key）作为其唯一标识。
OSS以HTTP RESTful API的形式对外提供服务，访问不同地域需要不同的访问域名（Endpoint）。当您请求访问OSS时，OSS通过使用访问密钥（AccessKey ID和AccessKey Secret）对称加密的方法来验证某个请求的发送者身份。
Object操作在OSS上具有原子性和强一致性。
存储空间
存储空间是用户用于存储对象（Object）的容器，所有的对象都必须隶属于某个存储空间。存储空间具有各种配置属性，包括地域、访问权限、存储类型等。用户可以根据实际需求，创建不同类型的存储空间来存储不同的数据。
对象
对象是OSS存储数据的基本单元，也被称为OSS的文件。和传统的文件系统不同，对象没有文件目录层级结构的关系。对象由元数据（Object Meta）、用户数据（Data）和文件名（Key）组成，并且由存储空间内部唯一的Key来标识。对象元数据是一组键值对，表示了对象的一些属性，例如文件类型、编码方式等信息，同时用户也可以在元数据中存储一些自定义的信息。
对象名称
在各语言SDK中，ObjectKey、Key以及ObjectName是同一概念，均表示对Object执行相关操作时需要填写的Object名称。例如向某一存储空间上传Object时，ObjectKey表示上传的Object所在存储空间的完整名称，即包含文件后缀在内的完整路径，如填写为abc/efg/123.jpg。
地域
Region表示OSS的数据中心所在物理位置。用户可以根据费用、请求来源等选择合适的地域创建Bucket。一般来说，距离用户更近的Region访问速度更快。更多信息，请参见[OSS](regions-and-endpoints.md)[已经开通的](regions-and-endpoints.md)[Region](regions-and-endpoints.md)。
访问域名
Endpoint表示OSS对外服务的访问域名。OSS以HTTP RESTful API的形式对外提供服务，当访问不同的Region的时候，需要不同的域名。通过内网和外网访问同一个Region所需要的Endpoint也是不同的。例如杭州Region的外网Endpoint是oss-cn-hangzhou.aliyuncs.com，内网Endpoint是oss-cn-hangzhou-internal.aliyuncs.com。具体的内容请参见[各个](regions-
