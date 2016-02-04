CREATE TABLE Word(
    word TEXT PRIMARY KEY,
    rank INTEGER,
    known_earlier BOOLEAN NOT NULL,     /* czy znane w momencie pytania */
    known_now BOOLEAN NOT NULL,    /* czy znane teraz */
    mod_time TIMESTAMP DEFAULT (DATETIME('now')) NOT NULL
);