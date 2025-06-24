{
  "server_url": "",
  "paths": {
    "/genecentric/{accession}": {
      "get": {
        "tags": [
          "genecentric"
        ],
        "summary": "Get gene centric proteins by Uniprot accession",
        "description": "",
        "operationId": "getGeneCentricByAccession",
        "produces": [
          "application/json",
          "application/xml"
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
              "$ref": "#/definitions/CanonicalGene"
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