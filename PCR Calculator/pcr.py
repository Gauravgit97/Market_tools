#'PUT CALL ratio-> This code is for calculte the pcr ration.'

# for this code the resource is a video : https://www.youtube.com/watch?v=41ZtgTcxiVc&t=368s


import pandas as pd   
import requests
import datetime
import time


def pcr():

    url="https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    headers ={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'acceptencoding' : 'gzip, deflate, br',
        'acceptlanguage': 'en-US,en;q=0.9'
    }

    session = requests.Session()
    request = session.get(url, headers=headers)
    cookies = dict(request.cookies)
    response = session.get(url,headers=headers,cookies=cookies).json()   #-->this to get all data form NSE in raw form, it look like HTML.


    def datafram(rawop,neededsp):
    
        data = []
        for i in range(0,len(rawop)):

            calloi = callcoi = cltp = putoi = putcoi = pltp = 0
            stp = rawop['strikePrice'][i]

            if stp in neededsp:
                if (rawop['CE'][i]==0):
                    calloi = callcoi = 0
                else:
                    calloi = rawop['CE'][i]['openInterest']
                    callcoi = rawop['CE'][i]['changeinOpenInterest']
                    cltp = rawop['CE'][i]['lastPrice']
        
                if (rawop['PE'][i]==0):
                    putoi = putcoi = 0
                else:
                    putoi = rawop['PE'][i]['openInterest']
                    putcoi = rawop['PE'][i]['changeinOpenInterest']
                    pltp = rawop['PE'][i]['lastPrice']


                    opdata = {
                    'CALL OI': calloi, 'CALL CHAG OI': callcoi, 'CALL LTP': cltp, 'STRIKE PRICE':stp,
                    'PUT OI':putoi, 'PUT CHAG OI':putcoi, 'PUT LTP':pltp
                    }
                    data.append(opdata)

        optionchain = pd.DataFrame(data)
        return optionchain


    rawdata = pd.DataFrame(response)              #-->the html change into 'records' and 'filtered' form
    rawop = pd.DataFrame(rawdata['filtered']['data'])      #-->from rawdata you get filter part

    presentNV = rawdata['records']['underlyingValue']
    stricPrices = rawdata['records']['strikePrices']


    neededsp = []
    for i in stricPrices:
        p = int(i - presentNV)

        if p <= 0 and p >= -400:
            neededsp.append(i)
        else:
            pass
    

        if p >= 0 and p<= 400:
            neededsp.append(i)
        else:
            pass

    def main():
    
        optionchain =datafram(rawop,neededsp)
        # print(optionchain)


        totalCCoi = int(optionchain['CALL CHAG OI'].sum())
        totlaPCoi = int(optionchain['PUT CHAG OI'].sum())
        ratio = totlaPCoi/totalCCoi

        # print(f"The present value of nifty is:- '{presentNV}'")
        # print(f"Total change in open intrest in 'CALL' -> '{totalCCoi}', and 'PUT' -> '{totlaPCoi}' ")
    

        if ratio < 0:
            ratio = ratio * -1

        # print(f"PCR -> '{ratio}'")
        totalOutPut = f'''The present value of nifty is:- '{presentNV}'
Total change in open intrest in 'CALL' -> '{totalCCoi}', and 'PUT' -> '{totlaPCoi}'
PCR -> '{ratio}' '''

        if ratio < 1:
            return f"{totalOutPut}  Market is bearish \n BUY-> 'PUT' \n "
        elif ratio <=1.5:
            return f"{totalOutPut}  Market is side-base, you can wait or \n BUY-> 'CALL' \n "
        else:
            return f"{totalOutPut}  Market is bullish \n BUY-> 'CALL' \n "

    run = main()
    print(run)
    return run



def present_time():
        hour = int(datetime.datetime.now().hour)
        minits = int(datetime.datetime.now().minute)
        return f"{hour}:{minits}"

i = 0
while True:
    i = i + 1
    ptime = present_time()
    # if ptime =='15:25' or ptime >'15:25':
    #     break
    
    output = pcr()
    w = open("poems.txt","a")
    w.write(f"{i}. {ptime} | {output} \n")
    w.close
    # print(output)
    time.sleep(300)
