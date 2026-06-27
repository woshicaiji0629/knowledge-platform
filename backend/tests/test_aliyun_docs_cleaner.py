from pathlib import Path

from knowledge_platform.scripts.clean_aliyun_docs import clean_document, clean_markdown


def test_clean_markdown_preserves_tables_and_rewrites_local_links(tmp_path: Path) -> None:
    data_root = tmp_path / "aliyun-docs"
    source_path = data_root / "products" / "ecs" / "documents" / "user-guide" / "instance.md"
    markdown = """# Raw Title

Source: https://help.aliyun.com/zh/ecs/user-guide/instance

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)

[AI 助理](https://www.aliyun.com/ai-assistant)

# 创建 ECS 实例

更新时间：

复制 MD 格式

本文介绍如何创建 ECS 实例，并选择适合业务负载的实例规格。

[实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)

| 类别 | 说明 |
| --- | --- |
| 规格 | 用于定义计算资源 |

[上一篇: xxx](products/ecs/documents/previous.md)[下一篇: yyy](products/ecs/documents/next.md)
"""

    cleaned = clean_markdown(markdown=markdown, source_path=source_path, data_root=data_root)

    assert "AI 助理" not in cleaned
    assert "复制 MD 格式" not in cleaned
    assert "上一篇" not in cleaned
    assert "# 创建 ECS 实例" in cleaned
    assert "| 类别 | 说明 |" in cleaned
    assert "](overview-of-instance-families.md)" in cleaned


def test_clean_document_discards_short_directory_page(tmp_path: Path) -> None:
    data_root = tmp_path / "aliyun-docs"
    source_path = data_root / "products" / "ack" / "documents" / "index.md"
    source_path.parent.mkdir(parents=True)
    source_path.write_text(
        "# https://help.aliyun.com/zh/ack/\n\nSource: https://help.aliyun.com/zh/ack/\n\n",
        encoding="utf-8",
    )
    document = {
        "id": "ack:index",
        "source": "aliyun_docs",
        "product": "ack",
        "topic": "features",
        "title": "https://help.aliyun.com/zh/ack/",
        "url": "https://help.aliyun.com/zh/ack/",
        "document_path": str(source_path),
    }

    cleaned_document = clean_document(data_root=data_root, document=document)

    assert cleaned_document.quality == "discarded"
    assert cleaned_document.discard_reason == "too_short"
    assert not Path(cleaned_document.cleaned_document_path).exists()


def test_clean_document_writes_candidate_for_short_reviewable_page(tmp_path: Path) -> None:
    data_root = tmp_path / "aliyun-docs"
    source_path = data_root / "products" / "ecs" / "documents" / "short.md"
    source_path.parent.mkdir(parents=True)
    source_path.write_text(
        "# 短文档\n\n"
        "Source: https://help.aliyun.com/zh/ecs/short\n\n"
        "# 连接实例\n\n"
        "本文介绍如何连接 ECS 实例，并配置登录凭据。适用于快速排查连接问题。"
        "连接前需要确认实例状态、安全组规则、公网地址、用户名和密码或密钥。"
        "如果连接失败，可以先检查网络连通性，再检查远程登录服务和账号权限。\n",
        encoding="utf-8",
    )
    document = {
        "id": "ecs:short",
        "source": "aliyun_docs",
        "product": "ecs",
        "topic": "deployment",
        "title": "短文档",
        "url": "https://help.aliyun.com/zh/ecs/short",
        "document_path": str(source_path),
    }

    cleaned_document = clean_document(data_root=data_root, document=document)

    assert cleaned_document.quality == "candidate"
    assert cleaned_document.discard_reason == "short_but_reviewable"
    assert Path(cleaned_document.cleaned_document_path).is_file()
    assert "/candidates/" in cleaned_document.cleaned_document_path


def test_clean_document_marks_anti_bot_raw_page(tmp_path: Path) -> None:
    data_root = tmp_path / "aliyun-docs"
    source_path = data_root / "products" / "ecs" / "documents" / "index.md"
    raw_path = data_root / "products" / "ecs" / "raw" / "index.html"
    source_path.parent.mkdir(parents=True)
    raw_path.parent.mkdir(parents=True)
    source_path.write_text(
        "# https://help.aliyun.com/zh/ecs/\n\nSource: https://help.aliyun.com/zh/ecs/\n\n",
        encoding="utf-8",
    )
    raw_path.write_text(
        "<script>window.location.replace('/_____tmd_____/punish?x5secdata=test')</script>",
        encoding="utf-8",
    )
    document = {
        "id": "ecs:index",
        "source": "aliyun_docs",
        "product": "ecs",
        "topic": "features",
        "title": "https://help.aliyun.com/zh/ecs/",
        "url": "https://help.aliyun.com/zh/ecs/",
        "document_path": str(source_path),
        "raw_path": str(raw_path),
    }

    cleaned_document = clean_document(data_root=data_root, document=document)

    assert cleaned_document.quality == "discarded"
    assert cleaned_document.discard_reason == "anti_bot_page"
    assert not Path(cleaned_document.cleaned_document_path).exists()
