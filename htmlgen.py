html_markup = """
<!DOCTYPE html>
<html>
<head>
    <title>HTML test</title>
</head>
<body>
    <h1>Hello there!</h1>
</body>
</html>
"""
# file path of the HTML file, the file can go in any directory
file_path = "test.html"
# writes HTML text to a file
with open(file_path, "w") as html_file:
    html_file.write(html_markup)
    
print(f"HTML file '{file_path}' has been successfully created.")
input("Press any key to exit this program.")
