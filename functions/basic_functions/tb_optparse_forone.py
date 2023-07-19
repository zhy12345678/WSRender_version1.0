def tb_optparse_forone(opt,robot_type):
    if robot_type in opt['type']:
        opt['type'] = robot_type
        return opt
    else:
        return None
