## API
您可以在创建LogStore的过程中，通过API调用[创建](developer-reference/api-sls-2020-12-30-createlogstore.md)[LogStore](developer-reference/api-sls-2020-12-30-createlogstore.md)传递ttl（数据保存时间）、hot_ttl（热存储数据保存时间）、infrequentAccessTTL（低频存储数据保存时间）参数来配置存储分层的保留策略。
同样地，对于已经创建的LogStore，您也可以通过调用[更新](developer-reference/api-sls-2020-12-30-updatelogstore.md)[LogStore](developer-reference/api-sls-2020-12-30-updatelogstore.md)接口，更新ttl、hot_ttl和infrequentAccessTTL参数的值，来动态调整存储分层的保留策略，以满足您对数据保留和成本控制的需求。
