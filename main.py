'''
This is Christopher Davis Portfolio Project
'''

from flask import*
import os
app=Flask(__name__)
PROFILE_IMAGE=os.path.join('static','profileimage')
IMAGES=os.path.join('static','images')
app.config['IMAGE_FOLDER']=PROFILE_IMAGE
app.config['IMAGE']=IMAGES
@app.route('/')
@app.route('/profile')
def profile():
    data=os.listdir(app.config['IMAGE_FOLDER'])
    images=os.listdir(app.config['IMAGE'])
    return render_template('main.html',profile_image=data,images=images)
if __name__=='__main__':
    if not os.path.exists(app.config['IMAGE_FOLDER']):
        os.mkdir(app.config['IMAGE_FOLDER'])
    if not os.path.exists(app.config['IMAGE']):
        os.mkdir(app.config['IMAGE'])
    app.run(debug=True)






















































