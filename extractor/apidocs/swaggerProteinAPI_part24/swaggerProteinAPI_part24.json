{
  "server_url": "",
  "paths": {
    "/proteins/{accession}/isoforms": {
      "get": {
        "tags": [
          "proteins"
        ],
        "summary": "Get UniProt isoform entries from parent entry accession",
        "description": "",
        "operationId": "getEntriesForIsoforms",
        "produces": [
          "application/xml",
          "application/json",
          "text/x-fasta",
          "text/x-flatfile"
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
                "$ref": "#/definitions/Entry"
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