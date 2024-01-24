# Imagine you have a 20 GB file with one string per line. Explain how you would sort this file.

# Ideas: External Sorting
# - 20GB -> Don't want to bring all of them into memory.
# - Suppose we have X available memory space
#   => We sort each chunk separately and save them back into the file system
# - Once all chunks are sorted, we merge the chunks, one by one. => Fully sorted file