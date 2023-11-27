from tkinter import *
import win32api
from tkinter import ttk
import time
from time import ctime,strftime,strptime
from datetime import date
#from tkinter.filedialog import asksaveasfile
import prices
import mysql.connector
from pyscreenshot import grab
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import shutil
from tkinter import messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox,AutocompleteEntry
import os.path
import pywhatkit
#--------------------------------------------------------------------------------

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

#database connection------------------------------------------------------------------

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1011',
    database='bill'
)
mycursor=mydb.cursor()


#tkinter window-------------------------------------------------------------------------

root=Tk()

style=ttk.Style()
style.theme_use('vista')
style.configure('Treeview',fieldbackground='black',background='light pink')
#root.resizable(False,False)
root.state('zoomed')
root.title('jewellery billing')
root.config(background='lavender')

'''bkg=PhotoImage(file='bis_1_r.png')
Label(root,image=bkg).place(x=0,y=293)'''



que_name="SELECT name FROM detail"
mycursor.execute(que_name)
rec=mycursor.fetchall()
name_list=[r for r , in rec]

que_name2="SELECT itemname FROM name_of_items"
mycursor.execute(que_name2)
rec2=mycursor.fetchall()
itemnamelist=[r for r , in rec2]

x=prices.gold_price()
y=prices.silver_price()

Label(root,text='Sangam Jewellers',font=("Times", "24", "bold italic"),bg='lavender',fg='teal').pack()
Label(root,text='chhoti line jagadhri , yamunanagar',fg='black',bg='lavender',font=("Times", "10", "bold italic")).pack()
Label(root,text='Customer Name ',bg='lavender',font=("Times", "10", "bold ")).place(x=0,y=80)
Label(root,text='Phone No ',bg='lavender',font=("Times", "10", "bold ")).place(x=200,y=80)
Label(root,text='Mail',bg='lavender',font=("Times", "10", "bold ")).place(x=355,y=80)
Label(root,text='Select Item',bg='lavender',font=("Times", "10", "bold ")).place(x=0,y=180)
Label(root,text='Enter Qty',bg='lavender',font=("Times", "10", "bold ")).place(x=200,y=180)
Label(root,text='stone wt',bg='lavender',font=("Times", "10", "bold ")).place(x=200,y=220)
Label(root,text='stone Rs',bg='lavender',font=("Times", "10", "bold ")).place(x=200,y=260)
Label(root,text='Enter Weight',bg='lavender',font=("Times", "10", "bold ")).place(x=355,y=180)
Label(root,text='Enter Rate',bg='lavender',font=("Times", "10", "bold ")).place(x=355,y=220)
Label(root,text='Labor',bg='lavender',font=("Times", "10", "bold ")).place(x=355,y=260)
Label(root,text='purity',bg='lavender',font=("Times", "10", "bold ")).place(x=0,y=220)
Label(root,text='GOLD: ',bg='lavender',font=("Times", "10", "bold ")).place(x=200,y=130)
Label(root,text='SILVER: ',bg='lavender',font=("Times", "10", "bold ")).place(x=355,y=130)
Label(root,text=x,fg='red',bg='lavender',font=("Times", "10", "bold ")).place(x=260,y=130)
Label(root,text=y,fg='red',bg='lavender',font=("Times", "10", "bold ")).place(x=410,y=130)





t=StringVar()
#total=Entry(root,width=10,textvariable=t).place(x=10,y=120)
w=StringVar()
#w.set(0)
weight=Entry(root,width=8,textvariable=w).place(x=440,y=180)
r=StringVar()
rate=Entry(root,width=8,textvariable=r).place(x=440,y=220)
q=StringVar()
quantity=Entry(root,width=8,textvariable=q).place(x=285,y=180)
st=StringVar()
stone=Entry(root,width=8,textvariable=st).place(x=285,y=220)
st.set(0.0)
cn=StringVar()
name=AutocompleteEntry(root,width=15,textvariable=cn,completevalues=name_list)
name.place(x=100,y=80)
pn=StringVar()
phone=Entry(root,width=12,textvariable=pn).place(x=270,y=80)
ml=StringVar()
maiil=Entry(root,width=20,textvariable=ml).place(x=400,y=80)
lb=StringVar()
sil_labor=Entry(root,width=8,textvariable=lb).place(x=440,y=260)
lb.set(0)
stpr=StringVar()
stone_price=Entry(root,width=8,textvariable=stpr).place(x=285,y=260)

