{
  "server_url": "",
  "paths": {
    "/mutagenesis/{accession}": {
      "get": {
        "tags": [
          "mutagenesis"
        ],
        "summary": "Get mutagenesis mapped to UniProt by accession",
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
          },
          {
            "name": "location",
            "in": "query",
            "description": "Filter by the amino acid range position in the sequence(s). Any valid amino acid range position within the length of the protein sequence such as 10-60 (start position to end position)",
            "required": false,
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