package com.alura.hackathon_flighontime.models;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "rutas")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Ruta {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false, length = 3)
    private String origin;
    
    @Column(nullable = false, length = 3)
    private String dest;
    
    @Column(nullable = false, length = 2, name = "airline_code")
    private String airlineCode;
    
    @Column(nullable = false)
    private Double distance;
    
    @Column(name = "num_vuelos")
    private Integer numVuelos;
    
    public Ruta(String origin, String dest, String airlineCode, Double distance, Integer numVuelos) {
        this.origin = origin;
        this.dest = dest;
        this.airlineCode = airlineCode;
        this.distance = distance;
        this.numVuelos = numVuelos;
    }
}