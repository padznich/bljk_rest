-- Last modification date: 2017-02-28 06:54:23.947

-- Prepare for new tables
DROP TABLE IF EXISTS detail_description;
DROP TABLE IF EXISTS grid_detail;
DROP TABLE IF EXISTS grid_summary;

-- tables

-- tables
-- Table: detail_description
CREATE TABLE detail_description (
    id serial  NOT NULL,
    hand varchar(32)  NULL,
    summ int  NULL,
    cards varchar(32)  NULL,
    action varchar(32)  NULL,
    rate real  NULL,
    win real  NULL,
    detail_id int  NOT NULL,
    CONSTRAINT detail_description_pk PRIMARY KEY (id)
);

-- Table: grid_detail
CREATE TABLE grid_detail (
    id serial  NOT NULL,
    game_id varchar(40)  NULL,
    time time  NULL,
    wagered real  NULL,
    result real  NULL,
    summary_id int  NOT NULL,
    identifier varchar(32)  NULL,
    CONSTRAINT grid_detail_pk PRIMARY KEY (id)
);

CREATE UNIQUE INDEX game_id on grid_detail (game_id ASC,summary_id ASC, identifier ASC);

-- Table: grid_summary
CREATE TABLE grid_summary (
    id serial  NOT NULL,
    date date  NOT NULL,
    game varchar(40)  NULL,
    min int  NULL,
    plays int  NULL,
    wagered real  NULL,
    winnings real  NULL,
    pending real  NULL,
    identifier varchar(32)  NULL,
    CONSTRAINT grid_summary_pk PRIMARY KEY (id)
);

CREATE UNIQUE INDEX date_game on grid_summary (date ASC,game ASC, identifier ASC);

-- foreign keys
-- Reference: detail_description_grid_detail (table: detail_description)
ALTER TABLE detail_description ADD CONSTRAINT detail_description_grid_detail
    FOREIGN KEY (detail_id)
    REFERENCES grid_detail (id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: summary_detail_by_id (table: grid_detail)
ALTER TABLE grid_detail ADD CONSTRAINT summary_detail_by_id
    FOREIGN KEY (summary_id)
    REFERENCES grid_summary (id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

insert into grid_summary (date, identifier) values('01-08-17', 1);
insert into grid_summary (date, identifier) values('02-08-17', 1);
insert into grid_summary (date, identifier) values('03-08-17', 1);

insert into grid_detail (time, summary_id, identifier) values('01-08-17 10:34:09', 1, 1);
insert into grid_detail (time, summary_id, identifier) values('02-08-17 10:34:09', 1, 1);
insert into grid_detail (time, summary_id, identifier) values('03-08-17 10:34:09', 1, 1);
insert into grid_detail (time, summary_id, identifier) values('01-08-17 10:34:09', 2, 1);
insert into grid_detail (time, summary_id, identifier) values('02-08-17 10:34:09', 2, 1);
insert into grid_detail (time, summary_id, identifier) values('03-08-17 10:34:09', 2, 1);
insert into grid_detail (time, summary_id, identifier) values('01-08-17 10:34:09', 3, 1);
insert into grid_detail (time, summary_id, identifier) values('02-08-17 10:34:09', 3, 1);
insert into grid_detail (time, summary_id, identifier) values('03-08-17 10:34:09', 3, 1);

insert into detail_description (detail_id) values(1);
insert into detail_description (detail_id) values(2);
insert into detail_description (detail_id) values(3);
insert into detail_description (detail_id) values(4);
insert into detail_description (detail_id) values(5);
insert into detail_description (detail_id) values(6);
insert into detail_description (detail_id) values(7);
insert into detail_description (detail_id) values(8);
insert into detail_description (detail_id) values(9);

select * from grid_summary;
select * from grid_detail;
select * from detail_description;

-- End of file.