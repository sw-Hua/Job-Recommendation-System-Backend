package com.jrsystem;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/jrSystem_DbTest")
public class JrSystem_DbTestController {
    private final JrSystem_DbTestService service;

    @Autowired
    public JrSystem_DbTestController(JrSystem_DbTestService service) {
        this.service = service;
    }

    @GetMapping("/")
    public List<JrSystem_DbTest> getAllJrSystem_DbTests() {
        return service.getAllJrSystem_DbTests();
    }

    @GetMapping("/{id}")
    public Optional<JrSystem_DbTest> getJrSystem_DbTestById(@PathVariable Integer id) {
        return service.getJrSystem_DbTestById(id);
    }

    @PostMapping("/")
    public JrSystem_DbTest createJrSystem_DbTest(@RequestBody JrSystem_DbTest jrSystem_DbTest) {
        return service.createJrSystem_DbTest(jrSystem_DbTest);
    }

    @PutMapping("/{id}")
    public JrSystem_DbTest updateJrSystem_DbTest(@PathVariable Integer id, @RequestBody JrSystem_DbTest updatedJrSystem_DbTest) {
        return service.updateJrSystem_DbTest(id, updatedJrSystem_DbTest);
    }

    @DeleteMapping("/{id}")
    public void deleteJrSystem_DbTest(@PathVariable Integer id) {
        service.deleteJrSystem_DbTest(id);
    }
}
