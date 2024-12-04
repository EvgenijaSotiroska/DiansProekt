package com.example.demo.service;

import com.example.demo.model.Issuer;
import com.example.demo.repository.IssuerRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class IssuerServiceImpl implements IssuerService{
    private final IssuerRepository issuerRepository;

    public IssuerServiceImpl(IssuerRepository issuerRepository) {
        this.issuerRepository = issuerRepository;
    }


    @Override
    public List<Issuer> findAll() {
        return this.issuerRepository.findAll();
    }

    @Override
    public Optional<Issuer> findById(Long id) {
        return this.issuerRepository.findById(id);
    }
}
