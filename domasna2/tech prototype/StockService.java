package com.example.demo.service;

import com.example.demo.model.Issuer;
import com.example.demo.model.Stock;

import java.util.List;
import java.util.Optional;

public interface StockService {
    List<Stock> findAll();
    Optional<Stock> findById(Long id);
}
