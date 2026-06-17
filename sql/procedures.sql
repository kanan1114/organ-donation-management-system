CREATE OR REPLACE PROCEDURE add_donor_proc(

    p_donor_id NUMBER,
    p_donor_name VARCHAR2,
    p_age NUMBER,
    p_gender VARCHAR2,
    p_blood_group VARCHAR2,
    p_organ_type VARCHAR2,
    p_city VARCHAR2,
    p_contact VARCHAR2

)

IS

BEGIN

    INSERT INTO Donor
    VALUES(

        p_donor_id,
        p_donor_name,
        p_age,
        p_gender,
        p_blood_group,
        p_organ_type,
        p_city,
        p_contact

    );

    COMMIT;

END;
/