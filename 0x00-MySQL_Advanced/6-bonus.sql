-- creates a stored procedure AddBonus
-- taking 3 points in order
-- user_id a user.id value
-- project_name new or already exist projects
-- score the score value of correction
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;
    SELECT id INTO project_id FROM projects WHERE name = project_name;

     IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;
    
     INSERT INTO corrections (user_id, project_id, score)
     VALUES (user_id, project_id, score);
END $$
DELIMITER; $$
