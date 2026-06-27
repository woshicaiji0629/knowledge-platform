## THP参数列表
透明大页THP（Transparent Huge Pages）是Linux内核中的一个通用特性，可以自动将小页面（通常为4 KB）合并成大页面（通常为2 MB或更大），以减少内存访问页表项PTE（Page Table Entries）大小和访问次数，同时减轻了TLB（Translation Lookaside Buffer）缓存的压力，提高内存访问的效率。
说明
以下参数均支持通过控制台或OpenAPI配置。
根据操作系统及其内核版本的不同，下列参数的默认值不同。更多信息，请参见[Linux Kernel THP](https://docs.kernel.org/admin-guide/mm/transhuge.html)[参数](https://docs.kernel.org/admin-guide/mm/transhuge.html)文档。
