#importing the bottle frame work and os
from bottle import Bottle,run,response,static_file
import os

#creating the application instance
app = Bottle()

#Set the base path directory where the file has stored
base_dir = os.path.abspath(os.path.dirname(__file__))
print("Base Directory",base_dir)

#creating an route for the method get method
@app.route('/downloadExcel/<filename:path>',method=['GET'])
def download_Excel(filename):
    try:
        file_path = os.path.join(base_dir,'reports',filename)
        if not os.path.isfile(file_path):
            raise FileNotFoundError("File Not Found")
        return static_file(filename,root=base_dir+'/reports',download = True)
    
    except FileNotFoundError as e:
        response.status = 404
        return {'status':False,'error':str(e)}
    
    except Exception as error:
        response.status = 500
        return {'status':False,'error':str(e)}
    

if __name__ == '__main__':
    run(app,debug=True)