{
  "server_url": "",
  "paths": {
    "/proteomics/{accession}": {
      "get": {
        "tags": [
          "proteomics"
        ],
        "summary": "Get proteomics peptides mapped to UniProt by accession",
        "description": "",
        "operationId": "getByAccession",
        "produces": [
          "application/json",
          "application/xml",
          "text/x-gff"
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
              "$ref": "#/definitions/ProteinFeatureInfo"
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