package com.alura.hackathon_flighontime.repository;

import com.alura.hackathon_flighontime.models.Ruta;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface IRutaRepository extends JpaRepository<Ruta, Long> {
    
    // Verificar si existe la ruta (cualquier aerolínea)
    boolean existsByOriginAndDest(String origin, String dest);
    
    // Verificar si la aerolínea específica opera la ruta
    boolean existsByOriginAndDestAndAirlineCode(String origin, String dest, String airlineCode);
}