CREATE TABLE BloodTypes(
    ID INT PRIMARY KEY,
    Blood VARCHAR(255)
);

CREATE TABLE Donations(
    ID INT PRIMARY KEY,
    Donation VARCHAR(255),
    Description TEXT
);

CREATE TABLE Donors(
    Email VARCHAR(255) PRIMARY KEY,
    Name VARCHAR(255),
    Gender BIT,
    BirthDate DATE,
    Phone VARCHAR(255),
    BloodType INT NOT NULL DEFAULT 0,
    CONSTRAINT FKBloodType FOREIGN KEY (BloodType) REFERENCES BloodTypes (ID)
);

CREATE TABLE DonorsDonations(
    DonorsEmail VARCHAR(255),
    DonationID INT,
    CONSTRAINT FOREIGN KEY (DonorsEmail) REFERENCES Donors (Email),
    CONSTRAINT FOREIGN KEY (DonationID) REFERENCES Donations (ID)
);


