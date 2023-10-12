-- creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER $$
CREATE PROCEDURE AddBonus(IN p_user_id INT, IN p_project_name varchar(255), IN p_score INT)
    BEGIN
        DECLARE p_id INT;
        SELECT id INTO p_id FROM projects WHERE name = p_project_name;
        IF p_id IS NULL THEN
            INSERT INTO projects (name) VALUES (p_project_name);
            SET p_id = LAST_INSERT_ID();
        END IF;
        INSERT INTO corrections (user_id, project_id, score) VALUES (p_user_id, p_id, p_score);
    END; $$
DELIMITER ;
