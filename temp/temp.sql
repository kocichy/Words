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


INSERT INTO notes VALUES (317701757,'4fe47458-b2a7-48ba-9d03-86c840b24711',1342701190172,1454759435,-1,'','akcentowaæ, podkreœlaæ, uwydatniaæ, uwypuklaæ, wskazywaæemphasize','akcentowaæ, podkreœlaæ, uwydatniaæ, uwypuklaæ, wskazywaæ',1467122191,0,'');
INSERT INTO cards VALUES (741483108,317701757,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (948352656,'6674424e-3748-401a-a4a1-ac5930ab5f1c',1342701190172,1454759435,-1,'','bardzo, szeroko, znaczniewidely','bardzo, szeroko, znacznie',1467122191,0,'');
INSERT INTO cards VALUES (826266973,948352656,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (941023930,'797cad48-6448-48eb-821e-5a7e8a1a826a',1342701190172,1454759435,-1,'','etyka, filozofiaphilosophy','etyka, filozofia',1467122191,0,'');
INSERT INTO cards VALUES (817805452,941023930,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (599050577,'65a5759b-6a61-4ef2-bee4-5c0340a537e6',1342701190172,1454759435,-1,'','budowaæ, czyniæ, dokonywaæ, konstruowaæ, skonstruowaæ, tworzyæ, wykonywaæ, zbudowaæconstruct','budowaæ, czyniæ, dokonywaæ, konstruowaæ, skonstruowaæ, tworzyæ, wykonywaæ, zbudowaæ',1467122191,0,'');
INSERT INTO cards VALUES (19660277,599050577,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (543845895,'23032160-0c52-4aa2-a3c1-a8513632f083',1342701190172,1454759435,-1,'','autoryzowaæ, pozwalaæ, pozwoliæ, umo¿liwiaæ, umo¿liwiæ, upowa¿niaæ, uzdalniaæ, uzdolniæ, w³¹czaæ, w³¹czyæenable','autoryzowaæ, pozwalaæ, pozwoliæ, umo¿liwiaæ, umo¿liwiæ, upowa¿niaæ, uzdalniaæ, uzdolniæ, w³¹czaæ, w³¹czyæ',1467122191,0,'');
INSERT INTO cards VALUES (837777742,543845895,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (242231954,'07efd377-bc98-4f8b-96e7-948f4b34f55e',1342701190172,1454759435,-1,'','ma³ofewer','ma³o',1467122191,0,'');
INSERT INTO cards VALUES (25363302,242231954,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (679274383,'2c69ef05-8e59-4165-b609-13f38d9e99ed',1342701190172,1454759435,-1,'','dowcip, koncepcja, koncept, myœl, pojêcie, pomys³concept','dowcip, koncepcja, koncept, myœl, pojêcie, pomys³',1467122191,0,'');
INSERT INTO cards VALUES (301266693,679274383,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (876703122,'b9ca37ff-b460-4e39-b471-216d396d899f',1342701190172,1454759435,-1,'','kod, kodeks, kodowaæ, numer, prawo, przepisy, szyfr, szyfrowaæ, zakodowaæcode','kod, kodeks, kodowaæ, numer, prawo, przepisy, szyfr, szyfrowaæ, zakodowaæ',1467122191,0,'');
INSERT INTO cards VALUES (913548851,876703122,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (152879303,'f14842d9-5be6-47bb-be7a-1543a950485d',1342701190172,1454759435,-1,'','myœleæ, oddaæ, ofiarowywaæ, planowaæ, przeznaczaæ, zamierzaæintend','myœleæ, oddaæ, ofiarowywaæ, planowaæ, przeznaczaæ, zamierzaæ',1467122191,0,'');
INSERT INTO cards VALUES (591252822,152879303,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (488818758,'68da751d-3659-48f8-a2d2-e43d9d352802',1342701190172,1454759435,-1,'','drapaæ, gama, kamieñ, kot³owiec, ³upina, ³uska, ³uskaæ, ³uszczyæ, niszczyciel, obieraæ, podzia³ka, przesadzaæ, skala, skalowaæ, skrobaæ, stopniowanie, szala, szalej, waga, wspinaæ, zgorzelinascale','drapaæ, gama, kamieñ, kot³owiec, ³upina, ³uska, ³uskaæ, ³uszczyæ, niszczyciel, obieraæ, podzia³ka, przesadzaæ, skala, skalowaæ, skrobaæ, stopniowanie, szala, szalej, waga, wspinaæ, zgorzelina',1467122191,0,'');
INSERT INTO cards VALUES (176937682,488818758,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (976114781,'047de37b-cb6c-4edf-8b5b-3e6ec8b2a830',1342701190172,1454759435,-1,'','sk³adnia, syntaktykasyntax','sk³adnia, syntaktyka',1467122191,0,'');
INSERT INTO cards VALUES (87172688,976114781,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (365879098,'efb32864-7d8d-46ef-9642-867a02eda6d9',1342701190172,1454759435,-1,'','informatyka, koder, programator, programista, programista specjalista w zakresie programowania, sterownikprogrammer','informatyka, koder, programator, programista, programista specjalista w zakresie programowania, sterownik',1467122191,0,'');
INSERT INTO cards VALUES (392100668,365879098,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (758990890,'40d5ce9a-d434-4da6-9a1a-63b94dc1694a',1342701190172,1454759435,-1,'','jawaJava','jawa',1467122191,0,'');
INSERT INTO cards VALUES (728818567,758990890,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (895412201,'f1d4679b-9803-49b8-9130-1cd3f36b543b',1342701190172,1454759435,-1,'','ekspres, ekspresowy, poci¹g pospieszny, szybkostrzelny, wyra¿aæ, wyraziæ, wyraŸnyexpress','ekspres, ekspresowy, poci¹g pospieszny, szybkostrzelny, wyra¿aæ, wyraziæ, wyraŸny',1467122191,0,'');
INSERT INTO cards VALUES (950335168,895412201,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (913129429,'9ee91bf0-08e1-483b-83ce-d6d3ad74080a',1342701190172,1454759435,-1,'','przedmiotowythe','przedmiotowy',1467122191,0,'');
INSERT INTO cards VALUES (603258748,913129429,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (240836952,'d60d4754-2691-4fbf-a619-a21915169e73',1342701190172,1454759435,-1,'','pyton, wieszczbiarzpython','pyton, wieszczbiarz',1467122191,0,'');
INSERT INTO cards VALUES (575072810,240836952,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (247231895,'bcf8f0a1-db72-4ddb-ab6e-1dad78cb50a6',1342701190172,1454759435,-1,'','czytelnoœæ, odczytywalnoœæ wskazañ przyrz¹du, przystosowanie do jazdy po drogach, trzymanie siê drogireadability','czytelnoœæ, odczytywalnoœæ wskazañ przyrz¹du, przystosowanie do jazdy po drogach, trzymanie siê drogi',1467122191,0,'');
INSERT INTO cards VALUES (900468665,247231895,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (779502825,'9fb0bb78-6734-49da-97e0-1419fc09a36e',1342701190172,1454759435,-1,'','byæ, czuæ, istnieæ, mieæ, miewaæ, nale¿eæ, nast¹piæ, nastêpowaæ, przys³ugiwaæ, wynosiæ, zaistnieæ, zostaæ, ¿yæbe','byæ, czuæ, istnieæ, mieæ, miewaæ, nale¿eæ, nast¹piæ, nastêpowaæ, przys³ugiwaæ, wynosiæ, zaistnieæ, zostaæ, ¿yæ',1467122191,0,'');
INSERT INTO cards VALUES (155262655,779502825,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (377844821,'0643463d-b942-45b9-9256-a89407a34380',1342701190172,1454759435,-1,'','a, i, oraz, zaœand','a, i, oraz, zaœ',1467122191,0,'');
INSERT INTO cards VALUES (294819850,377844821,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (957147152,'08548546-7952-4483-8332-a2597d99d384',1342701190172,1454759435,-1,'','do, ku, large extent, lesser degree, limited extent, na, po, pod, przy, w, wed³ug, wobec, za, zeto','do, ku, large extent, lesser degree, limited extent, na, po, pod, przy, w, wed³ug, wobec, za, ze',1467122191,0,'');
INSERT INTO cards VALUES (402715378,957147152,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (956405898,'8a9b656d-3ede-4230-aff8-73a52d2d619b',1342701190172,1454759435,-1,'','na, od, spoœród, z, zeof','na, od, spoœród, z, ze',1467122191,0,'');
INSERT INTO cards VALUES (383077653,956405898,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (530066658,'3a2d2057-d50c-4a94-808e-b53b57502f64',1342701190172,1454759435,-1,'','a, amper, jakiœ, pewien, wielea','a, amper, jakiœ, pewien, wiele',1467122191,0,'');
INSERT INTO cards VALUES (88527611,530066658,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (848656617,'4bffa23d-3372-4c3f-a38e-f8a8da6c6264',1342701190172,1454759435,-1,'','go, informatyczny, informatyka, jego, jej, nim, on, ono, tego, to, uczelnianyit','go, informatyczny, informatyka, jego, jej, nim, on, ono, tego, to, uczelniany',1467122191,0,'');
INSERT INTO cards VALUES (75128427,848656617,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (408863023,'31d940b6-f089-4b2e-9132-12cb1bc833c8',1342701190172,1454759435,-1,'','do, kierunek, na, plane, po, podczas, przede, w, we, wed³ug, wewn¹trz, wœród, zain','do, kierunek, na, plane, po, podczas, przede, w, we, wed³ug, wewn¹trz, wœród, za',1467122191,0,'');
INSERT INTO cards VALUES (55053714,408863023,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (71327133,'ded04921-4219-4033-8664-bd2f4fe68807',1342701190172,1454759435,-1,'','jaI','ja',1467122191,0,'');
INSERT INTO cards VALUES (436170587,71327133,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (490599731,'5ab868ea-a8bf-4efd-8bf2-8738d4a0be3d',1342701190172,1454759435,-1,'','do, licz¹c z grubsza, micro scopic scale, na, na wiatr, nad, ostro do wiatru, po, production scale, przy, rough calculation, u, w, wed³ug, windon','do, licz¹c z grubsza, micro scopic scale, na, na wiatr, nad, ostro do wiatru, po, production scale, przy, rough calculation, u, w, wed³ug, wind',1467122191,0,'');
INSERT INTO cards VALUES (796316399,490599731,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (797474548,'a68fb131-41eb-4b35-a39d-e26fbe0d76fc',1342701190172,1454759435,-1,'','albo, ani, b¹dŸ, czy, lubor','albo, ani, b¹dŸ, czy, lub',1467122191,0,'');
INSERT INTO cards VALUES (432294838,797474548,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (501943323,'b5e84b76-0a19-4fdd-8226-b495c73f765a',1342701190172,1454759435,-1,'','aran¿acja, cel, deseñ, oddaæ, ofiarowywaæ, planowaæ, pomyœleæ, projekt, projektowaæ, projektowanie, przeznaczaæ, rysownictwo, rysunek, wygl¹d, wzór, wzornictwo, zamiar, zamierzaæ, zamys³design','aran¿acja, cel, deseñ, oddaæ, ofiarowywaæ, planowaæ, pomyœleæ, projekt, projektowaæ, projektowanie, przeznaczaæ, rysownictwo, rysunek, wygl¹d, wzór, wzornictwo, zamiar, zamierzaæ, zamys³',1467122191,0,'');
INSERT INTO cards VALUES (788391175,501943323,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (220442223,'c8e14a96-21ff-4824-b937-f44f82827ea1',1342701190172,1454759435,-1,'','cel, rozmys³, zamiarpurpose','cel, rozmys³, zamiar',1467122191,0,'');
INSERT INTO cards VALUES (439873894,220442223,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (911762178,'0bbdcd3f-e5f2-4592-bb5b-bb975e248ccd',1342701190172,1454759435,-1,'','myus','my',1467122191,0,'');
INSERT INTO cards VALUES (666219088,911762178,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (79901969,'64ff20be-183e-4601-9c7f-cb2d88602da1',1342701190172,1454759435,-1,'','ani¿eli, ni¿than','ani¿eli, ni¿',1467122191,0,'');
INSERT INTO cards VALUES (676458737,79901969,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (553695288,'866896e7-5b21-49df-8557-8157cef3d150',1342701190172,1454759435,-1,'','podobny, takisuch','podobny, taki',1467122191,0,'');
INSERT INTO cards VALUES (265594351,553695288,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (207070457,'adafeeb1-2300-4d6d-9a02-ba261810b5f0',1342701190172,1454759435,-1,'','zarównoboth','zarówno',1467122191,0,'');
INSERT INTO cards VALUES (988235454,207070457,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (932217081,'f290045a-d4da-4a54-9ab2-05439bdaf2c9',1342701190172,1454759435,-1,'','dawaæ, dopuszczaæ, oddaæ, ofiarowywaæ, pozwalaæ, pozwoliæ, przeznaczyæ, przyznaæ, przyznawaæ, uwzglêdniaæ, uznawaæ, zezwalaæ, zezwoliæallow','dawaæ, dopuszczaæ, oddaæ, ofiarowywaæ, pozwalaæ, pozwoliæ, przeznaczyæ, przyznaæ, przyznawaæ, uwzglêdniaæ, uznawaæ, zezwalaæ, zezwoliæ',1467122191,0,'');
INSERT INTO cards VALUES (187361426,932217081,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (379307042,'ba727512-08ff-47a3-9717-7771d9c9a6dd',1342701190172,1454759435,-1,'','plan, program, programowaæprogram','plan, program, programowaæ',1467122191,0,'');
INSERT INTO cards VALUES (704849428,379307042,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (267523523,'0f35f141-bf85-4e7f-920b-46a126e16357',1342701190172,1454759435,-1,'','charakter, je¿yk, jêzyk, mowa, styllanguage','charakter, je¿yk, jêzyk, mowa, styl',1467122191,0,'');
INSERT INTO cards VALUES (628370992,267523523,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (360645022,'314cccdb-8b70-4d58-ae3b-04802a53a62e',1342701190172,1454759435,-1,'','dumny, g³ówny, mocno, silny, œwiatowy, wielki, wybitny, wysoki, wysoko, wy¿ baryczny, ¿ywyhigh','dumny, g³ówny, mocno, silny, œwiatowy, wielki, wybitny, wysoki, wysoko, wy¿ baryczny, ¿ywy',1467122191,0,'');
INSERT INTO cards VALUES (576875385,360645022,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (188258010,'72757b97-6012-475b-8246-0313f06be5b3',1342701190172,1454759435,-1,'','b³ahy, drobny, epizodyczny, ma³e, ma³ostkowy, ma³y, niedu¿y, nieliczny, niewielki, pod³ysmall','b³ahy, drobny, epizodyczny, ma³e, ma³ostkowy, ma³y, niedu¿y, nieliczny, niewielki, pod³y',1467122191,0,'');
INSERT INTO cards VALUES (331768000,188258010,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (520722569,'25140f6d-ae66-484a-8161-693903355307',1342701190172,1454759435,-1,'','du¿y, obfity, rozleg³y, szeroki, wielki, wielkoformatowylarge','du¿y, obfity, rozleg³y, szeroki, wielki, wielkoformatowy',1467122191,0,'');
INSERT INTO cards VALUES (238100371,520722569,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (754485939,'06854430-de0e-42f7-81ac-a60a4ecbce53',1342701190172,1454759435,-1,'','granica, kierunek, kolejka, kreska, kreœliæ, lina, linea³, linia, linijka, liniowaæ, przekreœlaæ, rodzaj, rysowaæ, rz¹d, specjalnoœæ, szereg, sznur, szpaler, wers, wiersz, wierszowanieline','granica, kierunek, kolejka, kreska, kreœliæ, lina, linea³, linia, linijka, liniowaæ, przekreœlaæ, rodzaj, rysowaæ, rz¹d, specjalnoœæ, szereg, sznur, szpaler, wers, wiersz, wierszowanie',1467122191,0,'');
INSERT INTO cards VALUES (459226306,754485939,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (60315603,'6cb3559c-a838-4cee-9084-7bfe99e47767',1342701190172,1454759435,-1,'','ca³kowity, cliæ, ewidentny, jasno, jasny, kasowaæ, klarowny, ocliæ, oczyszczaæ, oczywisty, odblokowaæ, odblokowywaæ, odp³acaæ, pe³ny, pogodnie, przecieraæ, przejaœniaæ, przejrzyœcie, sp³acaæ, sprecyzowaæ, sprz¹taæ, torowaæ, widny, wolny, wykarczowaæ, wyrazisty, wyraŸny, zamykaæclear','ca³kowity, cliæ, ewidentny, jasno, jasny, kasowaæ, klarowny, ocliæ, oczyszczaæ, oczywisty, odblokowaæ, odblokowywaæ, odp³acaæ, pe³ny, pogodnie, przecieraæ, przejaœniaæ, przejrzyœcie, sp³acaæ, sprecyzowaæ, sprz¹taæ, torowaæ, widny, wolny, wykarczowaæ, wyrazisty, wyraŸny, zamykaæ',1467122191,0,'');
INSERT INTO cards VALUES (478311988,60315603,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (448572332,'f0375fe0-72b4-45b2-b2fa-17c0573730ca',1342701190172,1454759435,-1,'','libella, naprawiaæ, poziom, poziomica, poziomnica, poziomy, równaæ, równia, równy, stopieñ, szczebel, wyrównaæ, wysokoœæ, zrównaæ, zrównywaælevel','libella, naprawiaæ, poziom, poziomica, poziomnica, poziomy, równaæ, równia, równy, stopieñ, szczebel, wyrównaæ, wysokoœæ, zrównaæ, zrównywaæ',1467122191,0,'');
INSERT INTO cards VALUES (961448949,448572332,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (244402943,'dd836067-4de6-4460-8a28-0f4059dc70bb',1342701190172,1454759435,-1,'','ewentualnoœæ, ewentualny, mo¿liwy, niemo¿liwypossible','ewentualnoœæ, ewentualny, mo¿liwy, niemo¿liwy',1467122191,0,'');
INSERT INTO cards VALUES (499726326,244402943,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (810252535,'5e0a2e8e-92cb-47c5-b98c-ee285dffc9e5',1342701190172,1454759435,-1,'','chroniæ, dawaæ, dostarczaæ, dostarczyæ, kierowaæ, oddaæ, postanawiaæ, przewidywaæ, zabezpieczaæ, zabezpieczyæ, zaopatrywaæ, zapewniaæ, zarz¹dzaæprovide','chroniæ, dawaæ, dostarczaæ, dostarczyæ, kierowaæ, oddaæ, postanawiaæ, przewidywaæ, zabezpieczaæ, zabezpieczyæ, zaopatrywaæ, zapewniaæ, zarz¹dzaæ',1467122191,0,'');
INSERT INTO cards VALUES (729889428,810252535,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
INSERT INTO notes VALUES (573376876,'32896d2b-3167-47a6-9c11-6f0452eff486',1342701190172,1454759435,-1,'','genera³, generalny, g³ówny, lo¿a, makroekonomia, ogólnikowy, ogólnobudowlany, ogólnogospodarczy, ogólnoœæ, ogólny, walnygeneral','genera³, generalny, g³ówny, lo¿a, makroekonomia, ogólnikowy, ogólnobudowlany, ogólnogospodarczy, ogólnoœæ, ogólny, walny',1467122191,0,'');
INSERT INTO cards VALUES (52379140,573376876,1342701190228,0,1454759435,-1,0,0,177,0,2500,0,0,0,0,0,0,'');
COMMIT;
