IF NOT EXISTS
(SELECT * FROM BloodTypes WHERE ID = 0 AND Blood IS NULL)
INSERT INTO BloodTypes
VALUES (0, NULL);

IF NOT EXISTS
(SELECT * FROM BloodTypes WHERE ID = 1 AND Blood = 'A')
INSERT INTO BloodTypes
VALUES (1, 'A');

IF NOT EXISTS
(SELECT * FROM BloodTypes WHERE ID = 2 AND Blood = 'B')
INSERT INTO BloodTypes
VALUES (2, 'B');

IF NOT EXISTS
(SELECT * FROM BloodTypes WHERE ID = 3 AND Blood = 'AB')
INSERT INTO BloodTypes
VALUES (3, 'AB');

IF NOT EXISTS
(SELECT * FROM BloodTypes WHERE ID = 4 AND Blood = 'O')
INSERT INTO BloodTypes
VALUES (4, 'O');

IF NOT EXISTS
(SELECT * FROM Donations WHERE ID = 1 AND Donation LIKE N'תרומת דם רגילה' AND Description LIKE N'תרומת דם רגילה סטנדרטית')
INSERT INTO Donations
VALUES (1 , N'תרומת דם רגילה', N'תרומת דם רגילה סטנדרטית');

IF NOT EXISTS
(SELECT * FROM Donations WHERE ID = 1 AND Donation LIKE N'טסיות' AND Description LIKE N'תרומת טסיות (החזרת דם)')
INSERT INTO Donations
VALUES (2 , N'טסיות', N'תרומת טסיות (החזרת דם)');

IF NOT EXISTS
(SELECT * FROM Donations WHERE ID = 1 AND Donation LIKE N'אפרזיס' AND Description LIKE N'תרומת כדוריות דם לבנות')
INSERT INTO Donations
VALUES (3 , N'אפרזיס', N'תרומת כדוריות דם לבנות');
