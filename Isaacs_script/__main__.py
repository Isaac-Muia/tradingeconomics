import tradingeconomics as te
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 2:
    print("Error: Usage is __main__.py 'country1' 'country2' ... 'countryn' 'indicator' ")
    exit(1)

te.login('guest:guest')

indicator = sys.argv[len(sys.argv) - 1]
x = []
y = []
countrys = ""

i = 1
while(i < len(sys.argv) - 1):
    country = sys.argv[i]
    countrys = country + " " + countrys
    print("\n" + country)
    print("date" + "       " + indicator)

    #Get country's indicator data
    data = te.getHistoricalData(country=country, indicator=indicator)

    xtmp = []
    ytmp = []
    #Put countrys data in x and y axis lists
    for line in data:
        xtmp.append(str(line["DateTime"]).split('T')[0])
        ytmp.append(round(line["Value"]))
        print(str(line["DateTime"]).split('T')[0] + " "  + str(line["Value"]))
    x.append(xtmp)
    y.append(ytmp)
    i += 1

#Plot data
a = 0
while(a < len(x)):
    plt.plot(list(reversed(x[a])),list(reversed(y[a])), label = sys.argv[a + 1])
    a += 1

plt.xlabel("Date")
plt.ylabel(indicator)

plt.title(indicator + " for " + countrys)
plt.legend()
plt.show()