| 类型 | 命令 | 语法 | 说明 | 版本变更 |
| --- | --- | --- | --- | --- |
| 写操作 | [TR.SETBIT](tairroaring-command.md) | TR.SETBIT key offset value | 设置 Roaring Bitmap 中指定偏移量（offset）的 bit 值（1 或者 0），并返回该 bit 位之前的值，Roaring Bitmap 的偏移量（offset）从 0 开始。 | -（表示未更新） |
| [TR.SETBITS](tairroaring-command.md) | TR.SETBITS key offset [offset1 offset2 ... offsetN] | 设置 Roaring Bitmap 中指定偏移量（offset）的 bit 值为 1，支持传入多个值。 | V2 新增 |  |
| [TR.CLEARBITS](tairroaring-command.md) | TR.CLEARBITS key offset [offset1 offset2 ... offsetN] | 设置 Roaring Bitmap 中指定偏移量（offset）的 bit 值为 0，若原值为 0 则不操作，支持传入多个值。 | V2 新增 |  |
| [TR.SETRANGE](tairroaring-command.md) | TR.SETRANGE key start end | 设置 Roaring Bitmap 中指定区间（偏移量）的 bit 值为 1。 | V2 更新，更新返回值为成功设置 bit 值为 1 的数量。 |  |
| [TR.APPENDBITARRAY](tairroaring-command.md) | TR.APPENDBITARRAY key offset bitarray | 将由连续的 0 或 1 组成的 bit 数组（bitarray）插入到 Roaring Bitmap 中指定偏移量（offset）之后的位置，并覆盖原有数据。 | V2 新增 |  |
| [TR.FLIPRANGE](tairroaring-command.md) | TR.FLIPRANGE key start end | 对 Roaring Bitmap 中指定区间（偏移量）的 bit 值执行位反转（1 反转为 0；0 反转为 1）。若指定 key 不存在，则自动创建目标 key，并以空 Roaring Bitmap 对指定区间的 bit 值执行位反转。 | V2 新增 |  |
| [TR.APPENDINTARRAY](tairroaring-command.md) | TR.APPENDINTARRAY key value [value1
