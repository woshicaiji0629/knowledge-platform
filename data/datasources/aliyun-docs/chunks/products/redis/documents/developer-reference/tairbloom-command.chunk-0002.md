## 基于TairBloom优化爬虫系统
在面对海量的URL时，将已经爬取过的URL进行过滤、去重操作，减少重复爬取的无效工作量，伪代码如下：
bool crawlerSystem( ) { while (true) { // 获取待爬取的URL。 url = getURLFromQueue() if (bf.exists(url_bloom, url)) { // 如果该URL可能已被爬取，则跳过。 continue; } else { // 爬取该URL内容。 doDownload(url) // 并将该URL加入TairBloom。 bf.add(url_bloom, url); } } }
