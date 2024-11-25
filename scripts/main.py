from IOT_temp_process import producer


class Runner(): 

    @staticmethod 
    def main() : 
        print('Method Initiated : ')
        producer.producer_main()



if __name__ == '__main__': 
    Runner.main()