import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://datasigmatex_user:p2FlDdrlENg46LqTh4thWxHPAry7DZvn@dpg-cv07nrqn91rc73flmsag-a/datasigmatex"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    cloudinary.config(
        cloud_name="dch1zqeid",
        api_key="832779739236957",
        api_secret="1lEut03YPYDu8BFtLQ1Q-olNm1Q",
        secure=True
    )
    
    UPLOAD_FOLDER = "cloudinary" 
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "pdf", "xls", "xlsx", "rar", "zip"}
    
    SECRET_KEY = "https://jwt.io/#debugger-io?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.cThIIoDvwdueQB468K5xDc5633seEFoqwxjF_xSJyQQ"
    FLASK_DEBUG = True
