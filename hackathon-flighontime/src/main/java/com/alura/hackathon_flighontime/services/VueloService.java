package com.alura.hackathon_flighontime.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.alura.hackathon_flighontime.models.Vuelo;
import com.alura.hackathon_flighontime.repository.IVueloRepository;

@Service
public class VueloService {

    @Autowired
    private IVueloRepository repository;

    public void save(Vuelo vuelo) {
        repository.save(vuelo);
    }

}
