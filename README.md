# tumonline_mailer

mails all students on the exported csv list, except for empty LV (~Anmeldeverfahren Dummy) and all students that were assigned a 'Fixplatz'

instructions:

1. use windows, have outlook open


2. python csv_mailer.py /path/to/recipients.csv /path/to/content.txt


<i>recipients.csv: standard tumonline export</i>

<i>content.txt: string only, salutation will be added automatically</i>

dummy run:

<b>python csv_mailer.py .\csv_test.csv .\txt_test.txt</b>

to preview who will be mailed, enter t (test) when prompted (e for execution when ready)
