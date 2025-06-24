{
  "server_url": "",
  "paths": {
    "/uniparc/sequence": {
      "post": {
        "tags": [
          "uniparc"
        ],
        "summary": "Get UniParc entries by sequence",
        "description": "",
        "operationId": "getBySequence",
        "consumes": [
          "text/plain",
          "application/json",
          "application/xml"
        ],
        "produces": [
          "application/json",
          "application/xml",
          "text/x-fasta"
        ],
        "parameters": [
          {
            "in": "body",
            "name": "body",
            "description": "Post uniparc Sequence in text, json or xml content type. Look the expected model in Data Type column",
            "required": true,
            "schema": {
              "$ref": "#/definitions/UniparcSequenceParam"
            },
            "x-examples": {
              "text/plain": "MLMPKRTKYR"
            }
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