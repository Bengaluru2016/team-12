    fo = open(filename, "r")
    filecontent = fo.read()
    encodedcontent = base64.b64encode(filecontent)  # base64

    sender = 'adityagampa149@gmail.com'
    mypass=os.getenv('PASSWORD')
    reciever = ['aditya281295@gmail.com']

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = COMMASPACE.join(reciever)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = 'Report for '+college

    msg.attach(MIMEText("Consolidated Report:"))

    with open(filename, "rb") as fil:
        part = MIMEApplication(
            fil.read(),
            Name=basename(filename)
        )
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(filename)
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sender,mypass)
    server.sendmail(sender, reciever, msg.as_string())
    server.quit()
