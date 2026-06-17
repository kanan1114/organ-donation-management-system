-- Display donor, recipient, hospital, and transplant details together
SELECT *
FROM Hospital
WHERE city = 'Delhi';


-- Display all audit logs

SELECT *
FROM Audit_Log;


-- Display latest audit activity

SELECT *
FROM Audit_Log
ORDER BY action_date DESC;


-- Find average donor age

SELECT AVG(age) AS average_age
FROM Donor;


-- Find maximum and minimum donor age

SELECT MAX(age) AS max_age,
       MIN(age) AS min_age
FROM Donor;


-- Nested query: donors matching recipient blood groups

SELECT donor_name, blood_group
FROM Donor
WHERE blood_group IN (
    SELECT blood_group
    FROM Recipient
);


-- Nested query: hospitals involved in transplants

SELECT hospital_name
FROM Hospital
WHERE hospital_id IN (
    SELECT hospital_id
    FROM Transplant
);


-- Display donor count city-wise

SELECT city,
       COUNT(*) AS donor_count
FROM Donor
GROUP BY city;


-- Display recipient count city-wise

SELECT city,
       COUNT(*) AS recipient_count
FROM Recipient
GROUP BY city;