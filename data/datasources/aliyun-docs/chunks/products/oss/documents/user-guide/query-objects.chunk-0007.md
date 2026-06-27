## 使用场景
SelectObject通常用于大文件分片查询、JSON文件查询、日志文件分析等场景。
大文件分片查询
和GetObject提供的基于Byte的分片下载类似，SelectObject也提供了分片查询的机制，包括以下两种分片方式：
按行分片：常用的分片方式，然而对于稀疏数据来说，按行分片可能会导致分片时负载不均衡。
按Split分片：Split是OSS用于分片的一个概念，一个Split包含多行数据，每个Split的数据大小大致相等。
说明
按Split分片比按行分片更加高效。
如果确定CSV文件列中不包含换行符，则基于Bytes的分片由于不需要创建Meta，其使用更为简便。如果列中包含换行符或者是JSON文件时，则使用以下步骤：
调用CreateSelectObjectMeta API获得该文件的总的Split数。如果该文件需要用SelectObject，则建议在查询前异步调用该接口，以节省扫描时间。
根据客户端资源情况选择合适的并发度n，用总的Split数除以并发度n得到每个分片查询应该包含的Split个数。
在请求Body中用诸如split-range=1-20的形式进行分片查询。
合并结果。
JSON文件查询
查询JSON文件时，在SQL的From语句中尽可能缩小From后的JSON Path范围。
如下是JSON文件示例：
{ "contacts":[ { "firstName": "John", "lastName": "Smith", "address": { "streetAddress": "21 2nd Street", "city": "New York", "state": "NY", "postalCode": "10021-3100" }, "phoneNumbers": [ { "type": "home", "number": "212 555-1234" }, { "type": "office", "number": "646 555-4567" }, { "type": "mobile", "number": "123 456-7890" } ] } ]}
如果要查找所有postalCode为10021开头的streetAddress，SQL可以写为select s.address.streetAddress from ossobject.contacts[*] s where s.address.postalCode like '10021%'或者select s.streetAddress from ossobject.contacts[*].address s where s.postalCode like '10021%'
由于select s.streetAddress from ossobject
