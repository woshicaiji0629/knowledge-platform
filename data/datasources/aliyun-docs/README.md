# Aliyun Docs Crawled Data

This directory stores Git-tracked crawler output for the Aliyun Docs data source.

```text
raw/       Raw HTML files saved by URL hash.
metadata/  Crawl metadata JSON files saved by URL hash.
```

Do not put Docker service volumes here. Runtime data for MySQL, Redis, vector stores, and similar services must use a separate runtime directory.
