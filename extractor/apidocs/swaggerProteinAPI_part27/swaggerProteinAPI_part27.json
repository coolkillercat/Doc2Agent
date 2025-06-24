{
  "server_url": "",
  "paths": {
    "/proteomes/genecentric/{upid}": {
      "get": {
        "tags": [
          "proteomes"
        ],
        "summary": "Get gene centric proteins by proteome UPID is deprecated, please use new /genecentric?upid= endpoint",
        "description": "",
        "operationId": "getGeneCentricByUpidDeprecated",
        "produces": [
          "application/json",
          "application/xml"
        ],
        "parameters": [
          {
            "name": "upid",
            "in": "path",
            "description": "UniProt Proteome UPID",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/Proteome"
            }
          },
          "400": {
            "description": "Invalid upid parameter. The value format should match the regular expression UP[0-9]{9}.",
            "schema": {
              "$ref": "#/definitions/ErrorMessage"
            }
          },
          "404": {
            "description": "Resources not found",
            "schema": {
              "$ref": "#/definitions/ErrorMessage"
            }
          }
        },
        "deprecated": true
      }
    }
  }
}