def check_weight():
    gett=w.get()
    gett=str(gett)
    count=0
    for i in gett:
        if i=='.':
            count+=1
    if count>1:
        messagebox.showerror('error','enter correct weight')

def f(event):
    que_all= f"SELECT phone,email FROM detail where name='{cn.get()}'"
    mycursor.execute(que_all)
    
    reco=mycursor.fetchall()
    
    phone_list=[(a,b) for a,b , in reco]
    
    pn.set(phone_list[-1][0])
    ml.set(phone_list[-1][1])

name.bind('<Return>',f)

p=StringVar()
gol=['916','833','750']
sil=['DS70','925','T925','999','S925','C70','C999']
purity=AutocompleteCombobox(root,width=10,textvariable=p)
purity.place(x=70,y=220)

def gold():
    
    itemchoosen['values']=itemnamelist
    #purity['values']=gol
    purity=AutocompleteCombobox(root,width=10,textvariable=p,completevalues=gol)
    purity.place(x=70,y=220)
    
    
def silver():
    
    itemchoosen['values']=itemnamelist
    #purity['values']=sil
    purity=AutocompleteCombobox(root,width=10,textvariable=p,completevalues=sil)
    purity.place(x=70,y=220)


v = IntVar()
a=Radiobutton(root, text = 'GOLD', variable = v,value = x,command=gold,bg='lavender',fg='teal',font=('Times','12','bold')).place(x=0,y=130)
b=Radiobutton(root, text = 'SILVER', variable = v,value = y,command=silver,bg='lavender',fg='teal',font=('Times','12','bold')).place(x=80,y=130)

#goldd=['chain','ring','bangles','tikka','bali','tops','locket','necklace','kada','bracelet']
'''items=['chain','kada','L ring','G ring','payal','bicchiya','bangles','bali','tops',
    'locket','bacha kada','bracelet','watch','bansuri','tikka','mangalsutra','necklace']'''


n=StringVar()
itemchoosen=AutocompleteCombobox(root,width=10,textvariable=n,completevalues=itemnamelist)
itemchoosen.place(x=70,y=180)
itemchoosen.current()


tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4","c5","c6","c7"), show='headings', height=10)
tree.column("# 1", anchor=CENTER,width=50)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER,width=120)
tree.heading("# 2", text="Item")
tree.column("# 3", anchor=CENTER,width=80)
tree.heading("# 3", text="qty")
tree.column("# 4", anchor=CENTER,width=80)
tree.heading("# 4", text="G Weight")
tree.column("# 5", anchor=CENTER,width=80)
tree.heading("# 5", text="Stones")
tree.column("# 6", anchor=CENTER,width=80)
tree.heading("# 6", text="Nt Weight")
tree.column("# 7", anchor=CENTER,width=80)
tree.heading("# 7", text="Purity")
tree.place(x=10,y=300)
# all transactions information--------------------------------------------------------------------------

'''def info():
    doot=Toplevel()
    
    doot.geometry('500x400+390+150')
    doot.title('jewellery billing')
    doot.config(background='lavender')
    
    customer=cn.get()

    query = f"SELECT phone FROM detail where name='{cn.get()}'"

    ## getting records from the table
    mycursor.execute(query)

    ## fetching all records from the 'cursor' object
    records = mycursor.fetchall()
    l=[r for r,in records]
    #print(l)
    ## Showing the data
    if records:
        
            
        Label(doot,text=records[1],bg='lavender').pack()
    else:

        Label(doot,text='No Customer Exists',fg='red',font=("Times", "30", "bold italic"),bg='lavender').pack()
      
                                            
Button(root,text='INFO',command=info,bg='teal',fg='pink').place(x=340,y=250)'''



