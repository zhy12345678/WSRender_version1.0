import re

def tb_optparse(in_, argv):
    if len(argv) == 1:
        argv = []

    if not isinstance(argv, list):
        raise ValueError('input must be a list')

    others = []
    arglist = []
    ls=[]

    argc = 1
    opt =in_

    if 'verbose' not in opt:
        opt['verbose'] = False
    if 'debug' not in opt:
        opt['debug'] = 0

    showopt = False
    choices = {}

    while argc <= len(argv):
        # index over every passed option
        option = argv[argc - 1]
        assigned = False

        if isinstance(option, str):
            if option == 'verbose':
                opt['verbose'] = True
                assigned = True
            elif option == 'verbose=2':
                opt['verbose'] = 2
                assigned = True
            elif option == 'verbose=3':
                opt['verbose'] = 3
                assigned = True
            elif option == 'verbose=4':
                opt['verbose'] = 4
                assigned = True
            elif option == 'debug':
                opt['debug'] = argv[argc]
                argc += 1
                assigned = True
            elif option == 'setopt':
                new = argv[argc]
                argc += 1
                assigned = True

                # copy matching field names from new opt struct to current one
                for f in new:
                    if f in opt:
                        opt[f] = new[f]
            elif option == 'showopt':
                showopt = True
                assigned = True
            else:
                if option in opt or 'd_' + option in opt or hasattr(opt, option):
                    # handle special case if we have opt.d_3d, this means we are looking for an option '3d'
                    if 'd_' + option in opt or hasattr(opt, 'd_' + option):
                        option = 'd_' + option

                    # ** BOOLEAN OPTION
                    val = opt[option]
                    if isinstance(val, bool):
                        # a boolean variable can only be set by an option
                        opt[option] = True
                    else:
                        # ** OPTION IS ASSIGNED VALUE FROM NEXT ARG
                        # otherwise grab its value from the next arg
                        try:
                            opt[option] = argv[argc]
                        except IndexError:
                            raise ValueError('too few arguments provided for option: [{}]'.format(option))
                        argc += 1
                    assigned = True
                elif len(option) > 2 and option[:2] == 'no' and option[3:] in opt:
                    # * BOOLEAN OPTION PREFIXED BY 'no'
                    val = opt[option[3:]]
                    if isinstance(val, bool):
                        # a boolean variable can only be set by an option
                        opt[option[3:]] = False
                        assigned = True
                else:
                    # the option doesn't match a field name
                    # let's assume it's a choice type
                    # opt.choose = ['this', 'that', 'other']
                    # we need to loop over all the passed options and look for those with a list value
                    for field in opt:
                        val = opt[field]
                        if isinstance(val, list):
                            for i in range(len(val)):
                                if val[i] is None:
                                    continue
                                # if we find a match, put the final value in the temporary structure choices
                                #
                                # eg. choices.choose = 'that'
                                #
                                # so that we can process input of the form
                                #
                                # 'this', 'that', 'other'
                                #
                                # which should result in the value 'other'
                                if option == val[i]:
                                    choices[field] = option
                                    assigned = True
                                    break
                                elif val[i][0] == '#' and option == val[i][1:]:
                                    choices[field] = i
                                    assigned = True
                                    break
                            if assigned:
                                break
        if not assigned:
            # non-matching options are collected
            if len(arglist) >= 2:
                arglist.append(argv[argc - 1])
            else:
                if isinstance(argv[argc - 1], str):
                    raise ValueError('unknown options: {}'.format(argv[argc - 1]))

        argc += 1

    # copy choices into the opt structure
    if choices:
        for field in choices:
            opt[field] = choices[field]

    # if enumerator value not assigned, set the default value
    if in_:
        for field in in_:
            if isinstance(in_[field], list) and isinstance(opt[field], list):
                val = opt[field]
                if val[0] is None:
                    opt[field] = val[0]
                elif val[0][0] == '#':
                    opt[field] = 1
                else:
                    opt[field] = val[0]

    if showopt:
        print('Options:')
        print(opt)
        print(arglist)

    if len(argv) == 3:
        # check to see if there is a valid linespec floating about in the unused arguments
        for i in range(len(arglist)):
            s = arglist[i]
            # get color
            match = re.search('[rgbcmywk]', s)
            if match:
                s2 = s[match.start(): match.end()]
                s = s[:match.start()] + s[match.end():]
            else:
                s2 = ''

            # get line style
            match = re.search('(--)|(-\.)|-|:', s)
            if match:
                s2 += s[match.start(): match.end()]
                s = s[:match.start()] + s[match.end():]

            # get marker style
            match = re.search('[o\+\*\.xsd\^v><ph]', s)
            if match:
                s2 += s[match.start(): match.end()]
                s = s[:match.start()] + s[match.end():]

            # found one
            if not s:

                ls = arglist[i]
                arglist.remove(ls)
                others = arglist
                break
        else:
            ls = ''
            others = arglist
    elif len(argv) == 2:
        others = arglist

    return opt, others, ls
