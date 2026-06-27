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
      raw/
      metadata/
```

Future sources must use separate sibling directories, for example:

```text
data/
  datasources/
    tencent-cloud/
      raw/
      metadata/
```

Runtime storage for Docker services must stay outside this directory. MySQL, Redis, vector database, and other mounted volumes should use a separate runtime directory such as:

```text
runtime-data/
  mysql/
  redis/
  vectorstore/
```

## File Naming

Each crawled page uses a stable URL hash as the file name:

```text
data/datasources/aliyun-docs/raw/<url_hash>.html
data/datasources/aliyun-docs/metadata/<url_hash>.json
```

The metadata file records:

- source
- url
- title
- fetched_at
- status_code
- content_type
- raw_path

## Current Crawler Behavior

The current crawler:

- validates seed URLs against the allowed Aliyun domains
- crawls pages breadth-first
- respects `max_pages` and `max_depth`
- saves raw HTML into the Aliyun source directory
- extracts title, plain text, and links using Python standard library parsing
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
