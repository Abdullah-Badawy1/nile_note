from website import create_app

# this is to run falsk application && start off web server
app=create_app()
if __name__=='__main__':
    app.run(debug=True)

