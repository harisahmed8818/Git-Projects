class Securefile :
    def __init__(self , filename , filesize):

       self.filename = filename # Public attribute  
       self._filesize = filesize  # Protective attribute
       self.__password = None # Private attribute
     
    def get_info(self):
       return f'{self.filename}({self._filesize} KB)'

    def password(self, password):
       self.__password = password

    def authenticate(self, password):
       return 'Access Granted' if self.__password == password else 'Access Denied'

File = Securefile('Report.pdf', 550)
print(File.get_info())

File.password('Mypassword')
print(File.authenticate('Mypassword'))
print(File.authenticate('Wrongpassword'))


