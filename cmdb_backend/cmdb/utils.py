from fabric.api import  settings, run
import traceback



def run_ssh(host, command):
    result = ""
    try:
        with settings(host_string=host, ):
            res = run(command)
            if not res.stderr:
                result = {
                    "status": "ok",
                    "result": res,
                }
            else:

                result = {
                    "status": "fail",
                    "result": res.stderr
                }
    except:
        tb = traceback.format_exc()
        result = {
            "status": "fail",
            "result": tb,
        }
    #import pdb;pdb.set_trace()
    return result


if __name__=="__main__":
    output=run_ssh('jenkins.lzd.co','dfasfate')
    #
    print(output)

