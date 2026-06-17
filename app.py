from flask import Flask, render_template, request, redirect,session
import oracledb

app = Flask(__name__)
app.secret_key = "organprojectsecret"

connection = oracledb.connect(
    user="organ_admin",
    password="organ123",
    host="localhost",
    port=1521,
    service_name="XEPDB1"
)
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        cursor = connection.cursor()

        query = """
        SELECT *
        FROM Admins
        WHERE username = :1
        AND password = :2
        """

        cursor.execute(query, [username, password])

        admin = cursor.fetchone()

        if admin:

            session['admin'] = username

            return redirect('/')

        else:

            return render_template(
                'login.html',
                error='Invalid Username or Password'
            )

    return render_template('login.html')
@app.route('/logout')
def logout():

    session.pop('admin', None)

    return redirect('/login')
@app.route('/')
def home():
    if 'admin' not in session:
       return redirect('/login')       
    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM Donor"
    )
    donor_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM Recipient"
    )
    recipient_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM Hospital"
    )
    hospital_count = cursor.fetchone()[0]

    return render_template(
        'index.html',
        donor_count=donor_count,
        recipient_count=recipient_count,
        hospital_count=hospital_count
    )


@app.route('/dashboard')
def dashboard():

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM Donor"
    )
    donor_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM Recipient"
    )
    recipient_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM Hospital"
    )
    hospital_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM Transplant"
    )
    transplant_count = cursor.fetchone()[0]

    return render_template(
        'dashboard.html',
        donor_count=donor_count,
        recipient_count=recipient_count,
        hospital_count=hospital_count,
        transplant_count=transplant_count
    )


@app.route('/donors')
def donors():

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM Donor"
    )

    donor_data = cursor.fetchall()

    return render_template(
        'donors.html',
        donors=donor_data
    )


@app.route('/recipients')
def recipients():

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM Recipient"
    )

    recipient_data = cursor.fetchall()

    return render_template(
        'recipients.html',
        recipients=recipient_data
    )


@app.route('/hospitals')
def hospitals():

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM Hospital"
    )

    hospital_data = cursor.fetchall()

    return render_template(
        'hospitals.html',
        hospitals=hospital_data
    )


@app.route('/transplants')
def transplants():

    cursor = connection.cursor()

    query = """
    SELECT
        d.donor_name,
        r.recipient_name,
        t.result_status,
        t.transplant_date
    FROM Transplant t
    JOIN Donor d
    ON t.donor_id = d.donor_id
    JOIN Recipient r
    ON t.recipient_id = r.recipient_id
    """

    cursor.execute(query)

    transplant_data = cursor.fetchall()

    return render_template(
        'transplants.html',
        transplants=transplant_data
    )


@app.route('/search', methods=['GET', 'POST'])
def search():

    donors = []

    if request.method == 'POST':

        blood_group = request.form['blood_group']

        cursor = connection.cursor()

        query = """
        SELECT *
        FROM Donor
        WHERE blood_group = :1
        """

        cursor.execute(query, [blood_group])

        donors = cursor.fetchall()

    return render_template(
        'search.html',
        donors=donors
    )


@app.route('/add_donor', methods=['GET', 'POST'])
def add_donor():

    if request.method == 'POST':

        donor_id = request.form['donor_id']
        donor_name = request.form['donor_name']
        age = request.form['age']
        gender = request.form['gender']
        blood_group = request.form['blood_group']
        organ_type = request.form['organ_type']
        city = request.form['city']
        contact = request.form['contact']

        cursor = connection.cursor()

        query = """
        INSERT INTO Donor
        VALUES(
            :1,:2,:3,:4,
            :5,:6,:7,:8
        )
        """

        try:

            cursor.execute(query, (
                donor_id,
                donor_name,
                age,
                gender,
                blood_group,
                organ_type,
                city,
                contact
            ))

            connection.commit()

            return redirect('/donors')

        except Exception as e:

            return render_template(
                'error.html',
                error_message=str(e)
            )

    return render_template('add_donor.html')

@app.route('/delete_donor/<int:donor_id>')
def delete_donor(donor_id):

    cursor = connection.cursor()

    query = """
    DELETE FROM Donor
    WHERE donor_id = :1
    """

    cursor.execute(query, [donor_id])

    connection.commit()

    return redirect('/donors')
@app.route('/edit_donor/<int:donor_id>', methods=['GET', 'POST'])
def edit_donor(donor_id):

    cursor = connection.cursor()

    if request.method == 'POST':

        donor_name = request.form['donor_name']
        age = request.form['age']
        city = request.form['city']
        contact = request.form['contact']

        query = """
        UPDATE Donor
        SET
            donor_name = :1,
            age = :2,
            city = :3,
            contact = :4
        WHERE donor_id = :5
        """

        cursor.execute(query, (
            donor_name,
            age,
            city,
            contact,
            donor_id
        ))

        connection.commit()

        return redirect('/donors')

    query = """
    SELECT *
    FROM Donor
    WHERE donor_id = :1
    """

    cursor.execute(query, [donor_id])

    donor = cursor.fetchone()

    return render_template(
        'edit_donor.html',
        donor=donor
    )
@app.route('/matches')
def matches():

    cursor = connection.cursor()

    query = """
    SELECT
        d.donor_name,
        d.blood_group,
        d.organ_type,
        r.recipient_name,
        r.required_organ
    FROM Donor d
    JOIN Recipient r
    ON d.blood_group = r.blood_group
    AND d.organ_type = r.required_organ
    """

    cursor.execute(query)

    match_data = cursor.fetchall()

    return render_template(
        'matches.html',
        matches=match_data
    )
if __name__ == '__main__':
    app.run(debug=True)