{
  "server_url": "",
  "paths": {
    "/coordinates/glocation/{taxonomy}/{chromosome}:{gPosition}": {
      "get": {
        "tags": [
          "coordinates"
        ],
        "summary": "Get genome coordinate by protein sequence position",
        "description": "",
        "operationId": "getProteinPositionByGenomeLocation",
        "produces": [
          "application/json",
          "application/xml"
        ],
        "parameters": [
          {
            "name": "taxonomy",
            "in": "path",
            "description": "Organism taxon ID",
            "required": true,
            "type": "string"
          },
          {
            "name": "chromosome",
            "in": "path",
            "description": "Chromosome name, i.e. 1, 2, X, etc.",
            "required": true,
            "type": "string"
          },
          {
            "name": "gPosition",
            "in": "path",
            "description": "Genome location position",
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
                "$ref": "#/definitions/PLocation2GLocationCollection"
              }
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