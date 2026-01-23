package com.alura.hackathon_flighontime.services;

import com.alura.hackathon_flighontime.models.Ruta;
import com.alura.hackathon_flighontime.models.adapter.AdapterFile;
import com.alura.hackathon_flighontime.models.adapter.IAdapter;
import com.alura.hackathon_flighontime.repository.IRutaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.FileInputStream;
import java.io.InputStream;
import java.util.List;

@Service
public class RutaService {

    @Autowired
    private IRutaRepository repository;

    public void cargarRutasSiNoExisten(IAdapter<Ruta> adapter, String path) throws Exception {
        if(repository.count() == 0) {
            System.out.println("\n🔄 Cargando rutas desde CSV...");
            InputStream inputStream = new FileInputStream(path);
            AdapterFile<Ruta> adapterFile = new AdapterFile<>(adapter);
            List<Ruta> rutaList = adapterFile.readFile(inputStream);
            repository.saveAll(rutaList);
            System.out.println("✅ Se cargaron " + rutaList.size() + " rutas en la base de datos.\n");
        } else {
            System.out.println("\n✅ Ya existen " + repository.count() + " rutas en la base de datos.\n");
        }
    }

    public boolean existeRuta(String origin, String dest) {
        return repository.existsByOriginAndDest(origin, dest);
    }

    public boolean aerolineaOperaRuta(String airlineCode, String origin, String dest) {
        return repository.existsByOriginAndDestAndAirlineCode(origin, dest, airlineCode);
    }
}