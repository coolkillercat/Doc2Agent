{
  "server_url": "",
  "paths": {
    "/coordinates/{taxonomy}/{locations}/feature": {
      "get": {
        "tags": [
          "coordinates"
        ],
        "summary": "Search UniProt entries by taxonomy and genomic coordinates",
        "description": "",
        "operationId": "getFeatureByLocations",
        "produces": [
          "application/json",
          "application/xml",
          "text/x-gff"
        ],
        "parameters": [
          {
            "name": "offset",
            "in": "query",
            "description": "Off set, page starting point, with default value 0",
            "required": false,
            "type": "integer",
            "default": 0,
            "minimum": 0.0,
            "format": "int32"
          },
          {
            "name": "size",
            "in": "query",
            "description": "Page size with default value 100. When page size is -1, it returns all records and offset will be ignored",
            "required": false,
            "type": "integer",
            "default": 100,
            "format": "int32"
          },
          {
            "name": "taxonomy",
            "in": "path",
            "description": "Organism taxon ID",
            "required": true,
            "type": "string"
          },
          {
            "name": "locations",
            "in": "path",
            "description": "genomic locations such as x:58205437-58219305,12452535-12452536,2:32452, before colon is the chromosome such as x:58205437-58219305, or without chromosome such as 12452535-12452536, means any chromosome",
            "required": true,
            "type": "string"
          },
          {
            "name": "in_range",
            "in": "query",
            "description": "When it is set to true for location search, only those entries that are in the range will be retrieved",
            "required": false,
            "type": "boolean"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/GnEntry"
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