
contents = ["All carrots are sliced", "All carrots are not sliced", "No carrots are sliced"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filenames in zip(contents, filenames):
    file = open(f"../files/{filenames}", "w")
    file.write(content)

