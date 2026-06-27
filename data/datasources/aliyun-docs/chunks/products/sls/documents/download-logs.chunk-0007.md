### 通过命令行工具下载
当您需要下载更大数量的日志时，可以通过命令行工具进行下载。
安装命令行工具。具体操作，请参见[安装](developer-reference/install-log-service-cli.md)[CLI](developer-reference/install-log-service-cli.md)。
获取当前账号的AccessKey。具体操作，请参见[访问密钥](developer-reference/access-key.md)。
获取下载日志的命令。具体步骤，请参见[get_log_all](developer-reference/get-log-all.md)。
例如：在命令行工具中执行下载命令，执行成功后自动下载到运行命令行的当前目录下的downloaded_data.txt。
aliyunlog log get_log_all --project="aliyun-test-project" --logstore="aliyun-test-logstore" --from_time="2024-07-01 15:33:00+8:00" --to_time="2024-07-09 15:23:00+8:00" --query="status:200|select request_method as method,COUNT(*) as pv group by method order by pv" --region-endpoint="cn-hangzhou.log.aliyuncs.com" --format-output=json --access-id="LT***CyGg" --access-key="8P***zi" >> ./downloaded_data.txt
更多信息，请参见[使用日志服务](developer-reference/overview-of-log-service-cli.md)[CLI](developer-reference/overview-of-log-service-cli.md)。
