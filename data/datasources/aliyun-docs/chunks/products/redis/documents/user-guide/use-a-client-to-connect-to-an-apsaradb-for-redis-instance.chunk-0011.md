### Spring Data Redis
本示例使用Maven方式进行构建，您也可以手动下载[Lettuce](https://github.com/lettuce-io/lettuce-core/releases)或[Jedis](https://github.com/redis/jedis/releases)客户端。
打开编译器，新建项目。
添加下述pom文件，并下载Lettuce或Jedis。
重要
若使用Lettuce，为避免Lettuce客户端黑洞问题带来的影响，建议使用6.3.0.RELEASE及以上版本，并设置TCP_USER_TIMEOUT参数。
<?xml version="1.0" encoding="UTF-8"?> <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd"> <modelVersion>4.0.0</modelVersion> <parent> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-parent</artifactId> <version>2.4.2</version> <relativePath/> <!-- lookup parent from repository --> </parent> <groupId>com.aliyun.tair</groupId> <artifactId>spring-boot-example</artifactId> <version>0.0.1-SNAPSHOT</version> <name>spring-boot-example</name> <description>Demo project for Spring Boot</description> <properties> <java.version>1.8</java.version> </properties> <dependencies> <dependency> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-web</artifactId> </dependency> <dependency> <groupId>org.springframework
