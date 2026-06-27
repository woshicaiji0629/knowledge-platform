S256或SM4，并指定具体的CMK ID。此后，所有上传至此Bucket的Object都会被加密。
为目标Object配置加密方式
上传Object或修改Object的meta信息时，在请求中携带x-oss-server-side-encryption参数，并设置参数值为KMS；携带x-oss-server-side-encryption-key-id参数，并设置参数值为指定CMK ID。此时，OSS将使用指定的KMS CMK，并通过AES256加密算法加密Object。如需修改加密算法，您还需增加x-oss-server-side-data-encryption参数，并设置参数值为SM4。更多信息，请参见[PutObject](../developer-reference/putobject.md)。
