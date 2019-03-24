import json
import matplotlib.pyplot as plt
import pandas as pd
plt.rcdefaults()

json_file = open("SBHSData.json").read()
data = json.loads(json_file)

# prints specific part
# print(data[0]['area'])

# writes to txt
#file = open("C:/Users/Abhinav/Downloads/json/SBHSData.txt", "w")
#json.dump(data, file, indent=2)

# fills up lists
listArea = []
listVersion = []
listUptime = []
listHostname = []

for item in data:
    area = item['area']
    try:
        version = item['version']
    except:
        version = ''
    try:
        uptime = item['uptime']
    except:
        uptime = ''
    hostname = item['hostname']
    listArea.insert(len(listArea), area)
    listVersion.insert(len(listVersion), version)
    listUptime.insert(len(listUptime), uptime)
    listHostname.insert(len(listHostname), hostname)

# pandas
df = pd.read_json(json_file)
# print(df.head())
# print(df.describe())
# print(df["area"].describe())


def infoHostname(str):
    area = df[df["hostname"] == str].describe().loc['top', 'area']
    uptime = df[df["hostname"] == str].describe().loc['top', 'uptime']
    version = df[df["hostname"] == str].describe().loc['top', 'version']
    try:
        return "Area: " + area + "\nUptime: " + uptime + "\nVersion: " + version
    except:
        return "No Area\nNo Uptime\nNo Version"


def infoArea1(str):
    return listArea.count(str)


def infoArea2(str):
    return df[df["area"] == str].describe().loc['top', 'version']


def infoVersion1(str):
    return listVersion.count(str)


def infoVersion2(str):
    return df[df["version"] == str].describe().loc['top', 'area']


def infoIndexArea(int):
    return listArea[int - 1]


def infoIndexVersion(int):
    return listVersion[int - 1]


def infoIndexUptime(int):
    return listUptime[int - 1]


def infoIndexHostname(int):
    return listHostname[int - 1]


def pie():
    setArea = set(listArea)

    bcloud = listArea.count('bcloud')
    blank = listArea.count('')
    tdmz = listArea.count('tdmz')
    admin = listArea.count('admin')
    dev = listArea.count('dev')
    one = listArea.count('1')
    prod = listArea.count('prod')
    apex = listArea.count('apex')
    inet = listArea.count('inet')
    feed = listArea.count('feed')
    storage = listArea.count('storage')
    corp = listArea.count('corp')

    percents = [bcloud, blank, tdmz, admin, dev, one, prod, apex, inet, feed, storage, corp]
    areas = ['bcloud', '-', 'tdmz', 'admin', 'dev', '1', 'prod', 'apex', 'inet', 'feed', 'storage', 'corp']
    colors = ['purple', 'green', 'blue', 'pink', 'brown', 'red', 'lightblue', 'teal', 'orange', 'lightgreen', 'yellowgreen', 'yellow']  # https://xkcd.com/color/rgb/

    plt.pie(percents, labels=areas, colors=colors, autopct='%1.1f%%', startangle=-15)
    plt.axis('equal')
    plt.title('Percent of Areas')
    plt.legend()
    mng = plt.get_current_fig_manager()
    # mng.window.state('zoomed')
    plt.show()


def histogram():
    # converts listUptime into ints and adds 0 if string is empty
    intListUptime = [(int(x) if x else 0) for x in listUptime]
    intListUptime.sort()

    plt.hist(intListUptime, 26, rwidth=0.8)
    plt.xlabel('Uptime')
    plt.ylabel('Number of Hosts')
    plt.title('Histogram of Uptime')
    mng = plt.get_current_fig_manager()
    # mng.window.state('zoomed')
    plt.show()


def version():
    uniqueVersion = list(set(listVersion))
    avgVersion = [None] * 55

    for x in range(0, 55):
        counter = 0
        for item in data:
            try:
                if(item['version'] == uniqueVersion[x]):
                    counter += int(item['uptime'])
            except:
                counter += 0
        counter /= listVersion.count(uniqueVersion[x])
        counter = int(round(counter))
        avgVersion[x] = counter

    plt.barh(uniqueVersion, avgVersion, align='center')
    plt.xlabel('Average Uptime')
    plt.ylabel('Version')
    plt.title('Average Uptime of Each Version')
    mng = plt.get_current_fig_manager()
    # mng.window.state('zoomed')
    plt.show()


def area():
    uniqueArea = list(set(listArea))
    avgArea = [None] * 12

    for x in range(0, 12):
        counter = 0
        for item in data:
            try:
                if(item['area'] == uniqueArea[x]):
                    counter += int(item['uptime'])
            except:
                counter += 0
        counter /= listArea.count(uniqueArea[x])
        counter = int(round(counter))
        avgArea[x] = counter

    plt.bar(uniqueArea, avgArea, align='center')
    plt.xlabel('Area')
    plt.ylabel('Average Uptime')
    plt.title('Average Uptime of Each Area')
    mng = plt.get_current_fig_manager()
    # mng.window.state('zoomed')
    plt.show()
