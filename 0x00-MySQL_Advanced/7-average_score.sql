-- creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
    BEGIN
        DECLARE u_avg FLOAT;
        SELECT AVG(score) INTO u_avg FROM corrections WHERE user_id = p_user_id;
        UPDATE users SET average_score = u_avg WHERE users.id = p_user_id;
    END; $$
DELIMITER ;
