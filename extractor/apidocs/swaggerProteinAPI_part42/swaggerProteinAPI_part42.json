{
  "server_url": "",
  "paths": {
    "/variation/accession_locations/{accession_locations}": {
      "get": {
        "tags": [
          "variation"
        ],
        "summary": "Get natural variants by list of accession and its locations",
        "description": "Among the available response content types, PEFF format (PSI Extended FASTA Format from the Human Proteome Organisation - Proteomics Standards Initiative, HUPO-PSI) is provided with only variants reported in the output.",
        "operationId": "getVariationForAccessionLocation",
        "produces": [
          "application/json",
          "application/xml",
          "text/x-gff",
          "text/x-peff"
        ],
        "parameters": [
          {
            "name": "accession_locations",
            "in": "path",
            "description": "UniProt accession(s). pipe | separated values accepted up to 100., example: P05067:5,7|P05067:12|0A024QZ33:2,5|A0A024QZ42:4",
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