### standard
基于[Unicode](https://unicode.org/reports/tr29/)[文本切割算法](https://unicode.org/reports/tr29/)拆分文档，适用于多数语言。
可选参数：
max_token_length：每个Token的长度上限，默认为255。若Token超过该长度，会根据指定的长度上限对Token进行拆分。
配置示例：
