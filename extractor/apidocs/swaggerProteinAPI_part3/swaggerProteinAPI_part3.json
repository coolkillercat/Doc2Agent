{
  "server_url": "",
  "paths": {
    "/coordinates": {
      "get": {
        "tags": [
          "coordinates"
        ],
        "summary": "Search genomic coordinates for UniProt entries",
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
            "name": "chromosome",
            "in": "query",
            "description": "Chromosome name, i.e. 1, 2, X, etc. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string",
            "maxItems": 50,
            "minItems": 1
          },
          {
            "name": "ensembl",
            "in": "query",
            "description": "Ensembl gene ID, transcript ID or translation ID. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string",
            "maxItems": 100,
            "minItems": 6
          },
          {
            "name": "gene",
            "in": "query",
            "description": "UniProt gene name. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string",
            "maxItems": 50,
            "minItems": 2
          },
          {
            "name": "protein",
            "in": "query",
            "description": "UniProt protein name",
            "required": false,
            "type": "string",
            "maxItems": 50,
            "minItems": 3
          },
          {
            "name": "taxid",
            "in": "query",
            "description": "Organism taxon ID. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string"
          },
          {
            "name": "location",
            "in": "query",
            "description": "Genome location range such as 58205437-58219305 (genome start to genome end)",
            "required": false,
            "type": "string"
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