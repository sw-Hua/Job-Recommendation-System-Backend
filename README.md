# Job Recommendation System

版本信息：Spring Boot 3.2.2



### [JrSystem算法项目链接](https://github.com/sw-Hua/Job-Recommendation-System-Algorithm/settings/access?guidance_task=)



### [JrSystem前端项目链接](https://github.com/sw-Hua/Job-Recommendation-System-Frontend)



### How to Create a Login Microservice?(Securing a Web Application)

https://spring.io/guides/gs/securing-web/



### SpringBoot with Postgres

https://tipsontech.medium.com/springboot-with-postgres-d6ca9050b494



### 启动docker-compose.yml

```bash
docker compose up -d
```





#### Postman测试

Post请求：

JPA

```
localhost:8080/jrSystem_DbTest/
```

MyBatis

```
localhost:8081/api/users
```



Body Content:

JPA

```json
{
    "name":"Songwen",
    "skill":"Java",
    "job":"Backend Programmer"
}
```

MyBatis

```json
{
	"id": "123",
	"username": "songwen",
	"password": "password"
}
```



### Spring Security 账号密码

**Login: **

```
login
```

**Password: **

````
pass
````







## 几大目标

1. **互联网高并发、海量处理、负载均衡、容错处理：**
   - 使用Spring Cloud提供的服务发现和负载均衡机制，确保微服务在高并发情况下能够平稳运行。（之后就会使用）
   - 引入熔断器（如Hystrix）进行容错处理，防止一个微服务的故障导致整个系统的崩溃。
   - [消息中间件的理解](https://www.youtube.com/watch?v=sqlV8mHoils)考虑使用消息中间件（如RabbitMQ、Kafka）进行异步处理，提高系统的吞吐量和处理能力。（考虑使用）
2. **深入理解并发编程，包括线程池、锁机制等：**
   - 在微服务中使用线程池来管理并发任务，提高性能。
   - 合理使用锁机制确保数据的一致性，避免多线程并发访问的问题。
   - 考虑使用分布式锁来协调不同微服务之间的操作。
3. **Java基础及开发经验：**
   - 利用Spring Boot提供的简化配置和快速开发特性，提高开发效率。
   - 使用Java的多线程特性来处理异步任务。
   - 充分利用Java的IO和网络编程特性，实现高效的数据交互。
4. **数据库设计与优化：**
   - 设计合理的数据库表结构，遵循数据库设计范式。
   - 使用MySQL的性能调优策略，如索引优化、SQL优化等。
   - 针对特定场景，考虑使用缓存来提高读取性能。
5. **编码规范和面向对象设计：**
   - 遵循项目中的编码规范，提高代码的可读性和可维护性。
   - 使用面向对象设计原则，合理划分微服务的职责和功能。
   - 应用设计模式来解决常见的问题，提高代码的灵活性和复用性。





#### [Building a Microservices From Scratch](https://hackernoon.com/building-java-microservices-from-scratch)



