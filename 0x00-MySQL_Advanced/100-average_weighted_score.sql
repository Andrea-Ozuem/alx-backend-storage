-- creates a stored procedure ComputeAverageWeightedScoreForUser that
--  computes and store the average weighted score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN p_user_id INT)
BEGIN
    DECLARE weight_fac INT;
    DECLARE sum_weight INT;
    SELECT SUM(projects.weight * corrections.score) INTO weight_fac FROM projects JOIN corrections 
        ON projects.id = corrections.project_id WHERE corrections.user_id = p_user_id;
    SELECT SUM(weight) INTO sum_weight FROM projects JOIN corrections ON projects.id = corrections.project_id
        WHERE corrections.user_id = p_user_id;
    UPDATE users SET average_score = weight_fac / sum_weight WHERE users.id = p_user_id;    
END; $$
DELIMITER ;
