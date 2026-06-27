# 使用SDK实现客户端加密-对象存储-阿里云

Source: https://help.aliyun.com/zh/oss/user-guide/client-side-encryption

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

# 客户端加密

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

OSS客户端加密是在数据上传至OSS之前，用户在本地加密数据，确保数据在传输和存储过程中的安全性。

## 免责声明

- 

使用客户端加密功能时，您需要对主密钥的完整性和正确性负责。因您维护不当导致主密钥用错或丢失，从而导致加密数据无法解密所引起的一切损失和后果均由您自行承担。

- 

在对加密数据进行复制或者迁移时，您需要对加密元数据的完整性和正确性负责。因您维护不当导致加密元数据出错或丢失，从而导致加密数据无法解密所引起的一切损失和后果均由您自行承担。

## 使用场景

- 

高度敏感数据：对于高度敏感数据（如PII、金融交易记录、医疗数据），用户可以在数据离开本地前加密，确保传输过程中的数据安全。

- 

合规要求：某些法规（如HIPAA、GDPR）要求严格的加密控制，客户端加密满足这些要求，因为密钥由用户管理，不通过网络传递。

- 

更强的自主控制权：企业或开发者希望完全控制加密过程（选择算法、管理密钥），客户端加密确保只有授权用户能解密和访问数据。

- 

跨区域数据迁移安全性：在跨区域数据迁移中，客户端加密确保数据始终加密，增强公网传输安全性。

## 背景信息

使用客户端加密时，会为每个Object生成一个随机数据加密密钥，用该随机数据加密密钥明文对Object的数据进行对称加密。主密钥用于生成随机的数据加密密钥，加密后的内容会作为Object的meta信息保存在服务端。解密时先用主密钥将加密后的随机密钥解密出来，再用解密出来的随机数据加密密钥明文解密Object的数据。主密钥只参与客户端本地计算，不会在网络上进行传输或保存在服务端，以保证主密钥的数据安全。

重要

- 

客户端加密支持分片上传超过5 GB的文件。上传时需指定文件总大小和分片大小，除最后一个分片外，其他分片大小需一致，且必须是16的整数倍。

- 

使用客户端加密上传文件后，加密元数据受保护，无法通过[CopyObject](products/oss/documents/developer-reference/copyobject.md)修改Object meta信息。

对于主密钥的使用，目前支持如下两种方式：

- 

[使用](products/oss/documents/user-guide/client-side-encryption.md)[KMS](products/oss/documents/user-guide/client-side-encryption.md)[托管用户主密钥](products/oss/documents/user-guide/client-side-encryption.md)

- 

[使用用户自主管理密钥](products/oss/documents/user-guide/client-side-encryption.md)

