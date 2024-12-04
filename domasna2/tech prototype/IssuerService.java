package com.example.demo.service;

import com.example.demo.model.Issuer;

import java.util.List;
import java.util.Optional;

public interface IssuerService {
    List<Issuer> findAll();
    Optional<Issuer> findById(Long id);
}
