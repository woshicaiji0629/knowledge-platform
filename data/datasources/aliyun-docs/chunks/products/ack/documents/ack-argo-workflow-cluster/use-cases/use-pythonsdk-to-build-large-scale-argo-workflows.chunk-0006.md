## 场景二：Map-Reduce
在Argo Workflows中实现MapReduce风格的数据处理的关键在于有效利用其DAG（有向无环图）模板，以组织和协调多个任务，从而模拟Map和Reduce阶段。以下是一个更加详细的示例，展示了如何使用Hera构建一个简单的MapReduce工作流，用于处理文本文件的单词计数任务。每一步都是一个Python函数，便于和Python生态进行集成。
[配置](../user-guide/configure-artifacts.md)[Artifacts](../user-guide/configure-artifacts.md)。
使用以下内容，创建map-reduce.py。
展开查看代码内容
from hera.workflows import DAG, Artifact, NoneArchiveStrategy, Parameter, OSSArtifact, Workflow, script from hera.shared import global_config import urllib3 urllib3.disable_warnings() # 设置访问地址。 global_config.host = "https://{{argo_server_IP}}:2746" global_config.token = "abcdefgxxxxxx" # 填入之前获取的Token。 global_config.verify_ssl = "" # 使用script装饰函数时，将script参数传递给script装饰器。这包括image、inputs、outputs、resources等。 @script( image="mirrors-ssl.aliyuncs.com/python:alpine3.6", inputs=Parameter(name="num_parts"), outputs=OSSArtifact(name="parts", path="/mnt/out", archive=NoneArchiveStrategy(), key="{{workflow.name}}/parts"), ) def split(num_parts: int) -> None: # 根据输入参数num_parts创建多个文件，文件中写入foo字符和parts编号 import json import os import sys os.mkdir("/mnt/out") part_ids = list(map(lambda x: str(x), range(num_parts))) for i, part_id in enumerate(part_ids, start=1): with open("/mnt/out/"
