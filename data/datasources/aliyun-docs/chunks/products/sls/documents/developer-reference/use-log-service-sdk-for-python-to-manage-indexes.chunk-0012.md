## 删除索引示例代码
以下代码用于删除指定LogStore的索引信息。
from aliyun.log import LogClient, IndexConfig import os # 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 accessKeyId = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID', '') accessKey = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET', '') # 日志服务的服务接入点。此处以杭州为例，其它地域请根据实际情况填写。 endpoint = "cn-hangzhou.log.aliyuncs.com" # 创建日志服务Client。 client = LogClient(endpoint, accessKeyId, accessKey) # Project名称。 project_name = "ali-test-project" # Logstore名称。 logstore_name = "ali-test-logstore2" if __name__ == '__main__': # 删除索引。 print("ready to delete index") client.delete_index(project_name, logstore_name) print("delete index success ")
预期结果如下：
ready to delete index delete index success
