from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        food = request.form['food']
        drink = request.form['drink']
        additional_info = request.form['additional-info']

        # Compose email message
        message = f"Name: {name}\nEmail: {email}\nFood: {food}\nDrink: {drink}\nAdditional Information: {additional_info}"

        # Send email
        sender_email = 'your-email@example.com'  # Replace with your email address
        receiver_email = 'your-email@example.com'  # Replace with the recipient's email address
        smtp_server = 'smtp.example.com'  # Replace with your SMTP server
        smtp_port = 587  # Replace with your SMTP server port
        smtp_username = 'your-username'  # Replace with your SMTP username
        smtp_password = 'your-password'  # Replace with your SMTP password

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(sender_email, receiver_email, message)

            return 'Thank you for your order!'
        except Exception as e:
            return f'An error occurred while processing your order: {str(e)}'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)