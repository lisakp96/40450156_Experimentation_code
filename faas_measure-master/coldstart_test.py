from utils import *

#coldstart = invocation send time - function exectuion time 
# + Kernel up time -> instance launched on new vs. excisting VM 

def coldstart_measure(
        rd_id,
        runtime,
        mem_size,
        thread_no,
        sleep_tm,
        wait_tm,
        log_file="tmp.log"):
    """
    Args:
        rd_id: an ID for this round of measurement
        runtime: "python2.7", "python3.6", "nodejs6.10", or "nodejs4.3"
        mem_size: the memory of the function
        thread_no: the number of workers (threads) initialized.
        sleep_tm: the function will start tasks after current time + sleep_tm;
        check code/python/index.py
        wait_tm: sleep for wait_tm before return
        log_file: the file for logging results 

    """
    func_prex = "coldstart"
    aws_id, aws_key, region, roles = get_config_basic()
    role = roles[0]
    zipped_code_path = os.path.join(os.getcwd(), "tmp.zip")
    func_handler = "index.handler"

    def worker_func(fop, **args):
        para = get_default_req(sleep_tm)
        res = fop.send_one_request(para)
        return res

    exp = Worker(log_file, rd_id, thread_no, worker_func)
    exp.init()

    para_list = []
    src_code_path = os.path.join(os.getcwd(), CODE_PATH[runtime])
    zip_code(zipped_code_path, src_code_path)


    fops = []
    for i in xrange(thread_no):
        func_name = func_prex + str(int(time.time() * 1000))[-8:]
        fop = FuncOp(
            aws_id,
            aws_key,
            region,
            role,
            runtime,
            mem_size,
            func_name)
        #fop.del_function()
        fop.create_function(zipped_code_path, func_handler)
        para = (fop,)
        para_list.append(para)
        fops.append(fop)

    exp.add_tasks(para_list)        # measuring coldstart latency
    exp.clear_queue()
    exp.add_tasks(para_list)        # measuring warmstart latency
    exp.clear_queue()

    for fop in fops:
        fop.del_function()

    time.sleep(wait_tm)


def main():
<<<<<<< HEAD
    runtime_list = ['python2.7','python3.6','python3.7'] 
    mem_list = [128, 3008]
=======
    runtime_list = ['python3.7'] 
    mem_list = [3008] 
>>>>>>> origin/fileupload_measurement
    rd_id = 1
    log_file = "tmp.log"
    clear_log = False
    thread_no = 2 #2 concurrent requests ? 
    sleep_tm = 5 #sleep 15 sec ? pause 10sec between batches ?
    wait_tm = 0

    open(log_file, "w")         # clear log file
    for rd_id in xrange(2):
        for runtime in runtime_list:
            for mem_size in mem_list:
                coldstart_measure(
                    rd_id,
                    runtime,
                    mem_size,
                    thread_no,
                    sleep_tm,
                    wait_tm,
                    log_file)

#0#1#2#0#us-east-1#
#python2.7
#128
#coldstart67253302

# 9198d5ac-ab89-43b1-bae2-21b611c1cdc5
# 9198d5ac-ab89-43b1-bae2-21b611c1cdc5
# sandbox-root-Pqytol
# sandbox-10302b
# 169.254.67.221
# 34.228.70.61
# 169.254.76.1
# 2626.94,5247.61
# #2,Intel(R) Xeon(R) Processor @ 2.50GHz
# #1593667205062.321
# #1593667263858.2239
# #58795.90283203125#1593667258821.511
# #1593667378792.823
# #119971.31201171875


if __name__ == '__main__':
    main()