def reset():
    cn.set('')
    pn.set('')
    ml.set('')
    purity.set('')
    w.set('')
    itemchoosen.set('')
    tree.delete(*tree.get_children())
    lis.clear()


#mail sending ---------------------------------------------------------------------------------
def whatsapp():
    x=os.listdir('Bills')
    z=[]
    q=[]
    for i in x:
        z.append(time.ctime(os.path.getmtime(f'Bills\{i}'))[4:])
        q.append(i)
    zp=list(zip(z,q))
    szp=sorted(zp)
    #print(szp)
    pywhatkit.sendwhats_image(f'+91{pn.get()}',f'Bills\\{szp[-1][1]}','Thanks for shopping with us 😊👍')

def printbill():
    x=os.listdir('Bills')
    z=[]
    q=[]
    for i in x:
        z.append(time.ctime(os.path.getmtime(f'Bills\{i}'))[4:])
        q.append(i)
    zp=list(zip(z,q))
    szp=sorted(zp)
    file_to_print = f'Bills\\{szp[-1][1]}'
      
    if file_to_print: 
        
        # Print Hard Copy of File 
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0) 

def mail():
    try:
        body = '''Hello,
        Thanks for shopping with us
        sicerely yours
        Mohit Handa
        '''
        # put your email here
        sender = 'mohithanda1011@gmail.com'
        # get the password in the gmail (manage your google account, click on the avatar on the right)
        # then go to security (right) and app password (center)
        # insert the password and then choose mail and this computer and then generate
        # copy the password generated here
        password = 'jiszebxqevycepih'
        # put the email of the receiver here
        receiver=ml.get()

        if receiver!=None:
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender
            message['To'] = receiver
            message['Subject'] = 'This email has an attacment, a pdf file'

            message.attach(MIMEText(body, 'plain'))

            pdfname = f'{cn.get()}.pdf'

            # open the file in bynary
            binary_pdf = open(pdfname, 'rb')

            payload = MIMEBase('application', 'octate-stream', Name=pdfname)
            # payload = MIMEBase('application', 'pdf', Name=pdfname)
            payload.set_payload((binary_pdf).read())

            # enconding the binary into base64
            encoders.encode_base64(payload)

            # add header with pdf name
            payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
            message.attach(payload)

            #use gmail with port
            session = smtplib.SMTP('smtp.gmail.com', 587)

            #enable security
            session.starttls()

            #login with mail_id and password
            session.login(sender, password)

            text = message.as_string()
            session.sendmail(sender, receiver, text)
            session.quit()
            
            messagebox.showinfo('information','Mail sent successfully',parent=boot)  
    except:
        
        messagebox.showwarning('warning','Email not given',parent=boot)

#moving to other location------------------------------------------------------------
def movee():
    source=f'D:/Users/HP/PycharmProjects/tkintergui/jewsoft/{cn.get()}.png'
    destination=f'D:/Users/HP/PycharmProjects/tkintergui/jewsoft/Bills/{cn.get()}.png'
    shutil.move(source,destination)

#____________________________________________________________________________________________________
def msg(message,title='info'):
    messagebox.showinfo(title,message)

