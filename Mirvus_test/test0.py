from pymilvus import MilvusClient, DataType

def operate_db():
  client = MilvusClient(uri='milvus_demo.db')
  return client


client = operate_db()


# 2 collection集合的操作
def operate_table():
    schema = client.create_schema(auto_id=False, enable_dynamic_field=True)
    schema.add_field(field_name='id', datatype=DataType.INT64, is_primary=True)
    schema.add_field(field_name='vector', datatype=DataType.FLOAT_VECTOR, dim=5)
    client.create_collection(collection_name='demo_v1', schema=schema)

    # 为向量字段创建索引
    index_params = client.prepare_index_params()
    index_params.add_index(field_name='vector', metric_type="COSINE")
    client.create_index(collection_name='demo_v1', index_params=index_params)




operate_table()

print(f"✅ 集合列表: {client.list_collections()}")

# mark:  5.3 Entity实体数据操作