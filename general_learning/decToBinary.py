def dec2bin(number):
    ## integer part:
    int_number = int(number)
    int_bin_str = ''
    while int_number != 0:
        (int_number, remainder) = divmod(int_number, 2)
        int_bin_str = str(remainder) + int_bin_str

    ## fractional part
    frac_number = number - int(number)
    frac_bin_str = ''
    count = 0
    while( count < 4):
        frac_bin_str += str(int(2.0 * frac_number))
        frac_number  = 2*frac_number - int(2*frac_number)
        count += 1

    return int_bin_str+"."+frac_bin_str

## MAIN ##
print(dec2bin(10))
print(dec2bin(2.22))
print(dec2bin(0.876))