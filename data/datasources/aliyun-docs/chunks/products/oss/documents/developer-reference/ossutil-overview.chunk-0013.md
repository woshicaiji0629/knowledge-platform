### 运行命令
创建Bucket。
ossutil mb oss://examplebucket
以下输出结果表明已成功创建examplebucket。
0.668238(s) elapsed
上传文件到Bucket。
创建本地文件uploadFile.txt。
echo 'Hello, OSS!' > uploadFile.txt
上传文件到存储空间examplebucket。
ossutil cp uploadFile.txt oss://examplebucket
以下输出结果表明文件已成功上传至examplebucket。
Success: Total 1 file, size 12 B, Upload done:(1 objects, 12 B), avg 44 B/s 0.271779(s) elapsed
下载文件。
将已上传的示例文件uploadFile.txt从examplebucket下载至本地localfolder文件夹下。
ossutil cp oss://examplebucket/uploadFile.txt localfolder/
以下输出结果表明文件已成功下载至本地localfolder文件夹下。
Success: Total 1 object, size 12 B, Download done:(1 files, 12 B), avg 74 B/s 0.162447(s) elapsed
列举examplebucket下的文件。
ossutil ls oss://examplebucket
以下输出结果表明已成功列举examplebucket下的文件。
LastModifiedTime Size(B) StorageClass ETAG ObjectName 2024-11-26 14:35:29 +0800 CST 12 Standard 1103F650EB2C292D179A032D2A97B0F5 oss://examplebucket/uploadFile.txt Object Number is: 1 0.124679(s) elapsed
删除examplebucket下的uploadFile.txt。
ossutil rm oss://examplebucket/uploadFile.txt
以下输出结果表明已成功删除examplebucket下的uploadFile.txt。
0.295530(s) elapsed
删除examplebucket。
ossutil rb oss://examplebucket
以下输出结果表明已成功删除examplebucket。
0.478659(s) elapsed
