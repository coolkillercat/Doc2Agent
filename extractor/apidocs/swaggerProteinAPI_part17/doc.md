{
  "server_url": "",
  "paths": {
    "/genecentric": {
      "get": {
        "tags": [
          "genecentric"
        ],
        "summary": "Search gene centric proteins",
        "description": "",
        "operationId": "getGeneCentricByUpid",
        "produces": [
          "application/json",
          "application/xml"
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
            "name": "upid",
            "in": "query",
            "description": "UniProt proteome UPID(s). Comma separated values accepted up to 100.",
            "required": false,
            "type": "string"
          },
          {
            "name": "accession",
            "in": "query",
            "description": "UniProt accession(s). Comma separated values accepted up to 100.",
            "required": false,
            "type": "string"
          },
          {
            "name": "gene",
            "in": "query",
            "description": "It is a unique gene identifier found in MOD, Ensembl, Ensembl Genomes, OLN ,ORF or UniProt Gene Name database. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/CanonicalGene"
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