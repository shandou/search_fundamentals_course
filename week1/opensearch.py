from flask import g, current_app
from opensearchpy import OpenSearch

# Create an OpenSearch client instance and put it into Flask shared space for use by the application
def get_opensearch():
    host = "localhost"
    port = 9200
    auth = ("admin", "admin")

    if "opensearch" not in g:
        #### Step 4.a:
        # Implement a client connection to OpenSearch so that the rest of the application can communicate with OpenSearch
        g.opensearch = OpenSearch(
            hosts=[{"host": host, "port": port}], http_auth=auth, scheme="https", verify_certs=False
        )

    return g.opensearch
