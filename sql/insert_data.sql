INSERT INTO Admins
VALUES(201, 'Riya Sharma', 22, 'A+', 'Kidney', 'High', 'Delhi');

INSERT INTO Recipient
VALUES(202, 'Arjun Mehta', 45, 'B+', 'Liver', 'Medium', 'Mumbai');

INSERT INTO Recipient
VALUES(203, 'Kunal Jain', 39, 'O+', 'Heart', 'Critical', 'Chandigarh');

INSERT INTO Recipient
VALUES(204, 'Mehak Verma', 30, 'AB+', 'Kidney', 'High', 'Pune');

INSERT INTO Recipient
VALUES(205, 'Tarun Kapoor', 50, 'A-', 'Lung', 'Critical', 'Jaipur');

INSERT INTO Recipient
VALUES(206, 'Nisha Gupta', 35, 'B-', 'Liver', 'High', 'Ludhiana');

INSERT INTO Recipient
VALUES(207, 'Harsh Bansal', 41, 'O-', 'Kidney', 'Medium', 'Delhi');

INSERT INTO Recipient
VALUES(208, 'Isha Khanna', 27, 'A+', 'Heart', 'Critical', 'Lucknow');


INSERT INTO Hospital
VALUES(301, 'Apollo Hospital', 'Delhi', '0112233445');

INSERT INTO Hospital
VALUES(302, 'Fortis Hospital', 'Mumbai', '0222233445');

INSERT INTO Hospital
VALUES(303, 'PGIMER', 'Chandigarh', '0172233445');

INSERT INTO Hospital
VALUES(304, 'Max Healthcare', 'Delhi', '0119988776');

INSERT INTO Hospital
VALUES(305, 'AIIMS', 'Delhi', '0115566778');


INSERT INTO Transplant
VALUES(401, 101, 201, 301, TO_DATE('2026-05-01','YYYY-MM-DD'), 'Successful');

INSERT INTO Transplant
VALUES(402, 102, 202, 302, TO_DATE('2026-05-03','YYYY-MM-DD'), 'Successful');

INSERT INTO Transplant
VALUES(403, 103, 203, 303, TO_DATE('2026-05-04','YYYY-MM-DD'), 'Pending');

INSERT INTO Transplant
VALUES(404, 104, 204, 304, TO_DATE('2026-05-05','YYYY-MM-DD'), 'Successful');

COMMIT;