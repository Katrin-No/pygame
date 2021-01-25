CREATE TABLE LAND(
                     LNR varchar(4) NOT NULL,
                     Name varchar(50) NOT NULL,
                     Einwohner decimal(20,2) NOT NULL,
                     Flaeche int NOT NULL,
                     Hauptstadt varchar(30) NOT NULL,
                     Kontinent varchar(15) NOT NULL,
                     KontinentFlaeche int NOT NULL,
                     KontinentEinwohner int NOT NULL
);

INSERT INTO LAND (LNR, Name, Einwohner, Flaeche, Hauptstadt, Kontinent, KontinentFlaeche, KontinentEinwohner) VALUES
('A', 'Österreich', '8.51', 83879, 'Wien', 'Europa', 10, 733),
('AC', 'Antigua und Barbuda', '0.09', 443, 'Saint John\s', 'Nordamerika', 24, 523),
('AF', 'Afghanistan', '33.40', 652230, 'Kabul', 'Asien', 44, 4010),
('AG', 'Algerien', '37.40', 2381741, 'Algiers', 'Afrika', 30, 944),
('AL', 'Albanien', '2.80', 28748, 'Tirana', 'Europa', 10, 733),
('AM', 'Armenien', '3.34', 29743, 'Eriwan', 'Asien', 44, 4010),
('AN', 'Andorra', '0.08', 468, 'Andorra la Vella', 'Europa', 10, 733),
('AO', 'Angola', '20.90', 1246000, 'Luanda', 'Afrika', 30, 944),
('AUS', 'Australien', '23.13', 7741220, 'Canberra', 'Australien', 9, 34),
('AZ', 'Aserbaidschan', '9.30', 86600, 'Baku', 'Asien', 44, 4010);

INSERT INTO LAND (LNR, Name, Einwohner, Flaeche, Hauptstadt, Kontinent, KontinentFlaeche, KontinentEinwohner) VALUES
('B', 'Belgien', '11.27', 30528, 'Brüssel', 'Europa', 10, 733),
('BA', 'Bahrein', '1.23', 750, 'Manama', 'Asien', 44, 4010),
('BB', 'Barbados', '0.27', 431, 'Bridgetown', 'Nordamerika', 24, 523),
('BD', 'Bangladesch', '152.90', 143998, 'Dhaka', 'Asien', 44, 4010),
('BF', 'Bahamas', '0.35', 13940, 'Nassau', 'Afrika', 30, 944),
('BG', 'Bulgarien', '7.36', 110879, 'Sofia', 'Europa', 10, 733),
('BH', 'Belize', '0.31', 22966, 'Belmopan', 'Nordamerika', 24, 523),
('BHU', 'Bhutan', '0.72', 38394, 'Thimbu', 'Asien', 44, 4010),
('BIH', 'Bosnien und Herzegowina', '3.79', 51197, 'Sarajevo', 'Europa', 10, 733),
('BOL', 'Bolivien', '10.06', 109858, 'Sucre', 'Südamerika', 18, 381),
('BR', 'Brasilien', '202.74', 8514877, 'Brasilia', 'Südamerika', 18, 381),
('BRU', 'Brunei', '0.41', 5765, 'Bandar Seri Begawan', 'Asien', 44, 4010),
('BU', 'Burundi', '10.56', 27830, 'Bujumbura', 'Afrika', 30, 944),
('BUR', 'Myanmar', '51.40', 676578, 'Naypyidaw', 'Asien', 44, 4010),
('BY', 'Weißrussland', '9.46', 207600, 'Minsk', 'Europa', 10, 733),
('C', 'Kuba', '11.21', 109884, 'Havanna', 'Nordamerika', 24, 523),
('CAM', 'Kamerun', '20.55', 475442, 'Jaunde', 'Afrika', 30, 944),
('CDN', 'Kanada', '35.16', 9984670, 'Ottawa', 'Nordamerika', 24, 523),
('CH', 'Schweiz', '8.18', 41285, 'Bern', 'Europa', 10, 733),
('CI', 'Elfenbeinküste', '20.15', 322461, 'Yamoussoukro', 'Afrika', 30, 944),
('CL', 'Sri Lanka', '21.20', 65610, 'Colombo', 'Asien', 44, 4010),
('CO', 'Kolumbien', '47.40', 1138748, 'Bogota', 'Südamerika', 18, 381),
('COK', 'Cookinseln', '0.12', 236, 'Avarua', 'Australien', 9, 34),
('CR', 'Costa Rica', '4.30', 51100, 'San Jose', 'Nordamerika', 24, 523),
('CY', 'Zypern', '0.89', 5896, 'Nicosia', 'Europa', 10, 733),
('CZ', 'Tschechische Republik', '10.53', 78866, 'Prag', 'Europa', 10, 733),
('D', 'Deutschland', '82.17', 357375, 'Berlin', 'Europa', 10180, 733000),
('DK', 'Dänemark', '5.63', 43094, 'Kopenhagen', 'Europa', 10, 733),
('DOM', 'Dominikanische Republik', '10.46', 48670, 'Santo Domingo', 'Nordamerika', 24, 523);