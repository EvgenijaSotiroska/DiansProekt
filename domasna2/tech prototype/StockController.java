package com.example.demo.web.controller;

import com.example.demo.model.Issuer;
import com.example.demo.model.Stock;
import com.example.demo.service.IssuerService;
import com.example.demo.service.StockService;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(value = "/api/stock")
@Validated
@CrossOrigin(origins="*")
public class StockController {
    private final StockService stockService;

    public StockController(StockService stockService) {
        this.stockService = stockService;
    }

    @GetMapping("/all")
    public List<Stock> findAll() {
        List<Stock> stocks = this.stockService.findAll();
        return stocks;
    }

    @GetMapping("/{id}")
    public ResponseEntity<Stock> findById(@PathVariable Long id) {
        return this.stockService
                .findById(id)
                .map(stock -> ResponseEntity.ok().body(stock))
                .orElseGet(() -> ResponseEntity.notFound().build());
    }
}
