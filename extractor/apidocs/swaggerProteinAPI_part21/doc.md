{
  "server_url": "",
  "paths": {
    "/proteins": {
      "get": {
        "tags": [
          "proteins"
        ],
        "summary": "Search UniProt entries",
        "description": "",
        "operationId": "search",
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
            "name": "accession",
            "in": "query",
            "description": "UniProt accession(s). Comma separated values accepted up to 100.",
            "required": false,
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
            "description": "0 for excluding isoform, 1 for isoform only and 2 for both canonical and isoform",
            "required": false,
            "type": "integer",
            "format": "int32"
          },
          {
            "name": "goterms",
            "in": "query",
            "description": "GO ontology terms",
            "required": false,
            "type": "string",
            "maxItems": 50,
            "minItems": 3
          },
          {
            "name": "keywords",
            "in": "query",
            "description": "UniProt keywords",
            "required": false,
            "type": "string",
            "maxItems": 50,
            "minItems": 3
          },
          {
            "name": "ec",
            "in": "query",
            "description": "UniProt EC number. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string"
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
            "name": "exact_gene",
            "in": "query",
            "description": "UniProt exact gene name. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string",
            "maxItems": 50,
            "minItems": 3
          },
          {
            "name": "protein",
            "in": "query",
            "description": "UniProt protein name",
            "required": false,
            "type": "string",
            "maxItems": 100,
            "minItems": 3
          },
          {
            "name": "organism",
            "in": "query",
            "description": "Organism name",
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
            "name": "pubmed",
            "in": "query",
            "description": "UniProt reference PubMed ID. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string"
          },
          {
            "name": "seqLength",
            "in": "query",
            "description": "Sequence length. Sequence length can be a single length value such as 123 or range 123-234",
            "required": false,
            "type": "string"
          },
          {
            "name": "md5",
            "in": "query",
            "description": "Sequence md5 value.",
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