package com.alura.hackathon_flighontime.services;

import com.alura.hackathon_flighontime.dtos.DatosVuelo;
import com.alura.hackathon_flighontime.dtos.FlightPredictionRequestDTO;
import com.alura.hackathon_flighontime.dtos.FlightPredictionResponseDTO;
import com.alura.hackathon_flighontime.exceptions.ValidarException;
import com.alura.hackathon_flighontime.models.Aerolinea;
import com.alura.hackathon_flighontime.models.Aeropuerto;
import com.alura.hackathon_flighontime.models.Vuelo;
import com.alura.hackathon_flighontime.services.consumo.ConsumoAPI;
import com.alura.hackathon_flighontime.services.consumo.ConvertirDatos;
import com.alura.hackathon_flighontime.services.consumo.IConvertirDatos;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ModeloService {

    private static final String FASTAPI_URL = "http://127.0.0.1:8000/predict";

    @Autowired
    private AeropuertoService aeropuertoService;

    @Autowired
    private AerolineaService aerolineaService;

    @Autowired
    private VueloService vueloService;

    @Autowired
    private PredictionService predictionService;
    
    @Autowired
    private RutaService rutaService; // ⭐ NUEVO

    public FlightPredictionResponseDTO enviarRequest(FlightPredictionRequestDTO requestDTO) {

        String iata_aerolinea = requestDTO.aerolinea();
        String iata_origen = requestDTO.origen();
        String iata_destino = requestDTO.destino();

        // Validación 1: Origen y destino diferentes
        if(iata_origen.equalsIgnoreCase(iata_destino)){
            throw new ValidarException("Origen y Destino deben ser diferentes.");
        }

        // Validación 2: Aerolínea existe
        boolean existeAerolinea = aerolineaService.existByIata(iata_aerolinea);
        if (!existeAerolinea) {
            throw new ValidarException("La Aerolínea no está registrada.");
        }

        // Validación 3: Aeropuertos existen
        boolean existeOrigen = aeropuertoService.existsByIata(iata_origen);
        boolean existeDestino = aeropuertoService.existsByIata(iata_destino);
        
        if (!existeOrigen) {
            throw new ValidarException("El Aeropuerto de Origen no está registrado.");
        }
        if (!existeDestino) {
            throw new ValidarException("El Aeropuerto de Destino no está registrado.");
        }

        // ⭐ Validación 4: La ruta existe
        if (!rutaService.existeRuta(iata_origen, iata_destino)) {
            throw new ValidarException(
                "No existe ninguna ruta de vuelos entre " + iata_origen + " y " + iata_destino + "."
            );
        }

        // ⭐ Validación 5: La aerolínea opera la ruta
        if (!rutaService.aerolineaOperaRuta(iata_aerolinea, iata_origen, iata_destino)) {
            throw new ValidarException(
                "La aerolínea " + iata_aerolinea + " no opera vuelos en la ruta " + 
                iata_origen + " → " + iata_destino + "."
            );
        }

        // Extraer entidades de la base de datos
        Aerolinea aerolinea = aerolineaService.fineByIata(iata_aerolinea);
        Aeropuerto aeropuerto_origen = aeropuertoService.findByIata(iata_origen);
        Aeropuerto aeropuerto_destino = aeropuertoService.findByIata(iata_destino);

        // Crear objeto vuelo
        Vuelo vuelo = new Vuelo(
                aerolinea,
                aeropuerto_origen,
                aeropuerto_destino,
                requestDTO.hora_partida(),
                requestDTO.dia_semana()
        );

        // Preparar request para FastAPI
        DatosVuelo vueloRequest = new DatosVuelo(vuelo);

        // Convertir a JSON y enviar a FastAPI
        IConvertirDatos conversion = new ConvertirDatos();
        String json = conversion.objetoAString(vueloRequest);
        String response = ConsumoAPI.getPrediction(FASTAPI_URL, json);

        return conversion.jsonAObjeto(response, FlightPredictionResponseDTO.class);
    }
}