package com.recommandationsystem.recommandTest;

import jakarta.persistence.EntityNotFoundException;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class JrSystem_DbTestService {
    private final JrSystem_DbTestRepository repository;

    // 增

    @Autowired
    public JrSystem_DbTestService(JrSystem_DbTestRepository repository) {
        this.repository = repository;
    }

    public List<JrSystem_DbTest> getAllJrSystem_DbTests() {
        return repository.findAll();
    }

    public Optional<JrSystem_DbTest> getJrSystem_DbTestById(Integer id) {
        return repository.findById(id);
    }

    public JrSystem_DbTest createJrSystem_DbTest(JrSystem_DbTest jrSystem_DbTest) {
        return repository.save(jrSystem_DbTest);
    }

    public JrSystem_DbTest updateJrSystem_DbTest(Integer id, JrSystem_DbTest updatedJrSystem_DbTest) {
        Optional<JrSystem_DbTest> existingJrSystem_DbTest = repository.findById(id);
        if (existingJrSystem_DbTest.isPresent()) {
            updatedJrSystem_DbTest.setId(id);
            return repository.save(updatedJrSystem_DbTest);
        } else {
            throw new EntityNotFoundException("JrSystem_DbTest not found with id: " + id);
        }
    }

    public void deleteJrSystem_DbTest(Integer id) {
        repository.deleteById(id);
    }

}
