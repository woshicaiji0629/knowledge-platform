## ossutil
创建一个名为inventory-configuration.xml的文件，内容如下：
<?xml version="1.0" encoding="UTF-8"?> <InventoryConfiguration> <Id>report1</Id> <IsEnabled>true</IsEnabled> <Destination> <OSSBucketDestination> <Format>CSV</Format> <AccountId>100000000000000</AccountId> <RoleArn>acs:ram::100000000000000:role/AliyunOSSRole</RoleArn> <Bucket>acs:oss:::destbucket</Bucket> <Prefix>prefix1/</Prefix> <Encryption> <SSE-KMS> <KeyId>keyId</KeyId> </SSE-KMS> </Encryption> </OSSBucketDestination> </Destination> <Schedule> <Frequency>Daily</Frequency> </Schedule> <IncludedObjectVersions>All</IncludedObjectVersions> <OptionalFields> <Field>Size</Field> <Field>LastModifiedDate</Field> <Field>ETag</Field> <Field>StorageClass</Field> <Field>IsMultipartUploaded</Field> <Field>EncryptionStatus</Field> </OptionalFields> </InventoryConfiguration>
执行以下命令：
ossutil api put-bucket-inventory --bucket examplebucket --inventory-id report1 --inventory-configuration file://inventory-configuration.xml
注意：关于put-bucket-inventory命令的详细用法，请参考[put-bucket-inventory](../developer-reference/put-bucket-inventory.md)。
