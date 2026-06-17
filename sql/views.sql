CREATE VIEW donor_recipient_view AS

SELECT
    d.donor_name,
    r.recipient_name,
    t.result_status

FROM Transplant t

JOIN Donor d
ON t.donor_id = d.donor_id

JOIN Recipient r
ON t.recipient_id = r.recipient_id;