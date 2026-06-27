## 原理介绍
TairBloom作为一种[Scalable Bloom Filter](https://gsd.di.uminho.pt/members/cbm/ps/dbloom.pdf)的实现，具有动态扩容的能力，同时误判率（False Positive Rate）维持不变。而Scalable Bloom Filter是在Bloom Filter的基础上进行优化的，下文将简单介绍Bloom Filter与Scalable Bloom Filter的基本原理。
Bloom Filter
布隆过滤器是一个高空间利用率的概率性数据结构，由Burton Bloom于1970年提出，用于测试一个元素是否在集合中。
新创建的布隆过滤器是一串被置为0的Bit数组（假设有m位），同时声明k个不同的Hash函数生成统一的随机分布（k是一个小于m的常数）。向布隆过滤器中添加元素时，通过k个Hash函数将元素映射到Bit中的k个点，并将这些位置的值设置为1，一个Bit位可能被不同数据共享。下图展示了假设布隆过滤器的k为3，向其插入X1、X2的过程。
查询元素时，仍通过k个Hash函数得到对应的k个位，判断目标位置是否为1，若目标位置全为1则认为该元素在布隆过滤器内，否则认为该元素不存在，下图展示了在布隆过滤器中查询Y1和Y2是否存在的过程。
由上图可以发现，虽然从未向布隆过滤器中插入过Y2这个元素，但是布隆过滤器却判断Y2存在，因此，布隆过滤器是可能存在误判的，即存在假阳性（false positive）。至此，可以得出关于布隆过滤器的几个特性：
Bit位可能被不同数据共享。
存在假阳性（false positive），且布隆过滤器中的元素越多，假阳性的可能性越大，但不存在假阴性（false negative），即不会将存在的元素误判为不存在。
元素可以被加入布隆过滤器，但无法被删除，因为Bit位是可以共享的，删除时有可能会影响到其他元素。
Scalable Bloom Filter
随着布隆过滤器中添加的元素越来越多，误判率也越来越高，若希望误判率稳定不变，需同步增加布隆过滤器的大小，但是布隆过滤器由于结构限制无法进行扩容。因此，Scalable Bloom Filter提出创建新的布隆过滤器，将多个布隆过滤器组装成一个布隆过滤器使用。
下图展示了一个Scalable Bloom Filter的基本模型（下文简称SBF）。该SBF一共包含BF0和BF1两层。在一开始，SBF只包含BF0层，假设在插入a、b、c三个元素后，BF0层已经无法保证用户设定的误判率，此时会创建新的一层（BF1层）进行扩容。因此，后面的d、e、f元素会插入到BF1层中。同理，当BF1层也无法满足误判率时，会创建新的一层（BF2层），如此进行下去。更多信息，请参见[Scalable Bloom Fil
