from .pinecone import PineconeTarget
from .qdrant import QdrantTarget
from .weaviate import WeaviateTarget
from .singlestore import SingleStoreTarget
from .supabase import SupabaseTarget
from .lancedb import LanceDBTarget

def get_target_database(config):
    target_type = config['target_database']
    if target_type == 'Pinecone':
        return PineconeTarget(config)
    elif target_type == 'Qdrant':
        return QdrantTarget(config)
    elif target_type == 'Weaviate':
        return WeaviateTarget(config)
    elif target_type == 'Single Store':
        return SingleStoreTarget(config)
    elif target_type == 'Supabase':
        return SupabaseTarget(config)
    elif target_type == 'LanceDB':
        return LanceDBTarget(config)
    else:
        raise ValueError(f"Unsupported target database: {target_type}")
