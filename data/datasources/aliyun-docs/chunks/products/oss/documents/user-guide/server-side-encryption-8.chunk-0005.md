## 操作方式
重要
如果您购买了KMS密钥轮转的增值服务，则服务端加密将支持对KMS密钥进行[密钥轮转](../../../kms/documents/key-management-service/user-guide/configure-key-rotation.md)。开启密钥轮转后，新密钥只对新写入的Object生效，密钥轮转前的存量Object的加密密钥保持不变。
如果您通过OSS更新KMS加密密钥，则新密钥仅适用于新写入的文件加密。更新密钥前写入的存量文件仍使用旧密钥加密。因此，更新密钥后不能删除旧密钥，否则会影响存量文件的正常访问。
