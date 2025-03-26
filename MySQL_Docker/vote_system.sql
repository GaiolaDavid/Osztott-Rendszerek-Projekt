-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE `User` (
    `UserID` int  NOT NULL ,
    `UserName` varchar(255)  NOT NULL ,
    `Gender` tinyint(1)  NOT NULL ,
    PRIMARY KEY (`UserID`)
);

CREATE TABLE `Answer` (
    `AnswerID` int  NOT NULL ,
    `AnswersString` varchar(255)  NOT NULL ,
    `Questions` int  NOT NULL ,
    `UserID` int  NOT NULL ,
    PRIMARY KEY (`AnswerID`)
);

ALTER TABLE `Answer` ADD CONSTRAINT `fk_Answer_UserID` FOREIGN KEY(`UserID`)
REFERENCES `User` (`UserID`);

CREATE INDEX `idx_User_UserName`
ON `User` (`UserName`);

