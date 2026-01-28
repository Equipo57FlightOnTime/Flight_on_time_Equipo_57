package com.alura.hackathon_flighontime.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.alura.hackathon_flighontime.models.Prediction;
import com.alura.hackathon_flighontime.repository.IPredictionRepository;

@Service
public class PredictionService {

    @Autowired
    private IPredictionRepository repository;

    public void save(Prediction prediction) {
        repository.save(prediction);
    }

}
