# 分片上传-对象存储-阿里云

Source: https://help.aliyun.com/zh/oss/user-guide/multipart-upload

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

# 分片上传

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

大文件上传面临网络中断风险和传输时间过长的挑战。分片上传通过将文件分割为多个小分片并发传输，提供断点续传能力和传输性能优化，有效应对网络不稳定环境下的文件传输需求。

## 工作原理

分片上传将大文件分割为多个小分片进行独立处理，各分片独立传输和校验，单个分片失败时仅需重传该分片，避免重新上传整个文件。分片上传使用Upload ID作为任务标识符，确保所有分片正确归属于同一个上传任务。核心流程分为三个步骤：

- 

初始化上传任务：调用InitiateMultipartUpload接口创建分片上传任务，获取唯一的Upload ID作为后续操作的标识符。

- 

上传文件分片数据：将文件切分为多个分片（Part）并发上传，每个分片大小在100KB到5GB之间，支持断点续传。

- 

合并分片完成上传：调用CompleteMultipartUpload接口将所有分片按序号合并为完整的对象文件。

## 实现大文件分片上传

根据应用场景和技术要求，可选择图形化工具、命令行工具或SDK来实现分片上传功能。

说明

- 

OSS控制台暂不支持分片上传操作。

- 

支持上传加密的压缩文件，但不支持上传目录。

### 通过工具自动分片

对于日常开发、测试、运维或手动上传场景，推荐使用图形化或命令行工具，工具会自动处理分片逻辑，操作便捷。

- 

图形化管理工具ossbrowser

使用[图形化管理工具](products/oss/documents/developer-reference/ossbrowser-2-0-overview.md)[ossbrowser 2.0](products/oss/documents/developer-reference/ossbrowser-2-0-overview.md)上传文件时，默认启用分片上传机制，并提供可视化的上传进度和状态监控。

- 

命令行工具ossutil

使用[命令行工具](products/oss/documents/developer-reference/ossutil-overview.md)[ossutil 2.0](products/oss/documents/developer-reference/ossutil-overview.md)的[cp](products/oss/documents/developer-reference/cp-upload-file.md)命令上传文件时，工具会自动对超过100MiB的文件启用分片上传，提高大文件上传的成功率和传输效率。如需手动控制分片上传过程，可组合使用[initiate-multipart-upload](products/oss/documents/developer-reference/initiate-multipart-upload.md)、[upload-part](products/oss/documents/developer-reference/upload-part.md)和[complete-multipart-upload](products/oss/documents/developer-reference/complete-multipart-upload.md)命令。

ossutil cp example.zip oss://example-bucket

### 通过SDK编程实现分片

各语言SDK提供完整的分片上传接口封装，支持自定义分片大小、并发控制和错误处理。以下为常见语言的SDK分片上传示例，更多语言的使用示例请参见[SDK](products/oss/documents/developer-reference/sdk-code-samples.md)[参考](products/oss/documents/developer-reference/sdk-code-samples.md)中对应语言的示例代码。

运行代码前需安装对应语言的SDK并配置访问凭证环境变量，使用RAM用户或RAM角色时还需参考[API](products/oss/documents/user-guide/multipart-upload.md)[和权限说明](products/oss/documents/user-guide/multipart-upload.md)进行接口授权。

## Java SDK V2

