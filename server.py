import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the swagger.yml file from the `specification_dir` to configure the endpoints
app.add_api('swagger.yml')


@app.route('/')
def home():
    """
    This function just responds to the browser URL localhost:5000
    """
    return "Endpoints are online."


# handling when app is run from cmd line
if __name__ == '__main__':
    print("running from cmd line")
    app.run(port=5000)
