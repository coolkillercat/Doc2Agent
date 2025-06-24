{
  "server_url": "",
  "paths": {
    "/variation/dbsnp/{dbid}": {
      "get": {
        "tags": [
          "variation"
        ],
        "summary": "Get natural variants in UniProt by NIH-NCBI SNP database identifier",
        "description": "Among the available response content types, PEFF format (PSI Extended FASTA Format from the Human Proteome Organisation - Proteomics Standards Initiative, HUPO-PSI) is provided with only variants reported in the output.",
        "operationId": "searchByDbSNP",
        "produces": [
          "application/json",
          "application/xml",
          "text/x-gff",
          "text/x-peff"
        ],
        "parameters": [
          {
            "name": "dbid",
            "in": "path",
            "description": "Cross-reference NIH-NCBI SNP database identifier, e.g. rs121918508",
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
            "name": "sourcetype",
            "in": "query",
            "description": "Filter by the sourceType for variants: uniprot, large scale study, mixed, clinvar, nci-tcga, cosmic curated, ensembl, gnomad, topmed and exac. Comma separated values accepted up to 2.",
            "required": false,
            "type": "string"
          },
          {
            "name": "consequencetype",
            "in": "query",
            "description": "Filter by consequenceType for variants: missense, stop gained or stop lost. Comma separated values accepted up to 2.",
            "required": false,
            "type": "string"
          },
          {
            "name": "wildtype",
            "in": "query",
            "description": "Search by specific wildType amino acid. Options: Any single letter amino acid and * for stop codon. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string"
          },
          {
            "name": "alternativesequence",
            "in": "query",
            "description": "Filter by the alternativeSequence amino acid. Any single letter amino acid and * for stopcodon and - for deletions. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string"
          },
          {
            "name": "location",
            "in": "query",
            "description": "Filter by the amino acid range position in the sequence(s). Any valid amino acid range position within the length of the protein sequence such as 10-60 (start position to end position)",
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