import sys  # first, we import the module
import math

args = sys.argv  # we get the list of arguments
tipo = list('diffannuity')
princ = list('--principal=')
pay = list('--payment=')
period = list('--periods=')
int1 = list('--interest=')
global payment_input, periods_input, interest_input, principal_input, interest_input1, periods_input1
global payment_input2, periods_input2, payment_input1, label2, principal_input1
global interest_input2, interest_input3, principal_input3, periods_input3


def annuity():
    global payment_input2, interest_input1, label2, periods_input1

    if payment2[0:10] == pay[0:10]:
        sum6 = ''
        for i in range(10, len(payment2)):
            sum6 += payment2[i]
        payment_input2 = float(sum6)
    else:
        print('Incorrect parameters4')
    if periods[0:9] == period[0:9]:
        sum1 = ''
        for i in range(10, len(periods)):
            sum1 += periods[i]
        periods_input1 = float(sum1)
    else:
        print('Incorrect parameters5')
    if interest[0:11] == int1[0:11]:
        sum2 = ''
        for i in range(11, len(interest)):
            sum2 += interest[i]
        interest_input1 = float(sum2)
    else:
        print('Incorrect parameters6')
    return payment_input2, periods_input1, interest_input1


def diff():
    global principal_input, interest_input2, periods_input, payment_input1, label
    label = False
    if principal[0:12] == princ[0:12]:
        sum10 = ''
        for i in range(12, len(principal)):
            sum10 += principal[i]
        principal_input = float(sum10)
    else:
        print('Incorrect parameters8')
    if periods[0:10] == period[0:10]:
        sum4 = ''
        for i in range(10, len(periods)):
            sum4 += periods[i]
        periods_input = float(sum4)
    else:
        print('Incorrect parameters7')
    if interest[0:10] == int1[0:10]:
        sum5 = ''
        for i in range(11, len(interest)):
            sum5 += interest[i]
        interest_input2 = float(sum5)
    else:
        print('Incorrect parameters9')
    return principal_input, periods_input, interest_input2


def annuity1():
    global principal_input1, payment_input2, interest_input3, label2
    if principal[0:12] == princ[0:12]:
        sum3 = ''
        for i in range(12, len(principal)):
            sum3 += principal[i]
        principal_input1 = float(sum3)
    if payment1[0:10] == pay[0:10]:
        sum6 = ''
        for i in range(10, len(payment1)):
            sum6 += payment1[i]
        payment_input2 = float(sum6)
    if interest[0:11] == int1[0:11]:
        sum4 = ''
        for i in range(11, len(interest)):
            sum4 += interest[i]
        interest_input3 = float(sum4)
    return principal_input1, payment_input2, interest_input3


def annuity2():
    global principal_input3, interest_input3, periods_input3
    if principal[0:12] == princ[0:12]:
        sum13 = ''
        for i in range(12, len(principal)):
            sum13 += principal[i]
        principal_input3 = float(sum13)
    if periods[0:9] == period[0:9]:
        sum14 = ''
        for i in range(10, len(periods)):
            sum14 += periods[i]
        periods_input3 = float(sum14)
    else:
        print('Incorrect parameters5')
    if interest[0:11] == int1[0:11]:
        sum15 = ''
        for i in range(11, len(interest)):
            sum15 += interest[i]
        interest_input3 = float(sum15)
    else:
        print('Incorrect parameters6')
    return principal_input3, periods_input3, interest_input3


