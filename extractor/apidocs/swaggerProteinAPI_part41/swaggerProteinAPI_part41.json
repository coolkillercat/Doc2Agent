{
  "server_url": "",
  "paths": {
    "/variation": {
      "get": {
        "tags": [
          "variation"
        ],
        "summary": "Search natural variants in UniProt",
        "description": "Among the available response content types, PEFF format (PSI Extended FASTA Format from the Human Proteome Organisation - Proteomics Standards Initiative, HUPO-PSI) is provided with only variants reported in the output.",
        "operationId": "search",
        "produces": [
          "application/json",
          "application/xml",
          "text/x-gff",
          "text/x-peff"
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
          },
          {
            "name": "accession",
            "in": "query",
            "description": "UniProt accession(s). Comma separated values accepted up to 100.",
            "required": false,
            "type": "string"
          },
          {
            "name": "disease",
            "in": "query",
            "description": "Search by disease name/ acronym for associated variants , e.g. alzheimer disease 1 or AD1. Partial names allowed.",
            "required": false,
            "type": "string",
            "maxItems": 60,
            "minItems": 2
          },
          {
            "name": "omim",
            "in": "query",
            "description": "Search by MIM ID, e.g. 104300. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string"
          },
          {
            "name": "evidence",
            "in": "query",
            "description": "Search by PubMed ID, e.g. 22472873. Comma separated values accepted up to 20.",
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
            "name": "dbtype",
            "in": "query",
            "description": "Cross reference database type, e.g, dbSNP, cosmic curate or ClinVar. Comma separated values accepted up to 2.",
            "required": false,
            "type": "string"
          },
          {
            "name": "dbid",
            "in": "query",
            "description": "Cross-reference database ID, e.g. rs121918508 for dbSNP, COSM29836 for cosmic curated, rcv61200 for ClinVar. Comma separated values accepted up to 20.",
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