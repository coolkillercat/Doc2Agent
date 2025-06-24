{
  "server_url": "",
  "paths": {
    "/proteomics-ptm": {
      "get": {
        "tags": [
          "proteomics-ptm"
        ],
        "summary": "Search proteomics peptide ptm in UniProt",
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
            "name": "taxid",
            "in": "query",
            "description": "Organism taxon ID. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string"
          },
          {
            "name": "upid",
            "in": "query",
            "description": "UniProt proteome UPID(s). Comma separated values accepted up to 100.",
            "required": false,
            "type": "string"
          },
          {
            "name": "datasource",
            "in": "query",
            "description": "Proteomics data source(s): PRIDE, PTMExchange. Comma separated values accepted up to 2.",
            "required": false,
            "type": "string",
            "maxItems": 2147483647,
            "minItems": 3
          },
          {
            "name": "peptide",
            "in": "query",
            "description": "Peptide sequence. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string",
            "maxItems": 2147483647,
            "minItems": 4
          },
          {
            "name": "unique",
            "in": "query",
            "description": "Peptide uniqueness (unique peptides map to one gene group only). Values can be true or false.",
            "required": false,
            "type": "string"
          },
          {
            "name": "ptm",
            "in": "query",
            "description": "Ptm name",
            "required": false,
            "type": "string"
          },
          {
            "name": "confidence_score",
            "in": "query",
            "description": "PTM Confidence score(s): Bronze, Silver, Gold",
            "required": false,
            "type": "array",
            "items": {
              "type": "string"
            },
            "collectionFormat": "multi"
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