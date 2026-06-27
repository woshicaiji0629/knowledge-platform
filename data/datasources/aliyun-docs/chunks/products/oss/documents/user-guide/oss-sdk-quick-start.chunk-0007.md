### 在Maven项目中加入依赖项（推荐方式）
在Maven工程中使用OSS Java SDK，只需在pom.xml中加入相应依赖即可。以在<dependencies>中加入3.17.4版本的依赖为例：
<dependency> <groupId>com.aliyun.oss</groupId> <artifactId>aliyun-sdk-oss</artifactId> <version>3.17.4</version> </dependency>
如果使用的是Java 9及以上的版本，则需要添加以下JAXB相关依赖。
<dependency> <groupId>javax.xml.bind</groupId> <artifactId>jaxb-api</artifactId> <version>2.3.1</version> </dependency> <dependency> <groupId>javax.activation</groupId> <artifactId>activation</artifactId> <version>1.1.1</version> </dependency> <!-- no more than 2.3.3--> <dependency> <groupId>org.glassfish.jaxb</groupId> <artifactId>jaxb-runtime</artifactId> <version>2.3.3</version> </dependency>
