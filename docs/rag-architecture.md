# RAG Architecture Skeleton

## 目标

本项目第一阶段先搭建阿里云官方文档问答系统骨架。阿里云官方文档是第一个数据源，系统设计不能绑定阿里云，后续需要支持其他官方文档、内部知识库、数据库和业务 API。

## 当前骨架

当前代码只实现模块边界和占位流程：

- `crawlers/`：数据采集入口和阿里云官方文档采集计划
- `documents/`：原始文档模型和字符切块器
- `vectorstores/`：向量库接口和内存检索占位实现
- `llm/`：规则型意图识别占位实现
- `sessions/`：内存会话和消息存储
- `services/`：检索、问答、采集计划编排
- `api/v1/routes/chat.py`：会话问答 API
- `api/v1/routes/ingestion.py`：采集计划 API

当前不做真实网络爬取、不调用 embedding 模型、不写入真实向量数据库、不调用 LLM。

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

  llm/
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

当前只生成计划，不真实爬取。

## 后续实施顺序

1. 实现阿里云文档真实爬取，包含 robots、限速、重试和缓存。
2. 实现 HTML 清洗，保留标题、正文、代码块、表格和来源 URL。
3. 实现稳定切块策略，按标题结构优先，保留 overlap。
4. 接入 embedding 模型。
5. 接入真实向量数据库。
6. 实现检索召回和引用来源展示。
7. 接入 LLM 回答生成。
8. 将会话存储从内存替换为 SQLite 或业务数据库。
9. 增加数据源管理、采集任务状态和索引状态页面。

## 待确认

- 第一批阿里云官方文档 URL。
- 允许的爬取频率和缓存策略。
- embedding/LLM 供应商。
- 向量数据库选型。
- 会话是否需要持久化。
- 是否需要后台任务队列处理采集和入库。
