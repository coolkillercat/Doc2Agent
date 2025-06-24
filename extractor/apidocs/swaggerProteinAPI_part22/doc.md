{
  "server_url": "",
  "paths": {
    "/proteins/interaction/{accession}": {
      "get": {
        "tags": [
          "proteins"
        ],
        "summary": "Get UniProt interactions by accession",
        "description": "",
        "operationId": "getAllInteractionEntries",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "accession",
            "in": "path",
            "description": "UniProt accession",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/UPInteraction"
              }
            }
          },
          "400": {
            "description": "Invalid accession parameter. The values's format should be a valid UniProtKB accession.",
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