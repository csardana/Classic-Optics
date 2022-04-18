package com.Gift;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

@SpringBootApplication(scanBasePackages = {"com.Gift.controllers","com.Gift"})
@EnableJpaAuditing

public class ClassicOptics {

	public static void main(String[] args) {
		SpringApplication.run(ClassicOptics.class, args);
	}

}
