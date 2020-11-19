from flask import Flask,render_template,request
import getClass
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('firstpage.html')

@app.route('/data',methods=['GET','POST'])
def receiveData():
    #print(request.args)
    if request.method == 'POST':
        uploaded_file = request.files['filename']
        print(request.form)
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        #captcha_response=request.form['g-recaptcha-response']
        # if(captcha_response==None or captcha_response==''):
        #     return 'Please enter captcha'
        return getClass.load_image(os.getcwd()+"\\\\"+uploaded_file.filename,os.getcwd()+"\\Models\\EN\\EN.h5")

if __name__ == '__main__':
    app.run()
