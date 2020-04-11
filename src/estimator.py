def estimator(data):
      currentlyInfectedImpact = int(data['reportedCases'] * 10)
      currentlyInfectedSevereImpact = int(data['reportedCases'] * 50)
      
      days = timeEstimate(data)
      
      infectionRequestTimeImpact = currentlyInfectedImpact * (2 ** (int(days / 3)))
      infectionRequestTimeSevereImpact = currentlyInfectedSevereImpact * (2 ** (int(days / 3)))
      
      severeCaseRequestTimeImpact = int(0.15 * infectionRequestTimeImpact)
      severeCaseRequestTimeSevereImpact = int(0.15 * infectionRequestTimeSevereImpact)
      
      beds = int(0.35 * data['totalHospitalBeds'])
      
      bedsRequesteTimeImpact = beds - severeCaseRequestTimeImpact
      bedsRequesteTimeSevereImpact = beds - severeCaseRequestTimeSevereImpact
      
      output = {
        "data": data,
        "impact": {
              "currentlyInfected": currentlyInfectedImpact,
              "infectionsByRequestedTime": infectionRequestTimeImpact,
              "severeCasesByRequestedTime": severeCaseRequestTimeImpact,
              "hospitalBedsByRequestedTime": bedsRequesteTimeImpact
        },
        "severeImpact": {
              "currentlyInfected":currentlyInfectedSevereImpact,
              "infectionsByRequestedTime": infectionRequestTimeSevereImpact,
              "severeCasesByRequestedTime": severeCaseRequestTimeSevereImpact,
              "hospitalBedsByRequestedTime": bedsRequesteTimeSevereImpact
             
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