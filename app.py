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
    try:
        if request.method == 'POST':
            uploaded_file = request.files['filename']
            print(request.form)
            if uploaded_file.filename != '':
                uploaded_file.save(os.getcwd()+'/images/'+uploaded_file.filename)
            captcha_response=request.form['g-recaptcha-response']
            if(captcha_response==None or captcha_response==''):
                return render_template('Invalid_Profile.html')
            image_path=os.getcwd()+"/images/"+uploaded_file.filename
            print(image_path,'\n')
            predictedClass=getClass.load_image(image_path,EN_model)
            return render_template('simplpc-4.html',
                                   cardiomegaly=predictedClass['Cardiomegaly'],
                                   consolidation=predictedClass['Consolidation'],
                                   pneumothorax=predictedClass['Pneumothorax'])
    except Exception as e:
        return e

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3000,debug=True)

#kill -9 $(ps -A | grep python | awk '{print $1}')