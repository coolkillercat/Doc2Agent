{
  "server_url": "",
  "paths": {
    "/antigen": {
      "get": {
        "tags": [
          "antigen"
        ],
        "summary": "Search antigens in UniProt",
        "description": "",
        "operationId": "search",
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
            "name": "accession",
            "in": "query",
            "description": "UniProt accession(s). Comma separated values accepted up to 100.",
            "required": false,
            "type": "string"
          },
          {
            "name": "antigen_sequence",
            "in": "query",
            "description": "Antigen sequence",
            "required": false,
            "type": "string",
            "maxItems": 2147483647,
            "minItems": 4
          },
          {
            "name": "antigen_id",
            "in": "query",
            "description": "Human Protein Atlas (HPA) antigen ID. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string",
            "maxItems": 2147483647,
            "minItems": 4
          },
          {
            "name": "ensembl_ids",
            "in": "query",
            "description": "Ensembl IDs. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string",
            "maxItems": 2147483647,
            "minItems": 4
          },
          {
            "name": "match_score",
            "in": "query",
            "description": "Minimum alignment score for the antigen sequence and the target protein sequence",
            "required": false,
            "type": "integer",
            "maximum": 100.0,
            "minimum": 0.0,
            "format": "int32"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/ProteinFeatureInfo"
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