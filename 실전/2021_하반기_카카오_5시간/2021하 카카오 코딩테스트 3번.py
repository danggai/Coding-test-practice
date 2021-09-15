import math

def solution(fees, records):
    answer = []

    splitedRecords = []

    parkingLot = []
    
    carNumbers = set()
    receipts = []

    for record in records:
        splitedRecord = record.split(" ")
        splitedRecords.append(splitedRecord)
        carNumbers.add(splitedRecord[1])

    for number in carNumbers:
        receipts.append([number, 0])
    
    receipts.sort()

    for record in splitedRecords:
        if record[2] == 'IN':
            parkingLot.append([record[0], record[1]])      # record[0]: 시간, record[1]: 번호
        elif record[2] == 'OUT':
            for car in parkingLot:
                if car[1] == record[1]:
                    for i in enumerate(receipts):
                        if i[1][0] == record[1]:
                            i[1][1] += timeComparisionToMinute(car[0], record[0])
                            parkingLot.remove(car)

    for car in parkingLot:
        for i in range(len(receipts)):
                if receipts[i][0] == car[1]:
                    receipts[i][1] += timeComparisionToMinute(car[0], "23:59")

    print(receipts)

    for receipt in receipts:
        if receipt[1] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((receipt[1]-fees[0])/fees[2])*fees[3])

    return answer

def timeComparisionToMinute(inTime, outTime):
    spInTime = inTime.split(":")
    spOutTime = outTime.split(":")

    return (int(spOutTime[0]) - int(spInTime[0]))*60 + int(spOutTime[1]) - int(spInTime[1])


fees = [180, 5000, 10, 600]
records	= ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	
print(solution(fees, records))
print("expect = [14600, 34400, 5000]")

fees = [120, 0, 60, 591]
records	= ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	
print(solution(fees, records))
print("expect = [0, 591]")

fees = [1, 461, 1, 10]	
records	= ["00:00 1234 IN"]	
print(solution(fees, records))
print("expect = [14841]")