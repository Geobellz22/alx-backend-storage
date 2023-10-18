-- create a function safeDiv that divides and 
-- returns the first by the second number

DELIMITER $$ ;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE result FLOAT;
        IF b = 0 THEN;
           RETURN 0;
        ELSE
            RETURN a / b;
        END IF;
    END $$
DELIMITER ; $$
