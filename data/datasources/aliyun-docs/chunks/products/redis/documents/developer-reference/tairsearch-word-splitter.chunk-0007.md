### IK
中文分词器，兼容ES的IK分词器插件。分为ik_max_word和ik_smart模式，ik_max_word模式会拆分出文档中所有可能存在的Token，ik_smart模式会在ik_max_word的基础上，对Token进行二次识别，选择出最有可能的Token。
说明
以“Redis是完全开源免费的，遵守BSD协议，是一个灵活的高性能key-value数据结构存储，可以用来作为数据库、缓存和消息队列。Redis比其他key-value缓存产品有以下三个特点：Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载到内存使用。”文档为例，ik_max_word和ik_smart的Token如下：
ik_max_word：
redis 是 完全 全开 开源 免费 的 遵守 bsd 协议 是 一个 一 个 灵活 的 高性能 性能 key-value key value 数据结构 数据 结构 存储 可以用 可以 用来 来作 作为 数据库 数据 库 缓存 和 消息 队列 redis 比 其他 key-value key value 缓存 产品 有 以下 三个 三 个 特点 redis 支持 数据 的 持久 化 可以 将 内存 中 的 数据 保存 存在 磁盘 中 重启 的 时候 可以 再次 加载 载到 内存 使用
ik_smart：
redis 是 完全 开源 免费 的 遵守 bsd 协议 是 一个 灵活 的 高性能 key-value 数据结构 存储 可以 用来 作为 数据库 缓存 和 消息 队列 redis 比 其他 key-value 缓存 产品 有 以下 三个 特点 redis 支持 数据 的 持久 化 可以 将 内存 中 的 数据 保 存在 磁盘 中 重启 的 时候 可以 再次 加 载到 内存 使用
组成部分：
Tokenizer：[IK Tokenizer](tairsearch-word-splitter.md)。
可选参数：
stopwords：停用词，分词器会过滤这些词。数组类型，单个停用词必须是字符串。配置后，会覆盖默认停用词。默认停用词如下：
["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"]
userwords：自定义词典，数组类型，单个词必须是字符串，配置后会追加至默认词典中。默认词典请参见[IK](h
