控制最大连接数。在高并发场景下，适当增加此值可以提高并发能力。 |
| limit_per_host | 每个主机的连接数限制 | 0（无限制） | 限制对单个主机的最大连接数，避免对单一服务端造成过大压力。 |
| ssl | SSL 上下文配置 | None | 用于 HTTPS 连接的 SSL 证书验证配置。 |

代码示例
运行代码前，请[配置](first-api-call-to-qwen.md)[API Key](first-api-call-to-qwen.md)[到环境变量](first-api-call-to-qwen.md)并[安装最新版](install-sdk.md)[SDK](install-sdk.md)。
以下代码示例展示了如何在异步场景下配置连接复用，并调用大模型服务：
import asyncio import aiohttp import ssl import certifi from dashscope import AioGeneration import dashscope import os async def main(): # 以下为华北2（北京）地域的URL，各地域的URL不同。 dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1' # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # 若没有配置环境变量，请用百炼API Key将下行替换为：dashscope.api_key = "sk-xxx" dashscope.api_key = os.getenv("DASHSCOPE_API_KEY") # 配置连接参数 connector = aiohttp.TCPConnector( limit=100, # 总连接数限制 limit_per_host=30, # 每个主机的连接数限制 ssl=ssl.create_default_context(cafile=certifi.where()), ) # 创建自定义Session并传入调用方法 async with aiohttp.ClientSession(connector=connector) as session: response = await AioGeneration.call( model='qwen-plus', prompt='你好，请介绍一下你自己', session=session, # 传入自定义 Session ) print(response) asyncio.run(main())
