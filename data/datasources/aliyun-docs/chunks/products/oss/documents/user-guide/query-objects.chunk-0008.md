s.postalCode like '10021%'或者select s.streetAddress from ossobject.contacts[*].address s where s.postalCode like '10021%'
由于select s.streetAddress from ossobject.contacts[*].address s where s.postalCode like '10021%'的JSON Path更加精确，因此性能更优。
在JSON文件中处理高精度浮点数
在JSON文件中需要进行高精度浮点数的数值计算时，建议设置ParseJsonNumberAsString选项为true, 同时将该值cast成Decimal。比如一个属性a值为123456789.123456789，用select s.a from ossobject s where cast(s.a as decimal) > 123456789.12345就可以保持原始数据的精度不丢失。
