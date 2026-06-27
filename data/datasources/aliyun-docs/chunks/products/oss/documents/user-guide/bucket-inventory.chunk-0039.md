ld>StorageClass</Field> <Field>LastModifiedDate</Field> <Field>ETag</Field> <Field>IsMultipartUploaded</Field> <Field>ObjectType</Field> <Field>ObjectAcl</Field> <Field>Crc64</Field> <Field>EncryptionStatus</Field> </OptionalFields> </IncrementalInventory> </InventoryConfiguration>
执行以下命令：
ossutil api put-bucket-inventory --bucket examplebucket --inventory-id report1 --inventory-configuration file://inventory-configuration.xml注意：关于put-bucket-inventory命令的详细用法，请参考[put-bucket-inventory](../developer-reference/put-bucket-inventory.md)。
