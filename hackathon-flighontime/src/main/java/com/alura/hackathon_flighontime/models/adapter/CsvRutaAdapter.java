package com.alura.hackathon_flighontime.models.adapter;

import com.alura.hackathon_flighontime.models.Ruta;
import com.opencsv.bean.ColumnPositionMappingStrategy;
import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;

import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.List;

public class CsvRutaAdapter implements IAdapter<Ruta> {
    
    @Override
    public List<Ruta> readFile(InputStream inputStream) {
        Reader reader = new InputStreamReader(inputStream);
        ColumnPositionMappingStrategy<Ruta> strategy = new ColumnPositionMappingStrategy<>();
        strategy.setType(Ruta.class);
        strategy.setColumnMapping("origin", "dest", "airlineCode", "distance", "numVuelos");

        CsvToBean<Ruta> csvToBean = new CsvToBeanBuilder<Ruta>(reader)
                .withMappingStrategy(strategy)
                .withType(Ruta.class)
                .withSeparator(',')
                .withSkipLines(1)
                .withIgnoreLeadingWhiteSpace(true)
                .build();
        
        List<Ruta> rutas = csvToBean.parse();
        
        // Limpiar espacios en blanco de los códigos IATA
        rutas.forEach(r -> {
            r.setOrigin(r.getOrigin().trim());
            r.setDest(r.getDest().trim());
            r.setAirlineCode(r.getAirlineCode().trim());
        });
        
        return rutas;
    }
}