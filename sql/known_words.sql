SELECT (SELECT count(*) FROM Word
WHERE ? <= rank AND rank < ? AND known_earlier = 1)
* 1.0 /
(SELECT count(*) FROM Word
WHERE ? <= rank AND rank < ?);