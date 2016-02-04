BEGIN TRANSACTION;
CREATE TABLE revlog (
    id              integer primary key,
    cid             integer not null,
    usn             integer not null,
    ease            integer not null,
    ivl             integer not null,
    lastIvl         integer not null,
    factor          integer not null,
    time            integer not null,
    type            integer not null
);
CREATE TABLE notes (
    id              integer primary key,
    guid            text not null,
    mid             integer not null,
    mod             integer not null,
    usn             integer not null,
    tags            text not null,
    flds            text not null,
    sfld            integer not null,
    csum            integer not null,
    flags           integer not null,
    data            text not null
);
CREATE TABLE graves (
    usn             integer not null,
    oid             integer not null,
    type            integer not null
);
CREATE TABLE col (
    id              integer primary key,
    crt             integer not null,
    mod             integer not null,
    scm             integer not null,
    ver             integer not null,
    dty             integer not null,
    usn             integer not null,
    ls              integer not null,
    conf            text not null,
    models          text not null,
    decks           text not null,
    dconf           text not null,
    tags            text not null
);
CREATE TABLE cards (
    id              integer primary key,
    nid             integer not null,
    did             integer not null,
    ord             integer not null,
    mod             integer not null,
    usn             integer not null,
    type            integer not null,
    queue           integer not null,
    due             integer not null,
    ivl             integer not null,
    factor          integer not null,
    reps            integer not null,
    lapses          integer not null,
    left            integer not null,
    odue            integer not null,
    odid            integer not null,
    flags           integer not null,
    data            text not null
);
CREATE INDEX ix_revlog_usn on revlog (usn);
CREATE INDEX ix_revlog_cid on revlog (cid);
CREATE INDEX ix_notes_usn on notes (usn);
CREATE INDEX ix_notes_csum on notes (csum);
CREATE INDEX ix_cards_usn on cards (usn);
CREATE INDEX ix_cards_sched on cards (did, queue, due);
CREATE INDEX ix_cards_nid on cards (nid);

INSERT INTO `col` VALUES (1,1342638000,1345895996617,1345895996564,11,0,0,0,'{"nextPos": 1, "estTimes": true, "activeDecks": [1], "sortType": "noteFld", "timeLim": 0, "sortBackwards": false, "addToCur": true, "curDeck": 1, "newSpread": 0, "dueCounts": true, "curModel": "1345895996596", "collapseTime": 1200}','{"1345895996596": {"vers": [], "name": "Basic", "tags": [], "did": 1, "usn": -1, "req": [[0, "all", [0]]], "flds": [{"size": 20, "name": "Front", "media": [], "rtl": false, "ord": 0, "font": "Arial", "sticky": false}, {"size": 20, "name": "Back", "media": [], "rtl": false, "ord": 1, "font": "Arial", "sticky": false}], "sortf": 0, "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n", "tmpls": [{"afmt": "{{FrontSide}}\n\n<hr id=answer>\n\n{{Back}}", "name": "Card 1", "qfmt": "{{Front}}", "did": null, "ord": 0, "bafmt": "", "bqfmt": ""}], "latexPost": "\\end{document}", "type": 0, "id": "1345895996596", "css": ".card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n", "mod": 1345895996}, "1342701190172": {"vers": [], "name": "Einfach", "tags": [], "did": 1342701190228, "usn": -1, "req": [[0, "all", [0]]], "flds": [{"name": "Front", "media": [], "sticky": false, "rtl": false, "ord": 0, "font": "Arial", "size": 12}, {"name": "Back", "media": [], "sticky": false, "rtl": false, "ord": 1, "font": "Arial", "size": 12}], "sortf": 0, "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n", "tmpls": [{"name": "Forward", "qfmt": "{{Front}}", "did": null, "bafmt": "", "afmt": "{{FrontSide}}\n\n<hr id=answer>\n\n{{Back}}", "ord": 0, "bqfmt": ""}], "latexPost": "\\end{document}", "type": 0, "id": 1342701190172, "css": ".card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n\n.card1 { background-color: #FFFFFF; }", "mod": 1342701190}, "1345895996595": {"vers": [], "name": "Cloze", "tags": [], "did": 1, "usn": -1, "flds": [{"size": 20, "name": "Text", "media": [], "rtl": false, "ord": 0, "font": "Arial", "sticky": false}, {"size": 20, "name": "Extra", "media": [], "rtl": false, "ord": 1, "font": "Arial", "sticky": false}], "sortf": 0, "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n", "tmpls": [{"afmt": "{{cloze:Text}}<br>\n{{Extra}}", "name": "Cloze", "qfmt": "{{cloze:Text}}", "did": null, "ord": 0, "bafmt": "", "bqfmt": ""}], "latexPost": "\\end{document}", "type": 1, "id": "1345895996595", "css": ".card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n\n.cloze {\n font-weight: bold;\n color: blue;\n}", "mod": 1345895996}}','{"1": {"desc": "", "name": "Default", "extendRev": 50, "usn": 0, "collapsed": false, "newToday": [0, 0], "timeToday": [0, 0], "dyn": 0, "extendNew": 10, "conf": 1, "revToday": [0, 0], "lrnToday": [0, 0], "id": 1, "mod": 1345895996}, "1342701190228": {"name": "Current words", "extendRev": 50, "usn": -1, "collapsed": false, "newToday": [37, 0], "timeToday": [37, 0], "dyn": 0, "extendNew": 10, "conf": 1, "revToday": [37, 0], "lrnToday": [37, 0], "id": 1342701190228, "mod": 1345895996, "desc": "Please see the <a href=''https://ankiweb.net/shared/info/1372516784''>shared deck page</a> for more info."}}','{"1": {"name": "Default", "replayq": true, "lapse": {"leechFails": 8, "minInt": 1, "delays": [10], "leechAction": 0, "mult": 0}, "rev": {"perDay": 100, "ivlFct": 1, "maxIvl": 36500, "minSpace": 1, "ease4": 1.3, "fuzz": 0.05}, "timer": 0, "maxTaken": 60, "usn": 0, "new": {"perDay": 20, "delays": [1, 10], "separate": true, "ints": [1, 4, 7], "initialFactor": 2500, "order": 1}, "mod": 0, "id": 1, "autoplay": true}}','{}');


