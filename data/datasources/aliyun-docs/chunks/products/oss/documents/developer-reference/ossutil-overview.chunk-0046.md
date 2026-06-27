### 命令选项类型

| 选项类型 | 选项 | 说明 |
| --- | --- | --- |
| 字符串 | --option string | 字符串参数可以包含 ASCII 字符集中的字母数字字符、符号和空格。 如果包含空格时，需要用引号引起来。 例如：--acl private。 |
| 布尔值 | --option | 打开或关闭某一选项。 例如：--dry-run。 |
| 整数 | --option Int | 无符号整数。 例如：--read-timeout 10。 |
| 时间戳 | --option Time | ISO 8601 格式，即 DateTime 或 Date。 例如：--max-mtime 2006-01-02T15:04:05。 |
| 字节单位后缀 | --option SizeSuffix | 默认单位是字节（B），也可以使用单位后缀形式，支持的单位后缀为：K（KiB）=1024 字节、M（MiB）、G（GiB）、G（GiB）、T（TiB）、P（PiB）、E（EiB） 例如：最小 size 为 1024 字节 --min-size 1024 --min-size 1K |
| 时间单位后缀 | --option Duration | 时间单位，默认单位是秒。支持的单位后缀为：ms 毫秒，s 秒，m 分钟，h 小时，d 天，w 星期，M 月，y 年。 支持小数。例如：1.5 天 --min-age 1.5d |
| 字符串列表 | --option strings | 支持单个或者多个同名选项，支持以逗号（,）分隔的多个值。 支持多选项输入的单值。 例如：--metadata user=jack,email=ja**@test.com --metadata address=china |
| 字符串数组 | --option stringArray | 支持单个或者多个同名选项，只支持多选项输入的单值。 例如 ：--include *.jpg --include *.txt。 |
