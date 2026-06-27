# 查询文件-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/query-objects

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/oss/documents/user-guide.md)

- [开发参考](products/oss/documents/developer-reference.md)

- [产品计费](products/oss/documents/billing.md)

- [常见问题](products/oss/documents/oss-faq.md)

- [动态与公告](products/oss/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 查询文件

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以使用SelectObject对目标文件执行SQL语句，返回执行结果。

说明

无地域属性的存储空间不支持使用SelectObject。

## 背景信息

目前Hadoop 3.0已经支持OSS在EMR上运行Spark、Hive、Presto等服务，同时阿里云MaxCompute以及Data Lake Analytics均支持从OSS直接处理数据。

OSS提供的GetObject接口决定了大数据平台只能把OSS数据全部下载到本地然后进行分析过滤，在很多查询场景下浪费了大量带宽和客户端资源。

SelectObject接口通过将条件和Projection下推到OSS层，只返回有用数据，减少带宽和处理量，节省CPU和内存资源，使基于OSS的数据分析更具吸引力。

## 费用说明

调用SelectObject接口查询数据时，按扫描的原文件实际大小计费。更多信息，请参见[数据处理费用](products/oss/documents/data-processing-fees.md)。

## 支持的文件类型

以下内容是对SelectObject支持的文件类型、支持的SQL语法等的详细介绍。

- 

RFC 4180标准的CSV（包括TSV等类CSV文件，行列分隔符和Quote字符可自定义）。

- 

JSON文件（UTF-8编码），支持DOCUMENT和LINES两种格式：。

- 

DOCUMENT是指整个文件是单一的JSON对象。

- 

LINES表示整个文件由多行JSON对象组成，每一行是一个JSON对象（但整个文件本身并不是一个合法的JSON对象），行间以换行符分隔（支持\\n，\\r\\n等，无需用户指定）。

- 

标准存储和低频访问存储类型的文件。归档、冷归档和深度冷归档存储类型文件需先执行解冻操作。

- 

OSS完全托管加密和KMS托管主密钥加密的文件。

## 支持的SQL语法

- 

SQL语句： Select From Where

- 

数据类型：string、int（64bit）、double（64bit）, decimal（128bit） 、timestamp、bool

- 

操作： 逻辑条件（AND,OR,NOT)， 算术表达式（+-*/%)， 比较操作（>,=, <, >=, <=, !=），String 操作 (LIKE, || )

重要

LIKE模糊匹配时对字母大小写敏感。

## 支持的数据类型

OSS中的CSV数据默认是String类型，您可以使用CAST函数进行数据转换。

通过SQL查询语句将_1和_2转换为int的示例：Select * from OSSOBject where cast (_1 as int) > cast(_2 as int)

SelectObject支持在Where条件中隐式转换，例如下面语句中的第一列和第二列将被转换成int：

Select _1 from ossobject where _1 + _2 > 100

对于JSON文件，若SQL中未指定cast函数，其类型根据JSON数据的实际类型而定，标准JSON内建的数据类型包括null、bool、int64、double、string等类型。

## 常见的SQL用例

常见的SQL用例包括CSV及JSON两种。

- 

CSV

| 应用场景 | SQL 语句 |
| --- | --- |
| 返回前 10 行数据 | select * from ossobject limit 10 |
| 返回第 1 列和第 3 列的整数，并且第 1 列大于第 3 列 | select _1, _3 from ossobject where cast(_1 as int) > cast(_3 as int) |
| 返回第 1 列以'陈'开头的记录的个数（注：此处 like 后的中文需要用 UTF-8 编码） | select count(*) from ossobject where _1 like '陈%' |
| 返回所有第 2 列时间大于 2018-08-09 11:30:25 且第 3 列大于 200 的记录 | select * from ossobject where _2 > cast('2018-08-09 11:30:25' as timestamp) and _3 > 200 |
| 返回第 2 列浮点数的平均值，总和，最大值，最小值 | select AVG(cast(_6 as double)), SUM(cast(_6 as double)), MAX(cast(_6 as double)), MIN(cast(_6 as double)) from ossobject |
| 返回第 1 列和第 3 列连接的字符串中以'Tom'为开头以’Anderson‘结尾的所有记录 | select * from ossobject where (_1 || _3) like 'Tom%Anderson' |
| 返回第 1 列能被 3 整除的所有记录 | select * from ossobject where (_1 % 3) = 0 |
| 返回第 1 列大小在 1995 到 2012 之间的所有记录 | select * from ossobject where _1 between 1995 and 2012 |
| 返回第 5 列值为 N,M,G,L 的所有记录 | select * from ossobject where _5 in ('N', 'M', 'G', 'L') |
| 返回第 2 列乘以第 3 列比第 5 列大 100 以上的所有记录 | select * from ossobject where _2 * _3 > _5 + 100 |


