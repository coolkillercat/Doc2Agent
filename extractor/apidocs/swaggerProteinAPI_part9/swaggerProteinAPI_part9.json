{
  "server_url": "",
  "paths": {
    "/coordinates/{dbtype}:{dbid}": {
      "get": {
        "tags": [
          "coordinates"
        ],
        "summary": "Search UniProt entries by genomic database cross reference IDs: Ensembl, CCDS, HGNC or RefSeq",
        "description": "",
        "operationId": "getByDbXRef",
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
            "name": "dbtype",
            "in": "path",
            "description": "Cross-reference database type: Ensembl, CCDC, HGNC or RefSeq",
            "required": true,
            "type": "string"
          },
          {
            "name": "dbid",
            "in": "path",
            "description": "Cross reference ID, such as ENSP00000351276 for Ensembl, NP_083392 for RefSeq, CCDS52493 for CCDS, 26588 for HGNC, (case insensitive).",
            "required": true,
            "type": "string",
            "maxItems": 50,
            "minItems": 4
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