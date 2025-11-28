# 复杂查询  

from pymilvus import MilvusClient, DataType, AnnSearchRequest, RRFRanker
import random


def operate_db():
  client = MilvusClient(uri='milvus_demo.db')
  return client

client = operate_db()

print(f"--✅ 集合列表--: {client.list_collections()}")


def complex_query():
  schema = client.create_schema(enable_dynamic_field=False)
  schema.add_field(field_name='film_id', datatype=DataType.INT64, is_primary=True)
  schema.add_field(field_name='filmVector', datatype=DataType.FLOAT_VECTOR, dim=5) # 向量字段
  schema.add_field(field_name="posterVector", datatype=DataType.FLOAT_VECTOR, dim=5) # 向量字段
  # #
  # 定义索引
  index_params = client.prepare_index_params()
  index_params.add_index(field_name='filmVector', index_type="IVF_FLAT",
                          metric_type="L2", params={"nlist": 128})
  index_params.add_index(field_name='posterVector', index_type="",
                          metric_type="COSINE")

  # 创建集合
  client.create_collection(collection_name='demo_v3', schema=schema, index_params=index_params)

  # 向量库中插入实体
  entities = []
  for  _ in range(1000):
      # 构造实体
      film_id = random.randint(1, 10000)
      film_vector = [random.random() for _ in range(5)]
      poster_vector = [random.random() for _ in range(5)]
      entity = {"film_id": film_id, "filmVector": film_vector, "posterVector": poster_vector}
      entities.append(entity)

  client.insert(collection_name='demo_v3', data=entities)






  # 多向量查询（注意和批量向量查询不同）
  # 多向量搜索使用 hybrid_search() API 在一次调用中执行多个 ANN 搜索请求。每个 AnnSearchRequest 代表特定矢量场上的单个搜索请求。
  # 示例创建两个 AnnSearchRequest 实例以对两个向量字段执行单独的相似性搜索。
  # 创建多搜索请求 filmVector
  query_filmVector = [[0.8896863042430693, 0.370613100114602, 0.23779315077113428, 0.38227915951132996, 0.5997064603128835]]
  dense_search_params = {"data": query_filmVector,
                          "anns_field": "filmVector",# 该参数值必须与集合模式中使用的值相同。
                          "param": {"metric_type": "L2", "nprobe": 10},# nprobe代表访问簇的数量
                          "limit": 2}
  request_1 = AnnSearchRequest(**dense_search_params)

  # 创建多搜索请求 posterVector
  query_posterVector = [[0.02550758562349764, 0.006085637357292062, 0.5325251250159071, 0.7676432650114147, 0.5521074424751443]]
  sparse_search_params = {"data": query_posterVector,
                          "anns_field": "posterVector",
                          # 该参数值必须与集合模式中使用的值相同。
                          "param": {"metric_type": "COSINE"},
                          "limit": 2
                          }
  request_2 = AnnSearchRequest(**sparse_search_params)

  reqs = [request_1, request_2]
  ranker = RRFRanker(100)

  res = client.hybrid_search(
      collection_name="demo_v3",
      reqs=reqs,
      ranker=ranker,
      limit=2
  )
  for hits in res:
      print("TopK results:")
      for hit in hits:
          print(hit)


complex_query()