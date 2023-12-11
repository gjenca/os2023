
import os.path

class DataDir:


    def __init__(self,dirname):

        self.dirname=dirname


    def __getitem__(self,filename):

        with open(self.dirname+'/'+filename) as f:

            return f.read()

    def __setitem__(self,filename,val):

        with open(os.path.join(self.dirname,filename),'w') as f:

            f.write(val)


        


            

    