import com.aliyun.sdk.service.oss2.OSSClient; import com.aliyun.sdk.service.oss2.credentials.CredentialsProvider; import com.aliyun.sdk.service.oss2.credentials.StaticCredentialsProvider; import com.aliyun.sdk.service.oss2.io.BoundedInputStream; import com.aliyun.sdk.service.oss2.models.*; import com.aliyun.sdk.service.oss2.transport.BinaryData; import java.io.File; import java.io.FileInputStream; import java.io.InputStream; import java.util.ArrayList; import java.util.List; /** * OSS分片上传示例 * 实现大文件的分片上传功能 */ public class MultipartUpload { public static void main(String[] args) { // 从环境变量获取访问凭证 String accessKeyId = System.getenv("OSS_ACCESS_KEY_ID"); String accessKeySecret = System.getenv("OSS_ACCESS_KEY_SECRET"); // 设置OSS地域和Endpoint String region = "cn-hangzhou"; String endpoint = "oss-cn-hangzhou.aliyuncs.com"; // 配置Bucket和文件信息 String bucket = "example-bucket"; String key = "dest.jpg"; String filePath = "dest.jpg"; // 创建凭证提供者 CredentialsProvider provider = new StaticCredentialsProvider(accessKeyId, accessKeySecret); // 初始化OSS客户端 OSSClient client = OSSClient.newBuilder() .credentialsProvider(provider) .region(region) .endpoint(endpoint) .build(); try { // 步骤1：初始化分片上传 InitiateMultipartUploadResult initiateResult = client.initiateMultipartUpload( InitiateMultipartUploadRequest.newBuilder() .bucket(bucket) .key(key) .build()); String uploadId = initiateResult.initiateMultipartUpload().uploadId(); System.out.printf("初始化分片上传成功，状态码:%d, 请求ID:%s, 上传ID:%s\n", initiateResult.statusCode(), initiateResult.requestId(), uploadId); // 步骤2：上传分片 File file = new File(filePath); long fileSize = file.length(); long partSize = 100 * 1024; // 每个分片100KB int partNumber = 1; List<Part> uploadParts = new ArrayList<>(); for (long start = 0; start < fileSize; start += partSize) { long curPartSize = Math.min(partSize, fileSize - start); // 读取文件分片并上传 try (InputStream is = new FileInputStream(file)) { is.skip(start); BoundedInputStream boundedInputStream = new BoundedInputStream(is, curPartSize); // 上传分片 UploadPartResult partResult = client.uploadPart(UploadPartRequest.newBuilder() .bucket(bucket) .key(key) .uploadId(uploadId) .partNumber((long) partNumber) .body(BinaryData.fromStream(boundedInputStream)) .build()); System.out.printf("状态码: %d, 请求ID: %s, 分片号: %d, ETag: %s\n", partResult.statusCode(), partResult.requestId(), partNumber, partResult.eTag()); uploadParts.add(Part.newBuilder() .partNumber((long) partNumber) .eTag(partResult.eTag()) .build()); } partNumber++; } // 步骤3：完成分片上传 uploadParts.sort((p1, p2) -> p1.partNumber().compareTo(p2.partNumber())); CompleteMultipartUpload completeMultipartUpload = CompleteMultipartUpload.newBuilder() .parts(uploadParts) .build(); CompleteMultipartUploadResult completeResult = client.completeMultipartUpload( CompleteMultipartUploadRequest.newBuilder() .bucket(bucket) .key(key) .uploadId(uploadId) .completeMultipartUpload(completeMultipartUpload) .build()); System.out.printf("完成分片上传，状态码:%d, 请求ID:%s, Bucket:%s, Key:%s, 位置:%s, ETag:%s\n", completeResult.statusCode(), completeResult.requestId(), completeResult.completeMultipartUpload().bucket(), completeResult.completeMultipartUpload().key(), completeResult.completeMultipartUpload().location(), completeResult.completeMultipartUpload().eTag()); } catch (Exception e) { System.out.printf("错误:\n%s", e); e.printStackTrace(); } finally { // 关闭客户端连接 try { client.close(); } catch (Exception e) { e.printStackTrace(); } } } }

## Java SDK V1

import com.aliyun.oss.*; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.common.comm.SignVersion; import com.aliyun.oss.model.*; import java.io.File; import java.io.FileInputStream; import java.io.InputStream; import java.util.ArrayList; import java.util.List; /** * OSS分片上传示例（V1 SDK） * 实现大文件的分片上传功能 */ public class MultipartUpload { public static void main(String[] args) { // 从环境变量获取访问凭证 String accessKeyId = System.getenv("OSS_ACCESS_KEY_ID"); String accessKeySecret = System.getenv("OSS_ACCESS_KEY_SECRET"); // 设置OSS地域和Endpoint String region = "cn-hangzhou"; String endpoint = "oss-cn-hangzhou.aliyuncs.com"; // 配置Bucket和文件信息 String bucketName = "example-bucket"; String objectName = "dest.jpg"; String filePath = "dest.jpg"; // 创建凭证提供者 DefaultCredentialProvider provider = new DefaultCredentialProvider(accessKeyId, accessKeySecret); // 配置客户端参数 ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration(); clientBuilderConfiguration.setSignatureVersion(SignVersion.V4); // 初始化OSS客户端 OSS ossClient = OSSClientBuilder.create() .credentialsProvider(provider) .clientConfiguration(clientBuilderConfiguration) .region(region) .endpoint(endpoint) .build(); try { // 步骤1：初始化分片上传 InitiateMultipartUploadRequest initiateRequest = new InitiateMultipartUploadRequest(bucketName, objectName); InitiateMultipartUploadResult initiateResult = ossClient.initiateMultipartUpload(initiateRequest); String uploadId = initiateResult.getUploadId(); System.out.printf("初始化分片上传成功，上传ID: %s\n", uploadId); // 步骤2：上传分片 File file = new File(filePath); long fileLength = file.length(); long partSize = 100 * 1024L; // 每个分片100KB // 计算分片数量 int partCount = (int) (fileLength / partSize); if (fileLength % partSize != 0) { partCount++; } // 保存已上传分片的ETag List<PartETag> partETags = new ArrayList<>(); // 遍历上传分片 for (int i = 0; i < partCount; i++) { long startPos = i * partSize; long curPartSize = (i + 1 == partCount) ? (fileLength - startPos) : partSize; // 创建分片上传请求 UploadPartRequest uploadPartRequest = new UploadPartRequest(); uploadPartRequest.setBucketName(bucketName); uploadPartRequest.setKey(objectName); uploadPartRequest.setUploadId(uploadId); uploadPartRequest.setPartNumber(i + 1); uploadPartRequest.setPartSize(curPartSize); // 读取文件分片并上传 try (InputStream instream = new FileInputStream(file)) { instream.skip(startPos); uploadPartRequest.setInputStream(instream); UploadPartResult uploadPartResult = ossClient.uploadPart(uploadPartRequest); partETags.add(uploadPartResult.getPartETag()); System.out.printf("上传分片 %d/%d 成功，ETag: %s\n", i + 1, partCount, uploadPartResult.getPartETag().getETag()); } } // 步骤3：完成分片上传 CompleteMultipartUploadRequest completeRequest = new CompleteMultipartUploadRequest( bucketName, objectName, uploadId, partETags); CompleteMultipartUploadResult completeResult = ossClient.completeMultipartUpload(completeRequest); System.out.printf("完成分片上传，ETag: %s\n", completeResult.getETag()); } catch (Exception e) { System.out.printf("错误: %s\n", e.getMessage()); e.printStackTrace(); } finally { // 关闭客户端连接 ossClient.shutdown(); } } }

## Python SDK V2

#!/usr/bin/env python3 # -*- coding: utf-8 -*- # OSS Python SDK V2 分片上传示例 # 实现大文件的分片上传功能 import alibabacloud_oss_v2 as oss import os def main(): # 从环境变量获取访问凭证 credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider() # 加载SDK的默认配置 config = oss.config.load_default() config.credentials_provider = credentials_provider # 设置OSS地域和Endpoint config.region = "cn-hangzhou" config.endpoint = "oss-cn-hangzhou.aliyuncs.com" # 初始化OSS客户端 client = oss.Client(config) # 配置Bucket和文件信息 bucket = "example-bucket" key = "dest.jpg" file_path = "dest.jpg" try: # 步骤1：初始化分片上传 initiate_result = client.initiate_multipart_upload( oss.InitiateMultipartUploadRequest( bucket=bucket, key=key )) upload_id = initiate_result.upload_id print(f"初始化分片上传成功，状态码:{initiate_result.status_code}, " f"请求ID:{initiate_result.request_id}, 上传ID:{upload_id}") # 步骤2：上传分片 file_size = os.path.getsize(file_path) part_size = 100 * 1024 # 每个分片100KB part_number = 1 upload_parts = [] offset = 0 with open(file_path, 'rb') as f: while offset < file_size: # 计算当前分片大小 current_part_size = min(part_size, file_size - offset) # 读取分片数据 f.seek(offset) part_data = f.read(current_part_size) # 上传分片 part_result = client.upload_part( oss.UploadPartRequest( bucket=bucket, key=key, upload_id=upload_id, part_number=part_number, body=part_data )) print(f"状态码: {part_result.status_code}, 请求ID: {part_result.request_id}, " f"分片号: {part_number}, ETag: {part_result.etag}") # 记录已上传的分片信息 upload_parts.append(oss.UploadPart( part_number=part_number, etag=part_result.etag )) offset += current_part_size part_number += 1 # 步骤3：完成分片上传 upload_parts.sort(key=lambda p: p.part_number) complete_result = client.complete_multipart_upload( oss.CompleteMultipartUploadRequest( bucket=bucket, key=key, upload_id=upload_id, complete_multipart_upload=oss.CompleteMultipartUpload( parts=upload_parts ) )) print(f"完成分片上传，状态码:{complete_result.status_code}, " f"请求ID:{complete_result.request_id}, " f"Bucket:{complete_result.bucket}, " f"Key:{complete_result.key}, " f"位置:{complete_result.location}, " f"ETag:{complete_result.etag}") except Exception as e: print(f"错误: {e}") raise if __name__ == "__main__": main()

## Python SDK V1

#!/usr/bin/env python3 # -*- coding: utf-8 -*- # OSS Python SDK V1 分片上传示例 # 实现大文件的分片上传功能 import os import oss2 from oss2.credentials import EnvironmentVariableCredentialsProvider from oss2 import SizedFileAdapter from oss2.models import PartInfo def main(): # 从环境变量获取访问凭证 auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider()) # 设置OSS地域和Endpoint region = "cn-hangzhou" endpoint = "oss-cn-hangzhou.aliyuncs.com" # 配置Bucket和文件信息 bucket_name = "example-bucket" key = "dest.jpg" file_path = "dest.jpg" # 初始化OSS Bucket bucket = oss2.Bucket(auth, endpoint, bucket_name, region=region) try: # 步骤1：初始化分片上传 upload_id = bucket.init_multipart_upload(key).upload_id print(f"初始化分片上传成功，上传ID: {upload_id}") # 步骤2：上传分片 file_size = os.path.getsize(file_path) part_size = 100 * 1024 # 每个分片100KB part_number = 1 parts = [] offset = 0 with open(file_path, 'rb') as fileobj: while offset < file_size: # 计算当前分片大小 current_part_size = min(part_size, file_size - offset) # 上传分片 result = bucket.upload_part( key, upload_id, part_number, SizedFileAdapter(fileobj, current_part_size) ) print(f"分片号: {part_number}, ETag: {result.etag}") # 记录已上传的分片信息 parts.append(PartInfo(part_number, result.etag)) offset += current_part_size part_number += 1 # 步骤3：完成分片上传 result = bucket.complete_multipart_upload(key, upload_id, parts) print(f"完成分片上传，ETag: {result.etag}") except Exception as e: print(f"错误: {e}") raise if __name__ == "__main__": main()

## Go SDK V2

package main // OSS Go SDK V2 分片上传示例 // 实现大文件的分片上传功能 import ( "context" "fmt" "io" "os" "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss" "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials" ) func main() { // 从环境变量获取访问凭证 // 配置OSS客户端，设置凭证提供者和Endpoint config := oss.LoadDefaultConfig(). WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()). WithRegion("cn-hangzhou"). WithEndpoint("oss-cn-hangzhou.aliyuncs.com") // 初始化OSS客户端 client := oss.NewClient(config) // 配置Bucket和文件信息 bucket := "example-bucket" key := "dest.jpg" filePath := "dest.jpg" // 步骤1：初始化分片上传 initResult, err := client.InitiateMultipartUpload(context.TODO(), &oss.InitiateMultipartUploadRequest{ Bucket: oss.Ptr(bucket), Key: oss.Ptr(key), }) if err != nil { fmt.Printf("错误: %v\n", err) return } uploadId := *initResult.UploadId fmt.Printf("初始化分片上传成功，上传ID: %s\n", uploadId) // 步骤2：上传分片 file, err := os.Open(filePath) if err != nil { fmt.Printf("错误: %v\n", err) return } defer file.Close() fileInfo, err := file.Stat() if err != nil { fmt.Printf("错误: %v\n", err) return } fileSize := fileInfo.Size() partSize := int64(100 * 1024) // 每个分片100KB partNumber := int32(1) var parts []oss.UploadPart for offset := int64(0); offset < fileSize; offset += partSize { // 计算当前分片大小 currentPartSize := partSize if offset+partSize > fileSize { currentPartSize = fileSize - offset } // 读取分片数据 file.Seek(offset, 0) partData := io.LimitReader(file, currentPartSize) // 上传分片 partResult, err := client.UploadPart(context.TODO(), &oss.UploadPartRequest{ Bucket: oss.Ptr(bucket), Key: oss.Ptr(key), UploadId: oss.Ptr(uploadId), PartNumber: partNumber, Body: partData, }) if err != nil { fmt.Printf("错误: %v\n", err) return } fmt.Printf("分片号: %d, ETag: %s\n", partNumber, *partResult.ETag) // 记录已上传的分片信息 parts = append(parts, oss.UploadPart{ PartNumber: partNumber, ETag: partResult.ETag, }) partNumber++ } // 步骤3：完成分片上传 completeResult, err := client.CompleteMultipartUpload(context.TODO(), &oss.CompleteMultipartUploadRequest{ Bucket: oss.Ptr(bucket), Key: oss.Ptr(key), UploadId: oss.Ptr(uploadId), CompleteMultipartUpload: &oss.CompleteMultipartUpload{ Parts: parts, }, }) if err != nil { fmt.Printf("错误: %v\n", err) return } fmt.Printf("完成分片上传，Bucket: %s, Key: %s, Location: %s, ETag: %s\n", *completeResult.Bucket, *completeResult.Key, *completeResult.Location, *completeResult.ETag) }

## Go SDK V1

package main // OSS Go SDK V1 分片上传示例 // 实现大文件的分片上传功能 import ( "fmt" "os" "github.com/aliyun/aliyun-oss-go-sdk/oss" ) func main() { // 从环境变量获取访问凭证 provider, _ := oss.NewEnvironmentVariableCredentialsProvider() // 创建OSS客户端实例 client, _ := oss.New( "oss-cn-hangzhou.aliyuncs.com", "", "", oss.SetCredentialsProvider(&provider), oss.AuthVersion(oss.AuthV4), oss.Region("cn-hangzhou"), ) // 获取Bucket对象 bucket, _ := client.Bucket("example-bucket") // 配置文件信息 key := "dest.jpg" filePath := "dest.jpg" // 步骤1：初始化分片上传 imur, err := bucket.InitiateMultipartUpload(key) if err != nil { fmt.Printf("错误: %v\n", err) return } fmt.Printf("初始化分片上传成功，上传ID: %s\n", imur.UploadID) // 步骤2：上传分片 file, err := os.Open(filePath) if err != nil { fmt.Printf("错误: %v\n", err) return } defer file.Close() fileInfo, err := file.Stat() if err != nil { fmt.Printf("错误: %v\n", err) return } fileSize := fileInfo.Size() partSize := int64(100 * 1024) // 每个分片100KB // 将文件分片 chunks, err := oss.SplitFileByPartSize(filePath, partSize) if err != nil { fmt.Printf("错误: %v\n", err) return } var parts []oss.UploadPart for _, chunk := range chunks { part, err := bucket.UploadPart(imur, file, chunk.Size, chunk.Number) if err != nil { fmt.Printf("错误: %v\n", err) return } fmt.Printf("分片号: %d, ETag: %s\n", chunk.Number, part.ETag) parts = append(parts, part) } // 步骤3：完成分片上传 _, err = bucket.CompleteMultipartUpload(imur, parts) if err != nil { fmt.Printf("错误: %v\n", err) return } fmt.Printf("完成分片上传，文件大小: %d 字节\n", fileSize) }

## 清理碎片文件

分片上传过程意外中断且未调用AbortMultipartUpload接口时，已上传的分片会作为碎片文件保留在Bucket中并持续产生存储费用。及时清理这些碎片文件可避免不必要的存储成本。

通过控制台

- 

前往[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)，单击目标Bucket。

- 

在文件列表单击碎片管理，查看并删除碎片文件。

通过生命周期规则

配置生命周期规则可实现对过期碎片的自动清理，减少手动维护工作量并防止遗漏。具体操作参见[通过生命周期规则清理过期碎片](products/oss/documents/user-guide/configuration-examples.md)。

通过工具

- 

图形化管理工具ossbrowser

在Bucket的文件列表页面单击文件碎片，查看并删除碎片文件。

- 

命令行工具ossutil

使用[abort-multipart-upload](products/oss/documents/developer-reference/abort-multipart-upload.md)命令取消分片上传任务并删除对应的分片数据。命令示例如下：

ossutil api abort-multipart-upload --bucket example-bucket --key dest.jpg --upload-id D9F4****************************

通过SDK

通过调用AbortMultipartUpload接口取消分片上传任务并删除对应的分片数据。以下为常见语言的SDK取消分片上传任务代码示例，更多语言的使用示例请参见[SDK](products/oss/documents/developer-reference/sdk-code-samples.md)[参考](products/oss/documents/developer-reference/sdk-code-samples.md)中对应语言的示例代码。

运行代码前需安装对应语言的SDK并配置访问凭证环境变量，使用RAM用户或RAM角色时还需参考[API](products/oss/documents/user-guide/multipart-upload.md)[和权限说明](products/oss/documents/user-guide/multipart-upload.md)进行接口授权。

## Java SDK V2

import com.aliyun.sdk.service.oss2.OSSClient; import com.aliyun.sdk.service.oss2.credentials.CredentialsProvider; import com.aliyun.sdk.service.oss2.credentials.StaticCredentialsProvider; import com.aliyun.sdk.service.oss2.models.AbortMultipartUploadRequest; import com.aliyun.sdk.service.oss2.models.AbortMultipartUploadResult; /** * OSS取消分片上传示例 * 演示如何取消一个分片上传任务 */ public class AbortMultipartUpload { public static void main(String[] args) { // 从环境变量获取访问凭证 String accessKeyId = System.getenv("OSS_ACCESS_KEY_ID"); String accessKeySecret = System.getenv("OSS_ACCESS_KEY_SECRET"); // 设置OSS地域和Endpoint String region = "cn-hangzhou"; String endpoint = "oss-cn-hangzhou.aliyuncs.com"; // 配置Bucket和文件信息 String bucket = "example-bucket"; String key = "dest.jpg"; String uploadId = "D9F4****************************"; // 创建凭证提供者 CredentialsProvider provider = new StaticCredentialsProvider(accessKeyId, accessKeySecret); // 初始化OSS客户端 OSSClient client = OSSClient.newBuilder() .credentialsProvider(provider) .region(region) .endpoint(endpoint) .build(); try { // 取消分片上传 AbortMultipartUploadResult result = client.abortMultipartUpload( AbortMultipartUploadRequest.newBuilder() .bucket(bucket) .key(key) .uploadId(uploadId) .build()); System.out.printf("取消分片上传成功，状态码: %d, 请求ID: %s\n", result.statusCode(), result.requestId()); } catch (Exception e) { System.out.printf("错误: %s\n", e.getMessage()); e.printStackTrace(); } finally { // 关闭客户端连接 try { client.close(); } catch (Exception e) { e.printStackTrace(); } } } }

## Java SDK V1

import com.aliyun.oss.*; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.common.comm.SignVersion; import com.aliyun.oss.model.*; /** * OSS取消分片上传示例（V1 SDK） * 演示如何取消一个分片上传任务 */ public class AbortMultipartUpload { public static void main(String[] args) { // 从环境变量获取访问凭证 String accessKeyId = System.getenv("OSS_ACCESS_KEY_ID"); String accessKeySecret = System.getenv("OSS_ACCESS_KEY_SECRET"); // 设置OSS地域和Endpoint String region = "cn-hangzhou"; String endpoint = "oss-cn-hangzhou.aliyuncs.com"; // 配置Bucket和文件信息 String bucketName = "example-bucket"; String objectName = "dest.jpg"; String uploadId = "D9F4****************************"; // 创建凭证提供者 DefaultCredentialProvider provider = new DefaultCredentialProvider(accessKeyId, accessKeySecret); // 配置客户端参数 ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration(); clientBuilderConfiguration.setSignatureVersion(SignVersion.V4); // 初始化OSS客户端 OSS ossClient = OSSClientBuilder.create() .credentialsProvider(provider) .clientConfiguration(clientBuilderConfiguration) .region(region) .endpoint(endpoint) .build(); try { // 取消分片上传 AbortMultipartUploadRequest abortMultipartUploadRequest = new AbortMultipartUploadRequest(bucketName, objectName, uploadId); ossClient.abortMultipartUpload(abortMultipartUploadRequest); System.out.printf("取消分片上传成功，上传ID: %s\n", uploadId); } catch (Exception e) { System.out.printf("错误: %s\n", e.getMessage()); e.printStackTrace(); } finally { // 关闭客户端连接 ossClient.shutdown(); } } }

## Python SDK V2

#!/usr/bin/env python3 # -*- coding: utf-8 -*- # OSS Python SDK V2 取消分片上传示例 # 取消分片上传任务并删除已上传的分片 import alibabacloud_oss_v2 as oss def main(): # 从环境变量获取访问凭证 credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider() # 加载SDK的默认配置 config = oss.config.load_default() config.credentials_provider = credentials_provider # 设置OSS地域和Endpoint config.region = "cn-hangzhou" config.endpoint = "oss-cn-hangzhou.aliyuncs.com" # 初始化OSS客户端 client = oss.Client(config) # 配置Bucket和文件信息 bucket = "example-bucket" key = "dest.jpg" upload_id = "D9F4****************************" # 取消分片上传 result = client.abort_multipart_upload( oss.AbortMultipartUploadRequest( bucket=bucket, key=key, upload_id=upload_id )) print(f"取消分片上传成功，状态码: {result.status_code}, 请求ID: {result.request_id}") if __name__ == "__main__": main()

## Python SDK V1

#!/usr/bin/env python3 # -*- coding: utf-8 -*- # OSS Python SDK V1 取消分片上传示例 import oss2 from oss2.credentials import EnvironmentVariableCredentialsProvider def main(): # 从环境变量中获取访问凭证 auth = oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider()) # 设置OSS地域和Endpoint region = "cn-hangzhou" endpoint = "https://oss-cn-hangzhou.aliyuncs.com" # 配置Bucket和文件信息 bucket_name = "example-bucket" key = "dest.jpg" upload_id = "D9F4****************************" # 初始化OSS客户端 bucket = oss2.Bucket(auth, endpoint, bucket_name, region=region) # 取消分片上传 bucket.abort_multipart_upload(key, upload_id) print(f"取消分片上传成功，上传ID: {upload_id}") if __name__ == "__main__": main()

## Go SDK V2

package main // OSS Go SDK V2 取消分片上传示例 import ( "context" "fmt" "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss" "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials" ) func main() { // 从环境变量获取访问凭证 // 配置OSS客户端，设置凭证提供者和Endpoint config := oss.LoadDefaultConfig(). WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()). WithRegion("cn-hangzhou"). WithEndpoint("oss-cn-hangzhou.aliyuncs.com") // 初始化OSS客户端 client := oss.NewClient(config) // 配置Bucket和文件信息 bucket := "example-bucket" key := "dest.jpg" uploadId := "D9F4****************************" // 取消分片上传 client.AbortMultipartUpload(context.TODO(), &oss.AbortMultipartUploadRequest{ Bucket: oss.Ptr(bucket), Key: oss.Ptr(key), UploadId: oss.Ptr(uploadId), }) fmt.Printf("取消分片上传成功，上传ID: %s\n", uploadId) }

## Go SDK V1

package main // OSS Go SDK V1 取消分片上传示例 import ( "fmt" "github.com/aliyun/aliyun-oss-go-sdk/oss" ) func main() { // 从环境变量获取访问凭证 provider, _ := oss.NewEnvironmentVariableCredentialsProvider() // 创建OSS客户端实例 client, _ := oss.New( "oss-cn-hangzhou.aliyuncs.com", "", "", oss.SetCredentialsProvider(&provider), oss.AuthVersion(oss.AuthV4), oss.Region("cn-hangzhou"), ) // 获取Bucket对象 bucket, _ := client.Bucket("example-bucket") // 配置文件信息 key := "dest.jpg" uploadId := "D9F4****************************" // 创建InitiateMultipartUploadResult对象 imur := oss.InitiateMultipartUploadResult{ UploadID: uploadId, Key: key, } // 取消分片上传 bucket.AbortMultipartUpload(imur) fmt.Printf("取消分片上传成功，上传ID: %s\n", uploadId) }

## 应用于生产环境

最佳实践

- 

性能优化：提升上传速度和稳定性

- 

合理控制并发数量：根据网络带宽和设备负载确定合理的并发分片数量。过多的并发连接会增加系统负载和网络拥塞，过少则无法充分利用网络资源。

- 

避免顺序前缀命名：上传大量文件时避免使用顺序前缀（如时间戳开头），防止请求集中在特定分区造成热点问题，影响整体上传性能。详见[OSS](products/oss/documents/user-guide/oss-performance-best-practices.md)[性能最佳实践](products/oss/documents/user-guide/oss-performance-best-practices.md)。

- 

可靠性保障：实现断点续传

分片上传任务无过期时间限制，支持暂停和恢复操作。利用Upload ID作为任务标识符，当单个分片上传失败时，仅需重传该分片，避免从头开始上传整个文件，大幅提升传输效率。

- 

成本优化：优化深度冷归档上传策略

对于需要存储到深度冷归档的大量文件，建议先上传为标准存储类型，再通过[生命周期规则](products/oss/documents/user-guide/lifecycle-rules-based-on-the-last-modified-time.md)自动转换存储类型，避免直接上传产生高额的PUT请求费用。

风险防范

- 

数据安全：防止文件覆盖

在上传请求header中设置x-oss-forbid-overwrite参数为true，防止覆盖同名文件造成数据丢失。也可开启[版本控制](products/oss/documents/user-guide/overview-78.md)功能保留历史版本。

## 配额与限制

| 限制项 | 说明 |
| --- | --- |
| 单个文件的大小 | 不超过 48.8TB |
| 分片数量 | 1~10,000 个 |
| 单个分片大小 | 最小值为 100KB，最大值为 5GB。最后一个分片的大小允许小于 100KB。 |
| 单次 ListParts 请求返回的分片最大数量 | 1,000 个 |
| 单次 ListMultipartUploads 请求返回的分片上传事件最大数量 | 1,000 个 |


## 计费说明

分片上传过程中不同接口产生相应的计费项目如下表所示。详细的计费说明请参见[请求费用](products/oss/documents/api-operation-calling-fees.md)和[存储费用](products/oss/documents/storage-fees.md)。

- 

- 

| API | 计费项 | 说明 |
| --- | --- | --- |
| InitiateMultipartUpload | PUT 类型请求 | 根据成功的请求次数计算请求费用。 |
| UploadPart | PUT 类型请求 | 根据成功的请求次数计算请求费用。 |
| 存储费用 | 根据分片的存储类型（与对象文件类型一致）、实际大小和存储时长收取存储费用。无最小计量单位限制，被删除或合并为完整的对象文件后停止计费。 |  |
| UploadPartCopy | PUT 类型请求 | 根据成功的请求次数计算请求费用。 |
| CompleteMultipartUpload | PUT 类型请求 | 根据成功的请求次数计算请求费用。 |
| 存储费用 | 根据对象文件的存储类型、大小和时长收取存储费用。 |  |
| AbortMultipartUpload | PUT 类型请求 | 根据成功的请求次数计算请求费用。 重要 在中国内地各地域，通过生命周期规则删除低频访问、归档、冷归档类型碎片的 PUT 类请求费用高于删除标准存储类型碎片的 PUT 类请求费用；通过生命周期规则删除深度冷归档存储类型碎片，不收取 PUT 类请求费用。 在中国香港以及海外地域，通过生命周期规则删除各存储类型碎片时不收取 PUT 类请求费用。 |
| ListMultipartUploads | PUT 类型请求 | 根据成功的请求次数计算请求费用。 |
| ListParts | PUT 类型请求 | 根据成功的请求次数计算请求费用。 |


## API和权限说明

阿里云主账号默认拥有全部API的操作权限。RAM用户或RAM角色使用分片上传功能需根据具体操作的API授予相应权限。更多信息请参见[RAM Policy](products/oss/documents/ram-policy-overview.md)和[RAM Policy](products/oss/documents/common-examples-of-ram-policies.md)[常见示例](products/oss/documents/common-examples-of-ram-policies.md)。

| API | Action | 说明 |
| --- | --- | --- |
| InitiateMultipartUpload | oss:PutObject | 初始化分片上传任务。 |
| oss:PutObjectTagging | 初始化分片上传任务时，如果通过 x-oss-tagging 指定对象文件的标签，则需要此操作的权限。 |  |
| kms:GenerateDataKey | 上传对象文件时，如果对象文件的元数据包含 X-Oss-Server-Side-Encryption: KMS，则需要这两个操作的权限。 |  |
| kms:Decrypt |  |  |
| UploadPart | oss:PutObject | 上传分片。 |
| UploadPartCopy | oss:GetObject | 从一个已存在的对象文件中拷贝数据来上传一个分片时，需要读取源对象文件的权限。 |
| oss:PutObject | 从一个已存在的对象文件中拷贝数据来上传一个分片时，需要写入目标对象文件的权限。 |  |
| oss:GetObjectVersion | 从一个已存在的对象文件中拷贝数据来上传一个分片时，如果通过 versionId 指定对象文件的版本，需要读取源对象文件的指定版本的权限。 |  |
| CompleteMultipartUpload | oss:PutObject | 将分片合并为对象文件。 |
| oss:PutObjectTagging | 将分片合并为对象文件时，如果通过 x-oss-tagging 指定对象文件的标签，则需要此操作的权限。 |  |
| AbortMultipartUpload | oss:AbortMultipartUpload | 取消分片上传事件并删除对应的分片数据。 |
| ListMultipartUploads | oss:ListMultipartUploads | 列举所有执行中的分片上传事件，即已经初始化但尚未完成或者尚未被中止的分片上传事件。 |
| ListParts | oss:ListParts | 列举指定 Upload ID 所属的所有已经上传成功的分片。 |


[上一篇：简单上传](products/oss/documents/user-guide/simple-upload.md)[下一篇：断点续传上传](products/oss/documents/user-guide/resumable-upload.md)

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
