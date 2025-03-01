class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://datasigmatex_user:p2FlDdrlENg46LqTh4thWxHPAry7DZvn@dpg-cv07nrqn91rc73flmsag-a/datasigmatex"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    UPLOAD_FOLDER = "gofile" 
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "pdf", "xls", "xlsx", "rar", "zip"}
    MAX_FILE_SIZE = 100 * 1024 * 1024  
    
    SECRET_KEY = "https://jwt.io/#debugger-io?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.cThIIoDvwdueQB468K5xDc5633seEFoqwxjF_xSJyQQ"
    FLASK_DEBUG = True
    
    GOFILE_API_URL = "https://api.gofile.io"
    GOFILE_ACCOUNT_ID = "c696de56-af90-456f-a1a8-524ca2f62971"  
    GOFILE_ACCOUNT_TOKEN = "3u2Xcm8tBy9gkAlYKz7G5zhCQDMt9G2H"  