def vill():
    
    global boot
    x=prices.gold_price()
    yhy=prices.silver_price()
    cname=cn.get()
    pno=pn.get()
    d1=date.today()
    cur_date=d1.strftime("%Y-%m-%d")
    m=ml.get()
    

    boot=Tk()
    boot.geometry('800x500+390+150')
    boot.resizable(0,0)
    boot.title('BILL')
    

    Label(boot,text='Sangam Jewellers',font=("Times", "24", "bold italic"),fg='teal').pack()
    Label(boot,text='chhoti line jagadhri , yamunanagar',fg='black',font=("Times", "10", "bold italic")).pack()
    
    
    
    Label(boot,text='                           |                           |                           |                           |                           |                           |                           |                           |').place(x=10,y=70)
    Label(boot,text='----------------------------------------------------------------------------------------------------------------------------------').place(x=90,y=90)
    Label(boot,text='                           |                           |                           |                           |                           |                           |                           |                           |').place(x=10,y=110)
    Label(boot,text='                           |                           |                           |                           |                           |                           |                           |                           |').place(x=10,y=130)
    
    
    Label(boot,text='ITEM',font=("Times", "10", "bold italic")).place(x=115,y=70)
    Label(boot,text='quantity',font=("Times", "10", "bold italic")).place(x=200,y=70)
    Label(boot,text='G Weight',font=("Times", "10", "bold italic")).place(x=285,y=70)
    Label(boot,text='Stones',font=("Times", "10", "bold italic")).place(x=370,y=70)
    Label(boot,text='Nt Weight',font=("Times", "10", "bold italic")).place(x=445,y=70)
    Label(boot,text='Purity',font=("Times", "10", "bold italic")).place(x=540,y=70)
    Label(boot,text='Making',font=("Times", "10", "bold italic")).place(x=625,y=70)
    Label(boot,text='TOTAL',font=("Times", "10", "bold italic")).place(x=700,y=70)

    time_string = strftime('%H:%M:%S %p')

    
    Label(boot,text=cname.capitalize()).place(x=0,y=0)
    Label(boot,text=time_string).place(x=0,y=20)
    Label(boot,text=pno).place(x=0,y=40)
    Label(boot,text='GOLD: ',font=('Times','10','bold')).place(x=0,y=300)
    Label(boot,text='SILVER: ',font=('Times','10','bold')).place(x=0,y=330)
    Label(boot,text=x,fg='red',font=('Times','10','bold')).place(x=50,y=300)
    Label(boot,text=yhy,fg='red',font=('Times','10','bold')).place(x=50,y=330)
    Label(boot,text='NOTE : "उधार एक जादू है, हम देंगे और आप गायब हो जाएंगे।"',fg='red',font=("Times", "15", "bold")).place(x=0,y=400)
    
    tot=[]
    z=105
    zz=205
    zzz=290
    m_c=375
    l_c=460
    g_c=545
    t_c=630
    e_c=715
    y=110
    why=150
    e=100

    rate=x
    rat=yhy
    ra=int(250)
    
    lbr=0
    def generatebill():
        global wname
        d=date.today() 
        cdate=d.strftime("%d-%m-%y")
        ctime=strftime('%H-%M')
        im = grab(bbox=(400, 180, 1190, 640))
        wname=cname+"_"+cdate+"_"+ctime
        im.save(f'Bills/{wname}.png')  
        
    mking=0
    lbr=0
    g=0
    r=0
    f=0
    for i in lis:
        i0=i[0]
        i1=i[1]
        i2=i[2]
        i3=i[3]
        i4=i[4]
        i5=i[5]
        ntweight=float(i2)-float(i3)
        levar=i[6]
        gram=i[7]
        if gram!='':
            f=ntweight*int(gram)
            mking=0
        else:
            if (i4=='833' or i4=='750' or i4=='916'):
                r=i5*0.0001*ntweight*(float(i4)+70)
                mking=r*0.2
                #lbr=r*0.02
                #g=r*0.03
                f=r+mking
            
            
            
            elif i4=='DS70':
                r=ntweight*i5*0.1
                #lbr=r*0.20
                #g=r*0.03
                mking=int(levar)
                f=r+mking
            
        
        Label(boot,text='                           |                           |                           |                           |                           |                           |                           |                           |').place(x=10,y=why)
        Label(boot,text=i[0],fg='teal').place(x=z,y=y)
        Label(boot,text=i[1],fg='teal').place(x=zz,y=y)
        Label(boot,text=i[2],fg='teal').place(x=zzz,y=y)
        Label(boot,text=i[3],fg='teal').place(x=m_c,y=y)
        Label(boot,text=float(i[2])-float(i[3]),fg='teal').place(x=l_c,y=y)
        Label(boot,text=i[4],fg='teal').place(x=g_c,y=y)
        Label(boot,text=round(mking),fg='teal').place(x=t_c,y=y)
        Label(boot,text=int(f),fg='teal').place(x=e_c,y=y)
        
        Label(boot,text='CHARGES %',font=('Times','10','bold')).place(x=650,y=300)
        Label(boot,text='MAKING       10 %').place(x=650,y=340)
        Label(boot,text='GST                2 %').place(x=650,y=360)
        Label(boot,text='LABOR          916 - 10%').place(x=650,y=380)
        Label(boot,text='                      833 - 2%').place(x=650,y=400)
        Label(boot,text='                      750 - 2%').place(x=650,y=420)
        
        def insert_to_db():
            mycursor=mydb.cursor()
            sql='INSERT INTO detail (Name,Phone,Item,Weight,Purity,Rate,Total,Metal,date,email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            if i3==1:
                val=(cname,pno,i[0],i[1],i[2],rate,f,'gold',cur_date,m)
                mycursor.execute(sql, val)
                mydb.commit()
            elif i3==2:
                if i[2]=='925' or i[2]=='T925':
                    val=(cname,pno,i[0],i[1],i[2],ra,f,'silver',cur_date,m)
                    mycursor.execute(sql, val)
                    mydb.commit()
                else:
                    val=(cname,pno,i[0],i[1],i[2],rat,f,'silver',cur_date,m)
                    mycursor.execute(sql, val)
                    mydb.commit()

            
            print('Items added successfully')
        tot.append(int(f))
        y+=20
        why+=20
        
    
    Label(boot,text=sum(tot),font=('Times','10','bold')).place(x=715,y=why-20)
    t.set((tot))
    
    
    Button(boot,text='EXIT',command=boot.destroy).place(x=400,y=470)
    Button(boot,text='GENERATE',command=generatebill).place(x=500,y=470)
    Button(boot,text='WAPP',command=combine_funcs(whatsapp)).place(x=600,y=470)
    Button(boot,text='MAIL',command=mail).place(x=650,y=470)
    Button(boot,text='PRINT',command=printbill).place(x=700,y=470)
    
    boot.mainloop()


