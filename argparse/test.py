import argparse

parser = argparse.ArgumentParser(
        prog='mongoBackuper',
        description='Loads documents, saves back after modify',
        epilog='With great power comes great responsibility, my padawan',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('-w_dir', '--w_dir', type=str,help='Path to working directory')   
parser.add_argument('-v_dir', '--v_dir',type=str,help='Path to versioning directory')
parser.add_argument('-srv_ip', '--srv_ip',type=int,help='srv_ip is the mongoDB Server ip')
parser.add_argument('-srv_port', '--srv_port',type=int,help='srv_port is the mongoDB Server port')
parser.add_argument('-w_db', '--w_db',type=str,help='w_db is the databases name')   
parser.add_argument('-w_coll', '--w_coll',type=str,help='w_coll is the collections name')         

parser.add_argument('-v', '--verbose',
                        action='store_true')  

args =  parser.parse_args()

"""
Hiermit kann man aus dem Code einen command invoken(Testzwecke)
parser.parse_args(['--sum', '7', '-1', '42'])
Namespace(accumulate=<built-in function sum>, integers=[7, -1, 42])
"""

#print(args)
print(args.w_dir)
print(args.v_dir)
print(args.srv_ip)
print(args.w_db)
print(args.w_coll)


