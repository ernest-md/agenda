DROP TABLE IF EXISTS contacts;

CREATE TABLE contacts (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    cognoms TEXT NOT NULL,
    correu TEXT NOT NULL,
    telf INTEGER NOT NULL,
    pais TEXT NOT NULL,
    address TEXT NOT NULL,
    poblacio TEXT NOT NULL,
    codipostal INTEGER NOT NULL,
    provincia TEXT NOT NULL,
    NIF TEXT NOT NULL
);

INSERT INTO contacts VALUES
(1, 'Ernest', 'Gladiador Valderrama', 'evgladiador1@gmail.com', 620963225, 'Espanya', 'C/Joan Maragall 2-6, 2º6ª', 'Mataró', 08303, 'Barcelona', '39971758N'),
(2, 'Marc', 'Serna Bogas', 'marcsernainfo@gmail.com', 678654356, 'Espanya', 'C/Pompeya 46, 2º', 'Mataró', 08301, 'Barcelona', '35647686Y'),
(3, 'Oriol', 'Perez Bejar', 'oriolperezbejar@gmail.com', 654786543, 'Espanya', 'C/Sant Jaume 23, 3º2ª', 'Mataró', 08302, 'Barcelona', '36578756T'),
(4, 'Aoxin', 'Zhou Zhou', 'aoxinzhou@gmail.com', 654342389, 'Espanya', 'C/Montserrat 12, 4º5ª', 'Mataró', 08304, 'Barcelona', '34235678K'),
(5, 'Emiliano', 'Lopez Sombra', 'shadow@gmail.com', 667456353, 'Espanya', 'C/Martoreu 24, 3º7ª', 'Calella', 08204, 'Barcelona', '32235678I');