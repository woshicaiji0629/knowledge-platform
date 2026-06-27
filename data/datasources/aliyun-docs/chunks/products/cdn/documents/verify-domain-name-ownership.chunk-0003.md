## 方法二：文件验证
在验证页面，单击方法2: 文件验证。
重要
在验证完成前请不要关闭验证页面。
单击verification.html，下载验证文件。
手动将验证文件上传到您主域名服务器（例如您的ECS、OSS、CVM、COS、EC2等）的根目录。例如：当前加速域名为image.example.com，您需要将该文件上传至example.com的根目录下。
确保可通过http://example.com/verification.html访问到该文件后，即可点击验证进行验证。
阿里云CDN后台将访问您服务器中http://example.com/verification.html文件链接进行验证。
如果文件内的记录值与验证文件记录值一致，则通过验证。
如果验证失败，请确保上述文件链接可访问，并且您上传的文件正确。
