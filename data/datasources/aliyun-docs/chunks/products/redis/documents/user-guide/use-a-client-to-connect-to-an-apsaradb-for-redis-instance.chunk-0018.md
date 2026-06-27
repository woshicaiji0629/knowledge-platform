(reply->type == REDIS_REPLY_ARRAY) { for (j = 0; j < reply->elements; j++) { printf("%u) %s\n", j, reply->element[j]->str); } } freeReplyObject(reply); /* Disconnects and frees the context */ redisFree(c); return 0; }
编译上述代码。
gcc -o example -g example.c -I /usr/local/include/hiredis -lhiredis
测试运行，完成连接。
./example r-bp10noxlhcoim2****.redis.rds.aliyuncs.com 6379 r-bp10noxlhcoim2**** password
