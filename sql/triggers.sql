CREATE OR REPLACE TRIGGER donor_age_trigger
    END IF;

END;
/


CREATE OR REPLACE TRIGGER donor_audit_trigger

AFTER INSERT OR DELETE OR UPDATE
ON Donor

FOR EACH ROW

BEGIN

    IF INSERTING THEN

        INSERT INTO Audit_Log(
            action_type,
            donor_id,
            action_date,
            performed_by
        )

        VALUES(
            'INSERT',
            :NEW.donor_id,
            SYSDATE,
            USER
        );

    ELSIF DELETING THEN

        INSERT INTO Audit_Log(
            action_type,
            donor_id,
            action_date,
            performed_by
        )

        VALUES(
            'DELETE',
            :OLD.donor_id,
            SYSDATE,
            USER
        );

    ELSIF UPDATING THEN

        INSERT INTO Audit_Log(
            action_type,
            donor_id,
            action_date,
            performed_by
        )

        VALUES(
            'UPDATE',
            :NEW.donor_id,
            SYSDATE,
            USER
        );

    END IF;

END;
/