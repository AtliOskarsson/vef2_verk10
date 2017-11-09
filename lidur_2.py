from sys import argv
from bottle import *
from pymysql import *
db=Connect(host="tsuts.tskoli.is",user="0207002620",password="snotra2000",db="0207002620_vef2verk10",)
cursor=db.cursor()
cursor.execute("select * from user")

numrows=int(cursor.rowcount)
users={}
for i in range(numrows):
    row=cursor.fetchone()
    if row:
        users[row[0]]=row[1]
@route("/")
def index():
    return template("templates/index.tpl")
@route('/login' ,method="POST")
def login():
    cursor = db.cursor()
    cursor.execute("select * from user")
    numrows = int(cursor.rowcount)
    users = {}
    for i in range(numrows):
        row = cursor.fetchone()
        if row:
            users[row[0]] = row[1]
    notendanafn=request.forms.get("notendanafn")
    lykilord=request.forms.get("lykilord")
    submit=request.forms.get("submit")
    if notendanafn=="":
        villa={"villa":"Vantar notendanafn"}
        return template("templates/villa.tpl",villa)
    elif lykilord=="":
        villa={"villa":"Vantar lykilord"}
        return template("templates/villa.tpl",villa)
    elif submit=="Sign-up":
        for x in users:
            if notendanafn == x:
                villa={"villa":"Notendanafn í notkun"}
                return template("templates/villa.tpl",villa)
        cursor.execute("""insert into user(user,pass) values(%s,%s)""",(notendanafn,lykilord))
        db.commit()
        cursor.close()
        redirect("/velkominn")
    for x in users:
        if notendanafn==x and lykilord==users[x]:
            redirect("/velkominn")
    else:
        villa={"villa":"Notendanafn eða/og lykilorð rangt"}
        return template("templates/villa.tpl",villa)

@route('/Velkominn')
def login():
    return template("templates/leynisida.tpl")

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')

run(host='0.0.0.0', port=argv[1])