- 

JSON

假设JSON文件如下：

{ "contacts":[ { "firstName": "John", "lastName": "Smith", "isAlive": true, "age": 27, "address": { "streetAddress": "21 2nd Street", "city": "New York", "state": "NY", "postalCode": "10021-3100" }, "phoneNumbers": [ { "type": "home", "number": "212 555-1234" }, { "type": "office", "number": "646 555-4567" }, { "type": "mobile", "number": "123 456-7890" } ], "children": [], "spouse": null }，…… #此处省略其他类似的节点 ]}

SQL用例如下：

| 应用场景 | SQL 语句 |
| --- | --- |
| 返回所有 age 是 27 的记录 | select * from ossobject.contacts[*] s where s.age = 27 |
| 返回所有的家庭电话 | select s.number from ossobject.contacts[*].phoneNumbers[*] s where s.type = "home" |
| 返回所有单身的记录 | select * from ossobject s where s.spouse is null |
| 返回所有没有孩子的记录 | select * from ossobject s where s.children[0] is null 说明 目前没有专用的空数组的表示方法，用以上语句代替。 |


## 使用场景

SelectObject通常用于大文件分片查询、JSON文件查询、日志文件分析等场景。

- 

大文件分片查询

和GetObject提供的基于Byte的分片下载类似，SelectObject也提供了分片查询的机制，包括以下两种分片方式：

- 

按行分片：常用的分片方式，然而对于稀疏数据来说，按行分片可能会导致分片时负载不均衡。

- 

按Split分片：Split是OSS用于分片的一个概念，一个Split包含多行数据，每个Split的数据大小大致相等。

说明

按Split分片比按行分片更加高效。

如果确定CSV文件列中不包含换行符，则基于Bytes的分片由于不需要创建Meta，其使用更为简便。如果列中包含换行符或者是JSON文件时，则使用以下步骤：

- 

调用CreateSelectObjectMeta API获得该文件的总的Split数。如果该文件需要用SelectObject，则建议在查询前异步调用该接口，以节省扫描时间。

- 

根据客户端资源情况选择合适的并发度n，用总的Split数除以并发度n得到每个分片查询应该包含的Split个数。

- 

在请求Body中用诸如split-range=1-20的形式进行分片查询。

- 

合并结果。

- 

JSON文件查询

查询JSON文件时，在SQL的From语句中尽可能缩小From后的JSON Path范围。

如下是JSON文件示例：

{ "contacts":[ { "firstName": "John", "lastName": "Smith", "address": { "streetAddress": "21 2nd Street", "city": "New York", "state": "NY", "postalCode": "10021-3100" }, "phoneNumbers": [ { "type": "home", "number": "212 555-1234" }, { "type": "office", "number": "646 555-4567" }, { "type": "mobile", "number": "123 456-7890" } ] } ]}

如果要查找所有postalCode为10021开头的streetAddress，SQL可以写为select s.address.streetAddress from ossobject.contacts[*] s where s.address.postalCode like '10021%'或者select s.streetAddress from ossobject.contacts[*].address s where s.postalCode like '10021%'

由于select s.streetAddress from ossobject.contacts[*].address s where s.postalCode like '10021%'的JSON Path更加精确，因此性能更优。

- 

在JSON文件中处理高精度浮点数

在JSON文件中需要进行高精度浮点数的数值计算时，建议设置ParseJsonNumberAsString选项为true, 同时将该值cast成Decimal。比如一个属性a值为123456789.123456789，用select s.a from ossobject s where cast(s.a as decimal) > 123456789.12345就可以保持原始数据的精度不丢失。

## 操作方式

### 使用OSS控制台

重要

通过控制台仅支持从128 MB以下的文件中提取40 MB以下的数据记录。

- 

登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。

- 

单击Bucket 列表，然后单击目标Bucket名称。

- 

在左侧导航栏，选择文件管理>文件列表。

- 

在目标文件右侧的操作栏下，选择>选取内容。

- 

在选取内容面板，按以下说明设置各项参数。

| 参数 | 说明 |
| --- | --- |
| 文件类型 | 仅支持 CSV 和 JSON 两种文件类型。 |
| 分隔符 | 仅适用于 CSV 文件。请选择半角逗号（,）或自定义分隔符。 |
| 标题行 | 仅适用于 CSV 文件。请选择文件第一行是否包含列标题。 |
| JSON 格式符 | 仅适用于 JSON 文件。请选择您的 JSON 文件对应的格式。 |
| 压缩格式 | 选择您当前的文件是否为压缩文件。目前压缩文件仅支持 GZIP 文件。 |


- 

单击显示文件预览。

重要

预览标准存储类型文件时，会产生Select扫描费用。预览低频访问、归档存储、冷归档存储或者深度冷归档存储类型文件时，会产生Select扫描费用和数据取回费用。更多信息，请参见[数据处理费用](products/oss/documents/data-processing-fees.md)。

- 

单击下一步，输入SQL语句并执行。

假设名为People的CSV文件有3列数据，分别是姓名、公司和年龄。

- 

如果想查找年龄大于50岁，并且名字以Lora开头的人（其中_1,_2,_3是列索引，代表第一列、第二列、第三列），可以执行以下SQL语句：

select * from ossobject where _1 like 'Lora*' and _3 > 50

- 

如果想统计这个文件有多少行，最大年龄与最小年龄是多少，可以执行以下SQL语句：

select count(*), max(cast(_3 as int)), min(cast(_3 as int)) from ossobject

- 

查看执行结果。

您还可以单击下载，将所选取的内容下载到本地。

### 使用阿里云SDK

当前仅支持通过Java SDK和Python SDK查询文件。

Java

import com.aliyun.oss.ClientBuilderConfiguration; import com.aliyun.oss.common.comm.SignVersion; import com.aliyun.oss.model.*; import com.aliyun.oss.OSS; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.OSSClientBuilder; import java.io.BufferedReader; import java.io.ByteArrayInputStream; import java.io.InputStreamReader; /** * Examples of create select object metadata and select object. * */ public class SelectObjectSample { // yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。 private static String endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 填写Bucket名称，例如examplebucket。 private static String bucketName = "examplebucket"; public static void main(String[] args) throws Exception { // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider(); // 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou。 String region = "cn-hangzhou"; // 创建OSSClient实例。 // 当OSSClient实例不再使用时，调用shutdown方法以释放资源。 ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration(); clientBuilderConfiguration.setSignatureVersion(SignVersion.V4); OSS ossClient = OSSClientBuilder.create() .endpoint(endpoint) .credentialsProvider(credentialsProvider) .clientConfiguration(clientBuilderConfiguration) .region(region) .build(); // 填写Object完整路径后，根据SELECT语句查询文件中的数据。Object完整路径中不能包含Bucket名称。 // 填写CSV格式的Object完整路径。 selectCsvSample("test.csv", ossClient); // 填写JSON格式的Object完整路径。 selectJsonSample("test.json", ossClient); ossClient.shutdown(); } private static void selectCsvSample(String key, OSS ossClient) throws Exception { // 填写上传的内容。 String content = "name,school,company,age\r\n" + "Lora Francis,School A,Staples Inc,27\r\n" + "Eleanor Little,School B,\"Conectiv, Inc\",43\r\n" + "Rosie Hughes,School C,Western Gas Resources Inc,44\r\n" + "Lawrence Ross,School D,MetLife Inc.,24"; ossClient.putObject(bucketName, key, new ByteArrayInputStream(content.getBytes())); SelectObjectMetadata selectObjectMetadata = ossClient.createSelectObjectMetadata( new CreateSelectObjectMetadataRequest(bucketName, key) .withInputSerialization( new InputSerialization().withCsvInputFormat( // 填写内容中不同记录之间的分隔符，例如\r\n。 new CSVFormat().withHeaderInfo(CSVFormat.Header.Use).withRecordDelimiter("\r\n")))); System.out.println(selectObjectMetadata.getCsvObjectMetadata().getTotalLines()); System.out.println(selectObjectMetadata.getCsvObjectMetadata().getSplits()); SelectObjectRequest selectObjectRequest = new SelectObjectRequest(bucketName, key) .withInputSerialization( new InputSerialization().withCsvInputFormat( new CSVFormat().withHeaderInfo(CSVFormat.Header.Use).withRecordDelimiter("\r\n"))) .withOutputSerialization(new OutputSerialization().withCsvOutputFormat(new CSVFormat())); // 使用SELECT语句查询第4列，值大于40的所有记录。 selectObjectRequest.setExpression("select * from ossobject where _4 > 40"); OSSObject ossObject = ossClient.selectObject(selectObjectRequest); // 读取内容。 BufferedReader reader = new BufferedReader(new InputStreamReader(ossObject.getObjectContent())); while (true) { String line = reader.readLine(); if (line == null) { break; } System.out.println(line); } reader.close(); ossClient.deleteObject(bucketName, key); } private static void selectJsonSample(String key, OSS ossClient) throws Exception { // 填写上传的内容。 final String content = "{\n" + "\t\"name\": \"Lora Francis\",\n" + "\t\"age\": 27,\n" + "\t\"company\": \"Staples Inc\"\n" + "}\n" + "{\n" + "\t\"name\": \"Eleanor Little\",\n" + "\t\"age\": 43,\n" + "\t\"company\": \"Conectiv, Inc\"\n" + "}\n" + "{\n" + "\t\"name\": \"Rosie Hughes\",\n" + "\t\"age\": 44,\n" + "\t\"company\": \"Western Gas Resources Inc\"\n" + "}\n" + "{\n" + "\t\"name\": \"Lawrence Ross\",\n" + "\t\"age\": 24,\n" + "\t\"company\": \"MetLife Inc.\"\n" + "}"; ossClient.putObject(bucketName, key, new ByteArrayInputStream(content.getBytes())); SelectObjectRequest selectObjectRequest = new SelectObjectRequest(bucketName, key) .withInputSerialization(new InputSerialization() .withCompressionType(CompressionType.NONE) .withJsonInputFormat(new JsonFormat().withJsonType(JsonType.LINES))) .withOutputSerialization(new OutputSerialization() .withCrcEnabled(true) .withJsonOutputFormat(new JsonFormat())) .withExpression("select * from ossobject as s where s.age > 40"); // 使用SELECT语句查询文件中的数据。 OSSObject ossObject = ossClient.selectObject(selectObjectRequest); // 读取内容。 BufferedReader reader = new BufferedReader(new InputStreamReader(ossObject.getObjectContent())); while (true) { String line = reader.readLine(); if (line == null) { break; } System.out.println(line); } reader.close(); ossClient.deleteObject(bucketName, key); } }

Python

import oss2 from oss2.credentials import EnvironmentVariableCredentialsProvider def select_call_back(consumed_bytes, total_bytes = None): print('Consumed Bytes:' + str(consumed_bytes) + '\n') # 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 auth = oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider()) # 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。 endpoint = "https://oss-cn-hangzhou.aliyuncs.com" # 填写Endpoint对应的Region信息，例如cn-hangzhou。注意，v4签名下，必须填写该参数 region = "cn-hangzhou" # yourBucketName填写存储空间名称。 bucket = oss2.Bucket(auth, endpoint, "yourBucketName", region=region) key ='python_select.csv' content ='Tom Hanks,USA,45\r\n'*1024 filename ='python_select.csv' # 上传CSV文件。 bucket.put_object(key, content) # Select API的参数。 csv_meta_params = {'RecordDelimiter': '\r\n'} select_csv_params = {'CsvHeaderInfo': 'None', 'RecordDelimiter': '\r\n', 'LineRange': (500, 1000)} csv_header = bucket.create_select_object_meta(key, csv_meta_params) print(csv_header.rows) print(csv_header.splits) result = bucket.select_object(key, "select * from ossobject where _3 > 44", select_call_back, select_csv_params) select_content = result.read() print(select_content) result = bucket.select_object_to_file(key, filename, "select * from ossobject where _3 > 44", select_call_back, select_csv_params) bucket.delete_object(key) ###JSON DOCUMENT key = 'python_select.json' content = "{\"contacts\":[{\"key1\":1,\"key2\":\"hello world1\"},{\"key1\":2,\"key2\":\"hello world2\"}]}" filename = 'python_select.json' # 上传JSON DOCUMENT。 bucket.put_object(key, content) select_json_params = {'Json_Type': 'DOCUMENT'} result = bucket.select_object(key, "select s.key2 from ossobject.contacts[*] s where s.key1 = 1", None, select_json_params) select_content = result.read() print(select_content) result = bucket.select_object_to_file(key, filename, "select s.key2 from ossobject.contacts[*] s where s.key1 = 1", None, select_json_params) bucket.delete_object(key) ###JSON LINES key = 'python_select_lines.json' content = "{\"key1\":1,\"key2\":\"hello world1\"}\n{\"key1\":2,\"key2\":\"hello world2\"}" filename = 'python_select.json' # 上传JSON LINE。 bucket.put_object(key, content) select_json_params = {'Json_Type': 'LINES'} json_header = bucket.create_select_object_meta(key,select_json_params) print(json_header.rows) print(json_header.splits) result = bucket.select_object(key, "select s.key2 from ossobject s where s.key1 = 1", None, select_json_params) select_content = result.read() print(select_content) result = bucket.select_object_to_file(key, filename, "select s.key2 from ossobject s where s.key1 = 1", None, select_json_params) bucket.delete_object(key)

package main import ( "context" "flag" "io" "log" "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss" "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials" ) // 定义全局变量 var ( region string // 存储区域 bucketName string // 存储空间名称 objectName string // 对象名称 ) // init函数用于初始化命令行参数 func init() { flag.StringVar(&region, "region", "", "The region in which the bucket is located.") flag.StringVar(&bucketName, "bucket", "", "The name of the bucket.") flag.StringVar(&objectName, "object", "", "The name of the object.") } func main() { // 解析命令行参数 flag.Parse() // 检查bucket名称是否为空 if len(bucketName) == 0 { flag.PrintDefaults() log.Fatalf("invalid parameters, bucket name required") } // 检查region是否为空 if len(region) == 0 { flag.PrintDefaults() log.Fatalf("invalid parameters, region required") } // 检查object名称是否为空 if len(objectName) == 0 { flag.PrintDefaults() log.Fatalf("invalid parameters, object name required") } // 加载默认配置并设置凭证提供者和区域 cfg := oss.LoadDefaultConfig(). WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()). WithRegion(region) // 创建OSS客户端 client := oss.NewClient(cfg) // 创建选择对象的请求 request := &oss.SelectObjectRequest{ Bucket: oss.Ptr(bucketName), // 存储空间名称 Key: oss.Ptr(objectName), // 对象名称 SelectRequest: &oss.SelectRequest{ Expression: oss.Ptr("select * from ossobject limit 10"), // 定义SQL查询表达式，查询对象中的前10行数据 InputSerializationSelect: oss.InputSerializationSelect{ CsvBodyInput: &oss.CSVSelectInput{ FileHeaderInfo: oss.Ptr("Use"), }, }, OutputSerializationSelect: oss.OutputSerializationSelect{ OutputHeader: oss.Ptr(true), }, }, } // 执行选择对象的请求 result, err := client.SelectObject(context.TODO(), request) if err != nil { log.Fatalf("failed to select object %v", err) } content, err := io.ReadAll(result.Body) if err != nil { log.Fatalf("failed to read object %v", err) } // 打印选择对象的结果 log.Printf("select object result:%#v\n", string(content)) }

### 使用命令行工具ossutil

您可以使用命令行工具ossutil来查询文件，ossutil的安装请参见[安装](products/oss/documents/install-ossutil2.md)[ossutil](products/oss/documents/install-ossutil2.md)。

以下命令用于为存储空间examplebucket中的exampleobject执行SQL语句，请求语法 CSV。

ossutil api select-object --bucket examplebucket --key exampleobject --select-request "{\"Expression\":\"c2VsZWN0IFllYXIsU3RhdGVBYmJyLCBDaXR5TmFtZSwgU2hvcnRfUXVlc3Rpb25fVGV4dCBmcm9tIG9zc29iamVjdA==\",\"InputSerialization\":{\"CSV\":{\"FileHeaderInfo\":\"Use\",\"Range\":\"line-range=0-100\"}},\"OutputSerialization\":{\"JSON\":{\"RecordDelimiter\":\",\"}}}"

关于该命令的更多信息，请参见[select-object](products/oss/documents/developer-reference/select-object.md)。

## 相关API

以上操作方式底层基于API实现，如果您的程序自定义要求较高，您可以直接发起REST API请求。直接发起REST API请求需要手动编写代码计算签名。更多信息，请参见[SelectObject](products/oss/documents/developer-reference/selectobject.md)。

[上一篇：存储空间清单](products/oss/documents/user-guide/bucket-inventory.md)[下一篇：数据处理](products/oss/documents/user-guide/data-transformation.md)

该文章对您有帮助吗？

反馈

### 为什么选择阿里云

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)

### 大模型

[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)

### 产品和定价

[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)

### 技术内容

[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)

### 权益

[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)

### 服务

[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)

### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

联系我们：4008013260

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
