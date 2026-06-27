### 表格（Pro版本）
表格由一组或多组单元格组成，表格中的项被组织为行和列，表格的第一行称为表头，指明表格每一列的内容和意义。例如查询每个http_referer对应的响应体总字节数，并用线图展示body_bytes_sent。
(*)| SELECT http_referer, array_agg(body_bytes_sent) as body_bytes_sent GROUP BY http_referer
使用场景：[表格](table.md)能够精确地展示每个数据项的具体数值。适用于数据分析、财务报表、科学实验记录等场景。
