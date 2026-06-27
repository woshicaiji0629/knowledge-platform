## 索引支持
mol和fp的比较运算操作支持Btree索引、Hash索引。例如：
CREATE INDEX molidx ON pgmol (mol); CREATE INDEX molidx ON pgmol (fp);
mol的%、#、@>、<@操作和fp结构的%、#操作支持Gist索引。例如：
CREATE INDEX molidx ON pgmol USING gist (mol);
