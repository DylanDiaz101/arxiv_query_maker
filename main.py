import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fetch_entries import fetch_entries

# check if today is the first day of the month; if not, exit.
if datetime.datetime.now().day != 1:
    print("Today is not the first day of the month. Exiting.")
    exit()

# define query URLs
# cognitive architecture search query
url_architecture = (
    'http://export.arxiv.org/api/query?'
    'search_query=all:cognitive+AND+all:architecture&'
    'start=0&max_results=10&sortBy=lastUpdatedDate&sortOrder=descending'
)

# cognitive modeling search query (includes "cognitive modeling" OR "computational cognitive modeling")
url_modeling = (
    'http://export.arxiv.org/api/query?'
    'search_query=all:%22cognitive%20modeling%22+OR+all:%22computational%20cognitive%20modeling%22&'
    'start=0&max_results=10&sortBy=lastUpdatedDate&sortOrder=descending'
)

# get entries
architecture_entries = fetch_entries(url_architecture)
modeling_entries = fetch_entries(url_modeling)

# sort the dates from most recent to less recent
architecture_entries.sort(
    key=lambda x: datetime.datetime.fromisoformat(x[1].replace("Z", "+00:00")),
    reverse=True
)
modeling_entries.sort(
    key=lambda x: datetime.datetime.fromisoformat(x[1].replace("Z", "+00:00")),
    reverse=True
)

# build the HTML email body with clickable links
html_body_lines = []
html_body_lines.append("<h2>Recent Cognitive Architecture Literature:</h2>")
html_body_lines.append("<ol>")
for idx, (title, published, pdf_link) in enumerate(architecture_entries, start=1):
    html_body_lines.append(
        f'<li>"{title}" : <a href="{pdf_link}">{pdf_link}</a> (Published: {published})</li>'
    )
html_body_lines.append("</ol>")

html_body_lines.append("<h2>Recent Computational Cognitive Modeling Literature:</h2>")
html_body_lines.append("<ol>")
for idx, (title, published, pdf_link) in enumerate(modeling_entries, start=1):
    html_body_lines.append(
        f'<li>"{title}" : <a href="{pdf_link}">{pdf_link}</a> (Published: {published})</li>'
    )
html_body_lines.append("</ol>")

email_body_html = "\n".join(html_body_lines)

# optionally, print the email body to the console for inspection
print(email_body_html)

# email configuration
my_email = "EMAIL"
password = "PASSWORD"  # Replace with your actual email password or app-specific password

# create a MIME email message with HTML content
msg = MIMEMultipart()
msg["From"] = my_email
msg["To"] = "RECEPIENT_EMAIL"
msg["Subject"] = "Recent Cognitive Architecture Literature"
msg.attach(MIMEText(email_body_html, "html"))

# send the email using Gmail's SMTP server (port 587 for TLS)
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.send_message(msg)
    print("Email sent successfully.")


