{
  "server_url": "",
  "paths": {
    "/coordinates/location/{accession}:{pStart}-{pEnd}": {
      "get": {
        "tags": [
          "coordinates"
        ],
        "summary": "Get genome coordinate by protein sequence position range",
        "description": "",
        "operationId": "getGenomeLocationByAccession",
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
          },
          {
            "name": "pStart",
            "in": "path",
            "required": true,
            "type": "integer",
            "format": "int32"
          },
          {
            "name": "pEnd",
            "in": "path",
            "required": true,
            "type": "integer",
            "format": "int32"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/PLocation2GLocationCollection"
            }
          },
          "400": {
            "description": "Invalid request Parameter.",
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