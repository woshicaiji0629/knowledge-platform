# 示例代码仅供参考，请勿直接在生产环境中使用 # Celery 伪代码示例 from celery import Celery from dashscope.threads import Runs celery_app = Celery('tasks', broker='redis://localhost:6379/0') @celery_app.task def process_run(thread_id, assistant_id): run = Runs.create(thread_id=thread_id, assistant_id=assistant_id) final_run = Runs.wait(run.id, thread_id=thread_id, timeout_seconds=60) return final_run.id4.2.3 水平扩容 vs 垂直扩容
水平扩容（Scale Out）：增加更多应用实例或容器节点，每个节点都可以调用 DashScope API；
垂直扩容（Scale Up）：升级服务器配置（CPU、内存、带宽），单机支持更多并发请求。
在现代云原生环境中，更常见的是水平扩容。配合容器编排（如 Kubernetes）或自动伸缩（Auto Scaling），可在请求量高峰时自动增加副本数，并在低峰时收缩，节省成本。
