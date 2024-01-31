package com.recommandationsystem.recommandTest;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.SequenceGenerator;
import lombok.*;
import java.time.LocalDateTime;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
@Entity
public class JrSystem_DbTest {
    /*
    @SequenceGenerator:
    @SequenceGenerator 注解用于定义一个序列生成器，这个生成器通常用于生成主键值。
    name 属性定义了生成器的名称，可以在 GeneratedValue 注解中引用。
    sequenceName 属性指定了要使用的数据库序列的名称。
     */
    @Id
    @SequenceGenerator(
            name = "JrSystem_DbTest_id_sequence",
            sequenceName = "JrSystem_DbTest_id_sequence"
    )
    @GeneratedValue(
            strategy = GenerationType.SEQUENCE,
            generator = "JrSystem_DbTest_id_sequence"
    )
    private Integer id;
    /*
     @SequenceGenerator:
    @SequenceGenerator 注解用于定义一个序列生成器，这个生成器通常用于生成主键值。
    name 属性定义了生成器的名称，可以在 GeneratedValue 注解中引用。
    sequenceName 属性指定了要使用的数据库序列的名称。
     */

    private String name;
    private String skill;
    private String job;
}
