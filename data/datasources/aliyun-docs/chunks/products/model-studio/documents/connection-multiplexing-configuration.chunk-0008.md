### HTTP同步调用方式
在同步调用场景中，您可以通过requests.Session实现连接复用。在同一个 Session 内的多次请求会复用底层 TCP 连接，避免重复建立连接的开销。
代码示例
运行代码前，请[配置](first-api-call-to-qwen.md)[API Key](first-api-call-to-qwen.md)[到环境变量](first-api-call-to-qwen.md)并[安装最新版](install-sdk.md)[SDK](install-sdk.md)。
以下代码示例展示了如何在同步场景下配置连接复用，并调用大模型服务：
import requests from dashscope import Generation import dashscope import os # 以下为华北2（北京）地域的URL，各地域的URL不同。 dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1' # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # 若没有配置环境变量，请用百炼API Key将下行替换为：dashscope.api_key = "sk-xxx" dashscope.api_key = os.getenv("DASHSCOPE_API_KEY") # 使用 with 语句确保 Session 正确关闭 with requests.Session() as session: response = Generation.call( model='qwen-plus', prompt='你好', session=session # 传入自定义 Session ) print(response)
如果需要在多次调用中复用同一个 Session，可以采用以下方式：
import requests from dashscope import Generation import dashscope import os # 以下为华北2（北京）地域的URL，各地域的URL不同。 dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1' # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # 若没有配置环境变量，请用百炼API Key将下行替换为：dashscope.api_key = "sk-xxx" dashscope.api_
