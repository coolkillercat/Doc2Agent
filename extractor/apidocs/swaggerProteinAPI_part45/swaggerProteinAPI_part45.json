{
  "server_url": "",
  "paths": {
    "/variation/{accession}": {
      "get": {
        "tags": [
          "variation"
        ],
        "summary": "Get natural variants by UniProt accession",
        "description": "Among the available response content types, PEFF format (PSI Extended FASTA Format from the Human Proteome Organisation - Proteomics Standards Initiative, HUPO-PSI) is provided with only variants reported in the output.",
        "operationId": "getVariation",
        "produces": [
          "application/json",
          "application/xml",
          "text/x-gff",
          "text/x-peff"
        ],
        "parameters": [
          {
            "name": "accession",
            "in": "path",
            "description": "UniProt accession",
            "required": true,
            "type": "string"
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
              "$ref": "#/definitions/ProteinFeatureInfo"
            }
          },
          "400": {
            "description": "Invalid accession parameter. The values's format should be a valid UniProtKB accession.",
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