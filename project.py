
class ATM(object):
  """
    blueprint for ATM 
  """

  def __init__(self, card_number, expiry_date, name, pin_number):
    self.card_number = card_number
    self.expiry_date = expiry_date
    self.name = name
    self.pin_number = pin_number

  def CashWithdrawal(self):
    print("Successful Transaction!")

  def BalanceInquiry(self):
    print("Inquiry sent successfully!")

def OnlineTransaction(self):
    print("Successful e-Transaction")

def MoneyTransfer(self):
    print("Transferred Succesfully!")

  


card = ATM("1223234256", "12/3/2025", "Pari", "2367")

print(card.CashWithdrawal())


        
