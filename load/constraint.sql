ALTER TABLE Names_
ADD CONSTRAINT Names_pri_key PRIMARY KEY (name_id);

ALTER TABLE Titles
ADD CONSTRAINT Titles_pri_key PRIMARY KEY (title_id);

ALTER TABLE Aliases
ADD CONSTRAINT Aliases_pri_key PRIMARY KEY (title_id,ordering);

ALTER TABLE Alias_attributes
ADD CONSTRAINT Alias_attributes_pri_key PRIMARY KEY (title_id,ordering);

ALTER TABLE Alias_types
ADD CONSTRAINT Alias_types_pri_key PRIMARY KEY (title_id,ordering);

ALTER TABLE Directors
ADD CONSTRAINT Directors_pri_key PRIMARY KEY (title_id,name_id);

ALTER TABLE Directors
ADD CONSTRAINT Directors_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id);

ALTER TABLE Writers
ADD CONSTRAINT Writers_pri_key PRIMARY KEY (title_id,name_id);

ALTER TABLE Writers
ADD CONSTRAINT Writers_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id);

ALTER TABLE Episode_belongs_to
ADD CONSTRAINT Episode_belongs_to_pri_key PRIMARY KEY (episode_title_id);

ALTER TABLE Episode_belongs_to
ADD CONSTRAINT Episode_belongs_to_ep_title_id_fkey FOREIGN KEY (episode_title_id) REFERENCES Titles(title_id);

ALTER TABLE Name_worked_as
ADD CONSTRAINT Name_worked_as_pri_key PRIMARY KEY (name_id,profession);

ALTER TABLE Name_worked_as
ADD CONSTRAINT Name_worked_as_name_id_fkey FOREIGN KEY (name_id) REFERENCES Names_(name_id);

ALTER TABLE Known_for
ADD CONSTRAINT Known_for_pri_key PRIMARY KEY (name_id,title_id);

ALTER TABLE Known_for
ADD CONSTRAINT Known_for_name_id_fkey FOREIGN KEY (name_id) REFERENCES Names_(name_id);

ALTER TABLE Principals
ADD CONSTRAINT Principals_pri_key PRIMARY KEY (title_id,ordering);

ALTER TABLE Had_role
ADD CONSTRAINT Had_role_pri_key PRIMARY KEY (title_id,name_id,role_(255));

ALTER TABLE Title_genres
ADD CONSTRAINT Title_genres_pri_key PRIMARY KEY (title_id,genre);

ALTER TABLE Title_genres
ADD CONSTRAINT Title_genres_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id);

ALTER TABLE Title_ratings
ADD CONSTRAINT Title_ratings_pri_key PRIMARY KEY (title_id);

ALTER TABLE Title_ratings
ADD CONSTRAINT Title_ratings_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id);

-- Missing Data

-- Disable foreign key check lock
SET foreign_key_checks = 0;

-- Aliases has titles that do not exist in Titles, i.e., there are entries in
-- IMDb's title.akas.tsv.gz that are not present in title.basics.tsv.gz. The same
-- issue arises when setting the foreign key for the Alias_attributes and
-- Alias_types tables.
ALTER TABLE Aliases
ADD CONSTRAINT Aliases_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id);

ALTER TABLE Alias_attributes
ADD CONSTRAINT Alias_attributes_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id);

ALTER TABLE Alias_types
ADD CONSTRAINT Alias_types_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id);

-- Ditto for Episode_belongs_to table.
ALTER TABLE Episode_belongs_to
ADD CONSTRAINT Episode_belongs_to_show_title_id_fkey FOREIGN KEY (parent_tv_show_title_id) REFERENCES Titles(title_id);

ALTER TABLE Known_for
ADD CONSTRAINT Known_for_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id);

ALTER TABLE Principals
ADD CONSTRAINT Principals_name_id_fkey FOREIGN KEY (name_id) REFERENCES Names_(name_id);

ALTER TABLE Principals
ADD CONSTRAINT Principals_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id);

ALTER TABLE Had_role
ADD CONSTRAINT Had_role_title_id_fkey FOREIGN KEY (title_id) REFERENCES Titles(title_id);

ALTER TABLE Had_role
ADD CONSTRAINT Had_role_name_id_fkey FOREIGN KEY (name_id) REFERENCES Names_(name_id);

ALTER TABLE Directors
ADD CONSTRAINT Directors_name_id_fkey FOREIGN KEY (name_id) REFERENCES Names_(name_id);

ALTER TABLE Writers
ADD CONSTRAINT Writers_name_id_fkey FOREIGN KEY (name_id) REFERENCES Names_(name_id);

-- Enable foreign key check lock
SET foreign_key_checks = 1;
