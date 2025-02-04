from singer.catalog import Catalog, CatalogEntry, Schema
from tap_twitter_ads.schema import get_schemas


def discover(reports=[], stream=None):
    schemas, field_metadata = get_schemas(reports)
    catalog = Catalog([])

    for stream_name, schema_dict in schemas.items():
        schema = Schema.from_dict(schema_dict)
        mdata = field_metadata[stream_name]

        table_metadata = {}
        for entry in mdata:
            if entry.get('breadcrumb') == ():
                table_metadata = entry.get('metadata', {})
        key_properties = table_metadata.get('table-key-properties')

        if not stream or stream == stream_name:
            catalog.streams.append(CatalogEntry(
                stream=stream_name,
                tap_stream_id=stream_name,
                key_properties=key_properties,
                schema=schema,
                metadata=mdata
            ))
    return catalog
