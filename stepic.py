good = {"foo" : "good", "bar": "good1"}
bad = {"foo": "bad", "bar": "bad1"}
PR = good
print(PR["foo"], PR["bar"])  # good good1
PR = bad
print(PR["foo"], PR["bar"])  # bad bad1