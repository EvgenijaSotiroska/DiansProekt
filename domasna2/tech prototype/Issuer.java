package com.example.demo.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Data
@Entity
@Table(name = "ISSUERS_DATABASE")
@AllArgsConstructor
@NoArgsConstructor
public class Issuer implements Serializable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String code;

    public Long getId() {
        return id;
    }

    public String getCode() {
        return code;
    }

}
