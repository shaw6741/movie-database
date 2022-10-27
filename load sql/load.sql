SET GLOBAL local_infile = 1;

LOAD DATA LOCAL INFILE  '/Users/my movie database/Aliases.tsv'
INTO TABLE Aliases
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE  '/Users/my movie database/Alias_attributes.tsv'
INTO TABLE Alias_attributes
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE  '/Users/my movie database/Alias_types.tsv'
INTO TABLE Alias_types
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/my movie database/Directors.tsv'
INTO TABLE Directors
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/my movie database/Writers.tsv'
INTO TABLE Writers
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/my movie database/Episode_belongs_to.tsv'
INTO TABLE Episode_belongs_to
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/my movie database/Names_.tsv'
INTO TABLE Names_
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/my movie database/Name_worked_as.tsv'
INTO TABLE Name_worked_as
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/my movie database/Known_for.tsv'
INTO TABLE Known_for
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/my movie database/Principals.tsv'
INTO TABLE Principals
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/my movie database/Had_role.tsv'
INTO TABLE Had_role
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/my movie database/Titles.tsv'
INTO TABLE Titles
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE  '/Users/my movie database/Title_genres.tsv'
INTO TABLE Title_genres
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE  '/Users/my movie database/Title_ratings.tsv'
INTO TABLE Title_ratings
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;
