import smtplib
from email.mime.text import MIMEText

# Naive version
def sendmail_0(from_addr, to_addr_list, cc_addr_list, subject, message, login, password, smtpserver='smtp.163.com'):
        'Naive version'
	header  = 'From: %s\n' % from_addr
	header += 'To: %s\n' % ','.join(to_addr_list)
	header += 'Cc: %s\n' % ','.join(cc_addr_list)
	header += 'Subject: %s\n\n' % subject
	message = header + message

	server = smtplib.SMTP(smtpserver)
	server.starttls()
	server.login(login, password)
	problems = server.sendmail(from_addr, to_addr_list + cc_addr_list, message)
	server.quit()
	return problems

# Simple text email, generate header via MIMEText
def sendmail_1(from_addr, to_addr_list, cc_addr_list, subject, message, login, password, smtpserver='smtp.163.com'):
        'Simple text email, generate header via MIMEText'
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = ','.join(to_addr_list)
        msg['Cc'] = ','.join(cc_addr_list)

        server = smtplib.SMTP(smtpserver)
	server.starttls()
	server.login(login, password)
        problems = server.sendmail(from_addr, to_addr_list + cc_addr_list, msg.as_string())
        server.quit()
        return problems


sendmail_1(from_addr = '',
		to_addr_list = [],
		cc_addr_list = [],
		subject = 'test',
		message = 'email via python',
		login = '',
		password = '')