lis=[]
listt=[]

class added_items:
    def __init__(self):
        self.z=285
        self.no=1

    def destroy(self):
        try:
            
            selected_item = tree.selection()[-1]
            #print(selected_item)
            tree.delete(selected_item)
            lis.remove(lis[int(selected_item[3])-1])
            #self.no-=1
        except:
            messagebox.showerror('error','No items to remove',parent=root)

    def add(self):
        
        global l

        gett=w.get()
        gett=str(gett)
        count=0
        for i in gett:
            if i=='.':
                count+=1
        if count>1:
            messagebox.showerror('error','enter correct weight',parent=root)

        elif itemchoosen.get()=='':
            messagebox.showerror('noitem','please select item',parent=root)
        elif w.get()=='':
            messagebox.showerror('noweight','please enter weight of item',parent=root)
        elif w.get()=='0':
            messagebox.showerror('noweight','weight cannot be 0',parent=root)
        

        elif p.get()=='':
            messagebox.showerror('nopurity','please select purity of item',parent=root)
        else:
            lis.append((itemchoosen.get(),q.get(),w.get(),st.get(),p.get(),v.get(),lb.get(),r.get()))
            tree.insert('', 'end',text="1",values=(self.no,lis[-1][0],lis[-1][1],lis[-1][2],lis[-1][3],float(lis[-1][2])-float(lis[-1][3]),lis[-1][4],lis[-1][5]))
            
            self.no+=1

        
obj=added_items()
    

Button(root,text='GET BILL',command=vill ,width=7,height=2,bg='medium purple' ,fg='white').place(x=30, y=570)
Button(root,text='ADD',command=obj.add,bg='medium purple',width=7,height=2,fg='white').place(x=310, y=570)
Button(root,text='EXIT',command=root.destroy ,width=7,height=2 ,bg='Indian Red' ,fg='white').place(x=240, y=570)
Button(root,text='RESET',command=reset ,width=7,height=2 ,bg='medium purple' ,fg='white').place(x=100, y=570)
Button(root,text='Remove',command=obj.destroy ,width=7,height=2 ,bg='medium purple',fg='white' ).place(x=170, y=570)

root.mainloop()
