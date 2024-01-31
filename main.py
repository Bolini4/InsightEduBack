
from website import create_app


app = create_app()


    
if __name__ == '__main__':
    # app.run(ssl_context=('cert.pem','key.pem'),port=50100,debug=True)#WITH HTTPS 
    app.run(host="10.40.208.74",debug=True)