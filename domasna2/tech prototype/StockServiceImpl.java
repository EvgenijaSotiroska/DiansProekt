package com.example.demo.service;

import com.example.demo.model.Issuer;
import com.example.demo.model.Stock;
import com.example.demo.repository.IssuerRepository;
import com.example.demo.repository.StockRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class StockServiceImpl implements StockService{
    private final StockRepository stockRepository;

    public StockServiceImpl(StockRepository stockRepository) {
        this.stockRepository = stockRepository;
    }


    @Override
    public List<Stock> findAll() {
        return this.stockRepository.findAll();
    }

    @Override
    public Optional<Stock> findById(Long id) {
        return this.stockRepository.findById(id);
    }
}