def diff_pag(principal_i, periods_i, interest_i):
    inter = interest_i / 100 / 12
    sum40 = 0
    for m in range(1, int(periods_input) + 1):
        dif_pag = principal_i / periods_i
        dif_pag = (principal_i - ((m - 1) * principal_i / periods_i)) * inter + dif_pag
        if (dif_pag - dif_pag // 1) == 0.0:
            dif_pag = round(dif_pag)
        elif (dif_pag - dif_pag // 1) >= 0.5:
            dif_pag = round(dif_pag)
        else:
            dif_pag = round(dif_pag) + 1
        sum40 += dif_pag
        print('Month:', m, ' payment is ', dif_pag)
    over = sum40 - principal_i
    if (over - over // 1) == 0.0:
        over = round(over)
    elif (over - over // 1) >= 0.5:
        over = round(over)
    else:
        over = round(over // 1) + 1
    print('\n')
    print('Overpayment =', over)
    return


def pay_annuity(principal_i, periods_i, interest_i):
    inter2 = interest_i / 100 / 12
    p_annuity = principal_i * ((1 + inter2) ** periods_i) * inter2 / ((1 + inter2) ** periods_i - 1)
    if p_annuity - p_annuity // 1 == 0:
        p_annuity = round(p_annuity)
    elif (p_annuity - p_annuity // 1) >= 0.5:
        p_annuity = round(p_annuity)
    else:
        p_annuity = round(p_annuity // 1) + 1
    over = p_annuity * periods_i - principal_i
    if (over - over // 1) == 0.0:
        over = round(over)
    elif (over - over // 1) >= 0.5:
        over = round(over)
    else:
        over = (over // 1) + 1
    p_annuity = str(p_annuity) + '!'
    print('Your annuity payment =', p_annuity)
    print('\n')
    print('Overpayment =', over)
    return


def pres_value(payment_i, periods_i, interest_i):
    inter = interest_i / 100 / 12
    pres_annuity2 = ((1 + inter) ** periods_i - 1) * payment_i / (1 + inter) ** periods_i / inter
    over = payment_i * periods_i - pres_annuity2
    if over - over // 1 == 0.0:
        over = round(over)
    elif over - over // 1 >= 0.5:
        over = round(over)
    else:
        over = round(over // 1 + 1)
    if (pres_annuity2 - pres_annuity2 // 1) == 0.0:
        pres_annuity2 = round(pres_annuity2 // 1)
    elif (pres_annuity2 - pres_annuity2 // 1) >= 0.5:
        pres_annuity2 = round(pres_annuity2 // 1)
    else:
        pres_annuity2 = round(pres_annuity2 // 1)
    pres_annuity2 = str(pres_annuity2) + '!'
    print('Your loan principal =', pres_annuity2)
    print('Overpayment =', over)


def per_tempo(principal_i, payment_i, interest_i):
    inter = interest_i / 100 / 12
    tempo1 = payment_i / (payment_i - inter * principal_i)
    tempo2 = inter + 1
    tempo = math.log(tempo1) / math.log(tempo2)
    tempo = tempo / 12
    if (tempo - tempo // 1) == 0.0:
        tempo = round(tempo)
    elif (tempo - tempo // 1) >= 0.5:
        tempo = round(tempo)
    else:
        tempo = tempo // 1 + 1
    over = tempo * 12 * payment_i - principal_i
    if tempo > 1:
        print('It will take', tempo, 'years to repay this loan!')
    else:
        print('It will take', tempo, 'year to repay this loan')
    if (over - over // 1) >= 0.0:
        over = round(over)
    elif (over - over // 1) >= 0.5:
        over = round(over)
    else:
        over = over // 1 + 1
    print('Overpayment =', over)


################################################################


if len(sys.argv) == 5:
    type1 = list(args[1])  # convert arguments to list
    principal = list(args[2])
    periods = list(args[3])
    interest = list(args[4])
    if type1[0:7] == list('--type='):
        if type1[7:11] == tipo[0:4]:
            if principal[0:12] == princ[0:12]:
                if periods[0:9] == period[0:9]:
                    if interest[0:11] == int1[0:11]:
                        diff()
                        # principal_input - periods_input - interest_input2
                        diff_pag(principal_input, periods_input, interest_input2)
                    else:
                        print('Incorrect parameters')
                else:
                    print('Incorrect parameters')
            else:
                print('Incorrect parameters')
        if type1[7:14] == tipo[4:14]:
            label2 = False
            if principal[0:12] == princ[0:12]:
                if periods[0:9] == period[0:9]:
                    if interest[0:11] == int1[0:11]:
                        annuity2()
                        label2 = True
                        # principal_input3 - periods_input3 - interest_input3
                        pay_annuity(principal_input3, periods_input3, interest_input3)
                    else:
                        label3 = True
                        print('Incorrect parameters')
                elif periods[0:10] == pay[0:10]:
                    if interest[0:11] == int1[0:11]:
                        payment1 = list(args[3])
                        annuity1()
                        label2 = True
                        # principal_input1 - payment_input2 - interest_input3
                        per_tempo(principal_input1, payment_input2, interest_input3)
                else:
                    print('Incorrect parameters')
            if principal[0:10] == pay[0:11]:
                payment2 = list(args[2])
                periods2 = list(args[3])
                if periods[0:9] == period[0:9]:
                    label2 = True
                    annuity()
                    # payment_input2 - periods_input1 - interest_input1
                    pres_value(payment_input2, periods_input1, interest_input1)
                else:
                    print('Incorrect parameters')
            if not label2:
                print('Incorrect parameters')
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
