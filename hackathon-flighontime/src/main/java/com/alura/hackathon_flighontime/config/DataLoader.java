package com.alura.hackathon_flighontime.config;

import com.alura.hackathon_flighontime.models.adapter.CsvAerolineaAdapter;
import com.alura.hackathon_flighontime.models.adapter.CsvAeropuertoAdapter;
import com.alura.hackathon_flighontime.models.adapter.CsvRutaAdapter; // ⭐ NUEVO
import com.alura.hackathon_flighontime.services.AerolineaService;
import com.alura.hackathon_flighontime.services.AeropuertoService;
import com.alura.hackathon_flighontime.services.RutaService; // ⭐ NUEVO
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.io.File;

@Component
public class DataLoader implements CommandLineRunner {

    private static final String path = "src" + File.separator +
            "main" + File.separator +
            "resources" + File.separator +
            "files" + File.separator;

    @Autowired
    private AerolineaService aerolineaService;
    
    @Autowired
    private AeropuertoService aeropuertoService;
    
    @Autowired
    private RutaService rutaService; // ⭐ NUEVO

    @Override
    public void run(String... args) throws Exception {
        aerolineaService.cargarAerolineasSiNoExisten(new CsvAerolineaAdapter(), path + "aerolineas.csv");
        aeropuertoService.cargarAeropuertosSiNoExisten(new CsvAeropuertoAdapter(), path + "aeropuertos.csv");
        rutaService.cargarRutasSiNoExisten(new CsvRutaAdapter(), path + "rutas_validas.csv"); // ⭐ NUEVO
    }
}