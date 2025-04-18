def list_to_string():
  username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]
  sum_variable = ""
  for i in username_list:
    sum_variable = sum_variable + i + ", "
  print(sum_variable)

list_to_string()