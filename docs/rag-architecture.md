# RAG Architecture

## 目标

本项目第一阶段先搭建阿里云官方文档问答系统骨架。阿里云官方文档是第一个数据源，系统设计不能绑定阿里云，后续需要支持其他官方文档、内部知识库、数据库和业务 API。

## 当前实现

当前代码已经形成阿里云官方文档 RAG 的第一版闭环：

- `crawlers/`：阿里云官方文档采集入口
- `documents/`：原始文档模型、清洗产物和切块器
- `embeddings/`：DashScope embedding Provider
- `vectorstores/`：内存检索和 Qdrant 向量库实现
- `llm/`：规则型意图识别、占位回答和 DashScope 回答生成
- `sessions/`：内存会话和消息存储
- `services/`：检索、问答、采集计划编排
- `api/v1/routes/chat.py`：会话问答 API
- `api/v1/routes/ingestion.py`：采集计划 API

默认配置仍使用内存检索和占位回答，避免本地开发时产生外部调用费用。设置 `VECTOR_STORE_PROVIDER=qdrant` 和 `ANSWER_GENERATOR_PROVIDER=dashscope` 后，会使用本地 Qdrant 索引、DashScope embedding 和 DashScope 文本生成。

## 目标链路

```text
Aliyun Docs URLs
  -> Crawler
  -> Raw HTML/Text
  -> Parser/Cleaner
  -> Chunker
  -> Embedding
  -> Vector Store
  -> Retrieval
  -> Intent + Session Context
  -> LLM Answer
  -> Frontend Chat UI
```

## 后端模块

```text
backend/src/knowledge_platform/
  crawlers/
    base.py
    aliyun_docs.py

  documents/
    models.py
    chunker.py

  vectorstores/
    base.py
    memory.py
    qdrant.py

  llm/
    answer.py
    intent.py

  sessions/
    models.py
    store.py

  services/
    chat_service.py
    retrieval_service.py
    ingestion_service.py
    factory.py
```

## 数据源原则

阿里云官方文档只是一种 `DocumentDataSource`，不是系统核心模型。后续新增数据源时，应复用以下通用流程：

```text
DataSource -> Crawler/Connector -> Document -> Chunk -> VectorStore -> Retrieval -> Answer
```

不要把阿里云字段直接扩散到会话、检索和回答生成层。阿里云专有字段应在 connector 或 mapper 层转换成内部文档模型。

## API 骨架

### 会话问答

```http
POST /api/v1/chat/sessions/{session_id}/messages
```

请求：

```json
{
  "message": "阿里云智能客服如何配置？"
}
```

响应包含：

- 会话信息
- 助手消息
- 意图识别结果
- 引用来源列表

### 采集计划

```http
POST /api/v1/ingestion/aliyun-docs/plan
```

请求：

```json
{
  "seed_urls": ["https://help.aliyun.com/"],
  "max_pages": 20,
  "max_depth": 1
}
```

当前采集计划接口只生成计划；真实采集、清洗、切块和入库通过 `scripts/` 下的命令执行。

## 后续实施顺序

1. 将会话存储从内存替换为 SQLite 或业务数据库。
2. 增加数据源管理、采集任务状态和索引状态页面。
3. 增加回答质量评测集，对比不同切块、召回和模型配置。
4. 将采集、清洗、切块、入库流程服务化，支持后台任务和重试。
5. 扩展更多产品文档和内部知识库数据源。

## 待确认

- 会话是否需要持久化。
- 是否需要后台任务队列处理采集和入库。
- 生产环境默认使用哪个 DashScope 文本模型。
- 回答是否需要更严格的引用编号格式。
