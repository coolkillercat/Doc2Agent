{
  "server_url": "",
  "paths": {
    "/features/{accession}": {
      "get": {
        "tags": [
          "features"
        ],
        "summary": "Get UniProt protein sequence features by accession ",
        "description": "",
        "operationId": "getByAccession",
        "produces": [
          "application/json",
          "application/xml",
          "text/x-gff"
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
            "name": "categories",
            "in": "query",
            "description": "Category type(s): MOLECULE_PROCESSING, TOPOLOGY, SEQUENCE_INFORMATION, STRUCTURAL, DOMAINS_AND_SITES, PTM, VARIANTS, MUTAGENESIS. Comma separated values accepted up to 20",
            "required": false,
            "type": "array",
            "items": {
              "type": "string"
            },
            "collectionFormat": "multi"
          },
          {
            "name": "types",
            "in": "query",
            "description": "Feature type(s): INIT_MET, SIGNAL, PROPEP, TRANSIT, CHAIN, PEPTIDE, TOPO_DOM, TRANSMEM, DOMAIN, REPEAT, ZN_FING, DNA_BIND, REGION, COILED, MOTIF, COMPBIAS, ACT_SITE, BINDING, SITE, NON_STD, MOD_RES, LIPID, CARBOHYD, DISULFID, CROSSLNK, VAR_SEQ, VARIANT, MUTAGEN, UNSURE, CONFLICT, NON_CONS, NON_TER, HELIX, TURN, STRAND, INTRAMEM. Comma separated values accepted up to 20",
            "required": false,
            "type": "array",
            "items": {
              "type": "string"
            },
            "collectionFormat": "multi"
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