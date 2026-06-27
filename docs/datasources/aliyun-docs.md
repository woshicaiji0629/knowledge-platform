# Aliyun Docs Data Source

## Scope

Aliyun Docs is the first document data source for the knowledge platform. It is a data source connector, not a separate service boundary.

Allowed domains:

- `help.aliyun.com`
- `www.alibabacloud.com`

## Data Directory

Crawler output is stored under a source-specific Git-tracked directory:

```text
data/
  datasources/
    aliyun-docs/
      products/
        ecs/
          raw/
          documents/
          metadata/
        redis/
          raw/
          documents/
          metadata/
      seeds.json
      manifest.json
      cleaned/
        products/
          ecs/
            documents/
            metadata/
      cleaned-manifest.json
      chunks/
        products/
          ecs/
            documents/
            metadata/
      chunk-manifest.json
      quality-report.json
```

Future sources must use separate sibling directories, for example:

```text
data/
  datasources/
    tencent-cloud/
      products/
        cvm/
          raw/
          documents/
          metadata/
```

Runtime storage for Docker services must stay outside this directory. MySQL, Redis, vector database, and other mounted volumes should use a separate runtime directory such as:

```text
runtime-data/
  mysql/
  redis/
  vector-store/
```

## File Naming

Each crawled page is saved under its product directory. URL paths are mapped to local paths:

```text
https://help.aliyun.com/zh/ecs/
  -> data/datasources/aliyun-docs/products/ecs/raw/index.html
  -> data/datasources/aliyun-docs/products/ecs/documents/index.md
  -> data/datasources/aliyun-docs/products/ecs/metadata/index.json

https://help.aliyun.com/zh/ecs/pricing
  -> data/datasources/aliyun-docs/products/ecs/raw/pricing.html
  -> data/datasources/aliyun-docs/products/ecs/documents/pricing.md
  -> data/datasources/aliyun-docs/products/ecs/metadata/pricing.json
```

The metadata file records:

- source
- product
- topic
- url
- title
- fetched_at
- status_code
- content_type
- raw_path
- document_path

The global `manifest.json` records crawled documents across products in crawl order.

## Cleaned Data Layer

The `cleaned/` directory stores Markdown documents that passed the first quality filter for product Q&A.

The cleaner:

- removes common navigation, search, console, favorite, and previous/next page noise
- keeps source URL headers
- keeps Markdown tables
- rewrites local product document links to relative cleaned-document links
- discards very short or directory-like pages
- marks Aliyun anti-bot verification pages as `anti_bot_page`
- writes per-document metadata with link and table counts

Cleaning outputs:

```text
data/datasources/aliyun-docs/cleaned/products/<product>/documents/
data/datasources/aliyun-docs/cleaned/products/<product>/metadata/
data/datasources/aliyun-docs/cleaned-manifest.json
data/datasources/aliyun-docs/quality-report.json
```

The cleaned layer is the preferred input for RAG indexing. Raw crawler output remains useful for traceability and future re-cleaning.

Current cleaned output:

- accepted documents: 1206
- candidate documents: 0
- discarded pages: 583

## Chunk Data Layer

The `chunks/` directory stores Markdown chunks generated from `cleaned-manifest.json`.

The chunker:

- splits by Markdown heading structure first
- keeps table blocks together where possible
- filters heading-only chunks without meaningful body text
- writes one Markdown file and one metadata JSON file per chunk
- records product, topic, title, source URL, cleaned document path, heading path, and chunk index
- records the registered chunking strategy and parameters in `chunk-manifest.json`

Clean and chunk jobs support bounded concurrent file workers:

```bash
cd backend
uv run python -m knowledge_platform.scripts.clean_aliyun_docs --workers 8
uv run python -m knowledge_platform.scripts.chunk_aliyun_docs \
  --chunker markdown-heading-table-preserve \
  --workers 8
```

## Vector Index Layer

Vector database runtime data is stored outside the source data directory:

```text
runtime-data/
  vector-store/
```

Local Qdrant can be started from the repository root:

```bash
docker compose -f docker-compose.vector.yml up -d
```

DashScope embeddings are read from environment variables. The API key must not be committed:

```bash
export DASHSCOPE_API_KEY=...
export DASHSCOPE_EMBEDDING_MODEL=text-embedding-v4
```

Index chunks into Qdrant:

```bash
cd backend
uv run python -m knowledge_platform.scripts.index_aliyun_docs \
  --collection aliyun_docs_product_v1 \
  --batch-size 10 \
  --concurrency 2
```

Search indexed chunks:

```bash
cd backend
uv run python -m knowledge_platform.scripts.search_aliyun_docs \
  --collection aliyun_docs_product_v1 \
  --limit 5
```

Chunk outputs:

```text
data/datasources/aliyun-docs/chunks/products/<product>/documents/
data/datasources/aliyun-docs/chunks/products/<product>/metadata/
data/datasources/aliyun-docs/chunk-manifest.json
```

Current chunk output:

- source documents: 1206
- chunks: 20920
- chunking strategy: `markdown-heading-table-preserve`
- default chunk size: 1200 characters with 160 characters overlap for long blocks

## First Batch Products

The first product QA batch focuses on:

- `ecs`: cloud server selection, pricing, deployment, features, performance
- `rds`: MySQL database selection, pricing, deployment, backup, performance
- `redis`: cache selection, pricing, connection, performance, troubleshooting
- `oss`: object storage features, pricing, permissions, CDN integration
- `model-studio`: model selection, API calling, app building, pricing
- `slb`: ALB/NLB/CLB selection, routing, health checks, pricing
- `vpc`: network planning, connectivity, isolation, troubleshooting
- `cdn`: acceleration, cache, HTTPS, OSS origin, pricing
- `sls`: log collection, query, alerting, delivery, pricing
- `ack`: Kubernetes clusters, workloads, ingress, elasticity, deployment

## Current Crawler Behavior

The current crawler:

- validates seed URLs against the allowed Aliyun domains
- crawls pages breadth-first
- respects `max_pages` and `max_depth`
- saves raw HTML into product-specific directories
- writes local Markdown documents for later review and indexing
- rewrites Aliyun links in Markdown to local document paths where possible
- converts basic HTML tables to Markdown tables
- skips Aliyun anti-bot verification pages instead of saving them as normal documents
- infers a coarse topic such as `features`, `pricing`, `deployment`, `performance`, `troubleshoot`, or `selection`
- returns internal `RawDocument` objects for later chunking and indexing

## Boundaries

The crawler does not yet implement:

- robots.txt policy handling
- request throttling configuration
- retry and backoff
- persistent crawl job state
- HTML cleaning rules tuned for Aliyun page structure
- embedding or vector database writes

These rules should be confirmed before expanding the crawler beyond the MVP.
