-- Create the user user_0d_1 if it does not exist and set its password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1 on the MySQL server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the changes
FLUSH PRIVILEGES;
