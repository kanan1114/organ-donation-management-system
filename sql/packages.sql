CREATE OR REPLACE PACKAGE donor_package AS

    PROCEDURE get_total_donors;

    PROCEDURE get_total_recipients;

END donor_package;
/


CREATE OR REPLACE PACKAGE BODY donor_package AS

    PROCEDURE get_total_donors IS

        total NUMBER;

    BEGIN

        SELECT COUNT(*)
        INTO total
        FROM Donor;

        DBMS_OUTPUT.PUT_LINE(
            'Total Donors: ' || total
        );

    END;


    PROCEDURE get_total_recipients IS

        total NUMBER;

    BEGIN

        SELECT COUNT(*)
        INTO total
        FROM Recipient;

        DBMS_OUTPUT.PUT_LINE(
            'Total Recipients: ' || total
        );

    END;

END donor_package;
/