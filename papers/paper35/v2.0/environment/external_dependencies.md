# External Dependencies

The bundle validation path uses Python standard library only.

Runtime network dependency:

- `scripts/07_desi_confrontation.py` fetches two public DESI DR2 BAO files from
  the CobayaSampler `bao_data` repository, checks SHA256, and does not
  redistribute those files.

No Planck likelihoods, JWST data products, LZ/XENONnT/PandaX tables, or DESI
data products are bundled.

See `data/external_data_sources.md` for source URLs, non-redistribution
discipline, and checksums.
