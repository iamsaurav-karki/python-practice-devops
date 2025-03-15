
# list 
name = ["saurav", "rahul", "ravi", "ankit"]
name.append("sushil")
name.remove("rahul")
print(name)

# tuple
name = ("saurav", "rahul", "ravi", "ankit")
print(name)

# dictionary
name = {
    "name": "saurav",
    "age": 25,
    "city": "kathmandu"
}
print(name)

# list of s3 buckets
s3_buckets_list = ["bucket1", "bucket2", "bucket3"]
print(s3_buckets_list)
print(len(s3_buckets_list))
s3_buckets_list.append("bucket4")
print(len(s3_buckets_list))

print(s3_buckets_list[0:2])
print(s3_buckets_list[1:3])

# concatenation
print(s3_buckets_list[0] + " " + s3_buckets_list[1])


number = [1, 21, 3, 4, 5]
number.sort()
print(number)


# list can have different data types
random = [1, 2, 3, 4, 5, "hari" , "sita", "gita", 3.4, 4.5]
print(random)