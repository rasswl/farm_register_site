from flask import Flask, render_template, request, redirect

app = Flask(__name__)
registered = {}  # اسم_المزرعة => (اسم المستخدم، رقم الهاتف)

@app.route('/', methods=['GET', 'POST'])
def index():
    msg = ''
    if request.method == 'POST':
        name = request.form.get('name').strip()
        farm = request.form.get('farm').strip()
        phone = request.form.get('phone').strip()
        if farm in registered:
            msg = 'اسم المزرعة موجود من قبل، رجاء اختر واحد جديد.'
        else:
            registered[farm] = (name, phone)
            return redirect('/success')
    return render_template('index.html', msg=msg)

@app.route('/success')
def success():
    return '<h3>تم التسجيل! شكرًا لك.</h3><a href="/">رجوع</a>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
