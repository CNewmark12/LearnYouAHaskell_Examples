from operator import contains
import os

directory_in_str = os.getcwd()
start = False
fileToWrite = os.path.join(directory_in_str,"HaskellExamples.html")
f = open(fileToWrite,"w",encoding='utf-8')

# Top of the file
f.write('''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Haskell Examples</title>
</head>

<script src="https://cdn.tailwindcss.com"></script>

<style>

.block {
   margin: 20px;
   padding: 8px;
   background-color:grey;
   transition: 0.5s;
}

.block:hover {
        margin: -2px;
        transition: 0.5s;
    }

.navbar {
        overflow: hidden;
        background-color: #333;
        position: fixed;
        /* Set the navbar to fixed position */
        top: 0;
        /* Position the navbar at the top of the page */
        width: 100%;
        /* Full width */
    }
    /* Links inside the navbar */
    
    .navbar a {
        float: left;
        display: block;
        color: #f2f2f2;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
    }
    /* Change background on mouse-over */
    
    .navbar a:hover {
        background: #ddd;
        color: black;
    }
    
</style>

<body>\n''')

#Make Nav bar
f.write('''
        <div class="navbar">
            <ul class="navigation">
        ''')


for file in os.listdir(directory_in_str):
    if file.endswith(".md") and file != "HaskellExamples.md":
        f.write(f''' 
                <li class="nav-item">
                    <a href="#{file[:len(file)-3]}">{file[:len(file)-3]}</a>
                </li>
                ''')
        

f.write('''</ul>
        </div>\n\n''')

#End Nav Bar   

#Render Examples
for file in os.listdir(directory_in_str):
    if file.endswith(".md") and file != "HaskellExamples.md":
        # print("\n\n")
        # print(file)
        f.write("\n\n")
        f.write("<h1 id=\""+file[:len(file)-3]+"\"class=\"text-center font-bold text-4xl my-40\">"+file[:len(file)-3]+ "</h1>\n") #section title
        f.write("  <div class=\"flex flex-row flex-wrap\">\n") #opening div for section
        
        filename = os.path.join(directory_in_str,file)
        with open(filename,"r",encoding='utf-8') as file:
            lines = file.readlines()
        for line in lines:
            if "~~~~" in line:
                if not start:
                    f.write('<div class=\"block rounded border-solid shadow-xl\"> \n\t<pre>\n\t\t<code style =\"color:black\">\n') #first line of block
                if start:
                    #f.write(line)
                    f.write("\t\t </code>\n \t</pre> \n</div>\n\n") #last line of block
                start = not start
                continue #don't write the first line with tildes
            if start:
                #print(line)
                f.write(line)
                
        f.write("</div>") #closing div
                
f.write("</body>\n </html>") #end of document
f.close()