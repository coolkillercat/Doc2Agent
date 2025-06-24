{
  "server_url": "",
  "paths": {
    "/coordinates/glocation/{taxonomy}/{chromosome}:{gstart}-{gend}": {
      "get": {
        "tags": [
          "coordinates"
        ],
        "summary": "Get genome coordinate by protein sequence position",
        "description": "",
        "operationId": "getProteinPositionByGenomeLocation2",
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
            "name": "gstart",
            "in": "path",
            "description": "Genome location start",
            "required": true,
            "type": "string"
          },
          {
            "name": "gend",
            "in": "path",
            "description": "Genome location end",
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