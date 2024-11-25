
import os.path
import json

class JsonDir:


    def __init__(self,dirname):

        self.dirname=dirname


    def __getitem__(self,filename):

        with open(self.dirname+'/'+filename) as f:

            return json.loads(f.read())

    def __setitem__(self,filename,val):

        with open(os.path.join(self.dirname,filename),'w') as f:

            f.write(json.dumps(val))


        


            

    
