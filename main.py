from pyscript import document, display

def average(event):
    #getting the value of each element from index.html
    name = document.getElementById("name").value
    Science = float(document.getElementById("sci").value)
    English = float(document.getElementById("english").value)
    Math = float(document.getElementById("math").value)
    Filipino = float(document.getElementById("fil").value)
    ICT = float(document.getElementById("ict").value)
    PE = float(document.getElementById("pe").value)
    subject = ["Science", "English", "Math", "Filipino", "ICT", "PE"] #list
    units = (5, 3, 2, 1)

#calculate for the general weighted average with subjects and units
    average = (Science * 5 + Math * 5 + English * 5 + Filipino * 3 + ICT * 2 + PE * 1)
    total_units = 21
    gen_ave = average / total_units

#get the summary using a list, offset and f-string
    summary = f"""
    Name: {name}
    {subject[0]}: {Science:.2f}
    {subject[1]}: {English:.2f}
    {subject[2]}: {Math:.2f}
    {subject[3]}: {Filipino:.2f}
    {subject[4]}: {ICT:.2f}
    {subject[5]}: {PE:.2f}
    Your General Weighted Average is: {gen_ave:.2f}
    """

#This shows the result from the summary to display in the output
    document.getElementById("summary").innerText = summary
