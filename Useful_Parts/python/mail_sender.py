import smtplib
import mimetypes
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart

# Naive version
def sendmail_0(from_addr, to_addr_list, cc_addr_list, subject, message, login, password, picfiles=[], audiofiles = [], otherfiles = [], smtpserver='smtp.163.com'):
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
def sendmail_1(from_addr, to_addr_list, cc_addr_list, subject, message, login, password, picfiles=[], audiofiles = [], otherfiles = [], smtpserver='smtp.163.com'):
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

# Text mail with files
def sendmail_2(from_addr, to_addr_list, cc_addr_list, subject, message, login, password, picfiles=[], audiofiles = [], otherfiles = [], smtpserver='smtp.163.com'):
	'Text mail with files'
	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg['From'] = from_addr
	msg['To'] = ','.join(to_addr_list)
	msg['Cc'] = ','.join(cc_addr_list)

	text = MIMEText(message)
	msg.attach(text)
	for file in picfiles:
		fp = open(file, 'rb')
		mimetype, mimeencoding = mimetypes.guess_type(file)
		if mimeencoding or (mimetype is None):
			mimetype = "application/octet-stream"
		maintype, subtype = mimetype.split('/')
		img = MIMEImage(fp.read(), _subtype = subtype)
		fp.close()
		img.add_header("Content-Disposition","attachment",filename = file.split('\\')[-1])
		msg.attach(img)
	for file in audiofiles:
		fp = open(file, 'rb')
		mimetype, mimeencoding = mimetypes.guess_type(file)
		if mimeencoding or (mimetype is None):
			mimetype = "application/octet-stream"
		maintype, subtype = mimetype.split('/')
		audio = MIMEAudio(fp.read(), _subtype = subtype)
		fp.close()
		audio.add_header("Content-Disposition","attachment",filename = file.split('\\')[-1])
		msg.attach(audio)
	for file in otherfiles:
		fp = open(file, 'rb')
		mimetype, mimeencoding = mimetypes.guess_type(file)
		if mimeencoding or (mimetype is None):
			mimetype = "application/octet-stream"
		maintype, subtype = mimetype.split('/')
		other = MIMEBase(maintype, subtype)
		other.set_payload(fp.read())
		encoders.encode_base64(other)
		fp.close()
		other.add_header("Content-Disposition","attachment",filename = file.split('\\')[-1])
		msg.attach(other)

	server = smtplib.SMTP(smtpserver)
	server.starttls()
	server.login(login, password)
	problems = server.sendmail(from_addr, to_addr_list + cc_addr_list, msg.as_string())
	server.quit()
	return problems


sendmail_2(from_addr = '',
		to_addr_list = [''],
		cc_addr_list = [],
		subject = 'test',
		message = 'email via python',
		login = '',
		password = '',
		picfiles = [],
		audiofiles = [],
		otherfiles = [])
