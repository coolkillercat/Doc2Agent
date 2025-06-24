{
  "server_url": "",
  "paths": {
    "/features": {
      "get": {
        "tags": [
          "features"
        ],
        "summary": "Search protein sequence features in UniProt",
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
            "name": "reviewed",
            "in": "query",
            "description": "The reviewed parameter can only be true or false",
            "required": false,
            "type": "string"
          },
          {
            "name": "gene",
            "in": "query",
            "description": "UniProt gene name. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string",
            "maxItems": 100,
            "minItems": 3
          },
          {
            "name": "exact_gene",
            "in": "query",
            "description": "UniProt exact gene name. Comma separated values accepted up to 20.",
            "required": false,
            "type": "string",
            "maxItems": 100,
            "minItems": 3
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
            "name": "categories",
            "in": "query",
            "description": "Category type(s): MOLECULE_PROCESSING, TOPOLOGY, SEQUENCE_INFORMATION, STRUCTURAL, DOMAINS_AND_SITES, PTM, VARIANTS, MUTAGENESIS. Comma separated values accepted up to 20",
            "required": false,
            "type": "string"
          },
          {
            "name": "types",
            "in": "query",
            "description": "Feature type(s): INIT_MET, SIGNAL, PROPEP, TRANSIT, CHAIN, PEPTIDE, TOPO_DOM, TRANSMEM, DOMAIN, REPEAT, ZN_FING, DNA_BIND, REGION, COILED, MOTIF, COMPBIAS, ACT_SITE, BINDING, SITE, NON_STD, MOD_RES, LIPID, CARBOHYD, DISULFID, CROSSLNK, VAR_SEQ, VARIANT, MUTAGEN, UNSURE, CONFLICT, NON_CONS, NON_TER, HELIX, TURN, STRAND, INTRAMEM. Comma separated values accepted up to 20",
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