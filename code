import sys
import argparse
import math

# initialize the parser
parser = argparse.ArgumentParser()

# Add the parameters positional/optional
parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--payment", type=float)
parser.add_argument("--interest", type=float)

# Parse the arguments
args = parser.parse_args()

pmt = []
if len(sys.argv) < 4:
    print("Incorrect Parameters")
elif args.type not in ["diff", "annuity"]:
    print("Incorrect Parameters")
elif args.interest == None:
    print("Incorrect Parameters")
else:
    iy = args.interest / (12 * 100)
    if args.type == "diff":
        for i in range(1, args.periods + 1):
            payments = math.ceil((args.principal / args.periods) + iy * (args.principal - ((args.principal * (i - 1)) / args.periods)))
            print(f"Payment {i}: paid out {math.ceil(payments)}")
            pmt.append(payments)
        overcharge = sum(pmt) - args.principal
        print(f"Overpayment = {math.ceil(overcharge)}")
    
    elif args.type == "annuity":
        if args.principal == None:
            args.principal = args.payment / ((iy * ((1 + iy) ** args.periods)) / (((1 + iy) ** args.periods) - 1))
            print(f"Your credit principal = {int(args.principal)}!")
            overcharge = (math.ceil(args.payment) * args.periods) - args.principal
            print(f"Overpayment = {overcharge}")
            
        elif args.payment == None:
            args.payment = args.principal * ((iy * ((1 + iy) ** args.periods)) / (((1 + iy) ** args.periods) - 1))
            print(f"Your annuity payment = {math.ceil(args.payment)}!")
            overcharge = (math.ceil(args.payment) * args.periods) - args.principal
            print(f"Overpayment = {overcharge}")
            
        elif args.periods == None:
            args.periods = math.ceil(math.log(args.payment / (args.payment - iy * args.principal), 1 + iy))
            years = args.periods // 12
            months = args.periods % 12
            if years == 0:
                if months == 1:
                    print(f"You need {months} month to repay this credit!")
                else:
                    print(f"You need {months} months to repay this credit!")
            elif years == 1:
                if months == 1:
                    print(f"You need {years} year and {months} month to repay this credit!")
                elif months == 0:
                    print(f"You need {years} year to repay this credit!")
                else:
                    print(f"You need {years} year and {months} months to repay this credit!")
            else:
                if months == 0:
                    print(f"You need {years} years to repay this credit!")
                elif months == 1:
                    print(f"You need {years} years and {months} month to repay this credit!")
                else:
                    print(f"You need {years} years and {months} months to repay this credit!")
                overcharge = (math.ceil(args.payment) * args.periods) - args.principal
                print(f"Overpayment = {overcharge}")
