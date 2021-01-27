IF NOT EXISTS
(SELECT [name] FROM sys.tables WHERE [name] = 'BloodTypes')
CREATE TABLE BloodTypes(
    ID INT PRIMARY KEY,
    Blood VARCHAR(255)
);

IF NOT EXISTS
(SELECT [name] FROM sys.tables WHERE [name] = 'Donations')
CREATE TABLE Donations(
    ID INT PRIMARY KEY,
    Donation NVARCHAR(255),
    Description NVARCHAR(512)
);

IF NOT EXISTS
(SELECT [name] FROM sys.tables WHERE [name] = 'Donors')
CREATE TABLE Donors(
    Email VARCHAR(255) PRIMARY KEY,
    Name NVARCHAR(255),
    Gender BIT,
    BirthDate DATE,
    Phone VARCHAR(255),
    BloodType INT NOT NULL DEFAULT 0 FOREIGN KEY REFERENCES BloodTypes(ID)
);

IF NOT EXISTS
(SELECT [name] FROM sys.tables WHERE [name] = 'DonorsDonations')
CREATE TABLE DonorsDonations(
    DonorsEmail VARCHAR(255) FOREIGN KEY REFERENCES Donors(Email),
    DonationID INT FOREIGN KEY REFERENCES Donations(ID),
);
