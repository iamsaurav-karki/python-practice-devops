# for loops

s3_buckets_list = ["bucket1", "bucket2", "bucket3"]
for bucket in s3_buckets_list:
  print(bucket)

# while loops
bucket = 0
while bucket < len(s3_buckets_list):
  print(s3_buckets_list[bucket])
  bucket += 1


# print numbers
for i in range(10):
  print(i)