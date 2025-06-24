{
  "server_url": "",
  "paths": {
    "/proteomes": {
      "get": {
        "tags": [
          "proteomes"
        ],
        "summary": "Search proteomes in UniProt",
        "description": "",
        "operationId": "search",
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
            "name": "name",
            "in": "query",
            "description": "Search proteome name",
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
            "name": "keyword",
            "in": "query",
            "description": "Terms the proteome contains",
            "required": false,
            "type": "string",
            "maxItems": 50,
            "minItems": 3
          },
          {
            "name": "xref",
            "in": "query",
            "description": "Proteome cross references such as Genome assembly ID or Biosample ID. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string",
            "maxItems": 50,
            "minItems": 3
          },
          {
            "name": "genome_acc",
            "in": "query",
            "description": "Genome accession. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string",
            "maxItems": 50,
            "minItems": 3
          },
          {
            "name": "is_ref_proteome",
            "in": "query",
            "description": "Reference Proteome(true) or not reference proteome (false)",
            "required": false,
            "type": "string"
          },
          {
            "name": "is_redundant",
            "in": "query",
            "description": "Redundant Proteome(true) or non redundant proteome (false)",
            "required": false,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/Proteome"
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