package com.jrsystem.businessservice.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class VersionController {

    @GetMapping("/resolve/version")
    public ResponseEntity<?> resolveVersion() {
        return ResponseEntity.ok(
                new Object() {
                    public final String version = "0.0.1-SNAPSHOT";
                });
    }
}