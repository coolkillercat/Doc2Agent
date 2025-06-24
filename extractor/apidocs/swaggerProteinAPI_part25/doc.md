{
  "server_url": "",
  "paths": {
    "/proteins/{dbtype}:{dbid}": {
      "get": {
        "tags": [
          "proteins"
        ],
        "summary": "Get UniProt entries by UniProt cross reference and its ID",
        "description": "",
        "operationId": "getByCrossReference",
        "produces": [
          "application/xml",
          "application/json",
          "text/x-fasta",
          "text/x-flatfile"
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
            "description": "Cross reference database type, e.g, Ensembl, PDBe, etc. ",
            "required": true,
            "type": "string"
          },
          {
            "name": "dbid",
            "in": "path",
            "description": "Cross-reference ID, e.g. ENSP00000351276 for Ensembl",
            "required": true,
            "type": "string"
          },
          {
            "name": "reviewed",
            "in": "query",
            "description": "Reviewed(true) or not Reviewed (false)",
            "required": false,
            "type": "string"
          },
          {
            "name": "isoform",
            "in": "query",
            "description": "0 for exclude isoform only and 1 for isoform only",
            "required": false,
            "type": "integer",
            "format": "int32"
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