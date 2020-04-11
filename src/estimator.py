import math
def estimator(data):
      currentlyInfectedImpact = int(data['reportedCases'] * 10)
      currentlyInfectedSevereImpact = int(data['reportedCases'] * 50)
      
      days = timeEstimate(data)
      
      infectionRequestTimeImpact = currentlyInfectedImpact * (2 ** (int(days / 3)))
      infectionRequestTimeSevereImpact = currentlyInfectedSevereImpact * (2 ** (int(days / 3)))
      
      severeCaseRequestTimeImpact = (0.15 * infectionRequestTimeImpact)
      severeCaseRequestTimeSevereImpact = (0.15 * infectionRequestTimeSevereImpact)
      
      beds = (0.35 * int(data['totalHospitalBeds']))
      
      bedsRequesteTimeImpact = int(beds - severeCaseRequestTimeImpact)
      bedsRequesteTimeSevereImpact = int(beds - severeCaseRequestTimeSevereImpact)
      
      casesForICUByRequestedTimeImpact = 0.05 * infectionRequestTimeImpact
      casesForICUByRequestedTimeSevereImpact = 0.05 * infectionRequestTimeSevereImpact
      
      casesForVentilatorsByRequestedTimeImpact = 0.02 * infectionRequestTimeImpact
      casesForVentilatorsByRequestedTimeSevereImpact = 0.02 * infectionRequestTimeSevereImpact
      
      dollarsInFlightImpact = int(infectionRequestTimeImpact * 0.65 * (data['region']['avgDailyIncomeInUSD']) * days)
      dollarsInFlightSevereImpact = int(infectionRequestTimeSevereImpact * 0.65 * (data['region']['avgDailyIncomeInUSD']) * days)
      
      output = {
        "data": data,
        "impact": {
              "currentlyInfected": currentlyInfectedImpact,
              "infectionsByRequestedTime": infectionRequestTimeImpact,
              "severeCasesByRequestedTime": severeCaseRequestTimeImpact,
              "hospitalBedsByRequestedTime": bedsRequesteTimeImpact,
              "casesForICUByRequestedTime": casesForICUByRequestedTimeImpact,
              "casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTimeImpact,
              "dollarsInFlight": dollarsInFlightImpact
        },
        "severeImpact": {
              "currentlyInfected":currentlyInfectedSevereImpact,
              "infectionsByRequestedTime": infectionRequestTimeSevereImpact,
              "severeCasesByRequestedTime": severeCaseRequestTimeSevereImpact,
              "hospitalBedsByRequestedTime": bedsRequesteTimeSevereImpact,
              "casesForICUByRequestedTime": casesForICUByRequestedTimeSevereImpact,
              "casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTimeSevereImpact,
              "dollarsInFlight": dollarsInFlightSevereImpact
             
        }
        
      }
      
      return output

def timeEstimate(data):
      if data['periodType'] == 'days':
            days = data['timeToElapse']
      elif data['periodType'] == 'weeks':
            days = data['timeToElapse'] * 7
      elif data['periodType'] == 'months':
            days = data['timeToElapse'] * 30
      return days