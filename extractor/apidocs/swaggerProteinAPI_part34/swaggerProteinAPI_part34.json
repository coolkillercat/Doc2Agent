{
  "server_url": "",
  "paths": {
    "/uniparc": {
      "get": {
        "tags": [
          "uniparc"
        ],
        "summary": "Search UniParc entries",
        "description": "",
        "operationId": "searchUniParc",
        "produces": [
          "application/json",
          "application/xml",
          "text/x-fasta"
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
            "name": "upi",
            "in": "query",
            "description": "UniParc ID (UPI). Comma separated values accepted up to 100",
            "required": false,
            "type": "string"
          },
          {
            "name": "dbtype",
            "in": "query",
            "description": "Search by Cross reference database type, e.g EMBL, RefSeq, Ensembl, etc.",
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
            "name": "dbid",
            "in": "query",
            "description": "All UniParc cross reference accessions, eg. AAC02967 (EMBL) or  XP_006524055 (RefSeq). Comma separated values accepted up to 100.",
            "required": false,
            "type": "string"
          },
          {
            "name": "gene",
            "in": "query",
            "description": "UniProt gene name. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string"
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
            "name": "organism",
            "in": "query",
            "description": "Organism name",
            "required": false,
            "type": "string",
            "maxItems": 50,
            "minItems": 3
          },
          {
            "name": "sequencechecksum",
            "in": "query",
            "description": "Sequence CRC64 checksum. eg 4104A3A57D1B08E3",
            "required": false,
            "type": "string"
          },
          {
            "name": "ipr",
            "in": "query",
            "description": "Search by InterPro identifier(s). Comma separated values accepted up to 20.",
            "required": false,
            "type": "string"
          },
          {
            "name": "signaturetype",
            "in": "query",
            "description": "Search by signature database type, e.g. SMART, SUPFAM, Pfam, PIRSF, PROSITE, etc. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string"
          },
          {
            "name": "signatureid",
            "in": "query",
            "description": "Search by signature database id, e.g. SM00044, SSF55073, PF00211, PIRSF039050, PS00452, etc. Comma separated values accepted up to 20.",
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
            "name": "seqLength",
            "in": "query",
            "description": "Sequence length. Sequence length can be a single length value such as 123 or range 123-234",
            "required": false,
            "type": "string"
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
          }
        }
      }
    }
  }
}