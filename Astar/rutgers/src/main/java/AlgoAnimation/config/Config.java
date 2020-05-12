package AlgoAnimation.config;

import AlgoAnimation.UI.MainScreen;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Scope;

//@Configuration
public class Config {

    @Bean
    @Scope("prototype")
    public MainScreen mainScreen() {
        return new MainScreen();
    }
}
