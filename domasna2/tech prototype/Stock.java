package com.example.demo.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Data
@Entity
@Table(name = "STOCK_DATABASE")
@AllArgsConstructor
@NoArgsConstructor
public class Stock implements Serializable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String code;
    private String date;
    private String lastTransaction;
    private String average;
    private String max;
    private String min;
    private String prom;
    private int quantity;
    private String turnover;
    private String totalTurnover;

    public String getAverage() {
        return average;
    }

    public String getCode() {
        return code;
    }

    public String getDate() {
        return date;
    }

    public Long getId() {
        return id;
    }

    public String getLastTransaction() {
        return lastTransaction;
    }

    public String getMax() {
        return max;
    }

    public String getMin() {
        return min;
    }

    public String getProm() {
        return prom;
    }

    public int getQuantity() {
        return quantity;
    }

    public String getTotalTurnover() {
        return totalTurnover;
    }

    public String getTurnover() {
        return turnover;
    }
}
