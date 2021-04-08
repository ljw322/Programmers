SELECT count(DISTINCT NAME) FROM ANIMAL_INS WHERE NAME is not NULL;
-- distinct 바깥 말고, count 안에 넣었어야 한다.