{
  "server_url": "",
  "paths": {
    "/uniparc/upi/{upi}": {
      "get": {
        "tags": [
          "uniparc"
        ],
        "summary": "Get UniParc entry by UniParc UPI",
        "description": "",
        "operationId": "getUniParcEntryByUpId",
        "produces": [
          "application/json",
          "application/xml",
          "text/x-fasta"
        ],
        "parameters": [
          {
            "name": "upi",
            "in": "path",
            "description": "UniParc ID (UPI)",
            "required": true,
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
              "$ref": "#/definitions/Entry"
            }
          },
          "400": {
            "description": "Invalid upid parameter. The value format should match the regular expression UPI[\\w]{10}.",
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