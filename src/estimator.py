def estimator(data):
  return data

def timeEstimate(data):
      if data['periodType'] == 'days':
            days = data['timeToElapse']
      elif data['periodType'] == 'weeks':
            days = data['timeToElapse'] * 7
      elif data['periodType'] == 'months':
            days = data['timeToElapse'] * 30
      return days