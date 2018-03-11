# Kevin Landau, M.S.
# Started preparing these tools on 03/27/2017

# The functions defined in this program can be imported into future programs/scripts that require multiple ways of
# parsing certain files/data.

def tab_separated_parser(data):
    '''

    :param data: This will be a string that contains tabs ('\t') as a delimiter.
    :return: This returns each item that is separated with a tab into a list, along with any end-of-lines ('\n') parsed
    out.
    '''

    parsed1 = data.rstrip('\n').split('\t')
    print (parsed1)

#tab_separated_parser(data= 'item1\titem2\titem3\titem4\n') # The argument string here is just an example.



# def comma_separated_parser():
#
#
# comma_separated_parser()
