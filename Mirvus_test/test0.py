from pymilvus import MilvusClient

def operate_db():
  clinet = MilvusClient(uri='milvus_demo.db')
  return clinet


operate_db()