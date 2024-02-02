import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import static org.springframework.security.config.Customizer.withDefaults;
//@Configuration
//public class WebSecurityConfig {
//
//    @Bean
//    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
//        http.csrf()
//                .disable()
//                .authorizeHttpRequests()
//                .anyRequest()
//                .authenticated()
//                .and()
//                .httpBasic()
//                .and()
//                .formLogin();
//
//        return http.build();
//    }
//}


            /*
            简而言之，配置：
            禁用 CSRF，
            仅允许经过身份验证的请求
            允许基本登录和表单登录
             */
@Configuration
@EnableWebSecurity
public class WebSecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
                .csrf().disable() // 禁用CSRF保护
                .authorizeRequests(authorize -> authorize
                        .anyRequest().authenticated() // 所有请求都需要认证
                )
                .httpBasic(withDefaults()) // 启用HTTP基本认证
                .formLogin(withDefaults()); // 启用表单登录

        return http.build();
    }
}





