# tumonline_mailer

mails all students on the list, except for empy LV and Fixplatz students

instructions:

1. use windows, have outlook open I guess


2. python csv_mailer.py /path/to/recipients.csv /path/to/content.txt


<i>recipients.csv: standard tumonline export</i>

<i>content.txt: string only, salutation will be added automatically</i>

dummy run:

<b>python csv_mailer.py .\csv_test.csv .\txt_test.txt</b>