完整的示例代码请参见[GitHub](https://github.com/aliyun/aliyun-oss-python-sdk/blob/master/examples/object_crypto.py)。

## 使用KMS托管用户主密钥

当使用KMS托管用户主密钥用于客户端数据加密时，无需向OSS加密客户端提供任何加密密钥，只需要在上传Object时指定KMS用户主密钥ID（即CMK ID）。具体工作原理如下图所示。

- 

加密并上传Object

- 

获取加密密钥。

通过CMK ID，客户端向KMS请求数据密钥，KMS返回数据明文密钥和数据密文密钥。

- 

加密数据并上传至OSS。

客户端使用数据明文密钥加密Object，并将加密后的Object和数据密文密钥上传至OSS。

- 

下载并解密Object

- 

下载Object。

客户端从OSS下载加密的Object和数据密文密钥。

- 

解密Object。

客户端将数据密文密钥和CMK ID发送至KMS服务器，KMS解密并返回数据明文密钥。

说明

- 

客户端会为每一个上传的Object获取一个唯一的数据加密密钥。

- 

为了保证数据的安全性，建议定期轮换或者更新CMK。

- 

您需要维护CMK ID与Object之间的映射关系。

## 使用用户自主管理密钥

使用用户自主管理密钥时，您需要生成并保管加密密钥。当客户端加密Object时，您需上传加密密钥（对称或非对称）至客户端。具体加密过程如下图所示。

- 

加密并上传Object

- 

用户向客户端提供主密钥（对称或非对称）。

- 

客户端生成一次性对称密钥（数据密钥），用于加密单个Object（每个Object生成一个数据密钥）。

- 

客户端使用数据密钥加密Object，并用主密钥加密数据密钥。

- 

客户端将加密的Object和加密的数据密钥作为Object元数据上传至OSS。

- 

下载并解密Object

- 

客户端从OSS下载加密的Object及其元数据。

- 

客户端使用元数据中的信息，授权确定主密钥来解密数据密钥，然后用解密后的数据密钥解密Object。

重要

- 

客户端不会将用户主密钥以及未加密的数据发送至OSS。请妥善保管加密密钥，若密钥丢失，将无法解密数据。

- 

数据密钥由客户端随机生成。

## 使用阿里云SDK

以下仅列举常见SDK客户端加密的代码示例。关于其他SDK客户端加密的代码示例，请参见[SDK](products/oss/documents/developer-reference/overview-21.md)[简介](products/oss/documents/developer-reference/overview-21.md)。

Java

import com.aliyun.oss.*; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.crypto.SimpleRSAEncryptionMaterials; import com.aliyun.oss.model.OSSObject; import java.io.BufferedReader; import java.io.ByteArrayInputStream; import java.io.InputStreamReader; import java.security.KeyPair; import java.security.interfaces.RSAPrivateKey; import java.security.interfaces.RSAPublicKey; import java.util.HashMap; import java.util.Map; public class Demo { public static void main(String[] args) throws Throwable { // Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。 String endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider(); // 填写Bucket名称，例如examplebucket。 String bucketName = "examplebucket"; // 填写Object完整路径，例如exampleobject.txt。Object完整路径中不能包含Bucket名称。 String objectName = "exampleobject.txt"; String content = "Hello OSS!"; // 填写您的RSA私钥字符串，可以使用OpenSSL工具生成。以下为RSA私钥字符串的示例值。 final String PRIVATE_PKCS1_PEM = "-----BEGIN RSA PRIVATE KEY-----\n" + "MIICWwIBAAKBgQCokfiAVXXf5ImFzKDw+XO/UByW6mse2QsIgz3ZwBtMNu59fR5z\n" + "ttSx+8fB7vR4CN3bTztrP9A6bjoN0FFnhlQ3vNJC5MFO1PByrE/MNd5AAfSVba93\n" + "I6sx8NSk5MzUCA4NJzAUqYOEWGtGBcom6kEF6MmR1EKib1Id8hpooY5xaQIDAQAB\n" + "AoGAOPUZgkNeEMinrw31U3b2JS5sepG6oDG2CKpPu8OtdZMaAkzEfVTJiVoJpP2Y\n" + "nPZiADhFW3e0ZAnak9BPsSsySRaSNmR465cG9tbqpXFKh9Rp/sCPo4Jq2n65yood\n" + "JBrnGr6/xhYvNa14sQ6xjjfSgRNBSXD1XXNF4kALwgZyCAECQQDV7t4bTx9FbEs5\n" + "36nAxPsPM6aACXaOkv6d9LXI7A0J8Zf42FeBV6RK0q7QG5iNNd1WJHSXIITUizVF\n" + "6aX5NnvFAkEAybeXNOwUvYtkgxF4s28s6gn11c5HZw4/a8vZm2tXXK/QfTQrJVXp\n" + "VwxmSr0FAajWAlcYN/fGkX1pWA041CKFVQJAG08ozzekeEpAuByTIOaEXgZr5MBQ\n" + "gBbHpgZNBl8Lsw9CJSQI15wGfv6yDiLXsH8FyC9TKs+d5Tv4Cvquk0efOQJAd9OC\n" + "lCKFs48hdyaiz9yEDsc57PdrvRFepVdj/gpGzD14mVerJbOiOF6aSV19ot27u4on\n" + "Td/3aifYs0CveHzFPQJAWb4LCDwqLctfzziG7/S7Z74gyq5qZF4FUElOAZkz123E\n" + "yZvADwuz/4aK0od0lX9c4Jp7Mo5vQ4TvdoBnPuGo****\n" + "-----END RSA PRIVATE KEY-----"; // 填写您的RSA公钥字符串，可以使用OpenSSL工具生成。以下为RSA公钥字符串的示例值。 final String PUBLIC_X509_PEM = "-----BEGIN PUBLIC KEY-----\n" + "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCokfiAVXXf5ImFzKDw+XO/UByW\n" + "6mse2QsIgz3ZwBtMNu59fR5zttSx+8fB7vR4CN3bTztrP9A6bjoN0FFnhlQ3vNJC\n" + "5MFO1PByrE/MNd5AAfSVba93I6sx8NSk5MzUCA4NJzAUqYOEWGtGBcom6kEF6MnR\n" + "1EKib1Id8hpooY5xaQID****\n" + "-----END PUBLIC KEY-----"; // 创建一个RSA密钥对。 RSAPrivateKey privateKey = SimpleRSAEncryptionMaterials.getPrivateKeyFromPemPKCS1(PRIVATE_PKCS1_PEM); RSAPublicKey publicKey = SimpleRSAEncryptionMaterials.getPublicKeyFromPemX509(PUBLIC_X509_PEM); KeyPair keyPair = new KeyPair(publicKey, privateKey); // 创建主密钥RSA的描述信息。创建后不允许修改。主密钥描述信息和主密钥一一对应。 // 如果所有的object都使用相同的主密钥，主密钥描述信息可以为空，但后续不支持更换主密钥。 // 如果主密钥描述信息为空，解密时无法判断文件使用的是哪个主密钥进行加密。 // 强烈建议为每个主密钥都配置描述信息，由客户端保存主密钥和描述信息之间的对应关系（服务端不保存两者之间的对应关系）。 Map<String, String> matDesc = new HashMap<String, String>(); matDesc.put("desc-key", "desc-value"); // 创建RSA加密材料。 SimpleRSAEncryptionMaterials encryptionMaterials = new SimpleRSAEncryptionMaterials(keyPair, matDesc); // 如果要下载并解密其他RSA密钥加密的文件，请将其他主密钥及其描述信息添加到加密材料中。 // encryptionMaterials.addKeyPairDescMaterial(<otherKeyPair>, <otherKeyPairMatDesc>); // 创建加密客户端。 // 当加密客户端不再使用时，调用shutdown方法以释放资源。 OSSEncryptionClient ossEncryptionClient = new OSSEncryptionClientBuilder(). build(endpoint, credentialsProvider, encryptionMaterials); try { // 加密上传文件。 ossEncryptionClient.putObject(bucketName, objectName, new ByteArrayInputStream(content.getBytes())); // 下载文件时自动解密。 OSSObject ossObject = ossEncryptionClient.getObject(bucketName, objectName); BufferedReader reader = new BufferedReader(new InputStreamReader(ossObject.getObjectContent())); StringBuffer buffer = new StringBuffer(); String line; while ((line = reader.readLine()) != null) { buffer.append(line); } reader.close(); // 查看解密后的内容是否与上传的明文一致。 System.out.println("Put plain text: " + content); System.out.println("Get and decrypted text: " + buffer.toString()); } catch (OSSException oe) { System.out.println("Caught an OSSException, which means your request made it to OSS, " + "but was rejected with an error response for some reason."); System.out.println("Error Message:" + oe.getErrorMessage()); System.out.println("Error Code:" + oe.getErrorCode()); System.out.println("Request ID:" + oe.getRequestId()); System.out.println("Host ID:" + oe.getHostId()); } catch (ClientException ce) { System.out.println("Caught an ClientException, which means the client encountered " + "a serious internal problem while trying to communicate with OSS, " + "such as not being able to access the network."); System.out.println("Error Message:" + ce.getMessage()); } finally { if (ossEncryptionClient != null) { ossEncryptionClient.shutdown(); } } } }

Python

import argparse import base64 import json from aliyunsdkkms.request.v20160120.DecryptRequest import DecryptRequest from aliyunsdkkms.request.v20160120.EncryptRequest import EncryptRequest from alibabacloud_dkms_transfer.kms_transfer_acs_client import KmsTransferAcsClient from typing import Optional, Dict import alibabacloud_oss_v2 as oss # 创建命令行参数解析器，用于接收用户输入的参数 parser = argparse.ArgumentParser(description="encryption kms sample") # 添加命令行参数 --region，表示存储空间所在的地域，必填项 parser.add_argument('--region', help='The region in which the bucket is located.', required=True) # 添加命令行参数 --bucket，表示存储空间的名称，必填项 parser.add_argument('--bucket', help='The name of the bucket.', required=True) # 添加命令行参数 --endpoint，表示其他服务访问 OSS 时使用的域名，可选项 parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS') # 添加命令行参数 --key，表示对象的名称（文件路径），必填项 parser.add_argument('--key', help='The name of the object.', required=True) # 添加命令行参数 --kms_id，表示用户的 CMK（Customer Master Key）ID，必填项 parser.add_argument('--kms_id', help='The id of the your CMK ID.', required=True) # 自定义主密钥加密器类，继承自 oss.crypto.MasterCipher class MasterKmsCipher(oss.crypto.MasterCipher): def __init__( self, mat_desc: Optional[Dict] = None, kms_client: Optional[KmsTransferAcsClient] = None, kms_id: Optional[str] = None, ): self.kms_client = kms_client self.kms_id = kms_id self._mat_desc = None # 如果提供了主密钥的描述信息，则将其序列化为 JSON 字符串 if mat_desc is not None and len(mat_desc.items()) > 0: self._mat_desc = json.dumps(mat_desc) def get_wrap_algorithm(self) -> str: # 返回加密算法名称，固定为 'KMS/ALICLOUD' return 'KMS/ALICLOUD' def get_mat_desc(self) -> str: return self._mat_desc or '' def encrypt(self, data: bytes) -> bytes: """ 使用 KMS 服务加密数据 :param data: 待加密的原始数据（字节格式） :return: 加密后的数据（字节格式） """ # 将原始数据编码为 Base64 格式 base64_crypto = base64.b64encode(data) # 构造加密请求对象 request = EncryptRequest() request.set_KeyId(self.kms_id) # 设置 CMK ID request.set_Plaintext(base64_crypto) # 设置待加密的 Base64 数据 # 调用 KMS 客户端执行加密操作，并获取响应 response = self.kms_client.do_action_with_exception(request) # 解析响应中的加密数据字段，并解码为字节格式 return base64.b64decode(json.loads(response).get('CiphertextBlob')) def decrypt(self, data: bytes) -> bytes: """ 使用 KMS 服务解密数据 :param data: 已加密的数据（字节格式） :return: 解密后的原始数据（字节格式） """ # 将加密数据编码为 Base64 格式 base64_crypto = base64.b64encode(data) # 构造解密请求对象 request = DecryptRequest() request.set_CiphertextBlob(base64_crypto) # 设置加密数据 # 调用 KMS 客户端执行解密操作，并获取响应 response = self.kms_client.do_action_with_exception(request) # 解析响应中的明文字段，并解码为字节格式 return base64.b64decode(json.loads(response).get('Plaintext')) def main(): # 解析命令行参数 args = parser.parse_args() # 从环境变量中加载凭证信息（AccessKeyId 和 AccessKeySecret） credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider() # 加载 SDK 的默认配置 cfg = oss.config.load_default() # 设置凭证提供者 cfg.credentials_provider = credentials_provider # 设置存储空间所在的地域 cfg.region = args.region # 如果用户提供了自定义的 endpoint，则设置到配置中 if args.endpoint is not None: cfg.endpoint = args.endpoint # 使用配置对象初始化 OSS 客户端 client = oss.Client(cfg) # 初始化 KMS 客户端，用于与 KMS 服务交互 kms_client = KmsTransferAcsClient( ak=credentials_provider._credentials.access_key_id, # 从凭证提供者中获取 AccessKeyId secret=credentials_provider._credentials.access_key_secret, # 从凭证提供者中获取 AccessKeySecret region_id=args.region # 指定地域信息 ) # 初始化主密钥加密器（MasterKmsCipher），用于加密和解密操作 mc = MasterKmsCipher( mat_desc={"desc": "your master encrypt key material describe information"}, # 主密钥描述信息 kms_client=kms_client, # KMS 客户端实例 kms_id=args.kms_id # 用户的 CMK ID ) # 创建加密客户端 encryption_client = oss.EncryptionClient(client, mc) # 定义要上传的数据 data = b'hello world' # 调用加密客户端的 put_object 方法上传加密对象 result = encryption_client.put_object( oss.PutObjectRequest( bucket=args.bucket, # 指定目标存储空间的名称 key=args.key, # 指定对象的名称（文件路径） body=data, # 指定要上传的数据 ) ) # 打印上传加密对象的结果 print(vars(result)) # 调用加密客户端的 get_object 方法获取加密对象的内容 result = encryption_client.get_object( oss.GetObjectRequest( bucket=args.bucket, # 指定目标存储空间的名称 key=args.key, # 指定对象的名称（文件路径） ) ) # 打印获取加密对象的结果 print(vars(result)) # 打印解密后的对象内容 print(result.body.read()) if __name__ == "__main__": # 程序入口，调用 main 函数执行逻辑 main()

Go

package main import ( "bytes" "io" "log" "github.com/aliyun/aliyun-oss-go-sdk/oss" osscrypto "github.com/aliyun/aliyun-oss-go-sdk/oss/crypto" ) func main() { // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 provider, err := oss.NewEnvironmentVariableCredentialsProvider() if err != nil { log.Fatalf("Error creating credentials provider: %v", err) } // 创建OSSClient实例。 // yourEndpoint填写Bucket对应的Endpoint，以华东1（杭州）为例，填写为https://oss-cn-hangzhou.aliyuncs.com。其它Region请按实际情况填写。 // yourRegion填写Bucket所在地域，以华东1（杭州）为例，填写为cn-hangzhou。其它Region请按实际情况填写。 clientOptions := []oss.ClientOption{oss.SetCredentialsProvider(&provider)} clientOptions = append(clientOptions, oss.Region("yourRegion")) // 设置签名版本 clientOptions = append(clientOptions, oss.AuthVersion(oss.AuthV4)) client, err := oss.New("yourEndpoint", "", "", clientOptions...) if err != nil { log.Fatalf("Error creating OSS client: %v", err) } // 创建一个主密钥的描述信息，创建后不允许修改。主密钥描述信息和主密钥一一对应。 // 如果所有的Object都使用相同的主密钥，主密钥描述信息可以为空，但后续不支持更换主密钥。 // 如果主密钥描述信息为空，解密时无法判断使用的是哪个主密钥。 // 强烈建议为每个主密钥都配置主密钥描述信息（json字符串），由客户端保存主密钥和描述信息之间的对应关系（服务端不保存两者之间的对应关系）。 // 由主密钥描述信息（json字符串）转换的map。 materialDesc := map[string]string{ "desc": "your master encrypt key material describe information", } // 根据主密钥描述信息创建一个主密钥对象。 // yourRsaPublicKey填写您自主管理的主密钥公钥信息，yourRsaPrivateKey填写您自主管理的主密钥私钥信息。 masterRsaCipher, err := osscrypto.CreateMasterRsa(materialDesc, "yourRsaPublicKey", "yourRsaPrivateKey") if err != nil { log.Fatalf("Error creating master RSA cipher: %v", err) } // 根据主密钥对象创建一个用于加密的接口，使用aes ctr模式加密。 contentProvider := osscrypto.CreateAesCtrCipher(masterRsaCipher) // 获取一个用于客户端加密的已创建Bucket。 // 客户端加密Bucket和普通Bucket具有相似的用法。 cryptoBucket, err := osscrypto.GetCryptoBucket(client, "yourBucketName", contentProvider) if err != nil { log.Fatalf("Error getting crypto bucket: %v", err) } // PutObject时自动加密。 err = cryptoBucket.PutObject("yourObjectName", bytes.NewReader([]byte("yourObjectValueByteArrary"))) if err != nil { log.Fatalf("Error putting object: %v", err) } // GetObject时自动解密。 body, err := cryptoBucket.GetObject("yourObjectName") if err != nil { log.Fatalf("Error getting object: %v", err) } defer body.Close() data, err := io.ReadAll(body) if err != nil { log.Fatalf("Error reading object data: %v", err) } log.Printf("Data: %s", string(data)) }

C++

#include <alibabacloud/oss/OssEncryptionClient.h> using namespace AlibabaCloud::OSS; int main(void) { /* 初始化OSS账号信息。*/ /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/ std::string Endpoint = "yourEndpoint"; /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/ std::string Region = "yourRegion"; /* 填写Bucket名称，例如examplebucket。*/ std::string BucketName = "examplebucket"; /* 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。*/ std::string ObjectName = "exampledir/exampleobject.txt"; /* 主密钥及描述信息。*/ std::string RSAPublicKey = "your rsa public key"; std::string RSAPrivateKey = "your rsa private key"; std::map<std::string, std::string> desc; desc["comment"] = "your comment"; /* 初始化网络等资源。*/ InitializeSdk(); ClientConfiguration conf; conf.signatureVersion = SignatureVersionType::V4; /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/ auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>(); OssClient client(Endpoint, credentialsProvider, conf); client.SetRegion(Region); CryptoConfiguration cryptoConf; auto materials = std::make_shared<SimpleRSAEncryptionMaterials>(RSAPublicKey, RSAPrivateKey, desc); OssEncryptionClient client(Endpoint, credentialsProvider, conf, materials, cryptoConf); /* 上传文件。*/ auto outcome = client.PutObject(BucketName, ObjectName, "yourLocalFilename"); if (!outcome.isSuccess()) { /* 异常处理。*/ std::cout << "PutObject fail" << ",code:" << outcome.error().Code() << ",message:" << outcome.error().Message() << ",requestId:" << outcome.error().RequestId() << std::endl; return -1; } /* 释放网络等资源。*/ ShutdownSdk(); return 0; }

PHP

<?php // 引入自动加载文件 加载依赖库 require_once 'vendor/autoload.php'; use AlibabaCloud\Dkms\Gcs\Sdk\Client as KmsClient; use AlibabaCloud\Oss\V2 as Oss; // 定义命令行参数描述 $optsdesc = [ "region" => ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域 "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名 "bucket" => ['help' => 'The name of the bucket', 'required' => True], // 存储空间名称是必填项 "key" => ['help' => 'The name of the object', 'required' => True], // 对象名称是必填项 ]; // 生成长选项列表 用于解析命令行参数 $longopts = \array_map(function ($key) { return "$key:"; // 每个参数后面加冒号 表示需要值 }, array_keys($optsdesc)); // 解析命令行参数 $options = getopt("", $longopts); // 检查必填参数是否缺失 foreach ($optsdesc as $key => $value) { if ($value['required'] === True && empty($options[$key])) { $help = $value['help']; echo "Error: the following arguments are required: --$key, $help"; // 提示用户缺少必填参数 exit(1); } } // 获取命令行参数值 $region = $options["region"]; // 存储空间所在区域 $bucket = $options["bucket"]; // 存储空间名称 $key = $options["key"]; // 对象名称 // 使用环境变量加载凭证信息 AccessKeyId 和 AccessKeySecret $credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider(); // 自定义KMS加密解密类 实现MasterCipherInterface接口 class KmsCipher implements Oss\Crypto\MasterCipherInterface { private $matDesc; private ?KmsClient $kmsClient; private ?string $keyId; private ?string $algorithm; public function __construct( $matDesc = null, ?string $keyId = null, ?KmsClient $kmsClient = null, ?string $algorithm = null ) { $this->keyId = $keyId; $this->matDesc = null; if (\is_array($matDesc)) { $val = json_encode($matDesc); if ($val !== false) { $this->matDesc = $val; } } else if (is_string($matDesc)) { $this->matDesc = $matDesc; } $this->kmsClient = $kmsClient; $this->algorithm = $algorithm; } // 加密方法 public function encrypt(string $data): string { $encryptRequest = new \AlibabaCloud\Dkms\Gcs\Sdk\Models\AdvanceEncryptRequest(); $encryptRequest->algorithm = $this->algorithm; $encryptRequest->keyId = $this->keyId; $encryptRequest->plaintext = \AlibabaCloud\Tea\Utils\Utils::toBytes($data); $runtimeOptions = new \AlibabaCloud\Dkms\Gcs\OpenApi\Util\Models\RuntimeOptions(); $encryptResponse = $this->kmsClient->advanceEncryptWithOptions($encryptRequest, $runtimeOptions); return base64_decode((string)$encryptResponse->ciphertextBlob); } // 解密方法 public function decrypt(string $data): string { $decryptRequest = new \AlibabaCloud\Dkms\Gcs\Sdk\Models\AdvanceDecryptRequest(); $decryptRequest->keyId = $this->keyId; $decryptRequest->ciphertextBlob = $data; $decryptRequest->algorithm = $this->algorithm; $runtimeOptions = new \AlibabaCloud\Dkms\Gcs\OpenApi\Util\Models\RuntimeOptions(); $decryptResponse = $this->kmsClient->advanceDecryptWithOptions($decryptRequest, $runtimeOptions); return base64_decode((string)$decryptResponse->plaintext); } // 获取包装算法 public function getWrapAlgorithm(): string { return "KMS/ALICLOUD"; } public function getMatDesc(): string { return $this->matDesc; } } /** * 构建专属KMS SDK Client对象 * @return KmsClient */ function getDkmsGcsSdkClient() { global $clientKeyFile, $password, $endpoint; // 构建专属KMS SDK Client配置 $config = new \AlibabaCloud\Dkms\Gcs\OpenApi\Models\Config(); $config->protocol = 'https'; $config->clientKeyFile = $clientKeyFile; $config->password = $password; $config->endpoint = $endpoint; // 验证服务端证书 $config->caFilePath = 'path/to/caCert.pem'; // 构建专属KMS SDK Client对象 return new \AlibabaCloud\Dkms\Gcs\Sdk\Client($config); } // 填写您在KMS应用管理获取的ClientKey文件路径 $clientKeyFile = '<your client key file path>'; // 填写您在KMS应用管理创建ClientKey时输入的加密口令 $password = '<your dkms client passowrd>'; // 填写您的专属KMS实例服务地址 $endpoint = '<your dkms instance service address>'; // 填写您在KMS创建的主密钥Id $kmsKeyId = '<your cmk id>'; // 加解密算法 $algorithm = '<your encrypt algorithm>'; // 专属KMS SDK Client对象 $kmsClient = getDkmsGcsSdkClient(); $cfg = Oss\Config::loadDefault(); $cfg->setCredentialsProvider($credentialsProvider); $cfg->setRegion($region); if (isset($options["endpoint"])) { $cfg->setEndpoint($options["endpoint"]); } $client = new Oss\Client($cfg); $materialDesc = ['desc' => 'your kms encrypt key material describe information']; $masterKmsCipher = new KmsCipher($materialDesc, $kmsKeyId, $kmsClient, $algorithm); $eClient = new \AlibabaCloud\Oss\V2\EncryptionClient($client, $masterKmsCipher); $eClient->putObject(new Oss\Models\PutObjectRequest( bucket: $bucket, key: $key, body: Oss\Utils::streamFor('hi kms') )); $result = $eClient->getObject(new Oss\Models\GetObjectRequest( bucket: $bucket, key: $key, )); $data = $result->body->getContents(); echo "get object data: " . $data;

[上一篇：数据加密](products/oss/documents/user-guide/data-encryption.md)[下一篇：服务端加密](products/oss/documents/user-guide/server-side-encryption-8.md)

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
