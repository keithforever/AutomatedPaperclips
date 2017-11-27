from splinter import Browser
#try:
browser = Browser('firefox')
browser.visit('http://www.decisionproblem.com/paperclips/index2.html')
btnMakePaperclip = browser.find_by_id('btnMakePaperclip').click()
spanWire = browser.find_by_id('wire')
clip = True
autoclippers = 0
readout1Main = browser.find_by_id('readout1').value

while (spanWire>0):
  if (clip):
    btnMakePaperclip = browser.find_by_id('btnMakePaperclip').click()

  spanWire = browser.find_by_id('wire').value
  clipDemand = browser.find_by_id('demand').value
  wireCost = browser.find_by_id('wireCost').value
  funds = browser.find_by_id('funds').value
  clipperCost = browser.find_by_id('clipperCost').value
  clipmakerLevel2 = browser.find_by_id('clipmakerLevel2').value
  spanWire = spanWire.replace(',', '')

  if (float(funds) > float(wireCost)):
    btnBuyWire = browser.find_by_id('btnBuyWire').click()
    print "Bought Wire"
    funds = browser.find_by_id('funds').value

  if(browser.find_by_id('btnMakeClipper').visible and float(funds) > float(clipperCost) and float(spanWire) > 700):
    btnMakeClipper = browser.find_by_id('btnMakeClipper').click()
    print "Purchased Autoclipper"
    autoclippers += 1

  if(autoclippers > 5):
    clip = False

  trust = browser.find_by_id('trust').value
  processors = browser.find_by_id('processors').value
  memory = browser.find_by_id('memory').value
  if(float(memory) + float(processors) < trust):
    if( float(processors)/float(memory) < (1/2) ):
      btnAddProc = browser.find_by_id('btnAddProc').click()
      print "Bought Processor"
    if( float(processors)/float(memory) > (1/2) ):
      btnAddMem = browser.find_by_id('btnAddMem').click()
      print "Bought Memory"

  if(float(clipDemand) < 100):
    btnLowerPrice = browser.find_by_id('btnLowerPrice').click()
    clipDemand = browser.find_by_id('demand').value
    print "Price Lowered"
    print "Demand = " + clipDemand

  projectButton = browser.find_by_css('projectButton').value
  if( projectButton is visible )

  readout1 = browser.find_by_id('readout1').value
  while(readout1 != readout1Main):
    print(readout1)
    readout1Main = readout1

def maxPPC( clipDemand ):
  margin = browser.find_by_id('margin').value
  unsoldClips = browser.find_by_id('unsoldClips').value
  avgRev = browser.find_by_id('avgRev').value


#except Exception as e: #all
#  browser.quit()
#  print e.__doc__
#  print e.message


