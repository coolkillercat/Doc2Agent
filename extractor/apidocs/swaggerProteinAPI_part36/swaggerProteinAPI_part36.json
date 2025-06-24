{
  "server_url": "",
  "paths": {
    "/uniparc/bestguess": {
      "get": {
        "tags": [
          "uniparc"
        ],
        "summary": "Get UniParc longest sequence for entries.",
        "description": "For a given user input (request parameters), Best Guess returns the UniParcEntry with a cross-reference to the longest active UniProtKB sequence (preferably from Swiss-Prot and if not then TrEMBL). It also returns the sequence and related information. If it finds more than one longest active UniProtKB sequence it returns 400 (Bad Request) error response with the list of cross references found.",
        "operationId": "getUniParcBestGuest",
        "produces": [
          "application/json",
          "application/xml",
          "text/x-fasta"
        ],
        "parameters": [
          {
            "name": "upi",
            "in": "query",
            "description": "UniParc ID (UPI). Comma separated values accepted up to 100",
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
            "name": "taxid",
            "in": "query",
            "description": "Organism taxon ID. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/Entry"
            }
          },
          "400": {
            "description": "Invalid request Parameter.",
            "schema": {
              "$ref": "#/definitions/ErrorMessage"
            }
          },
          "404": {
            "description": "Could not find best guess for the requested filter",
            "schema": {
              "$ref": "#/definitions/ErrorMessage"
            }
          }
        }
      }
    }
  }
}