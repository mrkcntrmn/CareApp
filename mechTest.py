import mechanize
br = mechanize.Browser()
br.open("https://www.dfps.state.tx.us/Child_Care/Search_Texas_Child_Care/CCLNET/Source/Provider/ppComplianceHistory.aspx?fid=773628&tab=2")
for f in br.forms():
    print f