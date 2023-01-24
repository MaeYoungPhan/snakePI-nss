create table Species (
	id INT,
	name VARCHAR(50)
);
insert into Species (id, name) values (1, 'Procyon cancrivorus');
insert into Species (id, name) values (2, 'Aonyx cinerea');
insert into Species (id, name) values (3, 'Pitangus sulphuratus');
insert into Species (id, name) values (4, 'Nannopterum harrisi');
insert into Species (id, name) values (5, 'Tamiasciurus hudsonicus');

create table Owners (
	id INT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	email VARCHAR(50)
);

insert into Owners (id, first_name, last_name, email) values (1, 'Jarrett', 'Thunder', 'jthunder0@amazon.de');
insert into Owners (id, first_name, last_name, email) values (2, 'Charline', 'Manton', 'cmanton1@china.com.cn');
insert into Owners (id, first_name, last_name, email) values (3, 'Lura', 'Cornbell', 'lcornbell2@ning.com');
insert into Owners (id, first_name, last_name, email) values (4, 'Bo', 'Pearn', 'bpearn3@hp.com');
insert into Owners (id, first_name, last_name, email) values (5, 'Veronike', 'Hellings', 'vhellings4@utexas.edu');
insert into Owners (id, first_name, last_name, email) values (6, 'Yule', 'Tilmouth', 'ytilmouth5@nps.gov');
insert into Owners (id, first_name, last_name, email) values (7, 'Agata', 'Vasilmanov', 'avasilmanov6@fema.gov');
insert into Owners (id, first_name, last_name, email) values (8, 'Irvin', 'Folshom', 'ifolshom7@mapquest.com');
insert into Owners (id, first_name, last_name, email) values (9, 'Jeanna', 'Dyas', 'jdyas8@amazon.co.uk');
insert into Owners (id, first_name, last_name, email) values (10, 'Ulick', 'Drinkhill', 'udrinkhill9@wsj.com');

create table Snakes (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(50),
	owner_id INTEGER,
	species_id INTEGER,
	gender VARCHAR(50),
	color VARCHAR(50),
	FOREIGN KEY (owner_id) REFERENCES Owners(id),
	FOREIGN KEY (species_id) REFERENCES Species(id)
);

insert into Snakes (id, name, owner_id, species_id, gender, color) values (1, 'Annotée', 2, 2, 'Female', 'Turquoise');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (2, 'Lorène', 1, 1, 'Male', 'Green');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (3, 'Alizée', 8, 1, 'Female', 'Blue');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (4, 'Océane', 7, 1, 'Male', 'Khaki');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (5, 'Almérinda', 4, 4, 'Male', 'Yellow');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (6, 'Athéna', 3, 5, 'Female', 'Violet');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (7, 'Bénédicte', 8, 2, 'Male', 'Mauv');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (8, 'Solène', 2, 3, 'Male', 'Yellow');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (9, 'Aí', 6, 4, 'Female', 'Goldenrod');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (10, 'Andréa', 9, 5, 'Male', 'Turquoise');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (11, 'Noémie', 6, 2, 'Male', 'Crimson');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (12, 'Gwenaëlle', 4, 1, 'Male', 'Puce');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (13, 'Océane', 9, 5, 'Male', 'Turquoise');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (14, 'Bérengère', 5, 2, 'Female', 'Turquoise');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (15, 'Lyséa', 7, 2, 'Male', 'Fuscia');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (16, 'Méghane', 1, 2, 'Male', 'Crimson');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (17, 'Léonore', 5, 1, 'Female', 'Yellow');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (18, 'Anaël', 6, 5, 'Female', 'Puce');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (19, 'Nélie', 7, 1, 'Female', 'Pink');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (20, 'Béatrice', 9, 1, 'Female', 'Green');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (21, 'Gösta', 5, 2, 'Female', 'Mauv');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (22, 'Clélia', 5, 3, 'Male', 'Purple');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (23, 'Méng', 2, 5, 'Female', 'Khaki');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (24, 'Angélique', 2, 1, 'Female', 'Mauv');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (25, 'Aimée', 10, 2, 'Female', 'Pink');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (26, 'Marie-françoise', 2, 1, 'Female', 'Green');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (27, 'Tán', 4, 2, 'Female', 'Teal');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (28, 'Andréanne', 5, 4, 'Female', 'Green');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (29, 'Stéphanie', 8, 5, 'Female', 'Purple');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (30, 'Liè', 7, 1, 'Female', 'Maroon');

SELECT * FROM Snakes ORDER BY id DESC

SELECT
	s.id,
	s.name,
	s.owner_id,
	s.species_id,
	s.gender,
	s.color
FROM Snakes s
WHERE s.species_id = 5