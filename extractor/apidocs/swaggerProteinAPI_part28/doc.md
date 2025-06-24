{
  "server_url": "",
  "paths": {
    "/proteomes/proteins/{upid}": {
      "get": {
        "tags": [
          "proteomes"
        ],
        "summary": "Get proteins by proteome UPID",
        "description": "",
        "operationId": "getProteinsByUpid",
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
          },
          {
            "name": "reviewed",
            "in": "query",
            "description": "Reviewed(true) or not Reviewed (false)",
            "required": false,
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
        }
      }
    }
  }
}