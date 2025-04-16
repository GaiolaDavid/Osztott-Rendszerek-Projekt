-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE `User` (
    `UserID` int  NOT NULL AUTO_INCREMENT ,
    `UserName` varchar(255)  NOT NULL ,
    `Gender` tinyint(1)  NOT NULL ,
    PRIMARY KEY (`UserID`)
);

CREATE TABLE `Answer` (
    `AnswerID` int  NOT NULL AUTO_INCREMENT ,
    `AnswersString` varchar(255)  NOT NULL ,
    `Questions` int  NOT NULL ,
    `UserID` int  NOT NULL ,
    PRIMARY KEY (`AnswerID`)
);

ALTER TABLE `Answer` ADD CONSTRAINT `fk_Answer_UserID` FOREIGN KEY(`UserID`)
REFERENCES `User` (`UserID`);

CREATE INDEX `idx_User_UserName`
ON `User` (`UserName`);
-- Insert data into User table
INSERT INTO `User` (`UserID`, `UserName`, `Gender`) VALUES
(1, 'Alice', 1),
(2, 'Bob', 0),
(3, 'Charlie', 0);

-- Insert data into Answer table
INSERT INTO `Answer` (`AnswerID`, `AnswersString`, `Questions`, `UserID`) VALUES
(1, 'Yes', 1, 1),
(2, 'No', 2, 2),
(3, 'Maybe', 3, 3);
