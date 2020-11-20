from flask import Flask,render_template,request
import getClass
import os,keras
app = Flask(__name__)
EN_model=keras.models.load_model(os.getcwd()+"/Models/EN/EN.h5")

@app.route('/')
def hello_world():
    return render_template('firstpage.html')

@app.route('/data',methods=['GET','POST'])
def receiveData():
    #print(request.args)
    try:
        if request.method == 'POST':
            uploaded_file = request.files['filename']
            print(request.form)
            if uploaded_file.filename != '':
                uploaded_file.save(uploaded_file.filename)
            #captcha_response=request.form['g-recaptcha-response']
            # if(captcha_response==None or captcha_response==''):
            #     return 'Please enter captcha'
            image_path=os.getcwd()+"/"+uploaded_file.filename
            #model_path=os.getcwd()+"/Models/EN/EN.h5"
            #image_path=os.getcwd()+"\\\\"+uploaded_file.filename
            #model_path=os.getcwd()+"\\Models\\EN\\EN.h5"
            print(image_path,'\n')
            return getClass.load_image(image_path,EN_model)
    except Exception as e:
        return e

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3000)
