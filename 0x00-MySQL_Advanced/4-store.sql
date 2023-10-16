-- script that create trigger 
-- decrease the quantity of an item
-- after adding a new order

DELIMITER $$

CREATE TRIGGER decrease_qunatity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity - NEW.number
    WHERE name = New.item_name;
END $$

DELIMITER ; $$
