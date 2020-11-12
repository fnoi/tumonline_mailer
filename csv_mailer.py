import sys, pandas as pd, win32com.client as win32

print ('number of arguments passed: ', format(len(sys.argv)), '- ok')
if len(sys.argv) != 3:
    print('error. please enter the paths to email list (csv) and desired email content (txt) along with script')
    exit()
else:
    print(str(sys.argv[1]))

if sys.argv[1].endswith('.csv'):
    csv = sys.argv[1]
elif sys.argv[1].endswith('.txt'):
    txt = sys.argv[1]

if sys.argv[2].endswith('.csv'):
    csv = sys.argv[2]
elif sys.argv[2].endswith('.txt'):
    txt = sys.argv[2]

o = win32.Dispatch('Outlook.Application')
for acc in o.Session.Accounts:
    if acc.DisplayName == 'exams.cms.bgu@tum.de':
        sender = acc
        break

df = pd.read_csv(csv,sep=';')
df_red = df[['VORNAME','NACHNAME','EMAIL','LV_TITEL','STATUS']].copy()

text_file = open(txt)
content = str(text_file.read())

for i in range(len(df_red)):
    if pd.isna(df_red.at[i,'LV_TITEL']) == False and df_red.at[i,'STATUS'] != 'Fixplatz':
        print(i, df_red.at[i,'VORNAME'])

    recipient = df_red.at[i,'EMAIL']
    firstname = df_red.at[i,'VORNAME']
    lastname = df_red.at[i,'NACHNAME']
    LV_name = df_red.at[i,'LV_TITEL']

    mail = o.CreateItem(0)
    mail.Recipients.Add(recipient)
    mail.Subject = 'Your application for \"' + str(LV_name) +'\"'
    mail.Bodyformat = 1
    mail.Body = 'Dear ' + str(firstname) + ' ' + str(lastname) + ',' + content

    mail._oleobj_.Invoke(*(64209, 0, 8, 0, sender))
    #mail.Display()
    mail.Send()