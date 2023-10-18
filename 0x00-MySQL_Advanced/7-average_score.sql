-- Create a stored procedure ComputeAverageScoreForUser
-- computes and store the average score for a student. 
-- An average score can be a decimal

DELIMITER $$;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average_score INT;
    UPDATE users
    SET average_score = (SELECT Avg(score) FROM corrections WHERE user_id = corrections.user_id)
    where id=user_id;
END $$
DELIMITER ; $$
