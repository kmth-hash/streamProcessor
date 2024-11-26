from IOT_temp_process import producer
import sys 

class Runner(): 

    @staticmethod 
    def main() : 
        currLoc = 'tempLoc' 

        if len(sys.argv) != 2 : 
            print('Location missing : ')
            # exit(0)
        else : 
            currLoc = sys.argv[1] 

        print('Method Initiated : ')
        producer.producer_main(currLoc)



if __name__ == '__main__': 
    Runner.main()