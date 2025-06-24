{
  "server_url": "",
  "paths": {
    "/uniparc/proteome/{upid}": {
      "get": {
        "tags": [
          "uniparc"
        ],
        "summary": "Get UniParc entries by Proteome UPID",
        "description": "",
        "operationId": "getByProteomeId",
        "produces": [
          "application/json",
          "application/xml",
          "text/x-fasta"
        ],
        "parameters": [
          {
            "name": "upid",
            "in": "path",
            "description": "UniProt Proteome UPID",
            "required": true,
            "type": "string"
          },
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
            "name": "rfDdtype",
            "in": "query",
            "description": "Response filter by Cross reference database type, e.g EMBL, RefSeq, Ensembl, etc. Comma separated values accepted.",
            "required": false,
            "type": "string"
          },
          {
            "name": "rfDbid",
            "in": "query",
            "description": "Response filter by all UniParc cross reference accessions, eg. AAC02967 (EMBL) or  XP_006524055 (RefSeq). Comma separated values accepted.",
            "required": false,
            "type": "string"
          },
          {
            "name": "rfActive",
            "in": "query",
            "description": "Response filter by Active(true) or not Active(false) Cross reference.",
            "required": false,
            "type": "string"
          },
          {
            "name": "rfTaxId",
            "in": "query",
            "description": "Response filter by organism taxon ID. Comma separated values accepted.",
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